import math

class Distancia:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0


    def datos(self):
        self.x2 = int(input("Inserta el segundo valor de x: "))
        self.x1 = int(input("Inserta el primer valor de x: "))
        self.y2 = int(input("Inserta el segundo valor de y: "))
        self.y1 = int(input("Inserta el primer valor de y: "))
        

    def operacion(self):
        self.res = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        print(f'El resultado es: {self.res}')

def main():
    obj = Distancia()  
    obj.datos()        
    obj.operacion()    

if __name__ == '__main__':
    main()