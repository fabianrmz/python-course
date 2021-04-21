x ={
    'pork': 123,
    'hello': 'there'
}
print(x)

x = dict([[1,2], ['final', 12]])
print(x)

x = dict([(1,2), {'final', 12}])
print(x)

x['shrimp']= 1.2323
print(x)

#obtain just the keys
print(x.keys())
print(x.values())
print(x.items())


#iterate trough dictionary
for key in x:
    print(key, x[key])

for key, value in x.items():
    print(key, value)