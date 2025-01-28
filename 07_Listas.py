

lista1 = ("Mario", 33, 9, 5, True, "German", 20.0)

print(lista1)
print(lista1[3])
print(lista1[2])
print(lista1[-1])
print(lista1[9])

lista1.append("vargas")
print(lista1)

lista1.insert(2, "Nada")
print(lista1)

lista1.extend("uno",1.1, True)
print(lista1)

lista1.remove(3)
print(lista1)
lista1.pop()
print(lista1)

lista2=("tres","cuatro")
lista3=lista1+lista2
print(lista3)

print(lista2*0)
lista3=[2,1,5,4,3]
print(lista4)
print(lista4.sort())

del lista6[0]
print(lista6)