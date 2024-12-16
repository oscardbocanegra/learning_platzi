# Operacioes de conjuntos

# Union de conjuntos
set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

# Aca podemos ver las 2 maneras de unir un conjuto
print( set_a | set_b )
set_c = set_a.union(set_b)
print(set_c)

# Interseccion
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# Diferencia
print(set_a - set_b)
set_c = set_a.difference(set_b)
print(set_c)