# Cython COLAMD python interface
#
# Part of the scikit-sparse project.
# Copyright (C) 2025 Bernard Roesler. All rights reserved.
# See pyproject.toml for full author list and LICENSE.txt for license details.
# SPDX-License-Identifier: BSD-2-Clause
#
# =============================================================================
#     File: colamd.pyx
#  Created: 2025-07-31 10:13
# =============================================================================

"""
============================================================================
Column Approximate Minimum Degree (COLAMD) Ordering (:mod:`sksparse.colamd`)
============================================================================

.. currentmodule:: sksparse.colamd

.. versionadded:: 0.5.0

Python interface to the `Column Approximate Minimum Degree (COLAMD)
<https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/COLAMD>`_ ordering
algorithm.


.. _colamd-interface:

Interface
---------

.. autosummary::
   :toctree: generated/

   colamd - Function to compute the column ordering of any shape sparse matrix.
   symamd - Function to compute the column ordering of a symmetric sparse matrix.
   colamd_get_defaults - Get the default knobs for COLAMD.


.. _colamd-exceptions:

Exceptions and Warnings
-----------------------

.. autosummary::
   :toctree: generated/

   COLAMDError - Base class for COLAMD errors.
   COLAMDValueError - Raised when COLAMD encounters a value error.
   COLAMDMemoryError - Raised when COLAMD runs out of memory.
   COLAMDInternalError - Raised when COLAMD encounters an internal error.
   COLAMDStats - Dataclass containing statistics about the ordering.


References
----------
* `SuiteSparse homepage <https://people.engr.tamu.edu/davis/suitesparse.html>`_
* `SuiteSparse COLAMD <https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/COLAMD>`_
* COLAMD Algorithm Publications:

  * T. A. Davis, J. R. Gilbert, S. Larimore, E. Ng, An approximate column
    minimum degree ordering algorithm, *ACM Transactions on Mathematical
    Software*, vol. 30, no. 3., pp. 353-376, 2004.

  * T. A. Davis, J. R. Gilbert, S. Larimore, E. Ng, Algorithm 836: COLAMD,
    an approximate column minimum degree ordering algorithm, *ACM
    Transactions on Mathematical Software*, vol. 30, no. 3., pp. 377-380,
    2004.

"""

from dataclasses import dataclass

import numpy as np
cimport numpy as np

from .utils import validate_csc_input

__all__ = [
    "COLAMDError",
    "COLAMDValueError",
    "COLAMDMemoryError",
    "COLAMDInternalError",
    "COLAMDStats",
    "colamd",
    "symamd",
    "colamd_get_defaults"
]


class COLAMDError(Exception):
    """Base class for COLAMD errors."""
    pass


class COLAMDValueError(COLAMDError, ValueError):
    """Raised when COLAMD encounters a value error."""
    pass


class COLAMDMemoryError(COLAMDError, MemoryError):
    """Raised when COLAMD runs out of memory."""
    pass


class COLAMDInternalError(COLAMDError, RuntimeError):
    """Raised when COLAMD encounters an internal error."""
    pass


# Define COLAMD error codes
_COLAMD_ERROR_CODES = dict({
    COLAMD_OK: "ok",
    COLAMD_OK_BUT_JUMBLED: "ok but A has unsorted columns or duplicate entries",
    COLAMD_ERROR_A_not_present: "A is a null pointer",
    COLAMD_ERROR_p_not_present: "p is a null pointer",
    COLAMD_ERROR_nrow_negative: "nrow is negative",
    COLAMD_ERROR_ncol_negative: "ncol is negative",
    COLAMD_ERROR_nnz_negative: "nnz is negative",
    COLAMD_ERROR_p0_nonzero: "p[0] is nonzero",
    COLAMD_ERROR_A_too_small: "A is too small",
    COLAMD_ERROR_col_length_negative: "column has a negative number of entries",
    COLAMD_ERROR_row_index_out_of_bounds: "row index out of bounds",
    COLAMD_ERROR_out_of_memory: "out of memory",
    COLAMD_ERROR_internal_error: "internal error"
})


