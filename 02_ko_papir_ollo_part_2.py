pontszam = 0

with open('files/02_rock_paper_scisors.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adat = sor.strip().split()

        if adat[0] == 'A' and adat[1] == 'X':
            pontszam += 3
        elif adat[0] == 'A' and adat[1] == 'Y':
            pontszam += 4
        elif adat[0] == 'A' and adat[1] == 'Z':
            pontszam += 8
        elif adat[0] == 'B' and adat[1] == 'X':
            pontszam += 1
        elif adat[0] == 'B' and adat[1] == 'Y':
            pontszam += 5
        elif adat[0] == 'B' and adat[1] == 'Z':
            pontszam += 9
        elif adat[0] == 'C' and adat[1] == 'X':
            pontszam += 2
        elif adat[0] == 'C' and adat[1] == 'Y':
            pontszam += 6
        elif adat[0] == 'C' and adat[1] == 'Z':
            pontszam += 7
    print(f'Összpontszám= {pontszam}')