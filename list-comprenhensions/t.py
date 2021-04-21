
unde_10 = [x for x in range(10)]
print(unde_10)

squares = [x**2 for x in unde_10]
print(squares)

odds = [x for x in range(30) if x%2!=0]
print(odds)

ten_x = [x*10 for x in range(10)]
print(ten_x)

#only numerics through s
s = 'if i got 1 penny for every cent gg 99 aa'
nums = [x for x in s if x.isnumeric()]
print(nums)

names = ['Raul', 'pedro', 'Juan']
idx = [k for k, v in enumerate(names) if v =='pedro']
print('index = ', str(idx[0]))

import random
letters = [x for x in 'ABCDEFGHI']
print(letters)
random.shuffle(letters)
print(letters)

letters = [x for x in letters if x!='C']
print(letters)