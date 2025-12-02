r"""
wip Runtime of circuits

===================
Runtime of circuits
===================

We demonstrate how to test the runtime of the packages `elementary_vectors <https://github.com/MarcusAichmayr/elementary_vectors>`_::
First, we import the package::

    sage: from elementary_vectors import *

We generate a random integer matrix and time the computation of its circuits::

    sage: M = random_matrix(ZZ, 7, 25)
    sage: circuits(M); # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Next, we consider a polynomial matrix with three variables::

    sage: M = random_matrix(PolynomialRing(ZZ, "x, y, z"), 5, 15)
    sage: timeit("circuits(M)") # long time
    ...

Now, we take a matrix over the algebraic numbers::

    sage: M = random_matrix(QQbar, 4, 15)
    sage: timeit("circuits(M)") # long time
    ...
    sage: timeit("circuit_supports(M)") # long time
    ...

TODO field extension
"""
