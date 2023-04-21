class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if (self.height > 50) or (self.width > 50):
      return "Too big for picture."
    
    output = ""
    i = 0
    #output += '*' * self.width
    while i < self.height:
      output += '*' * self.width + "\n"
      i += 1

    return output

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()
    

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    Rectangle.set_width(self, side)
    Rectangle.set_height(self, side)

  def set_width(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)

  def set_height(self, height):
    Rectangle.set_width(self, height)
    Rectangle.set_height(self, height)

  