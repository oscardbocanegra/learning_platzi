x = 5 #varible global

def modify_global():
    global x
    x += 3
    print(f'Valor modificado: {x}')

modify_global()  # Valor modificado: 8
print(x)  # 8