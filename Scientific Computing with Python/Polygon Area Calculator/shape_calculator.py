class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            width_string = self.width * "*"
            width_string += "\n"
            return width_string * self.height

    def get_amount_inside(self, shape):
        """Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""
        if shape.height > self.height or shape.width > self.width:
            return 0
        else:
            return int(self.height / shape.height) * int(self.width / shape.width)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width

    def set_height(self, height):
        self.height = height
        self.width = height
        self.side = height

    def __str__(self):
        return f"Square(side={self.side})"
