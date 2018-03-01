import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

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
        step1 = 1/self.magnetude()
        return self.times_scalar(step1)


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