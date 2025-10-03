# Copyright (C) 2018 Cyrus Cheng (Imperial College London)
#
# This file is part of FIAT (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    LGPL-3.0-or-later
#
# Modified by David A. Ham (david.ham@imperial.ac.uk), 2018

from FIAT import finite_element, polynomial_set, dual_set, functional
from FIAT.reference_element import (Point,
                                    DefaultLine,
                                    UFCInterval,
                                    UFCQuadrilateral,
                                    UFCHexahedron,
                                    UFCTriangle,
                                    UFCTetrahedron,
                                    make_affine_mapping,
                                    flatten_reference_cube)
from FIAT.P0 import P0Dual
import numpy as np

hypercube_simplex_map = {Point(): Point(),
                         DefaultLine(): DefaultLine(),
                         UFCInterval(): UFCInterval(),
                         UFCQuadrilateral(): UFCTriangle(),
                         UFCHexahedron(): UFCTetrahedron()}


class DPC0(finite_element.CiarletElement):
    def __init__(self, ref_el):
        flat_el = flatten_reference_cube(ref_el)
        poly_set = polynomial_set.ONPolynomialSet(hypercube_simplex_map[flat_el], 0)
        dual = P0Dual(ref_el)
        # Implement entity_permutations when we handle that for HigherOrderDPC.
        # Currently, orientation_tuples in P0Dual(ref_el).entity_permutations
        # are missing the extrinsic orientation entry (which should always be 0).
        # We should probably just change o_tuple -> (0, ) + o_tuple for non-
        # tensorproduct elements for consistency.
        dual.entity_permutations = None
        degree = 0
        formdegree = ref_el.get_spatial_dimension()  # n-form
        super().__init__(poly_set=poly_set,
                         dual=dual,
                         order=degree,
                         ref_complex=ref_el,
                         formdegree=formdegree)


class DPCDualSet(dual_set.DualSet):
    """The dual basis for DPC elements.  This class works for
    hypercubes of any dimension.  Nodes are point evaluation at
    equispaced points.  This is the discontinuous version where
    all nodes are topologically associated with the cell itself"""

    def __init__(self, ref_el, flat_el, degree):
        entity_ids = {}
        nodes = []

        # Change coordinates here.
        # Vertices of the simplex corresponding to the reference element.
        v_simplex = hypercube_simplex_map[flat_el].get_vertices()
        # Vertices of the reference element.
        v_hypercube = flat_el.get_vertices()
        # For the mapping, first two vertices are unchanged in all dimensions.
        v_ = [v_hypercube[0], v_hypercube[int(-0.5*len(v_hypercube))]]

        # For dimension 1 upwards,
        # take the next vertex and map it to the midpoint of the edge/face it belongs to, and shares
        # with no other points.
        for d in range(1, flat_el.get_dimension()):
            v_.append(tuple(np.asarray(v_hypercube[flat_el.get_dimension() - d] +
                            np.average(np.asarray(v_hypercube[::2]), axis=0))))
        A, b = make_affine_mapping(v_simplex, tuple(v_))  # Make affine mapping to be used later.

        # make nodes by getting points
        # need to do this dimension-by-dimension, facet-by-facet
        top = hypercube_simplex_map[flat_el].get_topology()

        cur = 0
        for dim in sorted(top):
            for entity in sorted(top[dim]):
                pts_cur = hypercube_simplex_map[flat_el].make_points(dim, entity, degree)
                pts_cur = [tuple(np.matmul(A, np.array(x)) + b) for x in pts_cur]
                nodes_cur = [functional.PointEvaluation(flat_el, x)
                             for x in pts_cur]
                nnodes_cur = len(nodes_cur)
                nodes += nodes_cur
                cur += nnodes_cur

        cube_topology = ref_el.get_topology()
        for dim in sorted(cube_topology):
            entity_ids[dim] = {}
            for entity in sorted(cube_topology[dim]):
                entity_ids[dim][entity] = []

        entity_ids[dim][0] = list(range(len(nodes)))
        super().__init__(nodes, ref_el, entity_ids)


class HigherOrderDPC(finite_element.CiarletElement):
    """The DPC finite element.  It is what it is."""

    def __init__(self, ref_el, degree):
        flat_el = flatten_reference_cube(ref_el)
        poly_set = polynomial_set.ONPolynomialSet(hypercube_simplex_map[flat_el], degree)
        dual = DPCDualSet(ref_el, flat_el, degree)
        formdegree = flat_el.get_spatial_dimension()  # n-form
        super().__init__(poly_set=poly_set,
                         dual=dual,
                         order=degree,
                         ref_complex=ref_el,
                         formdegree=formdegree)


def DPC(ref_el, degree):
    if degree == 0:
        return DPC0(ref_el)
    else:
        return HigherOrderDPC(ref_el, degree)
