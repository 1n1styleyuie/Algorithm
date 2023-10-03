alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = list(input())
time = 0

for i in word:
    for j in alphabet:
        if i in j:
            time += alphabet.index(j) + 3
print(time)