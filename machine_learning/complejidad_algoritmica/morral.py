

def morral(tamano_morral, pesos, valores, n):
    """Función recursiva para resolver el problema del morral (knapsack problem)
    Args:
        tamano_morral (int): Capacidad máxima del morral
        pesos (list): Lista de pesos de los objetos
        valores (list): Lista de valores de los objetos
        n (int): Número de objetos considerados
        Returns:
            int: Valor máximo que se puede obtener con la capacidad dada"""
    
    if n == 0 or tamano_morral == 0:
        return 0
    
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)
    
    else:
        return max(
            valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1),
            morral(tamano_morral, pesos, valores, n-1)
        )


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)