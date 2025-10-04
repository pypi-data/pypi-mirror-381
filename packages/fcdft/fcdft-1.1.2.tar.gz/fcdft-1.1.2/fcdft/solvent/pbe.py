import numpy
import scipy
import os
import fcdft
import fcdft.solvent.calculus_helper as ch

from fcdft.solvent import _attach_solvent
from pyscf.solvent import ddcosmo
from pyscf.tools import cubegen
from pyscf import lib
from pyscf.lib import logger
from pyscf.data.nist import *
from pyscf.data.radii import VDW
from pyscf import df
from pyscf import gto
from fcdft.lib import pbe_helper

try:
    OMP_NUM_THREADS = os.environ['OMP_NUM_THREADS']
except KeyError:
    OMP_NUM_THREADS = 1
PI = numpy.pi
KB2HARTREE = BOLTZMANN / HARTREE2J
M2HARTREE = AVOGADRO*BOHR**3*1.e-27

def pbe_for_scf(mf, solvent_obj=None, dm=None):
    if solvent_obj is None:
        solvent_obj = PBE(mf.mol)
    return _attach_solvent._for_scf(mf, solvent_obj, dm)

def gen_pbe_solver(solvent_obj, verbose=None):
    return solvent_obj._get_vind

def make_lambda(solvent_obj, mol, probe, stern_mol, stern_sam, coords, delta1, delta2, atomic_radii):
    """Ion-exclusion function.

    Args:
        mol (pyscf.gto.Mole): Mole object.
        probe (float): Probe radius in a.u..
        stern_mol (float): Molecular Stern layer thickness in a.u..
        stern_sam (float): SAM Stern layer thickness in a.u..
        coords (2D numpy.ndarray): Cartesian coordinates.
        delta1 (float): Broadening constant in error functions used for the molecular part.
        delta2 (float): Broadening constant in error functions used for the SAM part.
        atomic_radii (1D numpy.ndarray): Atomic radii

    Returns:
        1D array: Ion-exclusion function
    """
    atom_coords = mol.atom_coords()
    # Molecular Stern Layer
    dist = pbe_helper.distance_calculator(coords, atom_coords)
    x = (dist - atomic_radii[:,None] - probe - stern_mol) / delta2
    erf_list = 0.5e0*(1.0e0 + scipy.special.erf(x))
    erf_list[x < -8.0e0*delta2] = 0.0e0
    lambda_r = numpy.prod(erf_list, axis=0)

    # SAM Stern Layer
    zmin = coords[:,2].min()
    x = (coords[:,2] - zmin - (stern_sam + stern_mol)) / delta1
    _erf = scipy.special.erf(x)
    _erf[x < -8.0e0*delta1] = -1.0e0 # Value suppression
    lambda_z = 0.5e0 * (1.0e0 + _erf)
    lambda_r = lambda_z * lambda_r
    return lambda_r

def make_sas(solvent_obj, mol, probe, coords, delta2, atomic_radii):
    """Generating solvent-accessible surface

    Args:
        mol (pyscf.gto.Mole): Mole object.
        probe (float): probe radius in a.u..
        coords (2D numpy.ndarray): Cartesian coordinates.
        delta2 (float): broadening constant in a.u..
        atomic_radii (1D numpy.ndarray): Atomic radii

    Returns:
        1D numpy.ndarray: Solvent-accessible surface
    """
    atom_coords = mol.atom_coords()
    dist = pbe_helper.distance_calculator(coords, atom_coords)
    x = (dist - atomic_radii[:,None] - probe) / delta2
    _erf = scipy.special.erf(x)
    erf_list = 0.5e0 * (1.0e0 + _erf)
    S = numpy.prod(erf_list, axis=0)
    return S

