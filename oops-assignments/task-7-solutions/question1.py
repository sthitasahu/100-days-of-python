class Rectangle:

    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
   
    def calculate_perimter(self):
        return 2*(self.__length+self.__breadth)

    def calculate_area(self):
        return self.__length*self.__breadth
    
    def display(self):
        print("The length of the ractangle is :",self.__length)
        print("The breadth of teh rectangle is : ",self.__breadth)
        print("The perimeter of thr rectangle is: ",self.calculate_perimter())
        print("The area of the rectangle is: ",self.calculate_perimter())

obj=Rectangle(3,5)
obj.display()    