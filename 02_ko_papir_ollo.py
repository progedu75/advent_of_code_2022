pontszam = 0
victory = 0
egal = 0
losing = 0

with open('files/02_rock_paper_scisors.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adat = sor.strip().split()
        # print(adat)
        if adat[1] == 'X':
            pontszam += 1
        elif adat[1] == 'Y':
            pontszam += 2
        else:
            pontszam += 3

        if adat[0] == 'A' and adat[1] == 'X':
            pontszam += 3
        elif adat[0] == 'A' and adat[1] == 'Y':
            pontszam += 6
        elif adat[0] == 'A' and adat[1] == 'Z':
            pontszam += 0
        elif adat[0] == 'B' and adat[1] == 'X':
            pontszam += 0
        elif adat[0] == 'B' and adat[1] == 'Y':
            pontszam += 3
        elif adat[0] == 'B' and adat[1] == 'Z':
            pontszam += 6
        elif adat[0] == 'C' and adat[1] == 'X':
            pontszam += 6
        elif adat[0] == 'C' and adat[1] == 'Y':
            pontszam += 0
        elif adat[0] == 'C' and adat[1] == 'Z':
            pontszam += 3
    print(f'Összpontszám= {pontszam}')


