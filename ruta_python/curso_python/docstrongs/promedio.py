def calculate_average(numbers):
    """
    Calcular el promedio de una lista de números.

    Parametros:
    numbers (list): Una lista de números enteros o flotantes.

    Retorna:
    float: El promedio de los números en la lista.
    
    """
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))  # 3.0