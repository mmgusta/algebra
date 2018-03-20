# from decimal import Decimal, getcontext

from vector import Vector

#getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = 0*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0
        self.constant_term = constant_term

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            #basepoint_coords = self.dimension

            initial_index = Line.first_nonzero_index(n.coordinates)
            initial_coefficient = n.coordinates[initial_index]

            d= c/initial_coefficient
            #basepoint_coords[initial_index] = d

            self.basepoint = Vector([d])

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    def is_paralallel_to(self, ell):
        n1 = self.normal_vector
        n2 = ell.normal_vector

        if n1.isParallelTo(n2) :
            if self.is_same_line(ell):
                return 'Parallel, same line'
            else:
                return 'Parallel, not same line'
        else:
            points = self.intersection_potions(ell)
            return 'Not parallel, intersection ponts. X= ' + str(points[0]) + ' Y= ' + str(points[1])


    def is_same_line(self, l2):
        x0 = self.basepoint
        y0 = l2.basepoint

        basepoint_diff = x0.minus(y0)

        normal = self.normal_vector

        if normal.isOrthogonalTo(basepoint_diff):
            return True
        else:
            return False

    def intersection_potions(self, l2):
        k1, k2 = self.constant_term, l2.constant_term
        A,B,C,D = self.normal_vector.coordinates[0], self.normal_vector.coordinates[1], l2.normal_vector.coordinates[0], l2.normal_vector.coordinates[1]

        x = round(((D*k1) - (B*k2))/((A*D) - (B*C)), 3)
        y = round((-(C*k1) + (A*k2))/((A*D) - (B*C)), 3)

        return x,y

    # def is_near_zero(self, eps=1e-10):
    #     return abs(self) < eps

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not abs(item) < 1e-10:
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    
        

l1 = Line(normal_vector=Vector([4.046, 2.836]), constant_term=1.21)
l2 = Line(normal_vector=Vector([10.115, 7.09]), constant_term=3.025)
print('Resp:', l1.is_paralallel_to(l2))  

l3 = Line(normal_vector=Vector([7.204, 3.182]), constant_term=8.68)
l4 = Line(normal_vector=Vector([8.172, 4.114]), constant_term=9.883)
print('Resp:', l3.is_paralallel_to(l4))  

l5 = Line(normal_vector=Vector([1.182, 5.562]), constant_term=6.744)
l6 = Line(normal_vector=Vector([1.773, 8.343]), constant_term=9.525)
print('Resp:', l5.is_paralallel_to(l6))  