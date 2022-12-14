list_1 = ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N']
list_2 = ['L', 'P', 'T', 'V', 'H', 'C', 'G']
list_3 = ['D', 'C', 'Z', 'F']
list_4 = ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C']
list_5 = ['P', 'W', 'C']
list_6 = ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z']
list_7 = ['V', 'W', 'G', 'B', 'D']
list_8 = ['N', 'J', 'S', 'Q', 'H', 'W']
list_9 = ['R', 'C', 'Q', 'F', 'S', 'L', 'V']
abc = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
feladat = []
feladat_uj = []

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
        # print(feladat_uj)
        for x in range(1,3):
            if feladat_uj[x] == 1:
                feladat_uj[x] = 'list_1'
            elif feladat_uj[x] == 2:
                feladat_uj[x] = 'list_2'
            elif feladat_uj[x] == 3:
                feladat_uj[x] = 'list_3'
            elif feladat_uj[x] == 4:
                feladat_uj[x] = 'list_4'
            elif feladat_uj[x] == 5:
                feladat_uj[x] = 'list_5'
            elif feladat_uj[x] == 6:
                feladat_uj[x] = 'list_6'
            elif feladat_uj[x] == 7:
                feladat_uj[x] = 'list_7'
            elif feladat_uj[x] == 8:
                feladat_uj[x] = 'list_8'
            else:
                feladat_uj[x] = 'list_9'
        print(feladat_uj)
        feladat = []
        feladat_uj = []

