'''def get_formatted_name(first_name,last_name):
    full_name = {"finame":first_name,"sename":last_name}
    return full_name

while True:
    print("you can input 'q' at any time to quit ")
    first = input("please input your first name")
    if first == "q":
        break
    last = input("please input your last name")
    if last == "q":
        break
    full_name = get_formatted_name(first,last)
    print(full_name)
def greet(names):
    for name in names:
        print(f"Hello, {name.title()}")
name_list = ["Kai","kate","jack"]
greet(name_list)

def print_models(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"print model:{current_design}")
        completed_designs.append(current_design)

def show_complete_model(completed_designs):
    print("\nthe following:")
    for item in completed_designs:
        print(item)

unprinted_designs = ["aaa","bbb","ccc"]
completed_designs=["ddd"]

print_models(unprinted_designs[:],completed_designs)
show_complete_model(completed_designs)
print(unprinted_designs)

from make_cars import make_cars as mc
car = mc("suku","outback",color="blue",size="big")
print(car)'''
