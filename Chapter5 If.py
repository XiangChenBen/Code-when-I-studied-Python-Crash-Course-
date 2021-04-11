'''cars = ["audi","bmw","toyota","honda"]
for car in cars:
    if car.lower() == "bmw":
        print(car.upper())
    else:
        print(car.title())

#5-2
sentence = "I am smart"
print("is sentence == 'I am smart'?")
print(sentence.lower()=="i am smart")

age = 65
if age<4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age>=65:
    price = 20
print(f"the price is {price}")

sauce = ["mushroom",'tomato','pepper']
request = ["mushroom",'pepper']
for i in range(0,len(sauce)):
    if sauce[i] in request:
        print(f"add {sauce[i]}")

#5-3
favorite_fruits = ["apple",'banana','kiwi']
fruit=input()
if fruit in favorite_fruits:
    print(f"You really like {fruit}")'''

#5-8
users = ["jack","alice","admin","lois"]
del users[:]
if not users:
    print("empty now")
if users:
    for user in users:
        if user == "admin":
            print(f"Hello {user.title()}, see a report?")
        else:
            print(f"Hello {user.title()}, nice to see you again!")

else:
    print("We need to find some users")