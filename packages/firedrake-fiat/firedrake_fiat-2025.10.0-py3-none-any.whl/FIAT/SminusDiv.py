from functools import cached_property
from sympy import symbols, legendre, Array, diff
import numpy as np
from FIAT.finite_element import FiniteElement
from FIAT.dual_set import DualSet
from FIAT.polynomial_set import mis
from FIAT.reference_element import flatten_reference_cube

x, y, z = symbols('x y z')
variables = (x, y, z)
leg = legendre


def triangular_number(n):
    return ((n+1)*n)//2


def choose_ijk_total(degree):
    top = 1
    for i in range(1, 2 + degree + 1):
        top = i * top
    bottom = 1
    for i in range(1, degree + 1):
        bottom = i * bottom
    return top // (2 * bottom)


class TrimmedSerendipityDiv(FiniteElement):
    def __init__(self, ref_el, degree):
        if degree < 1:
            raise Exception("Trimmed serendipity elements only valid for k >= 1")

        flat_el = flatten_reference_cube(ref_el)
        dim = flat_el.get_spatial_dimension()
        self.fdim = dim
        if dim != 3:
            if dim != 2:
                raise Exception("Trimmed serendipity elements only valid for dimensions 2 and 3")

        flat_topology = flat_el.get_topology()
        entity_ids = {}
        cur = 0
        for top_dim, entities in flat_topology.items():
            entity_ids[top_dim] = {}
            for entity in entities:
                entity_ids[top_dim][entity] = []

        # 3-d case.
        if dim == 3:
            entity_ids[3] = {}
            for j in sorted(flat_topology[2]):
                entity_ids[2][j] = list(range(cur, cur + triangular_number(degree)))
                cur = cur + triangular_number(degree)
            interior_ids = 0
            for k in range(2, degree):
                interior_ids = interior_ids + 3 * choose_ijk_total(k - 2)
            if (degree > 1):
                interior_tilde_ids = 3
                for k in range(1, degree - 1):
                    interior_tilde_ids = interior_tilde_ids + 3
            if (degree == 4):
                interior_tilde_ids += choose_ijk_total(degree - 2) - (degree - 1) - (degree - 1) + 1
            if (degree > 4):
                interior_tilde_ids += choose_ijk_total(degree - 2) - (degree - 1) - (degree - 1) + 1
            if degree == 1:
                interior_tilde_ids = 0
            entity_ids[3][0] = list(range(cur, cur + interior_ids + interior_tilde_ids))
            cur = cur + interior_ids + interior_tilde_ids
        else:
            for j in sorted(flat_topology[1]):
                entity_ids[1][j] = list(range(cur, cur + degree))
                cur = cur + degree

            if (degree >= 2):
                entity_ids[2][0] = list(range(cur, cur + 2*triangular_number(degree - 2) + degree))

            cur += 2*triangular_number(degree - 2) + degree

        self.flat_el = flat_el
        nodes = [None] * cur
        dual = DualSet(nodes, ref_el, entity_ids)
        formdegree = dim - 1
        super().__init__(ref_el=ref_el,
                         dual=dual,
                         order=degree,
                         formdegree=formdegree,
                         mapping="contravariant piola")

    def degree(self):
        return self.get_order()

    def dual_basis(self):
        raise NotImplementedError(f"dual_basis is not implemented for {type(self).__name__}")

    def get_coeffs(self):
        raise NotImplementedError(f"get_coeffs not implemented for {type(self).__name__}")

    def tabulate(self, order, points, entity=None):

        if entity is None:
            entity = (self.ref_el.get_dimension(), 0)

        entity_dim, entity_id = entity
        transform = self.ref_el.get_entity_transform(entity_dim, entity_id)
        points = transform(points)

        phivals = {}

        for o in range(order+1):
            alphas = mis(self.fdim, o)
            for alpha in alphas:
                try:
                    polynomials = self.basis[alpha]
                except KeyError:
                    zr = tuple([0] * self.fdim)
                    polynomials = diff(self.basis[zr], *zip(variables, alpha))
                    self.basis[alpha] = polynomials
                T = np.zeros((len(polynomials[:, 0]), self.fdim, len(points)))
                for i in range(len(points)):
                    subs = {v: points[i][k] for k, v in enumerate(variables[:self.fdim])}
                    for ell in range(self.fdim):
                        for j, f in enumerate(polynomials[:, ell]):
                            T[j, ell, i] = f.evalf(subs=subs)
                phivals[alpha] = T

        return phivals

    def value_shape(self):
        return (self.fdim,)

    @cached_property
    def basis(self):
        degree = self.degree()
        if degree < 1:
            raise Exception("Trimmed serendipity face elements only valid for k >= 1")

        ref_el = self.get_reference_element()
        flat_el = flatten_reference_cube(ref_el)
        dim = flat_el.get_spatial_dimension()
        if dim != 2:
            if dim != 3:
                raise Exception("Trimmed serendipity face elements only valid for dimensions 2 and 3")

        verts = flat_el.get_vertices()
        dx = ((verts[-1][0] - x)/(verts[-1][0] - verts[0][0]), (x - verts[0][0])/(verts[-1][0] - verts[0][0]))
        dy = ((verts[-1][1] - y)/(verts[-1][1] - verts[0][1]), (y - verts[0][1])/(verts[-1][1] - verts[0][1]))
        x_mid = 2*x-(verts[-1][0] + verts[0][0])
        y_mid = 2*y-(verts[-1][1] + verts[0][1])
        try:
            dz = ((verts[-1][2] - z)/(verts[-1][2] - verts[0][2]), (z - verts[0][2])/(verts[-1][2] - verts[0][2]))
            z_mid = 2*z-(verts[-1][2] + verts[0][2])
        except IndexError:
            dz = None
            z_mid = None

        if dim == 3:
            FL = f_lambda_2_3d(degree, dx, dy, dz, x_mid, y_mid, z_mid)
            if (degree > 1):
                IL = I_lambda_2_3d(degree, dx, dy, dz, x_mid, y_mid, z_mid)
            else:
                IL = ()
            Sminus_list = FL + IL

        else:
            # Put all 2 dimensional stuff here.
            if degree < 1:
                raise Exception("Trimmed serendipity face elements only valid for k >= 1")

            EL = e_lambda_1_2d_part_one(degree, dx, dy, x_mid, y_mid)
            if degree >= 2:
                FL = trimmed_f_lambda_2d(degree, dx, dy, x_mid, y_mid)
            else:
                FL = ()
            Sminus_list = EL + FL
            Sminus_list = [[-a[1], a[0]] for a in Sminus_list]

        return {(0,) * dim: Array(Sminus_list)}


