def contar_vocales_consonantes(frase):
    vocales = 'aeiouAEIOU'
    contador_vocales = 0
    contador_consonantes = 0

    for caracter in frase:
        if caracter.isalpha():
            if caracter in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    if contador_vocales > contador_consonantes:
        return "La frase cuenta con más vocales que consonantes."
    elif contador_consonantes > contador_vocales:
        return "La frase cuenta con más consonantes que vocales."
    else:
        return "La frase cuenta con la misma cantidad de vocales y consonantes."

frase = input("Ingresa una frase: ")

resultado = contar_vocales_consonantes(frase)

print(resultado)