def make_eps(solvent_obj, coords, eps_sam, eps, stern_sam, delta1, sas):
    """Calculates the dielectric function.

    Args:
        coords (2D numpy.ndarray): Cartesian coordinates
        eps_sam (float): Dielectric constant of the self-assembled monolayer
        eps (float): Dielectric constant of the bulk solvent.
        stern_sam (float): Stern layer length of the self-assembled monolayer in atomic unit.
        delta1 (float): Broadening constant of error functions.
        sas (1D numpy.ndarray): Solvent-accessible surface.

    Returns:
        1D numpy.ndarray: Dielectric function
    """
    zmin = coords[:,2].min()
    x = (coords[:,2] - zmin - stern_sam) / delta1
    _erf = scipy.special.erf(x)
    eps_z = eps_sam + 0.5e0 * (eps - eps_sam) * (1.0e0 + _erf)
    eps_r = 1.0e0 + (eps_z - 1.0e0) * sas
    return eps_r

def make_grad_eps(solvent_obj, mol, coords, eps_sam, eps, probe, stern_sam, delta1, delta2, atomic_radii, sas):
    """Generates analytic gradient of the dielectric function.

    Args:
        mol (pyscf.gto.Mole): Mole object.
        coords (2D numpy.ndarray): Cartesian coordinates.
        eps_sam (float): Dielectric constant of the self-assembled monolayer.
        eps (float): Dielectric constant of the bulk solvent.
        probe (float): Probe radius.
        stern_sam (float): Thickness of the Stern layer formed by the self-assembled monolayer.
        delta1 (float): Width of error function along z-axis.
        delta2 (float): Width of error function used for molecular part.
        atomic_radii (1D numpy.ndarray): Atomic radii.
        sas (1D numpy.ndarray): Solvent-accessible surface.

    Returns:
        2D numpy.ndarray: Gradient of the dielectric function.
    """
    atom_coords = mol.atom_coords()
    return pbe_helper.grad_eps(atom_coords, coords, eps_sam, eps, probe, stern_sam, delta1, delta2, atomic_radii, sas)

def make_phi_sol(solvent_obj, dm=None, coords=None):
    """Generates solute potential in vacuum.

    Args:
        solvent_obj (:class:`PBE`): Solvent object.
        dm (2D numpy.ndarray): Density matrix
        coords (2D numpy.ndarray): Cartesian grids.

    Returns:
        numpy tag_array: Solute electrostatic potential.
    """
    if dm is None: dm = solvent_obj._dm
    if coords is None: coords = solvent_obj.grids.coords

    tot_ngrids = solvent_obj.grids.get_ngrids()
    
    logger.info(solvent_obj, 'Generating the solute electrostatic potential...')
    mol = solvent_obj.mol

    atom_coords = mol.atom_coords()
    Z = mol.atom_charges()
    dist = pbe_helper.distance_calculator(coords, atom_coords)
    dist[dist < 1.0e-100] = numpy.inf # Machine precision
    Vnuc = numpy.tensordot(1.0e0 / dist, Z, axes=([0], [0]))

    if dm.ndim == 3: # Spin-unrestricted
        dm = dm[0] + dm[1]

    gpu_accel = solvent_obj.gpu_accel

    if gpu_accel:
        logger.info(solvent_obj, 'Will utilize GPUs for computing the electrostatic potential.')
        import cupy
        nbatch = 256*256
        tot_ngrids = coords.shape[0]
        from gpu4pyscf.gto.int3c1e import int1e_grids
        _dm = cupy.asarray(dm.real)
        _Vele = cupy.zeros(tot_ngrids, order='C')
        for ibatch in range(0, tot_ngrids, nbatch):
            max_grid = min(ibatch+nbatch, tot_ngrids)
            _Vele[ibatch:max_grid] += int1e_grids(mol, coords[ibatch:max_grid], dm=_dm, direct_scf_tol=1e-14)
        Vele = _Vele.get()
        del _dm, _Vele,  cupy, int1e_grids # Release GPU memory
        lib.num_threads(OMP_NUM_THREADS) # GPU4PySCF sets OMP_NUM_THREADS=4 when running.

    else:
        Vele = numpy.empty(tot_ngrids, order='C')
        nao = mol.nao
        max_memory = solvent_obj.max_memory - lib.current_memory()[0] - Vele.nbytes*1e-6
        blksize = int(max(max_memory*.9e6/8/nao**2, 400))
        cintopt = gto.moleintor.make_cintopt(mol._atm, mol._bas, mol._env, 'int3c2e')
        for p0, p1 in lib.prange(0, tot_ngrids, blksize):
            fakemol = gto.fakemol_for_charges(coords[p0:p1])
            ints = df.incore.aux_e2(mol, fakemol, cintopt=cintopt)
            Vele[p0:p1] = numpy.tensordot(ints, dm.real, axes=([1,0], [0,1]))
            del ints

    MEP = Vnuc - Vele
    return lib.tag_array(MEP, Vnuc=Vnuc, Vele=-Vele)

