adatbazis = []
adatok = []
elf = []

with open('files/01_calories.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adat_1 = sor.strip().split()
        adatok.append(adat_1)
    # print(adatok)
    hossz = len(adatok)

    forrasfajl.seek(0)
    for i in range(1, len(adatok)):
        adat_2 = forrasfajl.readline().strip()
        if adat_2 != '' and adat_2 != '\n':
            elf.append(int(adat_2))
        else:
            adatbazis.append(elf)
            elf = []
print(f'{adatbazis=}')
osszegek = []
for lista in adatbazis:
    osszegek.append(sum(lista))
print(f'{osszegek=}')
print(f'max = {max(osszegek)}')

