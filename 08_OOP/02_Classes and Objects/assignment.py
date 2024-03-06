from math import hypot
class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    
    def area(self):
          return (1/2) * self.base * self.height
    
    def hypotenuse(self):
     return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()

        
        

triangle1 = RightTriangle(3, 4)
print("The area of triange_1 is", triangle1.area())
print("The hypotenuse of triangle1 is", triangle1.hypotenuse)
print("The perimeter of triangle1 is", triangle1.perimeter())
print("The large angle of triangle1 is", triangle1.min_angle())
print("The small angle of triangle1 is", triangle1.min_angle())

triangle2 = RightTriangle(2, 4)
print("The area of triangle2 is", triangle2.area())
print("The hypotenuse of triangle1 is", triangle2.hypotenuse)
print("The perimeter of triangle1 is", triangle2.perimeter())
print("The large angle of triangle2 is", triangle2.min_angle())
print("The small angle of triangle2 is", triangle2.min_angle())
