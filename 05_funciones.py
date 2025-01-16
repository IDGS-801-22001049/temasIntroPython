import os

def funcion1():
    num1 = int(input('Numero1: '))
    num2 = int(input('Numero2: '))
    suma = num1 + num2
    print(f'Resultado: {suma}')

def funcion2():
    num1 = int(input('Numero1: '))
    num2 = int(input('Numero2: '))
    resta = num1 - num2  
    print(f'Resultado: {resta}')

def funcion3():
    num1 = int(input('Numero1: '))
    num2 = int(input('Numero2: '))
    mult = num1 * num2
    print(f'Resultado: {mult}')

def funcion4():
    num1 = int(input('Numero1: '))
    num2 = int(input('Numero2: '))
    if num2 == 0:  
        print("Error: No se puede dividir por cero.")
    else:
        div = num1 / num2
        print(f'Resultado: {div}')

def run():
    while True:  
        os.system('cls')  
        print('1. suma')
        print('2. resta')
        print('3. mult')
        print('4. div')
        print('5. salir')
        op = int(input('Opcion: '))
        if op == 1:
            funcion1()
        elif op == 2:
            funcion2()
        elif op == 3:
            funcion3()
        elif op == 4:
            funcion4()
        elif op == 5:
            break  

        input("Presiona Enter para continuar...")  

if __name__ == "__main__": 
    run()