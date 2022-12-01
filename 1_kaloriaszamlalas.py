adatok = []
elf = []
with open('files/01_calories.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adat_1 = sor.strip().split()
    print(adat_1)
    '''
    adat = forrasfajl.readline().strip()
    print(adat)
    if adat != '' and adat != '\n':
        elf.append(adat)
    else:
        adatok.append(elf)
        elf = []
print(elf)
'''


