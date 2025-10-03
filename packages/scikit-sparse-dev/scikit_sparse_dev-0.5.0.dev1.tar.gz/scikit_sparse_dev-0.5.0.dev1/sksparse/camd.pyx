# Cython CAMD public Python interface
#
# Part of the scikit-sparse project.
# Copyright (C) 2025 Bernard Roesler
# See pyproject.toml for full author list and LICENSE.txt for license details.
# SPDX-License-Identifier: BSD-2-Clause
#
# =============================================================================
#     File: camd.pyx
#  Created: 2025-08-01 13:04
# =============================================================================

"""
=============================================================================
Constrained Approximate Minimum Degree (CAMD) Ordering (:mod:`sksparse.camd`)
=============================================================================

.. versionadded:: 0.5.0

Python interface to the `Constrained Approximate Minimum Degree (CAMD)
<https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/CAMD>`_ ordering
algorithm.


.. _camd-interface:

Interface
---------

.. autosummary::
   :toctree: generated/

   CAMDInfo - Dataclass to hold information statistics returned by the CAMD algorithm.
   camd - Main function to compute the CAMD ordering.
   camd_default_control - Get the default control parameters for CAMD.


.. _camd-exceptions:

Exceptions and Warnings
-----------------------

.. autosummary::
   :toctree: generated/

   CAMDError - Base class for CAMD-related errors.
   CAMDInvalidMatrixError - Raised when the input matrix is invalid for CAMD.
   CAMDMemoryError - Raised when CAMD runs out of memory.


References
----------
* `SuiteSparse homepage <https://people.engr.tamu.edu/davis/suitesparse.html>`_
* `SuiteSparse CAMD <https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/CAMD>`_
* AMD Algorithm Publication:
  Amestoy, P. R., Davis, T. A., & Duff, I. S. (1996). An approximate minimum
  degree ordering algorithm. *SIAM Journal on Matrix Analysis and Applications*,
  17(4), 886-905.
"""

from dataclasses import dataclass

import numpy as np
cimport numpy as np

from .utils import validate_csc_input

__all__ = [
    "CAMDError",
    "CAMDInvalidMatrixError",
    "CAMDMemoryError",
    "CAMDInfo",
    "camd",
    "camd_default_control"
]



class CAMDError(Exception):
    """Base class for CAMD-related errors."""
    pass


class CAMDInvalidMatrixError(CAMDError, ValueError):
    """Raised when the input matrix is invalid for CAMD."""
    pass


class CAMDMemoryError(CAMDError, MemoryError):
    """Raised when CAMD runs out of memory."""
    pass


