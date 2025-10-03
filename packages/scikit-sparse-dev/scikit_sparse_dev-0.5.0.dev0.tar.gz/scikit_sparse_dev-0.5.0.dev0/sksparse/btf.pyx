# Part of the scikit-sparse project.
# Copyright (C) 2025 Bernard Roesler. All rights reserved.
# See pyproject.toml for full author list and LICENSE.txt for license details.
# SPDX-License-Identifier: BSD-2-Clause
#
# =============================================================================
#     File: btf.pyx
#  Created: 2025-08-04 20:22
# =============================================================================

"""
=================================================
Block Triangular Form (BTF) (:mod:`sksparse.btf`)
=================================================

.. currentmodule:: sksparse.btf

.. versionadded:: 0.5.0

Python interface to the `Block Triangular Format (BTF)
<https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/BTF>`_ library.


Interface
---------

.. autosummary::
   :toctree: generated/

   maxtrans - Maximum transversal of a sparse matrix.
   strongcomp - Strongly connected components of a directed graph.
   btf - Permutation into Block Triangular Form (BTF).
   btf_q_permutation - Convert raw BTF column permutation to valid permutation.


References
----------
* `SuiteSparse homepage <https://people.engr.tamu.edu/davis/suitesparse.html>`_
* `SuiteSparse BTF <https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/BTF>`_
* Duff, Iain. "On Algorithms for Obtaining a Maximum Transversal", *ACM Trans.
  Mathematical Software*, vol 7, no. 1, pp. 315-330.
* "Algorithm 575: Permutations for a Zero-Free Diagonal", *ACM Trans.
  Mathematical Software*, vol 7, no. 1, pp. 387-390. Algorithm 575 is MC21A in
  the Harwell Subroutine Library.
"""

import numpy as np
cimport numpy as np

from .utils import validate_csc_input

__all__ = ['maxtrans', 'strongcomp', 'btf', 'btf_q_permutation']


def maxtrans(A):
    """Compute the maximum transversal of a sparse matrix.

    This function finds a permutation of the columns of a sparse matrix
    so that it has a zero-free diagonal, if possible [#maxtrans_h]_.

    Parameters
    ----------
    A : (M, N) {array-like, sparse array}
        An array convertible to a sparse matrix in Compressed Sparse Column
        (CSC) format.

    Returns
    -------
    jmatch : (M,) ndarray
        Array containing the maximum transversal.

        Adapted from the BTF maxtrans documentation [#maxtrans_h]_:

            The output is an array ``jmatch`` of size ``N``.  If row ``i`` is
            matched with column ``j``, then ``A[i, j]`` is nonzero, and then
            ``jmatch[i] = j``.  If the matrix is structurally nonsingular, all
            entries in the ``jmatch`` array are unique, and ``jmatch`` can be
            viewed as a column permutation if `A` is square.  That is, column
            `k` of the original matrix becomes column ``jmatch[k]`` of the
            permuted matrix.

            If row ``i`` is not matched with any column,
            then ``jmatch[i] = -1``.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [#maxtrans_h] BTF maxtrans header file:
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/BTF/Include/btf.h

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import random_array
    >>> from sksparse.btf import maxtrans
    >>> # Create a non-symmetric matrix
    >>> N = 11
    >>> rng = np.random.default_rng(56)
    >>> A = random_array((N, N - 3), density=0.5, format='csc', rng=rng)
    >>> jmatch = maxtrans(A)
    >>> jmatch
    array([ 0,  2,  1,  3,  4,  5,  7, -1,  6, -1, -1], dtype=int32)
    """
    A, use_int32, out_itype = validate_csc_input(A)

    M, N = A.shape

    if M == 0 or N == 0:
        return np.empty(0, dtype=out_itype)

    if A.nnz == 0:
        return np.full(M, -1, dtype=out_itype)

    # Declare typed memory views for Cython
    cdef int32_t[::1] Ap_mv_int32
    cdef int32_t[::1] Ai_mv_int32
    cdef int32_t[::1] Match_mv_int32
    cdef int32_t[::1] Work_mv_int32

    cdef int64_t[::1] Ap_mv_int64
    cdef int64_t[::1] Ai_mv_int64
    cdef int64_t[::1] Match_mv_int64
    cdef int64_t[::1] Work_mv_int64

    if use_int32:
        Ap_mv_int32 = A.indptr
        Ai_mv_int32 = A.indices
        jmatch = Match_mv_int32 = np.zeros(M, dtype=np.int32)
        Work_mv_int32 = np.zeros(5 * N, dtype=np.int32)
    else:
        Ap_mv_int64 = A.indptr
        Ai_mv_int64 = A.indices
        jmatch = Match_mv_int64 = np.zeros(M, dtype=np.int64)
        Work_mv_int64 = np.zeros(5 * N, dtype=np.int64)

    # Initialize output variable
    cdef double work
    maxwork = 0  # TODO default value?

    if use_int32:
        nnz_diag = btf_maxtrans(
            M,
            N,
            &Ap_mv_int32[0],
            &Ai_mv_int32[0],
            maxwork,
            &work,
            &Match_mv_int32[0],
            &Work_mv_int32[0]
        )
    else:
        nnz_diag = btf_l_maxtrans(
            M,
            N,
            &Ap_mv_int64[0],
            &Ai_mv_int64[0],
            maxwork,
            &work,
            &Match_mv_int64[0],
            &Work_mv_int64[0]
        )

    if nnz_diag < 0:
        raise ValueError(f"BTF maxtrans failed with error code: {nnz_diag}")

    return jmatch


