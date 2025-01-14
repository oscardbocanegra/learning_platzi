x = 100 # variable global

def local_function():
    x = 10 # variable local
    print(f'El valor de la variable es {x}')

def show_globla():
    print(f'El valor de la variable global es {x}')

local_function()  # El valor de la variable es 10 
show_globla()  # El valor de la variable global es 100