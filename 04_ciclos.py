x=0

while x<10:
    print(x)
    x=x+1

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

resultado = 0
contador = 0

while contador < b:
    resultado += a
    contador += 1

print("el resultado es", resultado)