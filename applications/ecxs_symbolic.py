r"""
ECXs symbolic example of [MPSZ25]_.

ECXs symbolic example
=====================

We compute the nonnegative circuits (elementary vectors) of a matrix with a parameter appearing in [MPSZ25]_.

The packages `elementary_vectors <https://github.com/MarcusAichmayr/elementary_vectors>`_ and `sign_vectors <https://github.com/MarcusAichmayr/sign_vectors>`_
are required::

    sage: from elementary_vectors import *
    sage: from sign_vectors import *

We define a matrix with a parameter::

    sage: var('mu')
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

    sage: circuits(M)
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

Case :math:`0 < \mu < 1`
------------------------

We compute the nonnegative circuits of the corresponding oriented matroid::

    sage: forget()
    sage: assume(mu > 0, mu < 1)
    sage: om = OrientedMatroid(M)
    sage: nn_om_circuits = [c for c in om.circuits() if c >= 0]
    sage: nn_om_circuits
    [(+0++00000++0), (+0++0+0+00++), (0000+0+++00+), (0+0++0++00++)]

Using their support, we find the nonnegative circuits (of the matrix)::

    sage: supports = [c.support() for c in nn_om_circuits]
    sage: [c for c in circuits(M) if c.support() in supports]
    [(mu, 0, mu, 1, 0, 0, 0, 0, 0, mu, -mu + 1, 0),
     (mu^2, 0, mu^2, mu, 0, mu^2, 0, mu, 0, 0, -mu^2 + mu, mu),
     (0, 0, 0, 0, mu, 0, mu, 1, mu, 0, 0, -mu + 1),
     (0, mu^2, 0, mu, mu^2, 0, mu^2, mu, 0, 0, mu, -mu^2 + mu)]

Case :math:`1 < \mu < 2`
------------------------

We compute the nonnegative circuits of the corresponding oriented matroid::

    sage: forget()
    sage: assume(mu > 1, mu < 2)
    sage: om = OrientedMatroid(M)
    sage: nn_om_circuits = [c for c in om.circuits() if c >= 0]
    sage: nn_om_circuits
    [(++++++++0+00), (++++++++000+), (+++++++++000), (++++++++00+0)]

Using their support, we find the nonnegative circuits (of the matrix)::

    sage: supports = [c.support() for c in nn_om_circuits]
    sage: [c for c in circuits(M) if c.support() in supports]
    [(mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 1, mu - 1, 1, 1, -mu^2 + 2*mu, 0, 0, 0),
     (1, mu - 1, 1, 1, mu - 1, mu^2 - 2*mu + 1, mu - 1, mu - 1, 0, -mu^2 + 2*mu, 0, 0),
     (mu^2 - mu, mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu, 0, 0, -mu^2 + 2*mu, 0),
     (mu, mu^2 - mu, mu, mu, mu^2 - mu, mu, mu^2 - mu, mu, 0, 0, 0, -mu^2 + 2*mu)]

Case :math:`\mu = 1`
--------------------

We compute the nonnegative circuits of the corresponding oriented matroid::

    sage: om = OrientedMatroid(M(mu=1))
    sage: nn_om_circuits = [c for c in om.circuits() if c >= 0]
    sage: nn_om_circuits
    [(0000+0+++000), (+0++00000+00), (0+0++0++00+0), (+0++0+0+000+)]

Using their support, we find the nonnegative circuits (of the matrix)::

    sage: supports = [c.support() for c in nn_om_circuits]
    sage: [c for c in circuits(M(mu=1)) if c.support() in supports]
    [(0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0),
     (1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0),
     (0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0),
     (1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1)]
"""
