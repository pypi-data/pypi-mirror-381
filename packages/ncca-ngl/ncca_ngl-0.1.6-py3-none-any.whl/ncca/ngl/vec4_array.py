"""
A container for ngl.Vec4 objects that mimics some of the behavior of a std::vector
"""

import numpy as np

from .vec4 import Vec4


class Vec4Array:
    """
    A class to hold a list of Vec4 objects and perform operations on them.
    """

    def __init__(self, values=None):
        """
        Initializes the Vec3Array.

        Args:
            values (iterable | int, optional): An iterable of Vec4 objects or an integer.
                If an integer, the array is initialized with that many default Vec3s.
                If an iterable, it's initialized with the Vec3s from the iterable.
                Defaults to None (an empty array).
        """
        self._data = []
        if values is not None:
            if isinstance(values, int):
                self._data = [Vec4() for _ in range(values)]
            else:
                for v in values:
                    if not isinstance(v, Vec4):
                        raise TypeError("All elements must be of type Vec4")
                    self._data.append(v)

    def __getitem__(self, index):
        """
        Get the Vec4 at the specified index.

        Args:
            index (int): The index of the element.

        Returns:
            Vec4: The Vec4 object at the given index.
        """
        return self._data[index]

    def __setitem__(self, index, value):
        """
        Set the Vec3 at the specified index.

        Args:
            index (int): The index of the element to set.
            value (Vec4): The new Vec3 object.
        """
        if not isinstance(value, Vec4):
            raise TypeError("Only Vec4 objects can be assigned")
        self._data[index] = value

    def __len__(self):
        """
        Return the number of elements in the array.
        """
        return len(self._data)

    def __iter__(self):
        """
        Return an iterator for the array.
        """
        return iter(self._data)

    def append(self, value):
        """
        Append a Vec4 object to the array.

        Args:
            value (Vec4): The Vec4 object to append.
        """
        if not isinstance(value, Vec4):
            raise TypeError("Only Vec4 objects can be appended")
        self._data.append(value)

    def extend(self, values):
        """
        Extend the array with a list of Vec4 objects.

        Args:
            values (list): A list of Vec4 objects to extend.
        """
        if not all(isinstance(v, Vec4) for v in values):
            raise TypeError("All elements must be of type Vec4")
        self._data.extend(values)

    def to_list(self):
        """
        Convert the array of Vec4 objects to a single flat list of floats.

        Returns:
            list: A list of x, y, z, w components concatenated.
        """
        return [comp for vec in self._data for comp in vec]

    def to_numpy(self):
        """
        Convert the array of Vec4 objects to a numpy array.

        Returns:
            numpy.ndarray: A numpy array of the vector data.
        """
        return np.array(self.to_list(), dtype=np.float32)

    def __repr__(self):
        return f"Vec4Array({self._data!r})"

    def __str__(self):
        return str(self._data)

    def sizeof(self):
        """
        Return the size of the array in bytes.

        Returns:
            int: The size of the array in bytes.
        """
        return len(self._data) * Vec4.sizeof()
