#Задача1

def delenie():
    p1 = input("enter first number: ")
    p2 = input("enter second number: ")

    try:
        r = round(float(p1) / float(p2), 2)

    except ZeroDivisionError as err:
        return err
    except ValueError as err2:
        return err2

    print(f'result{r}')

#Задача2

def func_2(fam_nam,name,year,town,email,tel):


    print (f'{fam_nam} {name} {year} года рожд., проживающий/ая в городе {town},телефон-{tel}  почта{email}')

func_2(fam_nam='ееее',name='оооо',year=1996,town='ыыыы',email='ллллл',tel=56565)

#Задача3

def my_func(a,b,c):
    al=[float(a),float(b),float(c)]
    return sum([x for x in al if x != min(al)])

#Задача4

def my_func():
    while True:
        try:
            x = float(input('ведите число  '))
            y = int(input('введите отрицательную степень  '))
            while y > 0:
                print('введите отрицательную степень  ')
                y = int(input())
            else:
                if y == 0:
                    return 1
                else:
                    return x ** y
        except ValueError:
            print('введите значения заново')

#Задача5


def s(*args):
    """Q-символ для выхода из программы"""

    summ = 0
    s1 = ' '
    s = str()
    print('введите числа через пробел, Q-символ для выхода из программы')

    while True:
        try:
            s1 = str(input())
            summ = summ + sum([float(x) for x in s1.split('Q')[0].split()])
            print(summ)
            if 'Q' in s1:
                break

        except ValueError as err:
            print(err)



#Задача6

def int_func(l):
    return l.capitalize()

def inc_func2(m):
    st=str()
    for word in m.split():
        st=st+' '+int_func(word)
    print(f'{st}')



