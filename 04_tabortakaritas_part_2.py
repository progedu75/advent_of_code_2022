szakasz_1 = []
szakasz_2 = []
count_szakasz_1 = 0
count_szakasz_2 = 0

atfedes = False
sorszam = 0
szamlalo = 0
eleme = 0
atfedes_szama = 0


def szetvalaszto(adat):
    atmeneti = []
    list_1 = []
    list_2 = []
    adat_uj = adat.strip().split(',')

    for i in adat_uj:
        # print(i)
        if len(i) == 3:
            atmeneti.append(i[0])
            atmeneti.append(i[2])
        elif len(i) == 4 and i[1] == '-':
            atmeneti.append(i[0])
            atmeneti.append(i[2] + i[3])
        elif len(i) == 5:
            atmeneti.append(i[0] + i[1])
            atmeneti.append(i[3] + i[4])
    list_1.append(atmeneti[0])
    list_1.append(atmeneti[1])
    list_2.append(atmeneti[2])
    list_2.append(atmeneti[3])
    return list_1, list_2

def szamlista(list):
    vegso_1 = []
    vegso_2 = []
    elso = list[0]
    masodik = list[1]
    for i in elso:
        vegso_1.append(int(i))
    for y in masodik:
        vegso_2.append(int(y))
    return vegso_1, vegso_2

with open('files/04_camp_cleaining.txt', 'r', encoding='utf-8') as sourcefile:
    for sor in sourcefile:
        sorszam += 1
    sourcefile.seek(0)

    for adat in sourcefile:
        pars = szetvalaszto(adat)
        parok = sorted(pars)
        adatok = list(szamlista(parok))
        # print(adatok, end='\t')
        for x in range(adatok[0][0], adatok[0][1]+1):
            szakasz_1.append(x)
        print(szakasz_1)
        for j in range(adatok[1][0], adatok[1][1] + 1):
            szakasz_2.append(j)
        print(szakasz_2)

        for a in szakasz_1:
            if a in szakasz_2:
                count_szakasz_1 += 1
        for b in szakasz_2:
            if b in szakasz_1:
                count_szakasz_2 += 1
        if count_szakasz_1 == len(szakasz_1) or count_szakasz_2 == len(szakasz_2):
            atfedes = True
            print(atfedes)
            szamlalo += 1
        else:
            atfedes = False
            print(atfedes)
        print('*************************')
        for elem in szakasz_2:
            if elem in szakasz_1:
                eleme += 1
        if eleme >= 1:
            atfedes_szama += 1
        eleme = 0
        szakasz_1 = []
        szakasz_2 = []
        count_szakasz_1 = 0
        count_szakasz_2 = 0
    print(atfedes_szama)
