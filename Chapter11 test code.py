from name_function import get_formatted_name

print("you can quit at any time when you input q")

while True:
    first_name = input("Please input the first name:")
    if first_name == "q":
        break
    last_name = input("Please input the last name:")
    if last_name == "q":
        break
    formatted_name = get_formatted_name(first_name,last_name)
    print(f"\tThe neat name is: {formatted_name}")
