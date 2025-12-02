r"""
ECXs symbolic example of [MPSZ25]_.

=====================
ECXs symbolic example
=====================

We compute the nonnegative circuits (elementary vectors) of a matrix with a parameter appearing in [MPSZ25]_.

The packages `elementary_vectors <https://github.com/MarcusAichmayr/elementary_vectors>`_ and `sign_vectors <https://github.com/MarcusAichmayr/sign_vectors>`_
are required::

    sage: from elementary_vectors import *
    sage: from sign_vectors import *

We define a matrix with a parameter::

    sage: var("mu")
    mu
    sage: M = matrix([[0, -1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0],
    ....:             [0, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0],
    ....:             [1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ....:             [1, 1, 0, -mu, 0, 0, 0, 0, 0, 0, 0, 0],
    ....:             [0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 0, 0],
    ....:             [0, 0, 0, 0, 1, 1, 0, -mu, 0, 0, 0, 0],
    ....:             [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0],
    ....:             [0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, -1]])
    sage: M
    [  0  -1   0   0   0   0   1   0  -1   0   0   0]
    [  0   0   1   0   0  -1   0   0   0  -1   0   0]
    [  1   0  -1   0   0   0   0   0   0   0   0   0]
    [  1   1   0 -mu   0   0   0   0   0   0   0   0]
    [  0   0   0   0   1   0  -1   0   0   0   0   0]
    [  0   0   0   0   1   1   0 -mu   0   0   0   0]
    [ -1   0   0   1   0   0   0   0   0   0  -1   0]
    [  0   0   0   0  -1   0   0   1   0   0   0  -1]

We compute all circuits (of the matrix)::

    sage: elements = circuits(M)
    sage: elements
    [(mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 1, mu - 1, 1, 1, -mu^2 + 2*mu, 0, 0, 0),
     (1, mu - 1, 1, 1, mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 0, -mu^2 + 2*mu, 0, 0),
     (mu^2 - mu, mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu, 0, 0, -mu^2 + 2*mu, 0),
     (mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu^2 - mu, mu, 0, 0, 0, -mu^2 + 2*mu),
     (-1, -mu + 1, -1, -1, 0, 0, 0, 0, mu - 1, -1, 0, 0),
     (0, -mu, 0, -1, 0, 0, 0, 0, mu, 0, -1, 0),
     (-1, -mu + 1, -1, -1, 1, -1, 1, 0, mu, 0, 0, -1),
     (mu, 0, mu, 1, 0, 0, 0, 0, 0, mu, -mu + 1, 0),
     (1, mu - 1, 1, 1, mu - 1, -mu + 1, mu - 1, 0, 0, mu, 0, -mu + 1),
     (-mu, mu, -mu, 0, mu, -mu, mu, 0, 0, 0, mu, -mu),
     (mu, mu^2 - mu, mu, mu, 0, mu, 0, 1, -mu^2 + mu, 0, 0, 1),
     (0, 0, 0, 0, 0, mu^2 - mu, 0, mu - 1, 0, -mu^2 + mu, 0, mu - 1),
     (mu^2, 0, mu^2, mu, 0, mu^2, 0, mu, 0, 0, -mu^2 + mu, mu),
     (0, 0, 0, 0, mu, 0, mu, 1, mu, 0, 0, -mu + 1),
     (mu, mu^2 - mu, mu, mu, mu^2 - mu, 0, mu^2 - mu, mu - 1, 0, mu, 0, -mu^2 + 2*mu - 1),
     (0, mu^2, 0, mu, mu^2, 0, mu^2, mu, 0, 0, mu, -mu^2 + mu),
     (0, 0, 0, 0, 1, mu - 1, 1, 1, 1, -mu + 1, 0, 0),
     (mu - 1, -mu + 1, mu - 1, 0, 1, mu - 1, 1, 1, mu, 0, -mu + 1, 0),
     (1, -1, 1, 0, -1, -mu + 1, -1, -1, 0, mu, -1, 0),
     (-1, 1, -1, 0, 0, 0, 0, 0, -1, -1, 1, 0),
     (0, 0, 0, 0, -1, 1, -1, 0, -1, -1, 0, 1),
     (-mu, mu, -mu, 0, 0, -mu, 0, -1, -mu, 0, mu, -1),
     (-mu, mu, -mu, 0, mu, 0, mu, 1, 0, -mu, mu, -mu + 1),
     (0, mu, 0, 1, mu, mu^2 - mu, mu, mu, 0, -mu^2 + mu, 1, 0),
     (0, -mu, 0, -1, -mu, mu, -mu, 0, 0, -mu, -1, mu),
     (mu^2 - mu, 0, mu^2 - mu, mu - 1, mu, mu^2 - mu, mu, mu, mu, 0, -mu^2 + 2*mu - 1, 0),
     (mu, 0, mu, 1, -mu, mu, -mu, 0, -mu, 0, -mu + 1, mu)]

This module offers a utility function to filter for nonnegative vectors::

    sage: from applications.ecxs_symbolic import non_negative_vectors

Case :math:`0 < \mu < 1`
========================

::

    sage: assume(mu > 0, mu < 1)
    sage: non_negative_vectors(elements)
    [(mu, 0, mu, 1, 0, 0, 0, 0, 0, mu, -mu + 1, 0),
     (mu^2, 0, mu^2, mu, 0, mu^2, 0, mu, 0, 0, -mu^2 + mu, mu),
     (0, 0, 0, 0, mu, 0, mu, 1, mu, 0, 0, -mu + 1),
     (0, mu^2, 0, mu, mu^2, 0, mu^2, mu, 0, 0, mu, -mu^2 + mu)]

Case :math:`1 < \mu < 2`
========================

::

    sage: forget()
    sage: assume(mu > 1, mu < 2)
    sage: non_negative_vectors(elements)
    [(mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 1, mu - 1, 1, 1, -mu^2 + 2*mu, 0, 0, 0),
     (1, mu - 1, 1, 1, mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 0, -mu^2 + 2*mu, 0, 0),
     (mu^2 - mu, mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu, 0, 0, -mu^2 + 2*mu, 0),
     (mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu^2 - mu, mu, 0, 0, 0, -mu^2 + 2*mu)]

Case :math:`\mu = 1`
====================

::

    sage: forget()
    sage: non_negative_vectors(circuits(M(mu=1)))
    [(0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0),
     (1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0),
     (0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0),
     (1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1)]
"""

