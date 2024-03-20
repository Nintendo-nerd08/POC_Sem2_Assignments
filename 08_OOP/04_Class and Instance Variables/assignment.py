class Rectangle:
    __counter=0
    
    def get_count():
        return Rectangle.__counter
    
    
    
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        __counter += 1
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__base * self.__height
 
 
 
#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
