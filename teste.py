nova_lista = [1, 2]
j = -1
print(nova_lista)

for i in range(len(nova_lista) - 1):
    nova_lista[j] = nova_lista[j - 1]
    j -= 1

print(nova_lista)
