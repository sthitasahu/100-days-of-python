class Counter:
    __count = 0
    def __init__(self):
        Counter.__count += 1
    
    def get_count(self):
        return Counter.__count
    
o1=Counter()
print(o1.get_count())
o2=Counter()
print(o2.get_count())   
o3=Counter()
print(o3.get_count())       
o4=Counter()
print(o4.get_count())