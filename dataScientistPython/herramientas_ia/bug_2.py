def calcular_promedio(notas):
    suma = 0
    contador = 0
    
    for nota in notas:  # corregido "on" -> "in"
        suma += nota
        contador += 1
    
    promedio = suma / contador
    
    if promedio >= 60:  # corregido ":" faltante
        mensaje = "Aprobado"
    else:  # corregido ":" faltante
        mensaje = "Reprobado"
    
    return promedio, mensaje

notas = [80, 75, 90, 65, 50]
promedio, resultado = calcular_promedio(notas)

print(f"El promedio es: {promedio}")  # usando f-string
print(f"El resultado es: {resultado}")