@dataclass(frozen=True)
class COLAMDStats:
    """Information statistics returned by the COLAMD algorithm.

    This class wraps the contents of the ``stats`` array returned by
    C ``colamd()`` into a Python dataclass.

    Attributes
    ----------
    N_rows_ignored : int
        The number of dense or empty rows ignored in the ordering.
    N_cols_ignored : int
        The number of dense or empty columns ignored in the ordering.
    Ncmpa : int
        The number of garbage collections performed.
    status : int
        Status code indicating the result of the COLAMD operation. If non-zero,
        ``colamd`` will throw an appropriate exception that interprets this
        status code.

    The following fields take on different meanings depending on the value of
    ``status``:

    info1 : int
        Value of ``status``:

        * 0: the highest numbered column that is unsorted or has
          duplicate entries.
        * -3: the value of ``n_row``.
        * -4: the value of ``n_col``.
        * -5: the value of ``nnz == p[n_col]``.
        * -6: the value of ``p[0]``.
        * -7: the required ``Alen`` value.
        * -8: the column with negative entries.
        * -9: the column with a row index out of bounds.
    info2 : int
        Value of ``status``:

        * 0: the last seen duplicate or unsorted row index.
        * -7: the actual ``Alen`` value.
        * -9: the bad row index.
    info3 : int
        Value of ``status``:

        * 0: the number of duplicates or unsorted row indices.
        * -9: ``n_row``.

    Notes
    -----
    Field descriptions are adapted from SuiteSparse ``colamd.c``
    [#colamd_fields]_.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [#colamd_fields] ``colamd.c`` - SuiteSparse AMD source file.
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/COLAMD/Source/colamd.c
    """
    N_rows_ignored : int
    N_cols_ignored : int
    Ncmpa : int
    status : int
    info1 : int
    info2 : int
    info3 : int

    @classmethod
    def from_array(cls, stats: "np.ndarray") -> "COLAMDStats":
        """Create a COLAMDStats instance from an array."""
        return cls(
            N_rows_ignored=int(stats[COLAMD_DENSE_ROW]),
            N_cols_ignored=int(stats[COLAMD_DENSE_COL]),
            Ncmpa=int(stats[COLAMD_DEFRAG_COUNT]),
            status=int(stats[COLAMD_STATUS]),
            info1=int(stats[COLAMD_INFO1]),
            info2=int(stats[COLAMD_INFO2]),
            info3=int(stats[COLAMD_INFO3]),
        )


def _colamd_base(
    A,
    is_symmetric=False,
    dense_row_thresh=None,
    dense_col_thresh=None,
    aggressive=None,
    return_info=False
):
    """A common base function for colamd and symamd."""
    A, use_int32, out_itype = validate_csc_input(A, is_symmetric)

    M, N = A.shape

    if M == 0 or N == 0:
        return np.empty(0, dtype=out_itype)

    if A.nnz == 0 or (not is_symmetric and M == 1):
        return np.arange(N, dtype=out_itype)

    if N == 1:
        return np.zeros(N, dtype=out_itype)

    # Get the recommended size for the Alen array
    if use_int32:
        Alen = colamd_recommended(A.nnz, M, N)
    else:
        Alen = colamd_l_recommended(A.nnz, M, N)

    if Alen == 0:
        raise ValueError("Recommended Alen is zero: one of {A.nnz, M, N} is erroneous.")

    # Set the default knobs
    knobs = np.zeros(COLAMD_KNOBS, dtype=np.double)
    cdef double[::1] knobs_mv = knobs
    colamd_set_defaults(&knobs_mv[0])

    # Override with user knobs if provided
    if dense_row_thresh is not None:
        knobs[COLAMD_DENSE_ROW] = float(dense_row_thresh)

    if dense_col_thresh is not None:
        knobs[COLAMD_DENSE_COL] = float(dense_col_thresh)

    if aggressive is not None:
        knobs[COLAMD_AGGRESSIVE] = 1.0 if aggressive else 0.0

    # Declare typed memory views for Cython
    cdef int32_t[::1] Ai_mv_int32
    cdef int64_t[::1] Ai_mv_int64

    cdef int32_t[::1] p_mv_int32
    cdef int64_t[::1] p_mv_int64

    cdef int32_t[::1] perm_mv_int32
    cdef int64_t[::1] perm_mv_int64

    cdef int32_t[::1] stats_mv_int32
    cdef int64_t[::1] stats_mv_int64

    # Compute the ordering
    if use_int32:
        stats = stats_mv_int32 = np.zeros(COLAMD_STATS, dtype=np.int32)

        if is_symmetric:
            Ai_mv_int32 = A.indices
            p_mv_int32 = A.indptr
            perm_mv_int32 = np.zeros(N + 1, dtype=np.int32, order='C')
            ok = c_symamd(
                N,
                &Ai_mv_int32[0],
                &p_mv_int32[0],
                &perm_mv_int32[0],
                &knobs_mv[0],
                &stats_mv_int32[0],
                calloc,
                free
            )
            # Only take the first N entries of the permutation array
            q_slice = perm_mv_int32[:N]
        else:
            # Copy the arrays, since they are altered in the C function
            workspace = np.zeros(Alen, dtype=np.int32, order='C')
            workspace[:A.nnz] = A.indices.copy()
            Ai_mv_int32 = workspace
            p_mv_int32 = np.ascontiguousarray(A.indptr).copy()
            ok = c_colamd(
                M,
                N,
                Alen,
                &Ai_mv_int32[0],
                &p_mv_int32[0],
                &knobs_mv[0],
                &stats_mv_int32[0]
            )
            q_slice = p_mv_int32[:N]
    else:
        stats = stats_mv_int64 = np.zeros(COLAMD_STATS, dtype=np.int64)

        if is_symmetric:
            Ai_mv_int64 = A.indices
            p_mv_int64 = A.indptr
            perm_mv_int64 = np.zeros(N + 1, dtype=np.int64, order='C')
            ok = c_symamd_l(
                N,
                &Ai_mv_int64[0],
                &p_mv_int64[0],
                &perm_mv_int64[0],
                &knobs_mv[0],
                &stats_mv_int64[0],
                calloc,
                free
            )
            q_slice = perm_mv_int64[:N]
        else:
            # Copy the arrays, since they are altered in the C function
            workspace = np.zeros(Alen, dtype=np.int64, order='C')
            workspace[:A.nnz] = A.indices.copy()
            Ai_mv_int64 = workspace
            p_mv_int64 = np.ascontiguousarray(A.indptr).copy()
            ok = c_colamd_l(
                M,
                N,
                Alen,
                &Ai_mv_int64[0],
                &p_mv_int64[0],
                &knobs_mv[0],
                &stats_mv_int64[0]
            )
            q_slice = p_mv_int64[:N]

    # Check the return status
    if ok:
        assert stats[COLAMD_STATUS] == COLAMD_OK, \
            "COLAMD returned OK but status is not COLAMD_OK."
    else:
        if stats[COLAMD_STATUS] == COLAMD_ERROR_out_of_memory:
            raise COLAMDMemoryError("COLAMD ran out of memory.")
        elif stats[COLAMD_STATUS] == COLAMD_ERROR_internal_error:
            raise COLAMDInternalError("COLAMD encountered an internal error.")
        else:
            raise COLAMDValueError(
                f"COLAMD returned an error:{_COLAMD_ERROR_CODES[stats[COLAMD_STATUS]]}."
            )

    # Return the permutation array
    q = np.asarray(q_slice)

    if return_info:
        return q, COLAMDStats.from_array(stats)
    else:
        return q


