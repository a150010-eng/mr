def doble(numero):
    return numero * 2

def es_par(numero):
    return numero % 2 == 0


if __name__ == "__main__":
    n = int(input("Ingresa un número: "))

    print("El doble es:", doble(n))
    print("¿Es par?", es_par(n))