def f_lambda_2_3d(degree, dx, dy, dz, x_mid, y_mid, z_mid):

    FL = tuple([(-leg(j, y_mid) * leg(k, z_mid) * a, 0, 0)
                for a in dx for k in range(0, degree) for j in range(0, degree - k)] +
               [(0, leg(j, x_mid) * leg(k, z_mid) * b, 0)
                for b in dy for k in range(0, degree) for j in range(0, degree - k)] +
               [(0, 0, -leg(j, x_mid) * leg(k, y_mid) * c)
                for c in dz for k in range(0, degree) for j in range(0, degree - k)])
    return FL


def I_lambda_2_3d_pieces(current_deg, dx, dy, dz, x_mid, y_mid, z_mid):
    assert current_deg > 1, 'invalid for i = 1'
    ILpiece = tuple([])
    for j in range(0, current_deg - 1):
        for k in range(0, current_deg - 1 - j):
            ILpiece += tuple([(0, 0, -leg(j, x_mid) * leg(k, y_mid) * leg(current_deg - 2 - j - k, z_mid) *
                               dz[0] * dz[1])] +
                             [(0, -leg(j, x_mid) * leg(k, y_mid) * leg(current_deg - 2 - j - k, z_mid) *
                               dy[0] * dy[1], 0)] +
                             [(-leg(j, x_mid) * leg(k, y_mid) * leg(current_deg - 2 - j - k, z_mid) * dx[0] *
                               dx[1], 0, 0)])
    return ILpiece


def I_lambda_2_3d_tilde(degree, dx, dy, dz, x_mid, y_mid, z_mid):
    assert degree > 1, 'invalid for i = 1'
    IL_tilde = tuple([(0, 0, leg(degree - 2, z_mid) * dz[0] * dz[1])] +
                     [(0, leg(degree - 2, y_mid) * dy[0] * dy[1], 0)] +
                     [(leg(degree - 2, x_mid) * dx[0] * dx[1], 0, 0)])
    IL_tilde += tuple([(leg(degree - j - 2, x_mid) * leg(j, y_mid) * dx[0] * dx[1], leg(degree - j - 1, x_mid) *
                        leg(j - 1, y_mid) * dy[0] * dy[1], 0) for j in range(1, degree - 1)] +
                      [(leg(degree - j - 2, x_mid) * leg(j, z_mid) * dx[0] * dx[1], 0, leg(degree - j - 1, x_mid) *
                        leg(j - 1, z_mid) * dz[0] * dz[1]) for j in range(1, degree - 1)] +
                      [(0, leg(degree - j - 2, y_mid) * leg(j, z_mid) * dy[0] * dy[1], leg(degree - j - 1, y_mid) *
                        leg(j - 1, z_mid) * dz[0] * dz[1]) for j in range(1, degree - 1)])
    for k in range(1, degree - 2):
        for l in range(1, degree - 1 - k):
            j = degree - 2 - k - l
            IL_tilde += tuple([(-leg(j, x_mid) * leg(k, y_mid) * leg(l, z_mid) * dx[0] * dx[1],
                                leg(j + 1, x_mid) * leg(k - 1, y_mid) * leg(l, z_mid) * dy[0] * dy[1],
                                -leg(j + 1, x_mid) * leg(k, y_mid) * leg(l - 1, z_mid) * dz[0] * dz[1])])
    return IL_tilde


