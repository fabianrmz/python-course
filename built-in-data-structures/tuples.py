x = ()

x = (1,2,3,4,5,6,7)
print(x)

x = 1, 1, 3
print(x)

list1 = [3,6,3]
x = tuple(list1)
print(x, type(x))
# not assignment in tuples x[2]=666, inmutables
print(x[2])


y = ([1,2], 3)
del(y[0][1])
print(y)