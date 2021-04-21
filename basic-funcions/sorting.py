x = "what are you doing"
print(sorted(x))


x = [1,2,43,4,1]
print(sorted(x))


# sort order based on second letter

z = ('kzzin', 'nzklas', 'john')
print(sorted(z, key=lambda k: k[1]))



# sort the same list

x = [5,2,7,4,8]
x.sort()
print(x)

#reversed x

print(x, reversed=True)