def I_lambda_2_3d(degree, dx, dy, dz, x_mid, y_mid, z_mid):
    IL = tuple([])
    for j in range(2, degree):
        IL += I_lambda_2_3d_pieces(j, dx, dy, dz, x_mid, y_mid, z_mid)
    IL += I_lambda_2_3d_tilde(degree, dx, dy, dz, x_mid, y_mid, z_mid)
    return IL


# Everything for 2-d should work already.
def e_lambda_1_2d_part_one(deg, dx, dy, x_mid, y_mid):
    EL = tuple(
        [(0, -leg(j, y_mid) * dx[0]) for j in range(deg)] +
        [(0, -leg(j, y_mid) * dx[1]) for j in range(deg)] +
        [(-leg(j, x_mid)*dy[0], 0) for j in range(deg)] +
        [(-leg(j, x_mid)*dy[1], 0) for j in range(deg)])

    return EL


def e_lambda_tilde_1_2d_part_two(deg, dx, dy, x_mid, y_mid):
    ELTilde = tuple([(-leg(deg, x_mid) * dy[0],
                      -leg(deg-1, x_mid) * dx[0] * dx[1] / (deg+1))] +
                    [(-leg(deg, x_mid) * dy[1],
                      leg(deg-1, x_mid) * dx[0] * dx[1] / (deg+1))] +
                    [(-leg(deg-1, y_mid) * dy[0] * dy[1] / (deg+1),
                      -leg(deg, y_mid) * dx[0])] +
                    [(leg(deg-1, y_mid) * dy[0] * dy[1] / (deg+1),
                      -leg(deg, y_mid) * dx[1])])
    return ELTilde


def e_lambda_1_2d(deg, dx, dy, x_mid, y_mid):
    EL = e_lambda_1_2d_part_one(deg, dx, dy, x_mid, y_mid)
    ELTilde = e_lambda_tilde_1_2d_part_two(deg, dx, dy, x_mid, y_mid)

    result = EL + ELTilde
    return result


def determine_f_lambda_portions_2d(deg):
    if (deg < 2):
        DegsOfIteration = []
    else:
        DegsOfIteration = []
        for i in range(2, deg):
            DegsOfIteration += [i]

    return DegsOfIteration


def f_lambda_1_2d_pieces(current_deg, dx, dy, x_mid, y_mid):
    if (current_deg == 2):
        FLpiece = [(leg(0, x_mid) * leg(0, y_mid) * dy[0] * dy[1], 0)]
        FLpiece += [(0, leg(0, x_mid) * leg(0, y_mid) * dx[0] * dx[1])]
    else:
        target_power = current_deg - 2
        FLpiece = tuple([])
        for j in range(0, target_power + 1):
            k = target_power - j
            FLpiece += tuple([(leg(j, x_mid) * leg(k, y_mid) * dy[0] * dy[1], 0)])
            FLpiece += tuple([(0, leg(j, x_mid) * leg(k, y_mid) * dx[0] * dx[1])])
    return FLpiece


def f_lambda_1_2d_trim(deg, dx, dy, x_mid, y_mid):
    DegsOfIteration = determine_f_lambda_portions_2d(deg)
    FL = []
    for i in DegsOfIteration:
        FL += f_lambda_1_2d_pieces(i, dx, dy, x_mid, y_mid)
    return tuple(FL)


def f_lambda_1_2d_tilde(deg, dx, dy, x_mid, y_mid):
    FLTilde = tuple([])
    FLTilde += tuple([(leg(deg - 2, y_mid)*dy[0]*dy[1], 0)])
    FLTilde += tuple([(0, leg(deg - 2, x_mid)*dx[0]*dx[1])])
    for k in range(1, deg - 1):
        FLTilde += tuple([(leg(k, x_mid) * leg(deg - k - 2, y_mid) * dy[0] * dy[1], -leg(k - 1, x_mid) * leg(deg - k - 1, y_mid) * dx[0] * dx[1])])

    return tuple(FLTilde)


def F_lambda_1_2d(deg, dx, dy, x_mid, y_mid):
    FL = []
    for k in range(2, deg):
        for j in range(k-1):
            FL += [(0, leg(j, x_mid)*leg(k-2-j, y_mid)*dx[0]*dx[1])]
            FL += [(leg(k-2-j, x_mid)*leg(j, y_mid)*dy[0]*dy[1], 0)]

    return tuple(FL)


def trimmed_f_lambda_2d(deg, dx, dy, x_mid, y_mid):
    FL = F_lambda_1_2d(deg, dx, dy, x_mid, y_mid)
    FLT = f_lambda_1_2d_tilde(deg, dx, dy, x_mid, y_mid)
    result = FL + FLT
    return result
