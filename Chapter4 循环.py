'''magicians = ["bana","anna","dick","cris"]
for magician in magicians:
    print(f"{magician.title()} is a great magician")
    print(f"I like {magician.title()}\n")
print("I love them")'''

'''
for number in range(1,5):
    print(number)
print("\n")
for number in range(5):
    print(number)
print("\n")
for number in range(1,11,2):
    print(number)
    
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = []
for digit in range(10):
    digits.append(digit)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
print(digits[1]+digits[2])

squares = [value**2 for value in range(1,11)]
print(squares)

#4.3
for value in range(1,21):
    print(f"{value}, ",end="")

#4.4 & 4.5
values = []
for value in range(1,1000001):
    values.append(value)
print(min(values))
print(max(values))
print(sum(values))

#4.7
values = [value**3 for value in range(3,31,3)]
for value in values:
    print(f"{value}, ",end="")'''

#4.13
menu = ("Pizza","Hamberger","Cream","Vegetable","Roaster")
for food in menu:
    print(food)
menu = ("Apple","Pie","Cream","Vegetable","Roaster")
print("\n")
for food in menu:
    print(food)
