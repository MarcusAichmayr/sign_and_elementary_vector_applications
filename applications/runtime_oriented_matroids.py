r"""
Runtime of Oriented Matroids

============================
Runtime of Oriented Matroids
============================

We demonstrate how to test the runtime of the package `sign_vectors <https://github.com/MarcusAichmayr/sign_vectors>`_::

    sage: from sign_vectors import *

Integers
========

We generate a random integer matrix and time the computation of its circuits::

    sage: P = random_matrix(ZZ, 5, 10)
    sage: om = OrientedMatroid(P)
    sage: om.circuits() # random
    {(00--0---+0),
     (0--++0+00-),
    ...
     (-+0+0+0++0)}
    sage: timeit("om.circuits()") # random
    125 loops, best of 3: 3.86 ms per loop

Real Algebraic Numbers
======================

Next, we consider a matrix over the real algebraic numbers::

    sage: P = random_matrix(AA, 4, 8)
    sage: om = OrientedMatroid(P)
    sage: om.circuits() # random
    {(0+-0+0++),
     (0+0-+0--),
    ...
     (+00-+++0)}
    sage: timeit("om.circuits()") # random
    625 loops, best of 3: 916 μs per loop
"""
