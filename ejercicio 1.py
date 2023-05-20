def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


while True:
    num = int(input("Ingresa un número: "))
    if es_primo(num):
        print("El número", num, "es primo.")
        break
