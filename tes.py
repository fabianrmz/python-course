# lista = [17,18,5,4,6,1]
# newLista =[]
# i= 0
# for n in lista:
#     i+=1
#     temp = -1
#     for j in lista[i:]:
#         if temp < j:
#             temp = j
#     newLista.append(temp)
# print(newLista)


lista = [1,2,3,2]

ans = 0
for n in lista:
    if lista.count(n) == 1:  ans += n
print(ans)




    