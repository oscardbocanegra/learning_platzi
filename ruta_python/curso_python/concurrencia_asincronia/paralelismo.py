import multiprocessing

#Funcion que calcule el cuadrado de un numero
def square(n):
    return n ** 2

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #crear un pool de procesos
    with multiprocessing.Pool() as pool:
        #Aplicar la funcion square a cada numero en la lista
        result = pool.map(square, numbers)