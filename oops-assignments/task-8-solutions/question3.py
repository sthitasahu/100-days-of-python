class Rectangle:
    def __new__(cls):
        raise RuntimeError("Use Rectangle.property() to create an instance.")

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    @classmethod
    def property(cls, length, breadth):
        # Create an instance using object.__new__() to bypass __new__()
        instance = super().__new__(cls)  
        instance.__length = length
        instance.__breadth = breadth
        return instance

    def calculate_area(self):
        return self.__length * self.__breadth

    def is_square(self):
        return True if self.__length == self.__breadth else False



rect1 = Rectangle.property(5, 8)
print(rect1.calculate_area())  # Output: 40
print(rect1.is_square())       # Output: False

rect2 = Rectangle.property(5, 5)
print(rect2.calculate_area())  # Output: 25
print(rect2.is_square())       # Output: True


#rect3=Rectangle(3,5)
# print(rect3.calculate_area())  #incorrect 
#print(rect3.is_square())       # incorrect