def make_rho_sol(solvent_obj, phi_sol=None, ngrids=None, spacing=None):
    """Solute charge density by solving the Poisson equation.
    
    Args:
        solvent_obj (:class:`PBE`): Solvent object.
        phi_sol (1D numpy.ndarray): Electrostatic potential of the solute molecule.
        ngrids (int): Number of grid points along each axis.
        spacing (float): Grid spacing

    Returns:
        1D numpy.ndarray: Solute charge density
    """
    if phi_sol is None: phi_sol = solvent_obj.phi_sol
    if spacing is None: spacing = solvent_obj.grids.spacing
    if ngrids is None: ngrids = solvent_obj.grids.ngrids
    solver = solvent_obj.solver
    nproc = lib.num_threads()
    if isinstance(solver, fcdft.solvent.solver.fft2d):
        phik = scipy.fft.fftn(phi_sol.reshape((ngrids,)*3), axes=(0,1), workers=nproc)
    else:
        phik = None

    rho_sol = -solver.laplacian(phi_sol, phik) / 4.0e0 / PI

    return rho_sol

def make_phi(solvent_obj, bias=None, phi_sol=None, rho_sol=None):
    """Non-linear Poisson-Boltzmann equation driver.

    Args:
        solvent_obj : An instance of :class:`PBE`
        bias (float, optional): Bias potential in atomic unit. Defaults to None.
        phi_sol (numpy.ndarray, optional): Solute potential in vacuum. Defaults to None.
        rho_sol (numpy.ndarray, optional): Solute charge density in vacuum. Defaults to None.

    Raises:
        RuntimeError: Infinite ion charge density.
        RuntimeError: PBE self-consistent cycle fails to converge.

    Returns:
        numpy.ndarray, numpy.ndarray, numpy.ndarray: Total potential, ion charge density, and polarization charge density.
    """
    if solvent_obj._intermediates is None: solvent_obj.build()
    _intermediates = solvent_obj._intermediates

    ngrids = solvent_obj.grids.ngrids
    tot_ngrids = solvent_obj.grids.get_ngrids()
    T = solvent_obj.T
    spacing = solvent_obj.grids.spacing
    stern_sam = solvent_obj.stern_sam / BOHR
    cb = solvent_obj.cb * M2HARTREE
    pzc = solvent_obj.pzc / HARTREE2EV
    ref_pot = solvent_obj.ref_pot / HARTREE2EV
    jump_coeff = solvent_obj.jump_coeff
    
    eps = _intermediates['eps']
    lambda_r = _intermediates['lambda_r']
    grad_eps = _intermediates['grad_eps']
    sas = _intermediates['sas']

    solver = solvent_obj.solver

    eta = 0.6e0
    kappa = 0.2e0

    phi_tot = numpy.zeros(tot_ngrids, dtype=numpy.float64)
    impose_bc, bc_grad, bc_lap = solvent_obj._gen_boundary_conditions()
    bc, phi_z, slope= impose_bc(solvent_obj, ngrids, spacing, bias, stern_sam, T, 
                                solvent_obj.eps_sam, solvent_obj.eps, sas, pzc, ref_pot, jump_coeff)
    grad_bc, grad_phi_z, grad_sas = bc_grad(solvent_obj, ngrids, spacing, T, slope, phi_z, sas)
    lap_bc = bc_lap(solvent_obj, ngrids, spacing, T, phi_z, grad_phi_z, sas, grad_sas)

    phi_tot += bc

    grad_lneps = pbe_helper.product_vector_scalar(grad_eps, 1.0e0/eps)
    get_rho_ions = solvent_obj._gen_get_rho_ions()
    rho_ions = get_rho_ions(solvent_obj, phi_tot, cb, lambda_r, T)

    rho_tot = rho_sol + rho_ions
    rho_iter = numpy.zeros(tot_ngrids)
    rho_pol = (1.0e0 - eps) / eps * rho_tot + rho_iter


    rho_iter_bc = 0.25e0 / PI * pbe_helper.product_vector_vector(grad_lneps, grad_bc)

    logger.info(solvent_obj, 'Bias vs. PZC = %.15f V', (bias - (ref_pot - pzc)) * HARTREE2EV)
    solver.whoareyou()

    max_cycle = solvent_obj.max_cycle
    iter = 0
    phik = None
    while iter < max_cycle:
        phi_old = phi_tot
        rho_iter_old = rho_iter
        rho_ions_old = rho_ions
        rho_pol_old = rho_pol

        phi_opt = phi_old - bc
        dphi_opt = solver.gradient(phi_opt, phik, ngrids, spacing)
        rho_iter = 0.25e0 / PI * pbe_helper.product_vector_vector(grad_lneps, dphi_opt)

        rho_iter = eta * rho_iter + (1.0e0 - eta) * rho_iter_old

        rho_tot = rho_sol + rho_ions_old
        rho_pol = (1.0e0 - eps) / eps * rho_tot + rho_iter

        _rho = 4.0e0*PI*(rho_tot+rho_pol+rho_iter_bc) + lap_bc
        phi_opt, phik = solver.solve(_rho, ngrids, spacing)
        phi_tot = phi_opt + bc

        rho_ions = get_rho_ions(solvent_obj, phi_tot, cb, lambda_r, T)
        if numpy.isnan(rho_ions).any():
            raise RuntimeError('PBE solver encountered infinite ion charge density!')

        rho_ions = kappa * rho_ions + (1.0e0 - kappa) * rho_ions_old

        drho_pol = abs(rho_pol - rho_pol_old)
        drho_ions = abs(rho_ions - rho_ions_old)
        logger.info(solvent_obj, 'PBE Iteration %3d max|drho(pol)| = %4.3e, max|drho(ions)| = %4.3e', 
                    iter+1, drho_pol.max(), drho_ions.max())
        if numpy.all(drho_pol < solvent_obj.thresh_pol) and numpy.all(drho_ions < solvent_obj.thresh_ions) and iter > 0:
            logger.info(solvent_obj, 'PBE Converged, max|drho(pol)| = %4.3e, max|drho(ions)| = %4.3e',
                        drho_pol.max(), drho_ions.max())
            return phi_tot, rho_ions, rho_pol
        iter += 1
    logger.info(solvent_obj, 'PBE failed to converge.')
    raise RuntimeError('PBE solver failed to converge. ' \
                       'Decreasing grid size might help convergence.')

