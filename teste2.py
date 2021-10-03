tail = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in range(5):

    j = -1

    for w in range(len(tail) - 1):
        tail[j] = tail[j - 1]
        j -= 1

print(tail)