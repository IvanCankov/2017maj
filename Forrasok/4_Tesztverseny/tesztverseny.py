#1. feladat
versenyzo = {}
o = 0
with open('valaszok.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split()
        if o == 0:
            valasz = ''.join(line)
            o += 1
        else:
            versenyzo[line[0]] = line[1]
print(f'2. feladat\tA vetélkedőn {len(versenyzo)} versenyző indult.')
azon = 'AB123' #input('3. feladat: A versenyző azonosítója = ')
print(f'{versenyzo[azon]}\t(a versenyző válasza)')
print(f'4. feladat:\n{valasz}\t(a helyes megoldás)')
for index, svara in enumerate(versenyzo[azon]):
    if valasz[index] == svara:
        print('+', end = '')
    else:
        print(' ', end = '')
print('')
sorsz = int(input('5. feladat:\tA feladat sorszáma = ')) - 1
helyes = 0
for svara in versenyzo:
    if versenyzo[svara][sorsz] == valasz[sorsz]:
        helyes += 1
print(f'A feladatra {helyes} fő, a versenyzők {helyes / len(versenyzo) * 100:.2f}%-a adott helyes választ.')