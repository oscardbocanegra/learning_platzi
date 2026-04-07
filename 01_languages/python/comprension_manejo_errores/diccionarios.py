import random

dict = {}
for i in range(1,11):
    dict[i] = i * 2
    
print(dict)

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(500, 500000)
    
print(population)

population_v2 = {country: random.randint(500, 50000) for country in countries}
print(population_v2)