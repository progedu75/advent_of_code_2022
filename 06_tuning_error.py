with open('files/06_tuning_error.txt', 'r', encoding='utf-8') as source:
    for sor in source:
        print(sor)

for index, ch in enumerate(sor):
    if index < 3:
        continue
    elif index == 3:
        if sor[index - 3 : index + 1].count(ch) > 1:
            continue
    elif index > 3:
        if sor[index - 3 : index + 1].count(sor[index - 3]) >1 or \
           sor[index - 3 : index + 1].count(sor[index - 2]) >1 or \
           sor[index - 3 : index + 1].count(sor[index - 1]) >1 or \
           sor[index - 3 : index + 1].count(sor[index]) >1:
            continue
        else:
            print(f'Az első jelölő karakter a {index}. indexű, \'{ch}\' elem, \nígy ezen karakterek észleléséig {index + 1} elemet kellett feldolgozni')
            break
