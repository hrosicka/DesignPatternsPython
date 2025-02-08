import math

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        raise NotImplementedError("draw() method must be implemented in subclasses.")

    def area(self):
        raise NotImplementedError("area() method must be implemented in subclasses.")

    def perimeter(self):
        raise NotImplementedError("perimeter() method must be implemented in subclasses.")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle of {self.color} color with radius {self.radius}.")

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def draw(self):
        print(f"Drawing a square of {self.color} color with side {self.side}.")

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side


class Ellipse(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b

    def draw(self):
        print(f"Drawing an ellipse of {self.color} color with major axis {self.a} and minor axis {self.b}.")

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.a**2 + self.b**2) / 2)


class ShapeFactory:
    def create_shape(self, type, color, *args):
        if type == "circle":
            return Circle(color, args[0])
        elif type == "square":
            return Square(color, args[0])
        elif type == "ellipse":
            return Ellipse(color, args[0], args[1])
        else:
            return None


# Creating a shape factory
factory = ShapeFactory()

# Creating shapes
circle = factory.create_shape("circle", "red", 5)
square = factory.create_shape("square", "blue", 10)
ellipse = factory.create_shape("ellipse", "green", 8, 4)

# Drawing shapes
circle.draw()
square.draw()
ellipse.draw()

# Calculating and printing area and perimeter
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
print(f"Square area: {square.area()}")
print(f"Square perimeter: {square.perimeter()}")
print(f"Ellipse area: {ellipse.area()}")
print(f"Ellipse perimeter: {ellipse.perimeter()}")