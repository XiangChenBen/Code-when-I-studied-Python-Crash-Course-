'''Name_add = input()
Name=[]
Name.append(Name_add.title())
print(Name)'''

#del pop remove 三个方法进行删除

Number = ["a","b","c","d","e","f"]
del Number[5]
print(Number)

first_number = Number.pop(0)
print(Number)
print(first_number)

Number.remove("c")
print(Number)

#remove 只删除第一个，多个需要循环删除
Number.append("d")
print(Number)
Number.remove("d")
print(Number)

#sort排序
people = ["jack","lois","dick","wen"]
people.sort()
print(people)
people.sort(reverse=True)
print(people)

