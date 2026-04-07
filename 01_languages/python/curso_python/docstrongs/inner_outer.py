x = 'global' # variable global

# Función externa
def outer_function():
    x = 'enclosing' # variable local

    # Función interna
    def inner_function():
        x = 'local' # variable local
        print(x)

    inner_function()
    print(x)

outer_function()  # local, enclosing
print(x)  # global