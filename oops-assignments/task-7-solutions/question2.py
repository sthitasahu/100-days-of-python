class BankAccount:
     def __init__(self,name,acc_no,balance) :
        self.__name=name
        self.__acc_no=acc_no
        self.__balance=balance
     
     def deposit(self,amount):
        self.__balance=self.__balance+amount

     def withdrawal(self,amount):
        if amount>=self.__balance:
            print("Insufficient balance")   
        else:
            self.__balance=self.__balance-amount
            reduction=self.__bankFees()
            self.__balance=self.__balance-reduction

     def __bankFees(self):
        return 0.05*self.__balance
    

     def display(self):
        print('Account Name:',self.__name)
        print('Account no: ', self.__acc_no)
        print('Balance: ',self.__balance)
    


cust=BankAccount("Amit",12345678910,900)
cust.display()
cust.deposit(100)
cust.display()
cust.withdrawal(100)   
cust.display()