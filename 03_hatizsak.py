with open('files/03_backpack.txt', 'r', encoding='utf-8') as source:
    lower_case_character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case_character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    sum = 0
    for row in source:
        data = row.strip()
        print(data, end='\t')
        for ch in data:
            if data.count(ch) == 2:
                if ch in lower_case_character:
                    print(ch, end='\t')
                    sum += lower_case_character.index(ch) + 1
                else:
                    print(ch, end='\t')
                    sum += upper_case_character.index(ch) + 27
        print(sum)
    # print(f'Az egyes elemtípusok prioritásának összege = {sum}')


