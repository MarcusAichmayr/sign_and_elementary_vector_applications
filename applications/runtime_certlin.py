r"""
Runtime of Certlin

==================
Runtime of Certlin
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

    sage: S.certify() # random
    (False, (0, 0, -264, 0, -186, 182, 190, 0, -178, 38))
    sage: S.certify(random=True) # random
    (False, (0, 0, 240, 60, 120, -180, -120, 240, 0, 0))

Consult the documentation of the package for the other commands.
Use the ``timeit`` command to test the runtime of the different commands::

    sage: timeit("S.certify()") # long time
    5 loops, best of 3: 87.5 ms per loop

To compare the runtime with polyhedral computations, we need to translate the system into a polyhedron::

    sage: from applications.runtime_certlin import polyhedron_from_general_system
    sage: P = polyhedron_from_general_system(S)
    sage: P # random
    The empty polyhedron in QQ^6
    sage: P = polyhedron_from_general_system(S, backend="polymake") # optional - polymake

We consider the polyhedron of the dual system::

    sage: P = polyhedron_from_general_system(S.dual())
    sage: P # random
    A 12-dimensional polyhedron in QQ^18 defined as the convex hull of 30 vertices and 30 rays

Use the method ``an_element`` to compute an element of the polyhedron.
"""

#############################################################################
#  Copyright (C) 2026                                                       #
#          Marcus S. Aichmayr (aichmayr@mathematik.uni-kassel.de)           #
#                                                                           #
#  Distributed under the terms of the GNU General Public License (GPL)      #
#  either version 3, or (at your option) any later version                  #
#                                                                           #
#  http://www.gnu.org/licenses/                                             #
#############################################################################

from sage.geometry.polyhedron.constructor import Polyhedron

from certlin import LinearInequalitySystem


def polyhedron_from_general_system(system: LinearInequalitySystem, backend: str = None) -> Polyhedron:
    r"""
    Return the polynomial associated with the system ``M x in I``.

    INPUT:

    - ``system`` -- a linear inequality system
    - ``backend`` -- a backend for polyhedra (default: ``None``)

    To use backends like ``"normaliz"`` and ``"polymake"``, see the documentation of the ``Polyhedron`` class.
    """
    equalities = []
    inequalities = []
    homogeneous = system.to_homogeneous()
    for line, interval in zip(homogeneous.matrix, homogeneous.intervals):
        if interval.is_pointed():
            equalities.append([0, *line])
        elif interval.is_open():
            inequalities.append([-1, *line])
        else:
            inequalities.append([0, *line])
    return Polyhedron(eqns=equalities, ieqs=inequalities, backend=backend)
