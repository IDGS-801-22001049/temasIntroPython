texto1 = "Hola"
texto2 = "mundo"
textofinal1 = texto1 + " " + texto2
print(textofinal1)

# Se imprime un saludo utilizando el formato de cadena, insertando texto1 y texto2
print("El saludo es: %s %s" % (texto1, texto2))

# Se crea una cadena de saludo utilizando el método format, insertando texto1 y texto2
saludofinal2 = "saludo: {x} {y}".format(x=texto1, y=texto2)

# Se imprime el saludo formateado
print(saludofinal2)

# Se asigna una cadena a la variable texto
texto = "Desarrollo web profesional UTL"

# Se imprime la cadena original
print(texto)

# Se imprime la cadena en mayúsculas
print(texto.upper())

# Se imprime la cadena en minúsculas
print(texto.lower())

# Se imprime la cadena con cada palabra capitalizada
print(texto.title())

# Se intenta encontrar la posición de un carácter o subcadena en texto, pero no se especifica qué buscar
# Esto generará un error, ya que find() requiere un argumento
print(texto.find())  # Esto debería ser texto.find("e") para buscar la letra 'e'

# Se cuenta cuántas veces aparece la letra "e" en la cadena texto
print(texto.count("e"))

# Se reemplaza "UTL" por "UTEC" en la cadena texto y se imprime el resultado
print(texto.replace("UTL", "UTEC"))

# Se separa la cadena texto en una lista de palabras utilizando el espacio como delimitador
cadenasSeparadas = texto.split(" ")

# Se imprime la lista de palabras separadas
print(cadenasSeparadas)