def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

# NUEVAS FUNCIONES MUY SIMPLES
def potencia(a, b):
    return a ** b

def modulo(a, b):
    return a % b


if __name__ == "__main__":
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")

    opcion = input("Elige una opción (1-6): ")

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    elif opcion == "5":
        print("Resultado:", potencia(a, b))
    elif opcion == "6":
        print("Resultado:", modulo(a, b))
    else:
        print("Opción inválida")

