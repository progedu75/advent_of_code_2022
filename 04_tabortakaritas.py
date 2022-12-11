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
with open('files/04_camp_cleaining.txt', 'r', encoding='utf-8') as sourcefile:
    for sor in sourcefile:
        sorszam += 1
    sourcefile.seek(0)

    for adat in sourcefile:
        parok = szetvalaszto(adat)
        print(parok, end='\t')
        if int(parok[0][0]) <= int(parok[1][0]):
            # print('true')
            for i in parok[1]:
                if int(i) in range(int(parok[0][0]),int(parok[0][1]) + 1):
                    atfedes = True
                else:
                    atfedes = False
        else:
            for i in parok[0]:
                if int(i) in range(int(parok[1][0]), int(parok[1][1]) + 1):
                    atfedes = True
                else:
                    atfedes = False
        print(atfedes)



'''
                if szakasz_1[0] <= szakasz_2[0]:
                    for i in szakasz_2:
                        if i in range(szakasz_1[0], szakasz_1[1] + 1):
                            atfedes = True
                        else:
                            atfedes = False
                else:
                    for i in szakasz_1:
                        if i in range(szakasz_2[0], szakasz_2[1] + 1):
                            atfedes = True
                        else:
                            atfedes = False
                print('\t', atfedes)
                if atfedes:
                    szamlalo += 1
                szakasz_1 = []
                szakasz_2 = []
                list_1 = []
                list_2 = []
                atfedes = False
                '''

