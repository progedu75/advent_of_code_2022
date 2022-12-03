with open('files/03_backpack.txt', 'r', encoding='utf-8') as source:
    lower_case_character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case_character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rows = 0
    list_1 = []
    list_2 = []
    sum_sor = 0
    sum_osszes = 0
    elemek = set()

    for row in source:
        data = row.strip()
        rows += 1
    source.seek(0)

    for i in range(1,rows+1):
        row = source.readline().strip()

        for x in range(0, int(len(row)/2)):
            list_1.append(row[x])

        for y in range(int(len(row)/2), len(row)):
            list_2.append(row[y])
        # print(list_1, list_2, sep='\t\t')

        for ch in list_1:
            if ch in list_2:
                elemek.add(ch)
        for elem in elemek:
            if elem in lower_case_character:
                sum_sor += lower_case_character.index(elem) + 1
            else:
                sum_sor += upper_case_character.index(elem) + 27
        sum_osszes += sum_sor
        print(row, sum_sor, sum_osszes, sep='\t')
        sum_sor = 0
        list_1 = []
        list_2 = []
        elemek = set()
    print(f'Az egyes elemtípusok prioritásának összege = {sum_osszes}')