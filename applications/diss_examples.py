r"""
Up-to-date examples of [DissTODO]_.

========================================================================================================
Computing Circuits and Sign Vectors with Applications to Linear Inequality Systems and Reaction Networks
========================================================================================================

Here are the up-to-date examples appearing in [DissTODO]_.
TODO link to diss

Circuits of a Matrix
====================

::

    sage: from elementary_vectors import *
    sage: P = matrix([[1, 2, 0, 0, 0], [0, 1, 2, -3, 0]])
    sage: P
    [ 1  2  0  0  0]
    [ 0  1  2 -3  0]
    sage: P.minors(2)
    [1, 2, -3, 0, 4, -6, 0, 0, 0, 0]

::

    sage: circuits(P)
    [(4, -2, 1, 0, 0), (-6, 3, 0, 1, 0), (0, 0, 0, 0, 1), (0, 0, 3, 2, 0)]
    sage: cocircuits(P)
    [(0, -1, -2, 3, 0), (1, 0, -4, 6, 0), (2, 4, 0, 0, 0)]

::

    sage: degenerate_circuits(P)
    [(0, 0, 0, 0, 1), (0, 0, 3, 2, 0)]
    sage: degenerate_cocircuits(P)
    [(0, -1, -2, 3, 0), (1, 0, -4, 6, 0), (2, 4, 0, 0, 0)]

::

    sage: circuit_kernel_matrix(P)
    [ 4 -2  1  0  0]
    [-6  3  0  1  0]
    [ 0  0  0  0  1]

::

    sage: circuit_supports(P)
    [[0, 1, 2], [0, 1, 3], [4], [2, 3]]
    sage: cocircuit_supports(P)
    [[1, 2, 3], [0, 2, 3], [0, 1]]

Oriented Matroids
=================

::

    sage: from sign_vectors import *
    sage: P = matrix([[1, 2, 0, 0, 0], [0, 1, 2, -3, 0]])
    sage: P
    [ 1  2  0  0  0]
    [ 0  1  2 -3  0]
    sage: om = OrientedMatroid(P)
    sage: om
    Oriented matroid of dimension 1 with elements of size 5.

::

    sage: om.chirotope()
    [+, +, -, 0, +, -, 0, 0, 0, 0]

::

    sage: om.cocircuits()
    {(-0+-0), (0++-0), (--000), (++000), (0--+0), (+0-+0)}
    sage: om.topes()
    {(---+0), (+--+0), (--+-0), (-++-0), (++-+0), (+++-0)}

::

    sage: om.faces()
    [{(00000)},
     {(-0+-0), (0++-0), (--000), (++000), (0--+0), (+0-+0)},
     {(---+0), (+--+0), (--+-0), (-++-0), (++-+0), (+++-0)}]
    
::

    sage: om.plot() # not tested
    Graphics object consisting of 39 graphics primitives

::

    sage: om.circuits()
    {(0000+), (0000-), (00++0), (-+0+0), (00--0), (+-0-0), (-+-00), (+-+00)}

::

    sage: om.dual()
    Oriented matroid of dimension 2 with elements of size 5.
    sage: om.matroid()
    Matroid of rank 2 on 5 elements with 5 bases

::

    sage: OrientedMatroid.from_chirotope("00--0+++++", 2, 5)
    Oriented matroid of dimension 1 with elements of size 5.

::

    sage: om = OrientedMatroid.from_circuits({"0+-0", "+00-", "0-+0", "-00+"})
    sage: om
    Oriented matroid of dimension 1 with elements of size 4.
    sage: om.chirotope()
    [+, +, 0, 0, -, -]

Linear Inequality Systems
=========================

General Systems
---------------

::

    sage: from certlin import *
    sage: M = matrix([[1, 0], [0, 1], [1, 1], [0, 1]])
    sage: lower_bounds = [2, 5, 0, -oo]
    sage: upper_bounds = [5, oo, 8, 5]
    sage: lower_bounds_closed = [True, True, False, False]
    sage: upper_bounds_closed = [False, False, False, True]
    sage: I = Intervals.from_bounds(lower_bounds, upper_bounds, lower_bounds_closed, upper_bounds_closed)
    sage: I
    [2, 5) x [5, +oo) x (0, 8) x (-oo, 5]
    sage: S = LinearInequalitySystem(M, I)
    sage: S
    [1 0]  x in [2, 5)
    [0 1]  x in [5, +oo)
    [1 1]  x in (0, 8)
    [0 1]  x in (-oo, 5]

::

    sage: S.certify()
    (True, (5/2, 5))

::

    sage: S.to_homogeneous()
    [ 1  0 -5]  x >  0
    [-1 -1  0]  x >  0
    [ 1  1 -8]  x >  0
    [ 0  0 -1]  x >  0
    [-1  0  2]  x >= 0
    [ 0 -1  5]  x >= 0
    [ 0  1 -5]  x >= 0
    sage: S.to_inhomogeneous()
    [ 1  0]  x <   5
    [-1 -1]  x <   0
    [ 1  1]  x <   8
    [-1  0]  x <= -2
    [ 0 -1]  x <= -5
    [ 0  1]  x <=  5

::

    sage: S.dual()
    [ 0  0  0  1  1  1  1]  x >  0
    [ 1  0  0  0  0  0  0]  x >= 0
    [ 0  1  0  0  0  0  0]  x >= 0
    [ 0  0  1  0  0  0  0]  x >= 0
    [ 0  0  0  1  0  0  0]  x >= 0
    [ 0  0  0  0  1  0  0]  x >= 0
    [ 0  0  0  0  0  1  0]  x >= 0
    [ 0  0  0  0  0  0  1]  x >= 0
    [-1  0  0  1 -1  1  0]  x =  0
    [ 0 -1  1  0 -1  1  0]  x =  0
    [ 2  5 -5 -5  0 -8 -1]  x =  0

Homogeneous Systems
-------------------

::

    sage: A = matrix([[1, 2], [0, 1]])
    sage: B = matrix([[2, 3]])
    sage: C = matrix([[-1, 0]])
    sage: S = HomogeneousSystem(A, B, C)
    sage: S
    [ 1  2]  x >  0
    [ 0  1]  x >  0
    [ 2  3]  x >= 0
    [-1  0]  x =  0

::

    sage: S.certify()
    (True, (0, 1))
    sage: S.find_solution()
    (0, 1)

::

    sage: S.dual()
    [ 1  1  0  0]  x >  0
    [ 1  0  0  0]  x >= 0
    [ 0  1  0  0]  x >= 0
    [ 0  0  1  0]  x >= 0
    [ 1  0  2 -1]  x =  0
    [ 2  1  3  0]  x =  0
    sage: S.dual().certify()
    (False, (-1, -1, 0, -3, 0, 1))

Inhomogeneous Systems
---------------------

::

    sage: A = matrix([[-1, -1]])
    sage: B = matrix([[1, 0], [1, 1]])
    sage: a = vector([0])
    sage: b = vector([1, 0])
    sage: S = InhomogeneousSystem(A, B, a, b)
    sage: S
    [-1 -1]  x <  0
    [ 1  0]  x <= 1
    [ 1  1]  x <= 0

::

    sage: S.certify()
    (False, (1, 0, 1))
    sage: S.certify_unsolvability()
    (1, 0, 1)

Chemical Reaction Networks
==========================

Running Example
---------------

::

    sage: from sign_crn import *
    sage: var("a, b, c")
    (a, b, c)
    sage: species("A, B, C, D, E")
    (A, B, C, D, E)
    sage: rn = ReactionNetwork()
    sage: rn.add_complexes([(0, A + B, a * A + b * B), (1, C)])
    sage: rn.add_complexes([(2, D, c * A + D), (3, A), (4, E)])
    sage: rn.add_reactions([(0, 1), (1, 0), (1, 2), (2, 0), (3, 4), (4, 3)])
    sage: rn
    Reaction network with 5 complexes, 6 reactions and 5 species.

::

    sage: rn.plot()
    Graphics object consisting of 16 graphics primitives

::

    sage: rn.incidence_matrix()
    [-1  1  0  1  0  0]
    [ 1 -1 -1  0  0  0]
    [ 0  0  1 -1  0  0]
    [ 0  0  0  0 -1  1]
    [ 0  0  0  0  1 -1]
    sage: rn.source_matrix()
    [1 0 0 0 0 0]
    [0 1 1 0 0 0]
    [0 0 0 1 0 0]
    [0 0 0 0 1 0]
    [0 0 0 0 0 1]
    sage: rn.laplacian_matrix()
    [        -k_0_1          k_1_0          k_2_0              0              0]
    [         k_0_1 -k_1_0 - k_1_2              0              0              0]
    [             0          k_1_2         -k_2_0              0              0]
    [             0              0              0         -k_3_4          k_4_3]
    [             0              0              0          k_3_4         -k_4_3]

::

    sage: rn.ode_rhs()
    (-k_0_1*x_A^a*x_B^b + k_2_0*x_A^c*x_D - k_3_4*x_A + k_1_0*x_C + k_4_3*x_E, -k_0_1*x_A^a*x_B^b + k_2_0*x_A^c*x_D + k_1_0*x_C, k_0_1*x_A^a*x_B^b - (k_1_0 + k_1_2)*x_C, -k_2_0*x_A^c*x_D + k_1_2*x_C, k_3_4*x_A - k_4_3*x_E)

::

    sage: rn.stoichiometric_matrix
    [-1  1  0  1 -1  1]
    [-1  1  0  1  0  0]
    [ 1 -1 -1  0  0  0]
    [ 0  0  1 -1  0  0]
    [ 0  0  0  0  1 -1]
    sage: rn.kinetic_order_matrix
    [   -a     a     c a - c    -1     1]
    [   -b     b     0     b     0     0]
    [    1    -1    -1     0     0     0]
    [    0     0     1    -1     0     0]
    [    0     0     0     0     1    -1]

::

    sage: rn.deficiency_stoichiometric
    0
    sage: rn.deficiency_kinetic_order
    0
    sage: rn.is_weakly_reversible()
    True

::

    sage: rn(a=2, b=1, c=1).has_robust_cbe()
    True

::

    sage: rn.has_robust_cbe() # random order
    [{a > 0, b > 0, a - c > 0}]

::

    sage: rn.has_at_most_one_cbe() # random order
    [{a >= 0, b >= 0, a - c >= 0}]

Unique Existence
----------------

::

    sage: from sign_crn.conditions import *
    sage: var("a")
    a
    sage: assume(a > 0)
    sage: P = matrix([[0, 0, 1, 1, -1, 0], [1, -1, 0, 0, 0, -1], [0, 0, 1, -1, 0, 0]])
    sage: P
    [ 0  0  1  1 -1  0]
    [ 1 -1  0  0  0 -1]
    [ 0  0  1 -1  0  0]
    sage: Pt = matrix([[1, 1, 0, 0, -1, a], [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0]])
    sage: Pt
    [ 1  1  0  0 -1  a]
    [ 1 -1  0  0  0  0]
    [ 0  0  1 -1  0  0]

::

    sage: uniqueness_condition(P, Pt)
    True
    sage: face_condition(P, Pt)
    True

::

    sage: nondegeneracy_condition(P, Pt(a=1/2))
    True

::

    sage: nondegeneracy_condition(P, Pt(a=1), certify=True)
    (False, (1, 1, 0, 0, -1, 1))
"""
