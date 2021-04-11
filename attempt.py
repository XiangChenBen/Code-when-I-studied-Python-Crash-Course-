people = ["bana","anna","dick","cris"]
print(f"Here is the original list:{people}")
print(f"\nHere is the sorted list (reversed Alphabet):{sorted(people,reverse=True)}") #临时性
print(f"\nHere is the original list again:{people}")
people.reverse() #永久性的
print(f"\nHere is the reversed list again:{people}")
people.reverse()
print(f"\nHere is the original list again:{people}")

#练习3.8
destinations = ["Paris","London","New Yorks","Singapore","Toronto"]
print(destinations)
print(sorted(destinations))
print(destinations)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)
print(destinations[-1]) #调取最后一个