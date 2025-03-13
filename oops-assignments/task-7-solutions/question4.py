# write your code here
import random 

class FlashCard:

    def __init__(self):
        self.__fruits = {
            'apple':'red',
            'banana':'yellow',
            'watermelon':'green',
            'strawberry':'pink',
            'guava':'green'
        }

    def quiz(self):

        while True:

            fruit,color = random.choices(list(self.__fruits.items()))[0]

            print('What is the color of {}'.format(fruit))
            user_answer = input()

            if user_answer.lower() == color:
                print('Sahi jawab')
            else:
                print('Galat jawab')

            option = int(input('enter 0 to play again. 1 to exit'))

            if option:
                break

print('Welcome to the fruit quiz')
fc = FlashCard()
fc.quiz()

