from io import open

class Cinepolis:

    def __init__(self):
        self.nombre = ""
        self.boletos = 0
        self.tarjeta_cineco = False

    def calcular_total(self):
        precio_unitario = 12.00
        total_bruto = self.boletos * precio_unitario

        if self.boletos > 5:
            descuento = 0.15
        elif 3 <= self.boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0.0

        total_descuento = total_bruto * descuento
        total_a_pagar = total_bruto - total_descuento

        if self.tarjeta_cineco:
            total_a_pagar *= 0.90

        return total_a_pagar

    def correccion_datos(self):
        while True:
            print("¿Qué desea corregir?")
            print("1. Cantidad de personas")
            print("2. Cantidad de boletos")
            opcion = input("Seleccione una opción (1/2): ")

            if opcion == "1":
                return "personas"
            elif opcion == "2":
                return "boletos"
            else:
                print("Opción no válida. Intente nuevamente.")

    def solicitar_datos(self):
        while True:
            continuar = input("¿Desea continuar o terminar? (continuar/terminar): ")
            if continuar not in ["continuar", "terminar"]:
                print("Debe introducir 'continuar' o 'terminar'.")
                continue

            if continuar == "terminar":
                self.ticket()
                break

            while True:
                self.nombre = input("Ingrese el nombre de la persona que realizará la compra: ")
                if self.nombre:
                    break
                print("El nombre no puede estar vacío.")
                
            while True:
                personas_compran = int(input("¿Cuántas personas van a comprar boletos?: "))
                if personas_compran < 1:
                    print("El número de personas debe ser al menos 1.")
                    continue
                break

            while True:
                boletos = int(input("Ingrese la cantidad total de boletos a comprar: "))
                if boletos < 1 or boletos > personas_compran * 7:
                    print(f"Cada persona puede comprar hasta 7 boletos. En total pueden comprar hasta {personas_compran * 7}.")
                    if self.correccion_datos() == "personas":
                        continue
                    else:
                        continue
                break

            self.boletos = boletos  

            while True:
                tarjeta_cineco_input = input("¿Usará la tarjeta CINECO para pagar? (si/no): ")
                if tarjeta_cineco_input in ["si", "no"]:
                    self.tarjeta_cineco = tarjeta_cineco_input == "si"
                    break
                print("Debe responder 'si' o 'no'.")

            self.resumen_compra()

            total = self.calcular_total()

            texto = open("total.txt", "a")
            texto.write(f"Comprador: {self.nombre}, Total: ${total:.2f}\n")
            texto.close()

    def resumen_compra(self):
        total = self.calcular_total()
        print("\n--- Resumen de la compra ---")
        print(f"Nombre del comprador: {self.nombre}")
        print(f"Cantidad de boletos comprados: {self.boletos}")
        print(f"Total a pagar: ${total:.2f}")

    def ticket(self):
        print("La compra ha sido terminada.")
        self.mostrar_corte()

    def mostrar_corte(self):
        try:
            texto = open("total.txt", "r")
            lectura = texto.read()
            texto.close()

            print("\n--- Corte de ventas ---")
            print("Detalle de las ventas realizadas:")
            print(lectura if lectura else "No hay ventas registradas.")

            total_ventas = sum(
                float(line.split('$')[1].strip()) 
                for line in lectura.splitlines() if '$' in line
            )
            print(f"Total de ventas: ${total_ventas:.2f}")

            
            texto = open("total.txt", "w")
            texto.write('')
            texto.close()

        except FileNotFoundError:
            print("No hay ventas registradas aún.")


def run():
    print("Bienvenido al sistema de compra de boletos de Cinepolis.\n")
    compra = Cinepolis()
    compra.solicitar_datos()

if __name__ == "__main__":
    run()