def colamd(
    A,
    dense_row_thresh=None,
    dense_col_thresh=None,
    aggressive=None,
    return_info=False
):
    return _colamd_base(
        A,
        is_symmetric=False,
        dense_row_thresh=dense_row_thresh,
        dense_col_thresh=dense_col_thresh,
        aggressive=aggressive,
        return_info=return_info
    )


def symamd(
    A,
    dense_row_thresh=None,
    dense_col_thresh=None,
    aggressive=None,
    return_info=False
):
    return _colamd_base(
        A,
        is_symmetric=True,
        dense_row_thresh=dense_row_thresh,
        dense_col_thresh=dense_col_thresh,
        aggressive=aggressive,
        return_info=return_info
    )


_COLAMD_DOC_TEMPLATE = """
{intro}
Parameters
----------
{A_param}
dense_row_thresh, dense_col_thresh : float, optional
    Threshold for considering a row/column dense. If
    None, use the default value from COLAMD. The default value is 10.
    The actual number of entries in a row/column is to be considered
    "dense" is ``max(dense_row_thresh * sqrt(M), 16)`` where ``M`` is the
    number of rows (or ``N`` for columns). Dense rows/columns are ignored
    during ordering and moved to the end of the matrix.
aggressive : bool, optional
    If True, use aggressive absorption. If None, uses the default value
    from COLAMD. The default value is True.

Returns
-------
q : (N,) :class:`~numpy.ndarray`
    The permutation vector.
stats : :class:`COLAMDStats`, optional
    If ``return_info`` is True, returns an object containing statistics
    about the ordering.

See Also
--------
{see_also}


.. versionadded:: 0.5.0

References
----------
.. {reftag} ``colamd.c`` - SuiteSparse AMD source file.
    https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/COLAMD/Source/colamd.c

Examples
--------
{example}
"""

# Define the docstrings
_colamd_reftag = "[#colamd_c]"

_colamd_intro = f"""Compute the column approximate minimum degree ordering of
a sparse matrix.

Adapted from the COLAMD documentation {_colamd_reftag}_:

    This function computes a column ordering for a sparse matrix `A` that
    is appropriate for LU factorization of symmetric or unsymmetric
    matrices, QR factorization, least squares, interior point methods for
    linear programming problems, and other related problems.

    COLAMD computes a permutation `Q` such that the Cholesky factorization
    of :math:`(AQ)^{{\\top}}(AQ)` has less fill-in and requires fewer floating
    point operations than :math:`A^{{\\top}}A`.  This also provides a good
    ordering for sparse partial pivoting methods, :math:`P(AQ) = LU`, where
    `Q` is computed prior to numerical factorization, and `P` is computed
    during numerical factorization via conventional partial pivoting with
    row interchanges.
"""

