# Copyright (C) 2008 Robert C. Kirby (Texas Tech University)
# Modified by Colin Cotter (Imperial College London)
#             David Ham (Imperial College London)
#
# This file is part of FIAT (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    LGPL-3.0-or-later

from FIAT import finite_element, polynomial_set, dual_set, functional, P0, quadrature
from FIAT.polynomial_set import mis
import numpy


class DiscontinuousTaylorDualSet(dual_set.DualSet):
    """The dual basis for Taylor elements.  This class works for
    intervals.  Nodes are function and derivative evaluation
    at the midpoint."""

    def __init__(self, ref_el, degree):
        nodes = []
        dim = ref_el.get_spatial_dimension()

        Q = quadrature.make_quadrature(ref_el, 2 * (degree + 1))

        f_at_qpts = numpy.ones(len(Q.wts))
        nodes.append(functional.IntegralMoment(ref_el, Q, f_at_qpts))

        vertices = ref_el.get_vertices()
        midpoint = tuple(sum(numpy.array(vertices)) / len(vertices))
        for k in range(1, degree + 1):
            # Loop over all multi-indices of degree k.
            for alpha in mis(dim, k):
                nodes.append(functional.PointDerivative(ref_el, midpoint, alpha))

        entity_ids = {d: {e: [] for e in ref_el.sub_entities[d]}
                      for d in range(dim + 1)}
        entity_ids[dim][0] = list(range(len(nodes)))

        super().__init__(nodes, ref_el, entity_ids)


class HigherOrderDiscontinuousTaylor(finite_element.CiarletElement):
    """The discontinuous Taylor finite element. Use a Taylor basis for DG."""

    def __init__(self, ref_el, degree):
        poly_set = polynomial_set.ONPolynomialSet(ref_el, degree)
        dual = DiscontinuousTaylorDualSet(ref_el, degree)
        formdegree = ref_el.get_spatial_dimension()  # n-form
        super().__init__(poly_set, dual, degree, formdegree)


def DiscontinuousTaylor(ref_el, degree):
    if degree == 0:
        return P0.P0(ref_el)
    else:
        return HigherOrderDiscontinuousTaylor(ref_el, degree)
