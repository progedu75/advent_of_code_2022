with open('files/06_tuning_error.txt', 'r', encoding='utf-8') as source:
    for sor in source:
        print(sor)

for index, ch in enumerate(sor):
    if index < 13:
        continue
    elif index == 13:
        if sor[index - 13 : index + 1].count(ch) > 1:
            continue
    elif index > 13:
        if sor[index - 13 : index + 1].count(sor[index - 13]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 12]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 11]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 10]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 9]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 8]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 7]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 6]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 5]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 4]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 3]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 2]) >1 or \
           sor[index - 13 : index + 1].count(sor[index - 1]) >1 or \
           sor[index - 13 : index + 1].count(sor[index]) >1:
            continue
        else:
            print(f'Az első jelölő karakter a {index}. indexű, \'{ch}\' elem, \nígy ezen karakterek észleléséig {index + 1} elemet kellett feldolgozni')
            break