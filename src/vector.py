import math
import typing


class Vector:
    """A class to represent a vector

    :param elements: A list of floats representing the elements of the vector
    """

    def __init__(self, elements: list[float]) -> None:
        """Initialize the vector"""
        for el in range(len(elements)):
            if not isinstance(elements[el], (int, float)):
                raise RuntimeError("Elements of the vector must be integers or floats")
            elements[el] = float(elements[el])

        self.elements = elements

    def norm(self) -> float:
        """Calculate the norm of the vector"""
        return math.sqrt(sum([el ** 2 for el in self.elements]))

    def cross(self, vector: 'Vector') -> 'Vector':
        """Calculate the cross product of two vectors"""
        if not len(self.elements) == 3 and not len(vector.elements) == 3:
            raise ValueError("Cross product is only defined for 3D vectors")

        el_1 = self.elements[1] * vector.elements[2] - self.elements[2] * vector.elements[1]
        el_2 = self.elements[2] * vector.elements[0] - self.elements[0] * vector.elements[2]
        el_3 = self.elements[0] * vector.elements[1] - self.elements[1] * vector.elements[0]
        return Vector([el_1, el_2, el_3])

    def ang(self, vector: 'Vector') -> float:
        """Calculate the angle between two vectors"""
        return math.acos(self * vector / (self.norm() * vector.norm()))

    def proj(self, vector: 'Vector') -> 'Vector':
        """Calculate the projection of a vector onto another vector"""
        factor = self * vector / math.pow(self.norm(), 2)
        return Vector([factor * el for el in self.elements])

    def __sum__(self, other: 'Vector') -> 'Vector':
        """Sum two vectors"""
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length")
        return Vector([self.elements[i] + other.elements[i] for i in range(len(self.elements))])

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors"""
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must have the same length")
        return Vector([self.elements[i] - other.elements[i] for i in range(len(self.elements))])

    def __mul__(self, other: typing.Union['Vector', int, float]) -> 'Vector' | float:
        """Dot product of two vectors"""
        if not isinstance(other, (Vector, int, float)):
            raise TypeError("Multiplication is only defined for vectors, integers, and floats")

        if isinstance(other, (int, float)):
            return Vector([el * other for el in self.elements])

        return sum([self.elements[i] * other.elements[i] for i in range(len(self.elements))])

    def __divmod__(self, other): # noqa
        """Divide vector by a scalar"""
        if not isinstance(other, (int, float)):
            raise TypeError("Division is only defined for integers and floats")

        return Vector([el / other for el in self.elements])

    def __str__(self) -> str:
        """Return a string representation of the vector"""
        return f"Vector({self.elements})"
