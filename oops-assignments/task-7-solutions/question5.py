class Instructor:
       
    def __init__(self,name,experience,technology,ratings) :
         self.__name=name
         self.__exp=experience
         self.__tech=technology
         self.__reviews=ratings

    def check_eligibility(self):
        if self.__exp>3 and self.__reviews>=4.5:
            return True
        elif self.exp<=3 and self.__reviews>=4.0:
            return True
        else:
            return False
         