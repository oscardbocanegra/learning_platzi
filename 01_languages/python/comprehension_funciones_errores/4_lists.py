numbers = []

for i in range(1, 11):
    numbers.append(i)
    
print(numbers)

numbers_v2 = [i for i in range(1,12)]
print(numbers_v2)

print("\n")

#Now on the following code we can see how is the syntaxis but this time with a conditional

numbers=[]

for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i*2)
        
print(numbers)

numbers_v2 = [i*2 for i in range(1,12) if i % 2 == 0]
print(numbers_v2)