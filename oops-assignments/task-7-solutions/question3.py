from math import sqrt


class Computation:

    def __init__(self):
        pass
    
    def Factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact

    def naturalSum(self,n):
        sum=0
        for i in range(1,n+1):
           sum=sum+i
        return sum
    
    def testPrime(self,n):
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True

    def testPrims(self,n,m):
        greater=min(n,m)
        commondivisors=0
        for i in range (1,greater+1):
            if (n%i==0 and m%i==0):
                commondivisors+=1
        if(commondivisors==1):
            print('The numbers are co-prime')
        else:
            print('The numbers are not co-prime')

    def tableMult(self,n):
        for k in range(1,11):
            print(k, "*",n,"=",k*n)
    
    def allTables(self):
        for k in range(1,11):
            print('\n The multiplication table of ',k ,'is:')
            self.tableMult(k)


    def listDivisor(self,n):
        L=[]
        for i in range(1,int(sqrt(n))):
            if n%i==0:
              L.append(i)
              L.append(int(n/i))
        L.sort()
        return L 

    def listPrimeDivisor(self,n):
        LDiv=[]
        for i in range(1,n+1):
            if (n%i==0 and  self.testPrime(i)):
                LDiv.append(i)
        return LDiv

        
Comput= Computation ()
Comput.testPrims(13, 7)
print ("List of divisors of 18:", Comput.listDivisor(18))
print ("List of prime divisors of 18:", Comput.listPrimeDivisor(18))
Comput.allTables()
