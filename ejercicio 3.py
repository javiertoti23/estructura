def met_burbuja(arr):
    n = len(arr)
    # Recorrer todos los elementos del arreglo
    for i in range(n):

        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):

            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [2, 9, 5, 8, 12, 4, 7, 25]
ordenado_arr = met_burbuja(arr)
print(ordenado_arr)