import os

version = "1.0.0"

print("Obfuscator by Igggosha. Version"+version)
value = int(input('Value: '))

os.mkdir('Negusus')
os.chdir('Negusus')

for i in range(value):
    with open(f'text{i}.txt', 'w') as f:
        for j in range(value*10000):
            f.write('Negus is a king of Nigeria! ')
