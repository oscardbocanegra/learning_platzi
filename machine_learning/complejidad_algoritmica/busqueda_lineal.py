def busqueda_lineal(lista, objetivo):
    """Realiza una búsqueda lineal en la lista para encontrar el objetivo.

    Args:
        lista (list): La lista en la que se realizará la búsqueda.
        objetivo: El valor que se está buscando en la lista.

    Returns:
        bool: True si el objetivo se encuentra en la lista, False en caso contrario.
    """
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9]
    objetivo = 7

    encontrado = busqueda_lineal(lista, objetivo)
    print(f"¿El objetivo {objetivo} se encuentra en la lista? {encontrado}")