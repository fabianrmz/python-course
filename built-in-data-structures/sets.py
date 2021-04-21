# faster access than list
x = {1,2,3,4,56,423,13}
print(x)

y = set()
print(y)

list1 = [2,3,4]
z = set(list1)
print(z)


#add
x = {2,5,3,67}
print(x)
x.add(666)
print(x)

x.remove(3)
print(x)

print(len(x))

print(x.pop(), x)

