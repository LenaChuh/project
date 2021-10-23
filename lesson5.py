from random import randint
import json
import re

# Задача1

with open("new_f1.txt", 'a') as f_obj:
    print('insert a string')
    x = str(input())
    while x != ' ':
        f_obj.write(x + '\n')
        x = str(input())
    else:
        f_obj.close()

# Задача2

try:
    with open("new_f2.txt", 'r') as f_obj:
        l2 = 0
        for line in f_obj:
            l2 += 1
            print(f'строка {l} количество слов {len(line.split())}')

except ValueError:
    print("Произошла ошибка ввода-вывода!")
finally:
    print(f'Итоговое колиичество строк {l}')
    f_obj.close()

# Задача3

try:
    with open("task.txt", 'r', encoding='utf-8') as f_obj:
        zf = 0
        l1 = 0
        for line in f_obj:
            l1 += 1
            zf += float(line.split()[1])
            if float(line.split()[1]) < 20000.0:
                print(f'Фамилия : {line.split()[0]}  оклад: {line.split()[1]}\n')

except ValueError:
    print("Произошла ошибка ввода-вывода!")
finally:
    m = round(zf / l, 1)
    print(f'Средняя зарплата {m}')
    f_obj.close()


# Задача4

def tr(mm):
    if mm == 'One':
        return 'Один'
    elif mm == 'Two':
        return 'Два'
    elif mm == 'Three':
        return 'Три'
    elif mm == 'Four':
        return 'Четыре'


with open("4task_r.txt", 'w+', encoding='utf-8') as o_obj:
    with open("4task.txt", 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            print(f'{str(tr(line.split()[0]))} — {line.split()[2]}', file=o_obj)
    f_obj.close()
o_obj.close()

# Задача5


x = 0

with open("5task_r.txt", 'w+', encoding='utf-8') as fi_obj:
    s = str()
    sum5 = sum([x for x in range(0, randint(13, 25))])
    for ss in [x for x in range(0, randint(13, 25))]:
        s = s + str(ss) + ' '

    print(sum5)
    print([x for x in range(0, randint(13, 25))])
    print(s)
    print(s, file=fi_obj)

# Задача6

pr = ['Информатика', 'Логика', 'Математика', 'Русский', 'Физкультура', 'Химия']
ch = [2, 46, 20, 10, 6, 20, 20]

with open("6task_r.txt", 'w+', encoding='utf-8') as pp_obj:
    n = ['(л)', '(пр)', '(лаб)']
    for p in pr:
        pp_obj.write(f'{p}: ')
        zn = [randint(10, 39) for _ in range(randint(1, 4))]
        for pp, nn in zip(zn, n):
            pp_obj.write(f'{pp} {nn} ')
        pp_obj.write(f'\n')
    pp_obj.close()

d = {}

with open("6task_r.txt", 'r', encoding='utf-8') as my_f:
    for line in my_f:
        d[line.split(':')[0]] = sum([int(x) for x in re.findall('\d', line)])
    my_f.close()
print(d)

# Задача7

s = 0
pr = 0
d_f = {}
d_av = {}
with open("text_7.txt", 'r', encoding='utf-8') as my_f:
    for line in my_f:
        ss = int(line.split()[3]) - int(line.split()[2])
        print(ss)
        if ss > 0:
            s += ss
            pr += 1
            d_f[line.split()[0]] = ss

        else:
            d_f[line.split()[0]] = ss * (-1)

    my_f.close()

    mn = s / pr
    print(mn)
    d_av['Средний доход'] = mn

with open("7task_r.json", "w") as write_f:
    json.dump([d_f, d_av], write_f)
