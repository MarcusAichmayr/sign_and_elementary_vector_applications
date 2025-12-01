r"""
Up-to-date examples of [AMR24]_.

==================================================================================================
A SageMath Package for Elementary and Sign Vectors with Applications to Chemical Reaction Networks
==================================================================================================

Here are the up-to-date examples appearing in [AMR24]_ for `ICMS 2024 <https://icms-conference.org/2024/>`_.
The paper is also available at `ARXIV <https://arxiv.org/abs/2407.12660>`_.

Elementary vectors
==================

Functions dealing with elementary vectors (circuits of a subspace given by a matrix)
are implemented in the package `elementary_vectors <https://github.com/MarcusAichmayr/elementary_vectors>`_.

We compute elementary vectors (circuits), using maximal minors::

    sage: from elementary_vectors import *
    sage: M = matrix([[1, 1, 2, 0], [0, 0, 1, 2]])
    sage: M
    [1 1 2 0]
    [0 0 1 2]
    sage: M.minors(2)
    [0, 1, 2, 1, 2, 4]
    sage: circuits(M)
    [(1, -1, 0, 0), (4, 0, -2, 1), (0, 4, -2, 1)]

Solvability of linear inequality systems
========================================

Our package `certlin <https://github.com/MarcusAichmayr/certlin>`_
provides tools for the solvability of linear inequality systems.
We state linear inequality systems as intersection of a vector space and a Cartesian product of intervals.
To represent these objects, we use a matrix and a list of intervals::

    sage: from certlin import *
    sage: M = matrix([[1, 0], [0, 1], [1, 1], [0, 1]])
    sage: M
    [1 0]
    [0 1]
    [1 1]
    [0 1]
    sage: lower = [2, 5, 0, -oo]
    sage: upper = [5, oo, 8, 5]
    sage: lower_closed = [True, True, False, False]
    sage: upper_closed = [False, False, False, True]
    sage: I = Intervals.from_bounds(lower, upper, lower_closed, upper_closed)
    sage: I
    [2, 5) x [5, +oo) x (0, 8) x (-oo, 5]
    sage: sys = LinearInequalitySystem(M, I)
    sage: sys
    [1 0]  x in [2, 5)
    [0 1]  x in [5, +oo)
    [1 1]  x in (0, 8)
    [0 1]  x in (-oo, 5]

The package can certify whether the system has a solution or not::

    sage: sys.certify()
    (True, (5/2, 5))
    sage: sys.find_solution()
    (5/2, 5)

Therefore, the system has a solution.

Sign vectors and oriented matroids
==================================

The package `sign_vectors <https://github.com/MarcusAichmayr/sign_vectors>`_
provides functions for sign vectors and oriented matroids.
We consider an oriented matroid given by a matrix and compute the cocircuits and covectors::

    sage: from sign_vectors import *
    sage: M = matrix([[1, 3, -2, 1], [0, 4, -2, 1]])
    sage: M
    [ 1  3 -2  1]
    [ 0  4 -2  1]
    sage: om = OrientedMatroid(M)
    sage: om.cocircuits()
    {(0-+-), (+-00), (-+00), (-0+-), (0+-+), (+0-+)}
    sage: om.covectors()
    {(0000),
     (0-+-),
     (-+-+),
     (+-00),
     (-+00),
     (-0+-),
     (0+-+),
     (+--+),
     (+-+-),
     (--+-),
     (-++-),
     (+0-+),
     (++-+)}

Chemical reaction networks
==========================

The package `sign_crn <https://github.com/MarcusAichmayr/sign_crn>`_
offers a user-friendly class to define (chemical) reaction networks::

    sage: from sign_crn import *
    sage: var("a, b, c")
    (a, b, c)
    sage: species("A, B, C, D, E")
    (A, B, C, D, E)
    sage: rn = ReactionNetwork()
    sage: rn.add_complexes([(0, A + B, a * A + b * B), (1, C), (2, D, c * A + D), (3, A), (4, E)])
    sage: rn.add_reactions([(0, 1), (1, 0), (1, 2), (2, 0), (3, 4), (4, 3)])
    sage: rn
    Reaction network with 5 complexes, 6 reactions and 5 species.
    sage: rn.complexes_stoichiometric
    {0: A + B, 1: C, 2: D, 3: A, 4: E}
    sage: rn.complexes_kinetic_order
    {0: a*A + b*B, 1: C, 2: c*A + D, 3: A, 4: E}

Several conditions for such networks based on sign vectors and maximal minors are implemented in this package.

Robustness of CBE
-----------------

To study robustness of CBE, we can compute the covectors of the stoichiometric and the kinetic-order matrix::

    sage: rn.stoichiometric_matrix
    [-1  1  0  1 -1  1]
    [-1  1  0  1  0  0]
    [ 1 -1 -1  0  0  0]
    [ 0  0  1 -1  0  0]
    [ 0  0  0  0  1 -1]
    sage: OrientedMatroid(rn.stoichiometric_matrix.T).covectors()
    {(00000),
     (--+-+),
     (0++-+),
     (++-00),
     (--+00),
     (++-++),
     (--0+0),
     (0-+0-),
     (--++-),
     (--+++),
     (++--+),
     (0-0+-),
     (++--0),
     (++---),
     (0-+--),
     (--+--),
     (-000+),
     (-0-++),
     (+0-+-),
     (0+-0+),
     (-+-++),
     (++-+0),
     (++-+-),
     (-+--+),
     (--++0),
     (00+-0),
     (--+-0),
     (0-++-),
     (+000-),
     (+-+0-),
     (++0--),
     (++0-+),
     (+0+--),
     (00-+0),
     (---++),
     (0+-++),
     (---+-),
     (+--+-),
     (+-++-),
     (-+0-+),
     (0+--+),
     (--+0+),
     (-0+-+),
     (-++-+),
     (++0-0),
     (+++--),
     (+++-+),
     (++-0+),
     (--+0-),
     (---+0),
     (++-0-),
     (--0+-),
     (--0++),
     (+-0+-),
     (+-+--),
     (0--+-),
     (+++-0),
     (-+-0+),
     (0+0-+)}

To compute the covectors of the kinetic-order matrix, we need to fix the parameters::

    sage: rn.kinetic_order_matrix
    [   -a     a     c a - c    -1     1]
    [   -b     b     0     b     0     0]
    [    1    -1    -1     0     0     0]
    [    0     0     1    -1     0     0]
    [    0     0     0     0     1    -1]
    sage: OrientedMatroid(rn.kinetic_order_matrix(a=2, b=1, c=1).T).covectors()
    {(00000),
     (--+-+),
     (0++-+),
     (++-00),
     (--+00),
     (-0+-0),
     (00+--),
     (0++--),
     (++-++),
     (--0+0),
     (0-+0-),
     (--++-),
     (--+++),
     (0--+0),
     (++---),
     (0-0+-),
     (--+--),
     (0+-0+),
     (++--+),
     (-000+),
     (-0-++),
     (+0-+-),
     (+0-++),
     (-+-++),
     (++-+0),
     (++-+-),
     (0++-0),
     (-+--+),
     (--++0),
     (0+0-+),
     (++--0),
     (--+-0),
     (0-++-),
     (+-+0-),
     (+0-+0),
     (0-+--),
     (++0--),
     (++0-+),
     (00-++),
     (+0+--),
     (---++),
     (---+-),
     (+--+-),
     (0+-++),
     (+-++-),
     (+--++),
     (-+0-+),
     (0+--+),
     (--+0+),
     (-0+-+),
     (-++-+),
     (-++--),
     (++0-0),
     (+++-0),
     (+++--),
     (+++-+),
     (++-0+),
     (--+0-),
     (---+0),
     (+--+0),
     (+000-),
     (++-0-),
     (-0+--),
     (0--++),
     (--0+-),
     (--0++),
     (+-0+-),
     (+-+--),
     (0--+-),
     (-+-0+),
     (-++-0)}

For :math:`a = 2`, :math:`b = 1` and :math:`c = 1`, the covectors of the stoichiometric matrix
are included in the closure of the covectors of the kinetic-order matrix.

A more efficient approach to study robustness of CBE
is to compute the maximal minors of the reduced matrices.
In this case, we do not need to fix the parameters::

    sage: rn.has_robust_cbe() # random order
    [{a > 0, b > 0, a - c > 0}]

Hence, the network has a unique positive CBE if and only if :math:`a, b > 0` and :math:`a > c`.

Uniqueness of CBE
-----------------

Similarly, we can use the maximal minors to study uniqueness of CBE::

    sage: rn.has_at_most_one_cbe() # random order
    [{a >= 0, b >= 0, a - c >= 0}]

Hence, positive CBE are unique if and only if :math:`a, b \geq 0` and :math:`a \geq c`.

Unique existence of CBE
-----------------------

Now, we consider a network given by two matrices involving a parameter.
(see Example 20 of [MHR19]_)
Depending on this parameter, the network has a unique positive CBE::

    sage: var("a")
    a
    sage: assume(a > 0)
    sage: S = matrix([[1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, -1], [0, 0, 1, 1, 2, 0]])
    sage: S
    [ 1  0  0  0  0  1]
    [ 0  1  0  0  0 -1]
    [ 0  0  1  1  2  0]
    sage: St = matrix([[-1, -1, 0, 0, -2, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, a, 1]])
    sage: St
    [-1 -1  0  0 -2  0]
    [ 0  0  1  1  0  0]
    [ 0  0  0  0  a  1]

The first two conditions depend on the sign vectors corresponding
to the rows of these matrices which are independent of the specific value for :math:`a`::

    sage: uniqueness_condition(S, St)
    True

Hence, there exists at most one equilibrium.
Also the face condition is satisfied::

    sage: face_condition(S, St)
    True

For specific values of :math:`a`, the pair of subspaces
determined by kernels of the matrices is nondegenerate.
This is exactly the case for :math:`a \in (0, 1) \cup (1, 2)`.
We demonstrate this for specific values::

    sage: degeneracy_condition(S, St(a=1/2))
    False
    sage: degeneracy_condition(S, St(a=3/2))
    False
    sage: degeneracy_condition(S, St(a=1))
    True
    sage: degeneracy_condition(S, St(a=2))
    True
    sage: degeneracy_condition(S, St(a=3))
    True
"""
