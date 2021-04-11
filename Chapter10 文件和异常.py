'''file_path = "D:\pythonProject\源代码文件\源代码文件\chapter_10\pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(f"The first million digits of PI is {pi_string[:52]}...")

birthday = input("Please input your birthday, in the form ddmmyy:")
if birthday in pi_string:
    print("Congratulations! Your Birthday is in the first million digits of PI")
else:
    print("Unfortunately, your birthday is not in the first million digits of PI")

message = "I love dogs,dogs love me,dogs dogs dogs"
new_message = message.replace("dog","cat",4)
print(message)
print(new_message)

guest_name = input("Please input your name")

filename = f"{guest_name}.txt"
with open(filename,"a") as file_object:
    file_object.write(f"This is a 自传 for {guest_name}")

#异常
def count_word(filename):
    try:
        with open(filename,encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} is not found")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"{filename} has {num_words} words")

filename = "alice.txt"
count_word(filename)

#数据的存储
import json
filename = "number.json"
numbers = [1,3,5,7,9,11]
with open(filename,"w") as f:
    json.dump(numbers,f)
with open(filename) as f:
    data = json.load(f)
print(data)'''

import json
def get_store_name():
    filename = "username.json"
    try:
        with open(filename) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name

def get_new_name():
    username = input("What is your name?")
    filename = f"username.json"
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"we will remember you when you come back again, {username}")

def greet_user():
    username = get_store_name()
    if username:
        print(f"Welcome back, {username}")
    else:
        get_new_name()

greet_user()