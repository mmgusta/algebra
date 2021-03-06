import math

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnetude(self):
        mag = 0
        for x in self.coordinates:
            mag += math.pow(x,2)
            pass
        return math.sqrt(mag)

    def normalized(self):
        try:
            step1 = 1/self.magnetude()
            return self.times_scalar(step1)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dotProduct(self, v):
        new_coordinates = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return round(sum(new_coordinates), 3)

    def angle(self, v, degree=False):
        try:
            #dot = self.dotProduct(v)
            #mag_v1 = self.magnetude()
            #mag_v2 = v.magnetude()
            #return math.acos(dot/(mag_v1*mag_v2)) #radians
            mag_v1 = self.normalized()
            mag_v2 = v.normalized()
            if not degree:
                return math.acos(mag_v1.dotProduct(mag_v2))
            else:
                return math.degrees(math.acos(mag_v1.dotProduct(mag_v2)))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Não consigo comparar um angulo com vetores zerados")
            else:
                raise e
        
    def isOrthogonalTo(self, v, tolerance = 1e-10):
        return abs(self.dotProduct(v)) < tolerance

    def isParallelTo(self, v):
        return(self.isZero() or
                v.isZero() or
                self.angle(v) == 0 or
                self.angle(v) == math.pi)

    def isZero(self, tolerance = 1e-10):
        return self.magnetude() < tolerance

    def projection(self, b):
        norm_b = b.normalized()
        dot_v = self.dotProduct(norm_b)
        proj_v = norm_b.times_scalar(dot_v)
        return proj_v

    def component(self, b):
        proj_v = self.projection(b)
        return self.minus(proj_v)

    def decomposition(self, b):
        proj_v = self.projection(b)
        comp_v = self.component(b)
        return proj_v.plus(comp_v)

    def crossProduct(self, v):
        coord1 = (self.coordinates[1]*v.coordinates[2]) - (v.coordinates[1]*self.coordinates[2])
        coord2 = -((self.coordinates[0]*v.coordinates[2]) - (v.coordinates[0]*self.coordinates[2]))
        coord3 = (self.coordinates[0]*v.coordinates[1]) - (v.coordinates[0]*self.coordinates[1])
        return Vector([coord1, coord2, coord3])

    def areaParallelogram(self, v):
        cross_prod = self.crossProduct(v)
        return cross_prod.magnetude()

    def areaTriangle(self, v):
        return self.areaParallelogram(v) / 2

# Ex1
# v1 = Vector([8.218, -9.341])
# v2 = Vector([-1.129, 2.111])
# print(v1.plus(v2))

# v3 = Vector([7.119, 8.215])
# v4 = Vector([-8.223, 0.878])
# print(v3.minus(v4))

# v5 = Vector([1.671, -1.012, -0.318])
# c = 7.41
# print(v5.times_scalar(c))

# Ex2
# v1 = Vector([-0.221, 7.437])
# print(v1.magnetude())

# v2 = Vector([8.813, -1.331, -6.247])
# print(v2.magnetude())

# v3 = Vector([5.581, -2.136])
# print(v3.normalized())

# v4 = Vector([1.996, 3.108, -4.554])
# print(v4.normalized()) 

# Ex3
# v1 = Vector([7.887, 4.138])
# v2 = Vector([-8.802,6.776])

# print(v1.dotProduct(v2))

# v3 = Vector([-5.955, -4.904, -1.874])
# v4 = Vector([-4.496, -8.755, 7.103])

# print(v3.dotProduct(v4))

# v5 = Vector([3.183, -7.627])
# v6 = Vector([-2.668, 5.319])

# print(v5.angle(v6))

# v7 = Vector([7.35, 0.221, 5.188])
# v8 = Vector([2.751, 8.259, 3.985])

# print(v7.angle(v8, degree=True))

# Ex5
# v1 = Vector([-7.579, -7.88])
# v2 = Vector([22.737, 23.64])
# print('Parallel:', v1.isParallelTo(v2))
# print('Orthogonal:', v1.isOrthogonalTo(v2))

# v3 = Vector([-2.029, 9.97, 4.172])
# v4 = Vector([-9.231, -6.639, -7.245])
# print('Parallel:', v3.isParallelTo(v4))
# print('Orthogonal:', v3.isOrthogonalTo(v4))

# v5 = Vector([-2.328, -7.284, -1.214])
# v6 = Vector([-1.821, 1.072, -2.94])
# print('Parallel:', v5.isParallelTo(v6))
# print('Orthogonal:', v5.isOrthogonalTo(v6))

# v7 = Vector([2.118, 4.827])
# v8 = Vector([0, 0])
# print('Parallel:', v7.isParallelTo(v8))
# print('Orthogonal:', v7.isOrthogonalTo(v8))


# Ex6
# v1 = Vector([3.039, 1.879])
# b1 = Vector([0.825, 2.036])
# print(v1.projection(b1))

# v2 = Vector([-9.88, -3.264, -8.159])
# b2 = Vector([-2.155, -9.353, -9.473])
# print(v2.component(b2))

# v3 = Vector([3.009, -6.172, 3.692, -2.51])
# b3 = Vector([6.404, -9.144, 2.759, 8.718])
# print(v3.projection(b3))
# print(v3.component(b3))

# Ex7
# v1 = Vector([8.462, 7.893, -8.187])
# v2 = Vector([6.984, -5.975, 4.778])
# print('Cross product',v1.crossProduct(v2))

# v3 = Vector([-8.987, -9.838, 5.031])
# v4 = Vector([-4.268, -1.861, -8.866])
# print('Area of parallelogram', v3.areaParallelogram(v4))

# v5 = Vector([1.5, 9.547, 3.691])
# v6 = Vector([-6.007, 0.124, 5.772])
# print('Area of triangle', v5.areaTriangle(v6))