@dataclass(frozen=True)
class CAMDInfo:
    """Information statistics returned by the CAMD algorithm.

    This class wraps the contents of the ``Info`` array output by
    ``camd_order()`` into a Python dataclass.

    Attributes
    ----------
    status : int
        Return status:
          * 0 = OK,
          * 1 = OK but jumbled,
          * -1 = out of memory,
          * -2 = invalid matrix.
    N : int
        Number of rows and columns of the input matrix ``A``.
    nz : int
        Number of nonzeros in the input matrix ``A``.
    symmetry : :class:`float` :math:`\in [0, 1]`
        Symmetry of pattern of ``A``. The symmetry is the number of "matched"
        off-diagonal entries divided by the total number of off-diagonal
        entries. An entry ``A[i, j]`` is matched if ``A[j, i]`` is also an
        entry, for any pair ``[i, j]`` where ``i != j``. In python code:

        .. code:: python

            S = A.astype(bool)
            B = sparse.tril(S, -1) + sparse.triu(S, 1)
            symmetry = (B * B.T).nnz / B.nnz

    nzdiag : int
        Number of entries on the diagonal of ``A``.
    nz_A_plus_AT : int
        Number of nonzeros in ``A + A.T`` (excluding diagonal).
        If ``A`` is perfectly symmetric (``symmetry = 1``), with a fully
        non-zero diagonal, then ``nz_A_plus_AT = nz - N`` (the smallest
        possible value).
        If ``A`` is perfectly unsymmetric (``symmetry = 0``, for an upper
        triangular matrix, *e.g.*) with no diagonal,
        then ``nz_A_plus_AT = 2 * nz`` (the largest possible value).
    Ndense : int
        Number of dense rows/columns ignored during ordering. These
        rows/columns are placed last in the output order ``p``.
    memory : float
        Memory used, in bytes. This is equal to:
        ``(1.2 * nz_A_plus_AT + 9 * N) * sizeof(int)``. This coefficient is at
        most ``2.4 * nz + 9 * N``. This accounting excludes the size of the
        input arguments ``Ap``, ``Ai``, and ``p``, which have a total size of
        ``nz + 2 * N + 1`` integers.
    Ncmpa : int
        Number of components in the matrix (excluding dense rows/columns).
    Lnz : int
        Number of nonzeros in the Cholesky factor ``L`` of ``A``, excluding
        the diagonal. This is a slight upper bound because of the approximate
        degree algorithm. It is a rough upper bound if there are many dense
        rows/columns. The remaining statistics are also slight or rough upper
        bounds for the same reason.
    Ndiv : int
        Number of division operations for LU or Cholesky factorization of the
        permuted matrix ``A[p][:, p]``.
    Nmultsubs_LDL : int
        Number of multiply-subtract pairs for ``LDL.T`` factorization.
    Nmultsubs_LU : int
        Number of multiply-subtract pairs for LU factorization, assuming that
        no numerical pivoting is required.
    dmax : int
        Maximum number of nonzeros in any column of ``L``, including the
        diagonal.

    Notes
    -----
    Field descriptions are adapted from SuiteSparse ``camd.h`` [#camd_h]_.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [#camd_h] ``camd.h`` - SuiteSparse CAMD header file.
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/CAMD/Include/camd.h
    """
    status: int
    N: int
    nz: int
    symmetry: float
    nzdiag: int
    nz_A_plus_AT: int
    Ndense: int
    memory: float
    Ncmpa: int
    Lnz: int
    Ndiv: int
    Nmultsubs_LDL: int
    Nmultsubs_LU: int
    dmax: int

    @classmethod
    def from_array(cls, info: "np.ndarray") -> "CAMDInfo":
        return cls(
            status=int(info[CAMD_STATUS]),
            N=int(info[CAMD_N]),
            nz=int(info[CAMD_NZ]),
            symmetry=float(info[CAMD_SYMMETRY]),
            nzdiag=int(info[CAMD_NZDIAG]),
            nz_A_plus_AT=int(info[CAMD_NZ_A_PLUS_AT]),
            Ndense=int(info[CAMD_NDENSE]),
            memory=float(info[CAMD_MEMORY]),
            Ncmpa=int(info[CAMD_NCMPA]),
            Lnz=int(info[CAMD_LNZ]),
            Ndiv=int(info[CAMD_NDIV]),
            Nmultsubs_LDL=int(info[CAMD_NMULTSUBS_LDL]),
            Nmultsubs_LU=int(info[CAMD_NMULTSUBS_LU]),
            dmax=int(info[CAMD_DMAX]),
        )


