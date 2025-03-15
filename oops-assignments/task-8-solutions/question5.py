class Student:

    def __init__(self):
       self.__sid=None
       self.__marks=None
       self.__age=None

    #setter methods 

    def set_sid(self, sid):
        self.__sid = sid

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    #getter methods

    def get_sid(self):
        return self.__sid

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def validate_marks(self):
        return self.__marks>=0 and self.__marks<=100

    def validate_age(self):
        return self.__age>20
    
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            return self.__marks>=65
        else:
            return False
     

#Code here

class Student:

  def __init__(self):
    self.__sid = None
    self.__marks = None
    self.__age = None

  # setter methods
  def set_sid(self,sid):
    self.__sid = sid
  def set_marks(self,marks):
    self.__marks = marks
  def set_age(self,age):
    self.__age = age

  # getters
  def get_sid(self):
    return self.__sid
  def get_marks(self):
    return self.__marks
  def get_age(self):
    return self.__age

  def validate_age(self):
    return self.__age>20

  def validate_marks(self):
    return self.__marks>=0 and self.__marks<=100

  def check_qualification(self):
    if self.validate_age() and self.validate_marks():
      return self.__marks>= 65
    else:
      return False

stu1 = Student()

stu1.set_sid(101)
stu1.set_marks(66)
stu1.set_age(19)

print(stu1.get_sid())
print(stu1.get_marks())
print(stu1.get_age())

print(stu1.check_qualification())