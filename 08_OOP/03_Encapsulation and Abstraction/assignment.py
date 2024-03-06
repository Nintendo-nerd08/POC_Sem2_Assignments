class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__base * self.__height
 

rectangle1 = Rectangle(3, 4)
print(" The base of rectangle1 is", rectangle1.get_base())
print(" The height of rectangle1 is", rectangle1.get_height())
print(" The pereimeter of rectangle1 is", rectangle1.get_perimeter())
print(" The area of rectangle1 is", rectangle1.get_area())

rectangle2 = Rectangle(2, 4)
print(" The base of rectangle2 is", rectangle2.get_base())
print(" The height of rectangle2 is", rectangle2.get_height())
print(" The pereimeter of rectangle2 is", rectangle2.get_perimeter())
print(" The area of rectangle2 is", rectangle2.get_area())

#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