def camd(A, constraints=None, dense_thresh=None, aggressive=None, return_info=False):
    """Compute the approximate minimum degree ordering of a sparse matrix.

    Adapted from the SuiteSparse `camd.h` documentation [0]_:

        CAMD finds a fill-reducing ordering of a sparse matrix ``A``,
        using the approximate minimum degree algorithm. The output is
        a permutation vector ``p`` such that the Cholesky factor of
        ``A[p][:, p]`` has fewer nonzeros than the Cholesky factor of ``A``.
        If ``A`` is not symmetric, the algorithm computes an ordering of
        ``A + A.T``.

    For more details on the entire package, see the SuiteSparse homepage [1]_
    and Github repository [2]_.

    Parameters
    ----------
    A : (N, N) array_like or sparse matrix
        A square matrix in CSC format or convertible to CSC.
    contraints : (N,) array_like, optional
        A 1D array of constraints for the ordering. Each node `i` in the graph
        of `A` has a constraint, ``constraints[i]``, in the range [0, N-1]. All
        nodes with ``constraints[i] = 0`` are ordered first, followed by nodes
        with `C(i) = 1`, and so on. Thus, ``constraints[p]`` is monotonically
        non-decreasing. If None, no constraints are applied, and the ordering
        will be similar to :func:`~sksparse.amd.amd`, except that the
        post-ordering is different.
    dense_thresh : float, optional
        Threshold number of entries for considering a row/column dense. If
        None, use the default value from CAMD. The default value is 10.

        Adapted from the SuiteSparse `camd.h` documentation [0]_:

            A dense row/column in ``A + A.T`` can cause CAMD to spend a lot of
            time in ordering the matrix. If ``dense_thresh >= 0``, rows/columns
            with more than ``max(dense_thresh * sqrt(N), 16)`` entries are
            ignored during the ordering, and placed last in the output order.
            The default value of ``dense_thresh`` is 10. If negative, no
            rows/columns are treated as "dense". Rows/columns with 16 or fewer
            off-diagonal entries are never considered "dense".

    aggressive : bool, optional
        If True, use aggressive absorption. If None, uses the default value
        from CAMD. The default value is True.

        Adapted from the SuiteSparse `camd.h` documentation [0]_:

            Controls whether or not to use aggressive absorption, in which
            a prior element is absorbed into the current element if is a subset
            of the current element, even if it is not adjacent to the current
            pivot element (refer to Amestoy, Davis, & Duff, 1996, for more
            details). The default value is ``True``, which means to perform
            aggressive absorption. This nearly always leads to a better
            ordering (because the approximate degrees are more accurate) and
            a lower execution time. There are cases where it can lead to
            a slightly worse ordering, however.

    return_info : bool, optional
        If True, returns additional information about the ordering process.
        Default is False.

    Returns
    -------
    p : ndarray
        The permutation vector such that the Cholesky factor of ``A[p][:, p]``
        has fewer nonzeros than the Cholesky factor of ``A``.
    info : ndarray, optional
        Additional information about the ordering process, returned if
        ``return_info`` is True. Contains various statistics and status codes.

    Raises
    ------
    ~scipy.sparse.SparseEfficiencyWarning
        If the input matrix is not in CSC format, a warning is raised and the
        matrix is converted to CSC format.
    ValueError
        If the input matrix is not square or cannot be converted to CSC format.
    CAMDInvalidMatrixError
        If the input matrix is invalid for CAMD, such as having unsupported
        data types or formats.
    CAMDMemoryError
        If the CAMD algorithm runs out of memory during execution.

    See Also
    --------
    ~sksparse.amd.amd, ~sksparse.colamd.colamd, ~sksparse.ccolamd.ccolamd

    Notes
    -----
    This function wraps the CAMD (Approximate Minimum Degree) algorithm from
    the SuiteSparse by Timothy A. Davis. For details, see the SuiteSparse
    repository [2]_.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [0] `camd.h` - Source header file from SuiteSparse.
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/CAMD/Include/camd.h
    .. [1] SuiteSparse homepage.
        https://people.engr.tamu.edu/davis/suitesparse.html
    .. [2] SuiteSparse GitHub repository.
        https://github.com/DrTimothyAldenDavis/SuiteSparse

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import coo_array
    >>> from sksparse.camd import camd
    >>> # Create a symmetric positive definite matrix from (Davis, Eqn 2.1)
    >>> N = 11
    >>> rows = np.array([5, 6, 2, 7, 9, 10, 5, 9, 7, 10, 8, 9, 10, 9, 10, 10])
    >>> cols = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 9])
    >>> rng = np.random.default_rng(565656)
    >>> vals = rng.random(len(rows), dtype=np.float64)
    >>> L = coo_array((vals, (rows, cols)), shape=(N, N))
    >>> A = L + L.T   # make it symmetric
    >>> A.setdiag(N)  # make it strongly positive definite
    >>> A = A.tocsc()
    >>> # Constrain the first K nodes to be ordered first
    >>> K = 4
    >>> C = np.full(N, K)
    >>> C[:K] = np.arange(K)  # constrained nodes
    >>> p, info = camd(A, constraints=C, return_info=True)
    >>> p
    array([ 0,  1,  2,  3,  8,  5,  6,  9,  4, 10,  7])
    >>> info
    CAMDInfo(status=0, N=11, nz=43, symmetry=1.0, nzdiag=11, nz_A_plus_AT=32,
        Ndense=0, memory=1248.0, Ncmpa=0, Lnz=19, Ndiv=19, Nmultsubs_LDL=29,
        Nmultsubs_LU=39, dmax=4)
    """
    A, use_int32, out_itype = validate_csc_input(A, require_square=True)

    N = A.shape[0]

    if N == 0:
        return np.empty(0, dtype=out_itype)

    if A.nnz == 0:
        return np.arange(N, dtype=out_itype)

    # Declare typed memory views for Cython
    cdef const int32_t[::1] Ap_mv_int32, Ai_mv_int32, constraints_mv_int32
    cdef int32_t[::1] p_mv_int32

    cdef const int64_t[::1] Ap_mv_int64, Ai_mv_int64, constraints_mv_int64
    cdef int64_t[::1] p_mv_int64

    # Always ensure arrays are contiguous and correct dtype
    if use_int32:
        Ap_mv_int32 = A.indptr
        Ai_mv_int32 = A.indices
        p = p_mv_int32 = np.empty(N, dtype=np.int32)
    else:
        Ap_mv_int64 = A.indptr
        Ai_mv_int64 = A.indices
        p = p_mv_int64 = np.empty(N, dtype=np.int64)

    # Prepare control parameters
    ctrl = np.empty(CAMD_CONTROL, dtype=np.double)
    cdef double[::1] ctrl_mv = ctrl

    camd_defaults(&ctrl_mv[0])

    # Update the defaults with user control parameters
    if dense_thresh is not None:
        ctrl[CAMD_DENSE] = float(dense_thresh)

    if aggressive is not None:
        ctrl[CAMD_AGGRESSIVE] = 1.0 if aggressive else 0.0

    info = np.zeros(CAMD_INFO, dtype=np.double)
    cdef double[::1] info_mv = info

    # Prepare constraints
    # Use a raw pointer to pass NULL if no constraints are given
    cdef const int32_t* C_ptr_int32 = NULL
    cdef const int64_t* C_ptr_int64 = NULL

    if constraints is not None:
        try:
            constraints = np.asarray(
                constraints,
                dtype=np.int32 if use_int32 else np.int64,
                order='C'
            )
        except ValueError:
            raise ValueError("Constraints must be an array of integers.")

        if len(constraints) != N:
            raise ValueError(
                "Constraints must have the same length as the matrix size."
            )

        if use_int32:
            constraints_mv_int32 = constraints
            C_ptr_int32 = &constraints_mv_int32[0]
        else:
            constraints_mv_int64 = constraints
            C_ptr_int64 = &constraints_mv_int64[0]

    # CAMD ordering
    if use_int32:
        status = camd_order(
            N,
            &Ap_mv_int32[0],
            &Ai_mv_int32[0],
            &p_mv_int32[0],
            &ctrl_mv[0],
            &info_mv[0],
            C_ptr_int32
        )
    else:
        status = camd_l_order(
            N,
            &Ap_mv_int64[0],
            &Ai_mv_int64[0],
            &p_mv_int64[0],
            &ctrl_mv[0],
            &info_mv[0],
            C_ptr_int64
        )

    if status == CAMD_OUT_OF_MEMORY:
        raise CAMDMemoryError("camd: out of memory")
    elif status == CAMD_INVALID:
        dump_info = CAMDInfo.from_array(info)
        raise CAMDInvalidMatrixError(f"camd: input matrix A is invalid:\n{dump_info}")

    if return_info:
        return p, CAMDInfo.from_array(info)
    else:
        return p


def camd_default_control():
    """Get the default control parameters for CAMD.

    Returns
    -------
    control : dict
        A dictionary containing the default control parameters for CAMD.

        The keys are:

        * 'dense_thresh': Threshold for considering a row/column dense. Rows or
          columns with more than ``max(dense_thresh * sqrt(N), 16)`` entries
          are permuted to the end of the matrix.
        * 'aggressive': Whether to use aggressive absorption.


    .. versionadded:: 0.5.0
    """
    cdef double[::1] ctrl_mv = np.empty(CAMD_CONTROL, dtype=np.float64)
    camd_defaults(&ctrl_mv[0])
    return dict(
        dense_thresh=ctrl_mv[CAMD_DENSE],
        aggressive=bool(ctrl_mv[CAMD_AGGRESSIVE]),
    )
