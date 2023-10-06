"""
HW13_1
Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError,
которое выбрасывается при некорректных значениях ширины и высоты,
как при создании объекта, так и при установке их через сеттеры.
"""


class NegativeValueError(Exception):
    pass


class Rectangle:

    def __init__(self, width: int, height: int = None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        elif height <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'width' and value <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
        if key == 'height' and value <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
        return object.__setattr__(self, key, value)

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __sub__(self, other):
        width = abs(self.width - other.width)
        height = abs(self.height - other.height)
        return Rectangle(width, height)


r = Rectangle(4, 4)
r.height = -3
