class Rectangle:

    #initializing with Width and Height 
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        
    #Set width method
    def set_width(self, width) : 
        self.width = width 

    #Set height method
    def set_height(self, height): 
        self.height = height

    #Defining the area
    def get_area(self) : 
        return self.width * self.height
    
    #Defining the Parameter
    def get_perimeter(self) :
        return (2 * self.width) + (2 * self.height)
    
    #Defining the Get Diagonal Method
    def get_diagonal(self) : 
        return (( self.width ** 2 ) + ( self.height ** 2 )) ** 0.5
    
    #Set get picture method
    def get_picture(self) : 
        if self.height >= 50 : 
            return "Too big for picture."
        elif self.width >= 50 : 
            return "Too big for picture."
        else: 
            width_rect = '*' * self.width
            line = width_rect + '\n'
            return (self.height * line)

class Square(Rectangle):
    
    def __init__(self, side) : 
        Rectangle.width = side
        Rectangle.height = side

    def set_side(self) : 
        pass



rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
#print(rect)
print(rect.get_picture())
print(rect)

sq = Square(9)
print(sq.get_area())
#sq.set_side(4)
#print(sq.get_diagonal())
#print(sq)
