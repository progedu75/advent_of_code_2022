from pprint import pprint
ladak = [
    ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    ['D', 'C', 'Z', 'F'],
    ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    ['P', 'W', 'C'],
    ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    ['V', 'W', 'G', 'B', 'D'],
    ['N', 'J', 'S', 'Q', 'H', 'W'],
    ['R', 'C', 'Q', 'F', 'S', 'L', 'V']
]

abc = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
feladat = []
feladat_uj = []
lada = []
legfelsok = []

with open('files/05_supply_stacks.txt', 'r', encoding='utf-8') as sourcefile:
    sourcefile.seek(335)
    for sor in sourcefile:
        sor = sor.strip()
        for i in sor:
            if i not in abc:
                feladat.append(i)
        if len(feladat) == 4:
            feladat_uj.append(int(feladat[0]+feladat[1]))
            feladat_uj.append(int(feladat[2]))
            feladat_uj.append(int(feladat[3]))
        else:
            feladat_uj.append(int(feladat[0]))
            feladat_uj.append(int(feladat[1]))
            feladat_uj.append(int(feladat[2]))
        print(feladat_uj, ladak[feladat_uj[1] - 1], ladak[feladat_uj[2] - 1], sep='\t\t')
        # for x in range(1, feladat_uj[0] + 1):
        if len(ladak[feladat_uj[1]-1]) == 1:
            ladak[feladat_uj[2] - 1].append(ladak[feladat_uj[1]-1][0])
            ladak[feladat_uj[1] - 1].remove(ladak[feladat_uj[1]-1][0])
        else:
            for s in ladak[feladat_uj[1]-1][len(ladak[feladat_uj[1]-1])-feladat_uj[0]:]:
                ladak[feladat_uj[2] - 1].append(s)
                ladak[feladat_uj[1] - 1].remove(s)
        print(ladak[feladat_uj[1] - 1], end='\t')
        print(ladak[feladat_uj[2] - 1])
        print('****************************************************')
        feladat = []
        feladat_uj = []
    print('***************************')
    pprint(ladak, sort_dicts=False)

    for y in ladak:
        legfelsok.append(y[-1])
    print("".join(legfelsok))