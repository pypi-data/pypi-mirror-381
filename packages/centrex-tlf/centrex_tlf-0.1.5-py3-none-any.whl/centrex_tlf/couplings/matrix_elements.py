import math
from functools import lru_cache
from typing import Dict, Tuple

import numpy as np
import numpy.typing as npt

from centrex_tlf import hamiltonian, states

__all__ = ["calculate_ED_ME_mixed_state", "ED_ME_coupled"]


def calculate_ED_ME_mixed_state(
    bra: states.CoupledState,
    ket: states.CoupledState,
    pol_vec: npt.NDArray[np.complex128] = np.array(
        [1.0, 1.0, 1.0], dtype=np.complex128
    ),
    reduced: bool = False,
    normalize_pol: bool = True,
) -> complex:
    ME = 0j

    # Transform to Omega basis if required. For the X state the basis is Coupled and
    # doesn't require to be transformed to the Omega basis, since Omega is 0.
    if bra.largest.basis is states.Basis.CoupledP:
        bra = bra.transform_to_omega_basis()
    if ket.largest.basis is states.Basis.CoupledP:
        ket = ket.transform_to_omega_basis()

    if normalize_pol:
        pol_vec /= np.linalg.norm(pol_vec)

    for amp_bra, basis_bra in bra.data:
        for amp_ket, basis_ket in ket.data:
            ME += (
                amp_bra.conjugate()
                * amp_ket
                * ED_ME_coupled(
                    basis_bra, basis_ket, pol_vec=tuple(pol_vec), rme_only=reduced
                )
            )

    return ME


@lru_cache(maxsize=int(1e6))
def ED_ME_coupled(
    bra: states.CoupledBasisState,
    ket: states.CoupledBasisState,
    pol_vec: Tuple[complex, complex, complex] = (1.0 + 0j, 1.0 + 0j, 1.0 + 0j),
    rme_only: bool = False,
) -> complex:
    """calculate electric dipole matrix elements between coupled basis states

    Args:
        bra (CoupledBasisState): coupled basis state object
        ket (CoupledBasisState): coupled basis state object
        pol_vec (Tuple[float, float, float]): polarization vector.
                                        Defaults to np.array([1,1,1]).
        rme_only (bool, optional): set True to return only reduced matrix
                                    element, otherwise angular component is
                                    included. Defaults to False.

    Returns:
        complex: electric dipole matrix element between bra en ket
    """

    # find quantum numbers for ground state
    F = bra.F
    mF = bra.mF
    J = bra.J
    F1 = bra.F1
    I1 = bra.I1
    I2 = bra.I2
    Omega = bra.Omega

    # find quantum numbers for excited state
    Fp = ket.F
    mFp = ket.mF
    Jp = ket.J
    F1p = ket.F1
    Omegap = ket.Omega

    # calculate the reduced matrix element
    # see Oskari Timgren's Thesis, page 131
    q = Omega - Omegap
    ME: complex = (
        (-1) ** (F1p + F1 + Fp + I1 + I2 - Omega)
        * math.sqrt(
            (2 * J + 1)
            * (2 * Jp + 1)
            * (2 * F1 + 1)
            * (2 * F1p + 1)
            * (2 * F + 1)
            * (2 * Fp + 1)
        )
        * hamiltonian.sixj_f(F1p, Fp, I2, F, F1, 1)
        * hamiltonian.sixj_f(Jp, F1p, I1, F1, J, 1)
        * hamiltonian.threej_f(J, 1, Jp, -Omega, q, Omegap)
        * float(np.abs(q) < 2)
    )

    # if we want the complete matrix element, calculate angular part
    if not rme_only:
        # calculate elements of the polarization vector in spherical basis
        ME *= angular_part(pol_vec, F, mF, Fp, mFp)

    # return the matrix element
    return ME


@lru_cache(maxsize=int(1e6))
def angular_part(
    pol_vec: Tuple[complex, complex, complex],
    F: int,
    mF: int,
    Fp: int,
    mFp: int,
) -> complex:
    """calculate polarization-dependent angular factor

    Args:
        pol_vec (Tuple[complex, complex, complex]): polarization vector
        F (int): total angular momentum quantum number
        mF (int): projection of total angular momentum
        Fp (int): total angular momentum quantum number of the final state
        mFp (int): projection of total angular momentum of the final state

    Returns:
        complex: angular factor ⟨F,mF| e_q·r |F',mF'⟩ with q = mF - mF'
    """
    # Cartesian → spherical-basis components
    p_vec: Dict[int, complex] = {
        +1: -1 / math.sqrt(2) * (pol_vec[0] + 1j * pol_vec[1]),  # σ⁺
        0: pol_vec[2],  # π
        -1: 1 / math.sqrt(2) * (pol_vec[0] - 1j * pol_vec[1]),  # σ⁻
    }

    # q that connects the two Zeeman sub-levels
    p = mF - mFp
    if abs(p) > 1:
        return 0.0

    angular = (-1) ** (F - mF) * hamiltonian.threej_f(F, 1, Fp, -mF, p, mFp) * p_vec[p]
    return angular
