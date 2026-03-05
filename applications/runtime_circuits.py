r"""
Runtime of circuits

===================
Runtime of circuits
===================

We demonstrate how to test the runtime of the package `elementary_vectors <https://github.com/MarcusAichmayr/elementary_vectors>`_::

    sage: from elementary_vectors import *

Integers
========

We generate random integer matrices and time the computation of their circuits::

    sage: M = random_matrix(ZZ, 5, 15)
    sage: circuits(M)
    ...
    sage: timeit("circuits(M)")
    ...

::

    sage: M = random_matrix(ZZ, 7, 25)
    sage: circuits(M) # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Field extensions
================

Next, we generate a matrix over :math:`\mathbb{Z}[\sqrt{2}]`::

    sage: F = NumberField(x^2 - 2, name="a")
    sage: M = random_matrix(F, 5, 30)
    sage: circuits(M) # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Now, we generate a matrix over :math:`\mathbb{Z}[\sqrt{2}, \sqrt{3}, \sqrt{5}]`::

    sage: F = NumberField([x^2 - 2, x^2 - 3, x^2 - 5], names="a, b, c")
    sage: M = random_matrix(F, 5, 20)
    sage: circuits(M) # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Polynomial rings
================

Next, we consider a polynomial matrix with three variables::

    sage: M = random_matrix(PolynomialRing(ZZ, "a, b, c"), 5, 15)
    sage: circuits(M) # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Algebraic numbers
=================

Finally, we take matrices over the algebraic numbers::

    sage: M = random_matrix(QQbar, 4, 15)
    sage: circuits(M) # long time
    ...
    sage: timeit("circuits(M)") # long time
    ...

Computing only the support of the circuits saves memory and time::

    sage: circuit_supports(M) # long time
    ...
    sage: timeit("circuit_supports(M)") # long time
    ...

Especially, for bigger matrices over the algebraic numbers,
we can only compute the support of the circuits
since the determinants can occupy a lot of memory::

    sage: M = random_matrix(QQbar, 5, 21)
    sage: circuit_supports(M) # long time
    ...
    sage: timeit("circuit_supports(M)") # long time
    ...
"""