_colamd_A_param = """A : (M, N) array_like or sparse matrix
    The input matrix for which to compute the column ordering.
    Must be 2D and convertible to CSC format. Need not be square."""

_colamd_example = """\
>>> import numpy as np
>>> from scipy.sparse import random_array
>>> from sksparse.colamd import colamd
>>> # Create a non-symmetric matrix
>>> N = 11
>>> rng = np.random.default_rng(56)
>>> A = random_array((N, N - 3), density=0.5, format='csc', rng=rng)
>>> A.setdiag(N)  # make the diagonal non-zero
>>> p, info = colamd(A, return_info=True)
>>> p
array([0, 3, 5, 6, 7, 1, 2, 4], dtype=int32)
>>> info
COLAMDStats(N_rows_ignored=0, N_cols_ignored=0, Ncmpa=0, status=0, info1=-1,
    info2=-1, info3=0)
"""

colamd.__doc__ = _COLAMD_DOC_TEMPLATE.format(
    intro=_colamd_intro,
    A_param=_colamd_A_param,
    see_also="symamd, ~sksparse.ccolamd.ccolamd, ~sksparse.ccolamd.csymamd",
    reftag=_colamd_reftag,
    example=_colamd_example,
)


# Define the docstring for symamd
_symamd_reftag = "[#symamd_c]"

_symamd_intro = f"""Compute the column approximate minimum degree ordering of
a sparse symmetric matrix.

Adapted from the COLAMD documentation {_symamd_reftag}_:

    This function computes an approximate minimum degree ordering for
    Cholesky factorization of symmetric matrices.

    Symamd computes a permutation `P` of a symmetric matrix `A` such that
    the Cholesky factorization of :math:`PAP^{{\\top}}` has less fill-in and
    requires fewer floating point operations than `A`.  Symamd constructs
    a matrix `M` such that :math:`M^{{\\top}}M` has the same nonzero pattern
    of `A`, and then orders the columns of `M` using colamd.  The column
    ordering of `M` is then returned as the row and column ordering `P` of
    `A`.
"""

_symamd_A_param = """A : (N, N) {array_like, sparse matrix}
    The input matrix for which to compute the column ordering.
    Must be 2D, square, and convertible to CSC format.

    .. note::

        This routine only accesses the lower triangular part of ``A``,
        which is *assumed* to be symmetric. If it is not, the results may
        be incorrect or undefined.

"""

_symamd_example = """\
>>> import numpy as np
>>> from scipy.sparse import random_array
>>> from sksparse.colamd import symamd
>>> # Create a non-symmetric matrix
>>> N = 11
>>> rng = np.random.default_rng(56)
>>> A = random_array((N, N - 3), density=0.5, format='csc', rng=rng)
>>> A.setdiag(N)           # make the diagonal non-zero
>>> A = (A.T @ A).tocsc()  # make it symmetric
>>> p, info = symamd(A, return_info=True)
>>> p
array([4, 6, 7, 0, 1, 2, 3, 5], dtype=int32)
>>> info
COLAMDStats(N_rows_ignored=0, N_cols_ignored=0, Ncmpa=0, status=0, info1=-1,
    info2=-1, info3=0)
"""

symamd.__doc__ = _COLAMD_DOC_TEMPLATE.format(
    intro=_symamd_intro,
    A_param=_symamd_A_param,
    see_also="colamd, ~sksparse.ccolamd.ccolamd, ~sksparse.ccolamd.csymamd",
    reftag=_symamd_reftag,
    example=_symamd_example,
)


def colamd_get_defaults():
    """Get the default knobs for COLAMD.

    Returns
    -------
    knobs : dict
        A dictionary containing the default knobs for COLAMD.

        The keys are:

        * 'dense_row_thresh': Threshold for considering a row/column dense.
          Rows with more than ``max(dense_row_thresh * sqrt(M), 16)`` entries
          are permuted to the end of the matrix.
        * 'dense_col_thresh': Like `dense_row_thresh`, but for columns.
        * 'aggressive': Default value for the aggressive knob.


    .. versionadded:: 0.5.0
    """
    knobs = np.zeros(COLAMD_KNOBS, dtype=np.double)
    cdef double[::1] knobs_mv = knobs
    colamd_set_defaults(&knobs_mv[0])
    return dict(
        dense_row_thresh=knobs[COLAMD_DENSE_ROW],
        dense_col_thresh=knobs[COLAMD_DENSE_COL],
        aggressive=knobs[COLAMD_AGGRESSIVE]
    )