def strongcomp(A, qin=None):
    """Compute the strongly connected components of a directed graph.

    This function finds a symmetric permutation of a sparse matrix so that
    ``A[p][:, p]`` is block upper triangular form [#strongcomp_h]_.

    Parameters
    ----------
    A : (N, N) {array-like, sparse array}
        An array convertible to a sparse matrix in Compressed Sparse Column
        (CSC) format. Must be square.
    qin : (N,) ndarray of int, optional
        A permutation vector. If provided, find the strongly connected
        components of ``A[:, qin]``.

    Returns
    -------
    p : (N,) ndarray of int
        The permutation vector such that ``A[p][:, p]`` is in block upper
        triangular form, unless ``q`` is provided (see below).
    q : (N,) ndarray of int, optional
        If ``q`` is provided on input, ``A[p][:, q]`` is in block upper
        triangular form.
    r : (Nb+1,) ndarray of int
        The array of indices of the start of each block in the permuted matrix.
        Block ``b`` is in rows/columns ``r[b]`` to ``r[b+1] - 1``.
        The number of blocks is ``len(r) - 1``.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [#strongcomp_h] BTF strongcomp header file:
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/BTF/Include/btf.h

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import random_array, block_diag
    >>> from sksparse.btf import strongcomp
    >>> # Create a matrix with at least 2 strongly connected components
    >>> M, N = 4, 7
    >>> rng = np.random.default_rng(56)
    >>> A0 = random_array((M, M), density=0.5, rng=rng)
    >>> A1 = random_array((N, N), density=0.5, rng=rng)
    >>> A = block_diag((A0, A1), format='csc')
    >>> # The first M rows/columns are ordered together, then the last N
    >>> p, r = strongcomp(A)
    array([ 0,  1,  3,  2, 10,  4,  5,  6,  7,  8,  9], dtype=int32)
    >>> r
    array([ 0,  3,  4,  5, 11], dtype=int32)
    """
    A, use_int32, out_itype = validate_csc_input(A, require_square=True)

    N = A.shape[0]

    if N == 0:
        p = np.empty(0, dtype=out_itype)
        r = np.zeros(1, dtype=out_itype)  # no blocks
        if qin is not None:
            q = np.empty(0, dtype=out_itype)
            return p, q, r
        else:
            return p, r

    if A.nnz == 0:
        p = np.arange(N, dtype=out_itype)
        r = np.zeros(N + 1, dtype=out_itype)
        r[-1] = N  # N blocks of size 1
        if qin is not None:
            q = np.arange(N, dtype=out_itype)
            return p, q, r
        else:
            return p, r

    # Declare typed memory views for Cython
    cdef int32_t[::1] Ap_mv_int32
    cdef int32_t[::1] Ai_mv_int32
    cdef int32_t[::1] P_mv_int32
    cdef int32_t[::1] Q_mv_int32
    cdef int32_t[::1] R_mv_int32
    cdef int32_t[::1] Work_mv_int32

    cdef int64_t[::1] Ap_mv_int64
    cdef int64_t[::1] Ai_mv_int64
    cdef int64_t[::1] P_mv_int64
    cdef int64_t[::1] Q_mv_int64
    cdef int64_t[::1] R_mv_int64
    cdef int64_t[::1] Work_mv_int64

    # Use a NULL pointer for Q if qin is not provided
    cdef int32_t* Q_ptr_int32 = NULL
    cdef int64_t* Q_ptr_int64 = NULL

    if qin is not None:
        try:
            q = np.ascontiguousarray(qin, dtype=np.int32 if use_int32 else np.int64)
        except ValueError:
            raise ValueError("qin must be an integer array.")

        if len(q) != N:
            raise ValueError("qin must have the same length"
                             "as the number of columns in A.")

        if use_int32:
            Q_mv_int32 = q
            Q_ptr_int32 = &Q_mv_int32[0]
        else:
            Q_mv_int64 = q
            Q_ptr_int64 = &Q_mv_int64[0]

    # Assign memory for the input/output arrays
    if use_int32:
        Ap_mv_int32 = A.indptr
        Ai_mv_int32 = A.indices
        p = P_mv_int32 = np.zeros(N, dtype=np.int32)
        R_mv_int32 = np.zeros(N + 1, dtype=np.int32)
        Work_mv_int32 = np.zeros(4 * N, dtype=np.int32)
    else:
        Ap_mv_int64 = A.indptr
        Ai_mv_int64 = A.indices
        p = P_mv_int64 = np.zeros(N, dtype=np.int64)
        R_mv_int64 = np.zeros(N + 1, dtype=np.int64)
        Work_mv_int64 = np.zeros(4 * N, dtype=np.int64)

    if use_int32:
        nblocks = btf_strongcomp(
            N,
            &Ap_mv_int32[0],
            &Ai_mv_int32[0],
            Q_ptr_int32,
            &P_mv_int32[0],
            &R_mv_int32[0],
            &Work_mv_int32[0]
        )
    else:
        nblocks = btf_l_strongcomp(
            N,
            &Ap_mv_int64[0],
            &Ai_mv_int64[0],
            Q_ptr_int64,
            &P_mv_int64[0],
            &R_mv_int64[0],
            &Work_mv_int64[0]
        )

    if nblocks < 0:
        raise ValueError(f"BTF strongcomp failed with error code: {nblocks}")

    # Take only the first nblocks of r
    if use_int32:
        r_slice = R_mv_int32[:nblocks + 1]
    else:
        r_slice = R_mv_int64[:nblocks + 1]

    r = np.asarray(r_slice)

    if qin is not None:
        return p, q, r
    else:
        return p, r


