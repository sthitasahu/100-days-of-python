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
         
    def allocate_course(self,tech):
        if self.check_eligibility():
            if tech in self.__tech:
               return 'Elgible to take the course '
            else :
                return 'This technology is unknown to the instructor'
        else:
            return 'Not eligible to take the course '

ins=Instructor('nitish',5,['Data Science','MLOPS','LLMOPS','Web Development'],5.0)
print(ins.check_eligibility())
print(ins.allocate_course('Data Science'))
print(ins.allocate_course('Machine Learning'))
    