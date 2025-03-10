"""
Simple example of using inheritance.
"""


class Base:
    """
    Simple base class.
    """

    def __init__(self, num):
        self._number = num

    def __str__(self):
        """
        Return human readable string.
        """
        return str(self._number)


class Sub(Base):
    """
    Simple sub class.
    """

    def __init__(self, num):
        super().__init__(num)

# Another working class
class Sub(Base):
    """
    Simple sub class.
    """

    pass


obj = Sub(42)
print(obj)
