r"""
Runtime of certlin

==================
Runtime of certlin
==================

We demonstrate how to test the runtime of the package `certlin <https://github.com/MarcusAichmayr/certlin>`_::

    sage: from certlin import *

To define a linear inequality system, we consider an (m x n) matrix and m intervals over a field::

    sage: m = 10
    sage: n = 5
    sage: field = ZZ
    sage: # field = AA # algebraic real numbers

We define a random linear inequality system::
    sage: M = random_matrix(field, m, n)
    sage: I = Intervals.random(m, ring=field)
    sage: S = LinearInequalitySystem(M, I)

There are different commands for certifying the solvability of the system::

    sage: S.certify()
    ...
    sage: S.certify(random=True)
    ...

Use the ``timeit`` command to test the runtime of the different commands::

    sage: timeit("S.certify()") # long time
    ...
"""
