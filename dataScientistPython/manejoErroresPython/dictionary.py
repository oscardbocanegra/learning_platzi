# dictionary comprehension

dic = {}
for i in range(1,6):
    dic[i] = i * 2

print(dic)

dic_v2 = {i: i * 2 for i in range(1,6)}
print(dic_v2)