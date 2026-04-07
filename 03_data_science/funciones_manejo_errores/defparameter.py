# If I punt a "=number" on the parameter this means that it is a 
#parameter that the funtion are going to take if we don't give the 
#respective numbers
def find_volume(lenght=1, width=1, depth=1):
    return lenght * width * depth

result = find_volume( 10, 20, 3 )
print(result)

result2 = find_volume()
print(result2)