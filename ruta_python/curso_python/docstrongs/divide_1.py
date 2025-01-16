def divide(a: int, b: int) -> float:
    # Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parametros deben ser enteros.")
    #Verificar que el segundo parametro no sea cero
    if b == 0:
        raise ValueError("El segundo parametro no puede ser cero.")
    
    return a / b

res_1 = divide(10, 5)
print(res_1)  # 2.0