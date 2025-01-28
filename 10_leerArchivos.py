from io import open
import math

lectura =""
texto = open("archivo.txt","r")
lectura = texto.readline()
lectura =texto.read()
texto.write("Hola mundo\n")
print(type(lectura))
for i in lectura:
    print(i)
texto.close()