def btf(A):
    """Permute the square sparse matrix into Block Triangular Form (BTF).

    This function finds a permutation of a sparse matrix so that
    `PAQ` (``A[p][:, q]``) is block upper triangular form with a zero-free
    diagonal, or with a maximum number of nonzeros on the diagonal if
    a zero-free permutation does not exist [#btf_h]_.

    Parameters
    ----------
    A : (N, N) {array-like, sparse array}
        An array convertible to a sparse matrix in Compressed Sparse Column
        (CSC) format. Must be square.

    Returns
    -------
    p : (N,) ndarray of int
        The row permutation vector such that ``A[p][:, q]`` is in block upper
        triangular form.
    q : (N,) ndarray of int
        The column permutation vector. If ``A`` is structurally nonsingular,
        ``A[p][:, q]`` has a zero-free diagonal. If ``A`` is structurally
        singular, ``q`` will contain negative entries. The permuted matrix
        is ``A[p][:, abs(q)]``. If ``q[k] < 0``, then ``PAQ[k, k]`` is zero.
    r : (Nb+1,) ndarray of int
        The array of indices of the start of each block in the permuted matrix.
        Block ``b`` is in rows/columns ``r[b]`` to ``r[b+1] - 1``.
        The number of blocks is ``len(r) - 1``.

    Notes
    -----
    Adapted from the BTF documentation [#btf_h]_:

        The function finds a maximum matching (or perhaps a limited matching if
        the work is limited), via the :func:`.maxtrans` function. If a complete
        matching is not found, :func:`.btf` completes the permutation, but
        flags the columns of ``A[p][:, q]`` to denote which columns are not
        matched. If the matrix is structurally rank deficient, some of the
        entries on the diagonal of the permuted matrix will be zero.

    .. versionadded:: 0.5.0

    References
    ----------
    .. [#btf_h] BTF header file:
        https://github.com/DrTimothyAldenDavis/SuiteSparse/blob/dev/BTF/Include/btf.h

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import random_array, block_diag
    >>> from sksparse.btf import btf
    >>> # Create a matrix with at least 2 strongly connected components
    >>> M, N = 4, 7
    >>> rng = np.random.default_rng(56)
    >>> A0 = random_array((M, M), density=0.5, rng=rng)
    >>> A1 = random_array((N, N), density=0.5, rng=rng)
    >>> A = block_diag((A0, A1), format='csc')
    >>> # The first M rows/columns are ordered together, then the last N
    >>> p, q, r = btf(A)
    >>> p
    array([ 0,  3,  1,  2, 10,  4,  5,  6,  7,  8,  9], dtype=int32)
    >>> q
    array([ 0,  1,  2, -5, 10,  6,  5,  7,  8,  4,  9], dtype=int32)
    >>> r
    array([ 0,  2,  3,  4,  5, 11,  9, 10,  0,  0,  0,  0], dtype=int32)
    """
    A, use_int32, out_itype = validate_csc_input(A, require_square=True)

    N = A.shape[0]

    if N == 0:
        p = np.empty(0, dtype=out_itype)
        q = np.empty(0, dtype=out_itype)
        r = np.zeros(1, dtype=out_itype)  # no blocks
        return p, q, r

    if A.nnz == 0:
        # p = [0, 1, ..., N - 1]
        p = np.arange(N, dtype=out_itype)
        # q = [-2, -3, ..., -(N + 1)]
        q = -np.arange(N, dtype=out_itype) - 2  # flag all columns
        r = np.arange(N + 1, dtype=out_itype)      # N blocks of size 1
        return p, q, r

    # Declare typed memory views for Cython
    cdef int32_t[::1] Ap_mv_int32
    cdef int32_t[::1] Ai_mv_int32
    cdef int32_t[::1] P_mv_int32
    cdef int32_t[::1] Q_mv_int32
    cdef int32_t[::1] R_mv_int32
    cdef int32_t[::1] Work_mv_int32

    cdef int64_t[::1] Ap_mv_int64
    cdef int64_t[::1] Ai_mv_int64
    cdef int64_t[::1] P_mv_int64
    cdef int64_t[::1] Q_mv_int64
    cdef int64_t[::1] R_mv_int64
    cdef int64_t[::1] Work_mv_int64

    # Assign memory for the input/output arrays
    if use_int32:
        Ap_mv_int32 = A.indptr
        Ai_mv_int32 = A.indices
        p = P_mv_int32 = np.zeros(N, dtype=np.int32)
        q = Q_mv_int32 = np.zeros(N, dtype=np.int32)
        r = R_mv_int32 = np.zeros(N + 1, dtype=np.int32)
        Work_mv_int32 = np.zeros(5 * N, dtype=np.int32)
    else:
        Ap_mv_int64 = A.indptr
        Ai_mv_int64 = A.indices
        p = P_mv_int64 = np.zeros(N, dtype=np.int64)
        q = Q_mv_int64 = np.zeros(N, dtype=np.int64)
        r = R_mv_int64 = np.zeros(N + 1, dtype=np.int64)
        Work_mv_int64 = np.zeros(5 * N, dtype=np.int64)

    maxwork = 0  # TODO default value?
    cdef double work
    cdef int32_t nmatch_int32
    cdef int64_t nmatch_int64

    if use_int32:
        nblocks = btf_order(
            N,
            &Ap_mv_int32[0],
            &Ai_mv_int32[0],
            maxwork,
            &work,
            &P_mv_int32[0],
            &Q_mv_int32[0],
            &R_mv_int32[0],
            &nmatch_int32,
            &Work_mv_int32[0]
        )
    else:
        nblocks = btf_l_order(
            N,
            &Ap_mv_int64[0],
            &Ai_mv_int64[0],
            maxwork,
            &work,
            &P_mv_int64[0],
            &Q_mv_int64[0],
            &R_mv_int64[0],
            &nmatch_int64,
            &Work_mv_int64[0]
        )

    if nblocks < 0:
        raise ValueError(f"BTF failed with error code: {nblocks}")

    return p, q, r


