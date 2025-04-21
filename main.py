from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import sumar_avanzada

def mostrar_menu():
    print("\n" + "="*50)
    print(" " * 18 + "CALCULADORA PYTHON")
    print("="*50 + "\n")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada (múltiples números)")
    print("6. Salir\n")
    print("-"*50)

def obtener_entero(mensaje):
    while True:
        try:
            return int(input("\n" + mensaje))
        except ValueError:
            print("\nError: Debe ingresar un número entero. Intente nuevamente.")

def obtener_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("\nError: Debe ingresar un número válido. Intente nuevamente.")

def main():
    while True:
        mostrar_menu()
        opcion = obtener_entero("Seleccione una opción (1-6): ")
        
        if opcion == 1:
            print("\n" + "="*30)
            print("OPERACIÓN DE SUMA".center(30))
            print("="*30)
            a = obtener_float("\n• Primer número:  ")
            b = obtener_float("• Segundo número: ")
            print("\n" + ">"*5 + f" Resultado: {sumar(a, b)} " + "<"*5 + "\n")
        
        elif opcion == 2:
            print("\n" + "="*30)
            print("OPERACIÓN DE RESTA".center(30))
            print("="*30)
            a = obtener_float("\n• Primer número:  ")
            b = obtener_float("• Segundo número: ")
            print("\n" + ">"*5 + f" Resultado: {restar(a, b)} " + "<"*5 + "\n")
        
        elif opcion == 3:
            print("\n" + "="*30)
            print("OPERACIÓN DE MULTIPLICACIÓN".center(30))
            print("="*30)
            a = obtener_float("\n• Primer número:  ")
            b = obtener_float("• Segundo número: ")
            print("\n" + ">"*5 + f" Resultado: {multiplicar(a, b)} " + "<"*5 + "\n")
        
        elif opcion == 4:
            print("\n" + "="*30)
            print("OPERACIÓN DE DIVISIÓN".center(30))
            print("="*30)
            a = obtener_float("\n• Primer número:  ")
            b = obtener_float("• Segundo número: ")
            try:
                print("\n" + ">"*5 + f" Resultado: {dividir(a, b)} " + "<"*5 + "\n")
            except ValueError as e:
                print(f"\nError: {e}\n")
        
        elif opcion == 5:
            print("\n" + "="*30)
            print("SUMA AVANZADA".center(30))
            print("="*30)
            while True:
                try:
                    entrada = input("\nIngrese números separados por espacio: ")
                    numeros = list(map(float, entrada.split()))
                    if len(numeros) < 2:
                        print("\n¡Debe ingresar al menos 2 números!\n")
                        continue
                    print("\n" + ">"*5 + f" Resultado: {sumar_avanzada(*numeros)} " + "<"*5 + "\n")
                    break
                except ValueError:
                    print("\nError: Solo ingrese números válidos separados por espacios\n")
        
        elif opcion == 6:
            print("\n" + "="*30)
            print("¡HASTA PRONTO!".center(30))
            print("="*30 + "\n")
            break
        
        else:
            print("\nOpción inválida. Debe ser un número entre 1 y 6\n")

if __name__ == "__main__":
    main()