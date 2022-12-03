with open('files/03_backpack.txt', 'r', encoding='utf-8') as source:
    lower_case_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case_character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    rows = 0
    list_1 = []
    list_2 = []
    list_3 = []
    elemek = set()
    sum_team = 0
    sum_osszes = 0

    for row in source:
        data = row.strip()
        rows += 1
    source.seek(0)
    # print(rows)

    for i in range(1, int(rows / 3) + 1):

        list_1 = source.readline().strip()
        list_2 = source.readline().strip()
        list_3 = source.readline().strip()

        for ch in list_1:
            if ch in list_2 and ch in list_3:
                elemek.add(ch)

        for elem in elemek:
            if elem in lower_case_character:
                sum_team += lower_case_character.index(elem) + 1
            else:
                sum_team += upper_case_character.index(elem) + 27
        sum_osszes += sum_team
        print(list_1, list_2, list_3, elem, sum_team, sum_osszes, sep='\t')
        sum_team = 0
        elemek = set()
    print(f'Az egyes elemtípusok prioritásának összege = {sum_osszes}')



        # print('')
        # print(row)