def btf_q_permutation(q):
    """Convert a raw BTF column permutation vector to a valid permutation.

    Parameters
    ----------
    q : (N,) ndarray of int
        The raw BTF column permutation vector. Contains negative entries for
        unmatched columns.

    Returns
    -------
    q_perm : (N,) ndarray of int
        The valid BTF column permutation vector. Contains only non-negative
        entries, where unmatched columns are replaced with their shifted
        absolute values.

    Notes
    -----
    In C, the values of ``q`` are converted using ``j = BTF_UNFLIP(Q[k])``,
    which is a macro for:

    .. code:: C

        j = (Q[k] < 0) ? -Q[k] - 2 : Q[k]

    This function is a Python equivalent of that macro.

    .. versionadded:: 0.5.0

    Examples
    --------
    >>> import numpy as np
    >>> from sksparse.btf import btf_q_permutation
    >>> q = np.array([0, 1, 2, -5, 10, 6, 5, 7, 8, 4, 9], dtype=np.int32)
    >>> btf_q_permutation(q)
    array([ 0,  1,  2,  3, 10,  6,  5,  7,  8,  4,  9], dtype=int32)
    """
    q = np.asarray(q)

    if q.ndim != 1:
        raise ValueError("Input must be a 1D array.")

    idx = q < 0
    q[idx] = -q[idx] - 2  # flip negative values
    return q
