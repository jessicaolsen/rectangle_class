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
   
   #Defining if string is called
    def __str__(self) : 
        return "Rectangle(width={}, height={})".format(self.width,self.height)

    #Determines how many times a shape will fit inside the given shape
    def get_amount_inside(self, shape) : 
        self.shape = shape
        num_times = int(self.get_area() / (shape.width * shape.height))
        return num_times

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
    
    #Initializing Square class
    def __init__(self, side) : 
        self.width = side
        self.height = side
        
    #Defining Side = Width = Height
    def set_side(self, side) : 
        self.width = side
        self.height = side
    
    #Set width method
    def set_width(self, side) : 
        self.width = side
        self.height = side

    #Set height method
    def set_height(self, side): 
        self.height = side
        self.width = side
    
    #Defining if String is called
    def __str__(self) : 
        return "Square(side={})".format(self.width)


rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect.get_picture())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
