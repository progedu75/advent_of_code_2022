szakasz_1 = []
szakasz_2 = []
atfedes = False
sorszam = 0
szamlalo = 0

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
with open('files/04_camp_cleaining.txt', 'r', encoding='utf-8') as sourcefile, \
        open('files/kimenet.txt', 'w', encoding='utf-8') as celfajl:
    for sor in sourcefile:
        sorszam += 1
    sourcefile.seek(0)

    for adat in sourcefile:
        parok = szetvalaszto(adat)
        print(sorted(parok), end='\t')
        if int(parok[0][0]) < int(parok[1][0]):
            # print('true')
            # for i in parok[1]:
            if int(parok[1][0]) in range(int(parok[0][0]),int(parok[0][1]) + 1) and int(parok[1][1]) in range(int(parok[0][0]),int(parok[0][1]) + 1):
                atfedes = True
                # szamlalo += 1
            else:
                atfedes = False
        elif int(parok[0][0]) == int(parok[1][0]) and int(parok[0][0]) == int(parok[0][1]):
            if int(parok[0][0]) in range(int(parok[1][0]), int(parok[1][1]) + 1):
                atfedes = True
        elif int(parok[0][0]) == int(parok[1][0]) and int(parok[0][0]) != int(parok[0][1]):
            if int(parok[0][1]) in range(int(parok[1][0]), int(parok[1][1]) + 1):
                atfedes = True
        else:
            # for i in parok[0]:
                if int(parok[0][0]) in range(int(parok[1][0]), int(parok[1][1]) + 1) and int(parok[0][1]) in range(int(parok[1][0]), int(parok[1][1]) + 1):
                    atfedes = True
                    # szamlalo += 1
                else:
                    atfedes = False
        # print(atfedes)
        print(sorted(parok), atfedes, sep='\t', file=celfajl)
        if atfedes == True:
            szamlalo += 1
    print(f'{szamlalo=}')




'''
                
                if atfedes:
                    szamlalo += 1
                szakasz_1 = []
                szakasz_2 = []
                list_1 = []
                list_2 = []
                atfedes = False
                '''

