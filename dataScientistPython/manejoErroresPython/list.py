# List comprehension
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)