# Polygon Area Calculator
## Assignment
In this assignment I used object oriented programming to create a Rectangle class and a Square class. The Square class is a subclass of Rectangle and inherits its methods and attributes using Inheritance (A common object orientated practice/method).
### Rectangle Class
* 'set_width': Sets the width
* 'set_height': Sets the height
* 'get_area': Returns area '(width * height)'
* 'get_perimeter': Returns perimeter '(2 * width + 2 * height)'
* 'get_diagonal': Returns diagonal '((width ** 2 + height ** 2) ** .5)'
* 'get_picture': Returns a string that represents the shape using lines of "*".
* 'get_amount_inside': Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations)
### Square Class
The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The '__init__' method should store the side length in both the width and height attributes from the Rectangle class.
* 'set_side': Sets both the width and height to the same value
* 'set_width': Sets both the width and height to the same value
* 'set_height': Sets both the width and height to the same value

The unit tests for this project are in test_module.py.