class PBE(ddcosmo.DDCOSMO):
    _keys = {'cb', 'T', 'bias', 'stern_sam', 'delta1', 'delta2', 'eps_sam', 'probe', 'kappa', 'stern_mol', 'cation_rad', 'anion_rad', 'rho_sol', 'rho_ions', 'rho_pol', 'phi_pol', 'phi_tot', 'phi_sol', 'L', 'nelectron', 'phi_pol', 'thresh_pol', 'thresh_ions', 'thresh_amg', 'gpu_accel', 'cycle', 'atom_bottom', 'pzc', 'jump_coeff', 'ref_pot', 'solver', 'equiv'}
    def __init__(self, mol, cb=0.0, cation_rad=4.3, anion_rad=4.3, T=298.15, stern_mol=0.44, stern_sam=8.1, equiv=11, **kwargs):
        ddcosmo.DDCOSMO.__init__(self, mol)
        self.grids = Grids(mol, **kwargs)
        self.radii_table = VDW # in a.u.
        self.probe = 1.4 # in angstrom. Water (1.4 Å)
        self.stern_mol = stern_mol # in angstrom. Stein et al.
        self.stern_sam = stern_sam # in angstrom. SAM Stern layer length Hammes-Schiffer 2020
        self.eps_sam = 2.284 # Benzene
        self.delta1 = 0.265 # in angstrom. Arias 2005 paper
        self.delta2 = 0.265 # in angstrom. Stein et al.
        self.cb = cb # in mol/L
        self.T = T # Temperature in Kelvin.
        self.cation_rad = cation_rad # in angstrom
        self.anion_rad  = anion_rad # in angstrom
        self.pzc = -4.8 # in eV
        self.jump_coeff = 0.73115e0 # Jellium model with 1M electrolyte solution
        self.equiv = equiv

        self.kappa = None
        self.max_cycle = 200
        self.phi_tot = None
        self.phi_sol = None
        self.phi_pol = None
        self.rho_sol = None
        self.rho_ions = None
        self.rho_pol = None
        self.bias = None # Placeholder <- WBLMolecule
        self.nelectron = None # Placeholder <- WBLMolecule
        self.ref_pot = None # Placeholder <- WBLMolecule
        self.L = None
        self.thresh_pol = 1.0e-5
        self.thresh_ions = 1.0e-6
        self.thresh_amg = 1.0e-8 # Determined through numerical test. Lower threshold loses symmetry
        self.gpu_accel = False
        self.atom_bottom = None
        self.solver = None
        
    def dump_flags(self, verbose=None):
        logger.info(self, '******** %s ********', self.__class__)
        logger.info(self, 'Probe radius = %.5f Angstrom', self.probe)
        logger.info(self, 'Dielectric constant of the SAM = %.5f', self.eps_sam)
        logger.info(self, 'Dielectric constant of the solvent = %.5f', self.eps)
        logger.info(self, 'Broadening of the SAM Stern layer = %.5f Angstrom', self.delta1)
        logger.info(self, 'Broadening of the molecular Stern layer = %.5f Angstrom', self.delta2)
        logger.info(self, 'SAM Stern layer length = %.5f Angstrom', self.stern_sam)
        logger.info(self, 'Electrolyte concentration = %.5f mol/L', self.cb)
        logger.info(self, 'Electrolyte type = %d:%d (cation:anion)', self.equiv // 10, self.equiv % 10)
        logger.info(self, 'Temperature = %.5f Kelvin', self.T)
        logger.info(self, 'Potential of zero charge = %.5f V', self.pzc)
        logger.info(self, 'Box length = %.5f Angstrom', self.grids.length * BOHR)
        logger.info(self, 'Total grids = %d', self.grids.get_ngrids())
        logger.info(self, 'Polarization charge density threshold = %4.3e', self.thresh_pol)
        logger.info(self, 'Ion charge density threshold = %4.3e', self.thresh_ions)

    def _get_vind(self, dm):
        if not self._intermediates or self.grids.coords is None:
            self.build()
        if not (isinstance(dm, numpy.ndarray) and dm.ndim == 2):
            dm = dm[0] + dm[1]

        spacing = self.grids.spacing
        coords = self.grids.coords
        ngrids = self.grids.ngrids
        bias = self.bias / HARTREE2EV # in eV --> a.u.

        phi_sol = self.make_phi_sol(dm, coords)
        self.phi_sol = phi_sol
        rho_sol = self.make_rho_sol(phi_sol, ngrids, spacing)
        self.rho_sol = rho_sol
        phi_tot, rho_ions, rho_pol = self.make_phi(bias, phi_sol, rho_sol)
        self.phi_tot = phi_tot
        self.rho_pol = rho_pol
        self.rho_ions = rho_ions

        phi_pol = phi_tot - phi_sol
        self.phi_pol = phi_pol

        # Zero out the boundary values to eliminate error
        ngrids = self.grids.ngrids
        rho_sol = rho_sol.reshape((ngrids,)*3)
        idx = numpy.array([-4, -3, -2, -1, 0, 1, 2, 3])
        rho_sol[idx,:,:] = 0.0e0
        rho_sol[:,idx,:] = 0.0e0
        rho_sol[:,:,idx] = 0.0e0
        rho_sol = rho_sol.flatten()

        # Reaction field contribution
        Gsolv_elst = numpy.dot(rho_sol, phi_pol)*spacing**3

        # Dielectric contribution by Fisicaro
        Gsolv_diel = -0.5e0*(numpy.dot(rho_sol, phi_pol)
                           + numpy.dot(rho_ions, phi_tot))*spacing**3

        # Osmotic pressure contribution
        cb = self.cb * M2HARTREE
        lambda_r = self._intermediates['lambda_r']
        T = self.T
        if self.cb == 0.0e0:
            Gsolv_osm = 0.0e0
        else:
            Gsolv_osm = self.energy_osm(phi_tot, cb, lambda_r, T, spacing)

        logger.info(self, "E_es= %.15g, E_diel= %.15g, E_osm= %.15g", Gsolv_elst, Gsolv_diel, Gsolv_osm)

        Gsolv = Gsolv_elst + Gsolv_diel + Gsolv_osm
        vmat = self._get_vmat(phi_pol)
        return Gsolv, vmat

    def _get_vmat(self, phi_pol):
        logger.info(self, 'Constructing the correction to the Hamiltonian...')
        mol = self.mol
        coords = self.grids.coords
        spacing = self.grids.spacing
        nao = mol.nao

        vmat = numpy.zeros([nao, nao], order='C')
        max_memory = self.max_memory - lib.current_memory()[0]
        blksize = int(max(max_memory*.9e6/8/nao, 400))
        vmat = numpy.zeros([nao, nao], order='C')
        for p0, p1 in lib.prange(0, phi_pol.size, blksize):
            ao = mol.eval_gto('GTOval', coords[p0:p1])
            vmat -= 0.5e0*numpy.dot(ao.T * phi_pol[p0:p1], ao)
        vmat = vmat * spacing**3
        return vmat
    
    def _get_v(self):
        pass

    def build(self):
        if self.grids.coords is None:
            self.grids.build()
            atom_coords = self.mol.atom_coords()
            coords = self.grids.coords
            box_center = (coords.max(axis=0) + coords.min(axis=0)) / 2.0e0
            bottom_center = box_center.copy()
            bottom_center[2] = self.grids.coords[:,2].min()

            if self.atom_bottom != 'center':
                if self.atom_bottom is None:
                    atom_bottom = numpy.argmin(atom_coords, axis=0)[2]
                else:
                    atom_bottom = self.atom_bottom
                r = atom_coords[atom_bottom]
                atomic_radii = self.get_atomic_radii()
                r_atom_bottom = atomic_radii[atom_bottom]
                shift = r - bottom_center
                coords += shift - numpy.array([0.0e0, 0.0e0, r_atom_bottom])
                self.grids.coords = coords

        logger.info(self, 'Grid spacing = %.5f Angstrom', self.grids.spacing * BOHR)

        mol = self.mol
        coords = self.grids.coords
        ngrids = self.grids.ngrids
        spacing = self.grids.spacing
        probe = self.probe / BOHR # angstrom to a.u.
        stern_mol = self.stern_mol / BOHR # angstrom to a.u.
        stern_sam = self.stern_sam / BOHR # angstrom to a.u.
        delta1 = self.delta1 / BOHR # angstrom to a.u.
        delta2 = self.delta2 / BOHR # angstrom to a.u.
        atomic_radii = self.get_atomic_radii()
        eps_sam = self.eps_sam
        eps_bulk = self.eps
        cb = self.cb * M2HARTREE # mol/L to a.u.

        lambda_r = self.make_lambda(mol, probe, stern_mol, stern_sam, coords, delta1, delta2, atomic_radii)
        sas = self.make_sas(mol, probe, coords, delta2, atomic_radii)
        eps = self.make_eps(coords, eps_sam, eps_bulk, stern_sam, delta1, sas)
        grad_eps = self.make_grad_eps(mol, coords, eps_sam, eps_bulk, probe, stern_sam, delta1, delta2, atomic_radii, sas)

        if self.L is None:
            self.L = ch.poisson((ngrids,)*3, format='csr')

        self.kappa = numpy.sqrt(8.0e0 * PI * cb / self.eps / KB2HARTREE / self.T)
        self._intermediates = {
            'grids': self.grids.coords,
            'lambda_r': lambda_r,
            'eps': eps,
            'grad_eps': grad_eps,
            'sas': sas
        }
        if self.solver == 'fft2d':
            from fcdft.solvent.solver import fft2d
            self.solver = fft2d(ngrids=ngrids, spacing=spacing, verbose=self.verbose, stdout=self.stdout)
        else:
            from fcdft.solvent.solver import multigrid
            self.solver = multigrid(ngrids=ngrids, spacing=spacing, verbose=self.verbose, stdout=self.stdout)
        self.solver.build()
    
    def _gen_get_rho_ions(self):
        equiv = self.equiv
        if equiv == 11:
            from fcdft.solvent.ions import _one_to_one
            return _one_to_one
        elif equiv == 21:
            from fcdft.solvent.ions import _two_to_one
            return _two_to_one
        elif equiv == 12:
            from fcdft.solvent.ions import _one_to_two
            return _one_to_two
        else:
            raise NotImplementedError

    def _gen_boundary_conditions(self):
        equiv = self.equiv
        from fcdft.solvent import boundary
        if equiv == 11:
            return boundary.one_to_one_bc, boundary.one_to_one_bc_grad, boundary.one_to_one_bc_lap
        elif equiv == 21:
            return boundary.two_to_one_bc, boundary.two_to_one_bc_grad, boundary.two_to_one_bc_lap
        elif equiv == 12:
            return boundary.one_to_two_bc, boundary.one_to_two_bc_grad, boundary.one_to_two_bc_lap
        else:
            raise NotImplementedError

    def energy_osm(self, phi_tot=None, cb=None, lambda_r=None, T=None, spacing=None, equiv=None):
        if phi_tot is None: phi_tot = self.phi_tot
        if cb is None: cb = self.cb * M2HARTREE
        if lambda_r is None: lambda_r = self._intermediates['lambda_r']
        if T is None: T = self.T
        if spacing is None: spacing = self.grids.spacing
        if equiv is None: equiv = self.equiv
        from fcdft.solvent import ions
        if equiv == 11:
            return ions.one_to_one_energy_osm(self, phi_tot, cb, lambda_r, T, spacing)
        elif equiv == 21:
            return ions.two_to_one_energy_osm(self, phi_tot, cb, lambda_r, T, spacing)
        elif equiv == 12:
            return ions.one_to_two_energy_osm(self, phi_tot, cb, lambda_r, T, spacing)
        else:
            raise NotImplementedError
        
    def __setattr__(self, key, val):
        if key in ('radii_table', 'atom_radii', 'delta1', 'delta2', 'eps', 'stern', 'probe'):
            self.reset()
        super(PBE, self).__setattr__(key, val)


    def reset(self, mol=None):
        '''Reset mol and clean up relevant attributes for scanner mode'''
        if mol is not None:
            self.mol = mol
        self._intermediates = None
        return self

    def nuc_grad_method(self, grad_method):
        raise DeprecationWarning('Use the make_grad_object function from '
                                 'pyscf.solvent.grad.ddcosmo_grad or '
                                 'pyscf.solvent._ddcosmo_tdscf_grad instead.')
        
    def grad(self, dm):
        from fcdft.solvent.grad import pbe
        return pbe.kernel(self, dm, self.verbose)

    def to_gpu(self):
        self.gpu_accel = True
        return self
    
    make_lambda = make_lambda
    make_sas = make_sas
    make_eps = make_eps
    make_grad_eps = make_grad_eps
    make_phi_sol = make_phi_sol
    make_rho_sol = make_rho_sol
    make_phi = make_phi

class Grids(cubegen.Cube):
    def __init__(self, mol, ngrids=97, length=20):
        self.mol = mol
        self.ngrids=ngrids
        self.alignment = 0
        self.length = length / BOHR
        self.spacing = None
        self.coords = None
        self.verbose = mol.verbose
        self.center = None
        super().__init__(mol, nx=ngrids, ny=ngrids, nz=ngrids, margin=self.length/2, extent=[self.length, self.length, self.length])
        
    def get_coords(self):
        atom_coords = self.mol.atom_coords()
        self.center = (atom_coords.max(axis=0) + atom_coords.min(axis=0)) / 2.0e0
        xs, ys, zs = self.xs, self.ys, self.zs
        frac_coords = lib.cartesian_prod([xs, ys, zs])
        box_center = self.box.sum(axis=1) / 2.0e0
        return frac_coords @ self.box + (self.center - box_center)

    def dump_flags(self, verbose=None):
        logger.info(self, 'Grid spacing = %.5f Angstrom', self.grids.spacing * BOHR)

    def build(self, mol=None, *args, **kwargs):
        if mol is None: mol = self.mol
        self.coords = self.get_coords()
        self.boxorig = self.coords[0]
        self.spacing = self.length / (self.nx - 1)
        if self.spacing != self.length / (self.ny - 1) or self.spacing != self.length / (self.nz - 1):
            raise ValueError('Mismatch in ngrids. Current nx, ny, nz = %d, %d, %d' % (self.nx, self.ny, self.nz))
        return self

    def reset(self, mol=None):
        self.coords = None
        self.atom_coords = None
        self.center = None
        return self

if __name__=='__main__':
    from pyscf import gto
    from pyscf.dft import RKS
    mol = gto.M(
        atom='''
C       -1.1367537947      0.1104289172      2.4844663896
C       -1.1385831318      0.1723328088      3.8772156394
C        0.0819843127      0.0788096973      1.7730802291
H       -2.0846565855      0.1966185690      4.4236084687
C        0.0806058727      0.2041086872      4.5921211233
C        1.2993389981      0.1104289172      2.4844663896
H        2.2526138470      0.0865980845      1.9483127672
C        1.2994126658      0.1723829840      3.8783367991
H        2.2453411518      0.1966879024      4.4251589385
H       -2.0869454458      0.0863720324      1.9432143952
C        0.0810980584      0.2676328718      6.0213144069
N        0.0819851974      0.3199013851      7.1972568519
S        0.0000000000      0.0000000000      0.0000000000
H        1.3390319419     -0.0095801980     -0.2157234144''',
        charge=0, basis='6-31g**', verbose=5)
    mf = RKS(mol, xc='pbe')
    from fcdft.wbl.rks import *
    wblmf = WBLMoleculeRKS(mol, xc='pbe', broad=0.01, smear=0.2, nelectron=70.00, ref_pot=5.51)
    wblmf.pot_cycle=100
    wblmf.pot_damp=0.7
    wblmf.conv_tol=1e-7
    wblmf.kernel()
    dm = wblmf.make_rdm1()
    cm = PBE(mol, cb=1.0, length=20, ngrids=41, stern_sam=8.1, equiv=21)
    cm._dm = dm
    cm.atom_bottom=12
    cm.solver = 'multigrid'
    solmf = pbe_for_scf(wblmf, cm)
    solmf.kernel()