#############################################################################
#  Copyright (C) 2025                                                       #
#          Marcus S. Aichmayr (aichmayr@mathematik.uni-kassel.de)           #
#                                                                           #
#  Distributed under the terms of the GNU General Public License (GPL)      #
#  either version 3, or (at your option) any later version                  #
#                                                                           #
#  http://www.gnu.org/licenses/                                             #
#############################################################################

from sage.modules.free_module_element import vector

from sign_vectors import sign_vector


def non_negative_vectors(vectors: list[vector]) -> list[vector]:
    r"""
    Return nonnegative vectors.

    INPUT:

    - ``vectors`` -- an iterable of vectors

    OUTPUT:

    Return all vectors that are nonnegative in each component.
    If a vector is nonpositive in each component, its negative is returned.

    EXAMPLES::

        sage: from sign_crn.utility import non_negative_vectors
        sage: l = [vector([1, 1, 0, -1]), vector([0, 0, 0, 0]), vector([1, 0, 0, 1])]
        sage: l
        [(1, 1, 0, -1), (0, 0, 0, 0), (1, 0, 0, 1)]
        sage: non_negative_vectors(l)
        [(0, 0, 0, 0), (1, 0, 0, 1)]
        sage: var("a")
        a
        sage: evs = [vector([0, 0, 1, 0, 0]), vector([0, 0, 0, 1, 0]), vector([-1, -a, 0, 0, a])]
        sage: evs
        [(0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (-1, -a, 0, 0, a)]
        sage: non_negative_vectors(evs)
        ...
        UserWarning: Cannot determine sign of symbolic expression, using 0 instead.
        [(0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (1, a, 0, 0, -a)]
        sage: assume(a > 0)
        sage: non_negative_vectors(evs)
        [(0, 0, 1, 0, 0), (0, 0, 0, 1, 0)]

    TESTS::

        sage: l = [vector([x, 0, 0])]
        sage: non_negative_vectors(l)
        [(x, 0, 0)]
    """
    result = []
    for element in vectors:
        if sign_vector(element) >= 0:
            result.append(element)
        elif sign_vector(element) < 0:
            result.append(-element)
    return result
