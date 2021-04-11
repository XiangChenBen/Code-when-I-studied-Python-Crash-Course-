'''class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sits down")

    def rollover(self):
        print(f"{self.name} roll over")

class Tidi(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.size = 10
        self.runspeed = Run_speed()

    def desceibe_tidi(self):
        print(f"Tidi is small with a size = {self.size}")

    def sit(self):
        print("Tidi does not want to sit down")

class Run_speed():
    def __init__(self,runspeed=20):
        self.runspeed = runspeed

    def describe_speed(self):
        print(f"the running speed is {self.runspeed}")

my_dog = Dog("KKR",8)
your_dog = Dog("AAR",10)
his_dog = Tidi("JJR",13)

print(f"my dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")
my_dog.sit()
my_dog.rollover()

print(f"\nyour dog's name is {your_dog.name}")
print(f"your dog's age is {your_dog.age}")
your_dog.sit()
your_dog.rollover()

print(f"\nhis dog's name is {his_dog.name}")
print(f"his dog's age is {his_dog.age}")
his_dog.sit()
his_dog.rollover()
his_dog.size = 20
his_dog.desceibe_tidi()
his_dog.runspeed = Run_speed(40)
his_dog.runspeed.describe_speed()'''

'''
#9-13
import random

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self,trials=1):
        for trial in range(1,trials+1):
            result = random.randint(1, self.sides)
            print(f"{trial} trial: {result}")

dice = Die(10)
dice.roll_die(20)'''

#9-14
from random import choice
code = ["1","2","3","4","5","6",'a','b','c',"d"]
my_ticket = set(['1','2','c','b'])
count_time = 0
while True:
    count_time += 1
    copy_code = code[:]
    prize = []
    for i in range(0,4):
        selected_str = choice(copy_code)
        prize.append(selected_str)
        copy_code.remove(selected_str)

    print(prize)
    if  set(prize) == my_ticket:
        print(f"Yes, you get it after {count_time}")
        break

