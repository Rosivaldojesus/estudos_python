dados = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
]

result = []

for lista in dados:
    for item in lista:
        result.append(item)

print(result)
print("---------------------------------")

result_2 = []
for lista in dados:
    result_2 += lista
print(result_2)
print("---------------------------------")
print("---------------------------------")
print([item for lista in dados for item in lista])