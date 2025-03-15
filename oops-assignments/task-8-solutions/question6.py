class Scoop:
    counter=0
    def __init__(self, flavour):
        self.flavour = flavour
        self.__price = None
        Scoop.counter += 1

    def __str__(self):
        return ("Flavour-{} and Price- {}".format(self.flavour, self.__price))

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    @staticmethod
    def show_scoop_count():
        return Scoop.counter

class Bowl:
    counter = 0

    def __init__(self):
        self.__scoops = []
        Bowl.counter += 1

    def add_scoops(self, *scoops):
        for scoop in scoops:
            self.__scoops.append(scoop)
    
    def show(self):
        total = 0
        for scoop in self.__scoops:
            print(scoop)
            total += scoop.get_price()
        print(f"Total: {total}")

    @staticmethod
    def show_bowl_count():
        return Bowl.counter


choco = Scoop('chocolate')
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)

vanilla = Scoop('vanilla')
vanilla.set_price(150)

bowl = Bowl()

bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# add_scoops should handle both scener

bowl.show()
print(Bowl.show_bowl_count())
print(Scoop.show_scoop_count())

