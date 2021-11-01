# Задача1
import datetime

now = datetime.datetime.now()


class Date:

    @classmethod
    def num(cls, dat):
        d, m, y = int(str(dat).split('-')[0]), int(str(dat).split('-')[1]), int(str(dat).split('-')[2])

        return d, m, y

    @staticmethod
    def validation(obj):

        day, month, year = Date.num(obj)

        if (day > 0 and day < 32) * (month > 0 and month < 32) * (year > 0 and year <= now.year) == 1:
            print("Valid date")
        else:
            print("Not valid date")


mc = Date()
mc.num('30-23-1946')
mc.validation('30-23-2056')


# Задача2


class MyError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


x = input("Enter first number:-")
y = input("Enter second number:-")


def divide(x, y):
    try:
        result = float(x) / float(y)
    except ZeroDivisionError:
        print(MyError("division by zero!"))

    except ValueError:
        print('Please, enter numbers')


    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(x, y)


# Задача3
class Except:
    def __init__(self, text):
        self.text = text

    def check(self):
        h = self.text
        if h.isdigit() == True:
            return int(self.text)
        elif h == 'stop':
            return 'stop'
        else:
            print((f'enter numbers'))
            return 0


def my_func():
    spisok = list()
    t = 1
    print('введите число')

    while t > 0:
        x = Except(input()).check()
        if x == 'stop':
            print(spisok)
            break
        elif x == 0:
            pass
        else:
            spisok.append(x)


my_func()

# Задача4

from abc import ABC, abstractmethod


class Orgtehnika(ABC):
    total_filled_cells = 0

    def __init__(self, qty, location, responsible_person):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person

    @property
    @abstractmethod
    def filled_cells(self):
        pass

    def __add__(self, other):
        Orgtehnika.total_filled_cells += self.filled_cells + other.filled_cells

        return Orgtehnika.total_filled_cells

    def __str__(self):
        r = Orgtehnika.total_filled_cells
        Orgtehnika.total_filled_cells = 0
        return f'{r}'


class Printer(Orgtehnika):

    def __init__(self, qty, location, responsible_person, kartridges):
        super().__init__(qty, location, responsible_person)
        self.kart = kartridges

    @property
    def filled_cells(self):
        return (self.qty[0]) * 2


class Skaner(Orgtehnika):

    @property
    def filled_cells(self):
        return (self.qty[0]) * 4


class Xerox(Orgtehnika):

    def __init__(self, qty, location, responsible_person, speed):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person
        self.speed = speed

    @property
    def filled_cells(self):
        return (self.qty[0]) * 1


# Задача5


from abc import ABC, abstractmethod


class Orgtehnika(ABC):
    total_filled_cells = 0
    departments = {'buh': {'x': 0, 'p': 0, 's': 0, 'log': {'x': 0, 'p': 0, 's': 0}}}

    def __init__(self, qty, location, responsible_person):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person

    @classmethod
    def priemka(cls, name, q, dep):
        print('введите наименование товара (x,p,s), количество, отдел')
        cls.departments[dep][name] = cls.departments[dep][name] + q
        return cls.departments[dep][name]

    @property
    @abstractmethod
    def filled_cells(self):
        pass

    def __add__(self, other):
        Orgtehnika.total_filled_cells += self.filled_cells + other.filled_cells

        return Orgtehnika.total_filled_cells

    def __str__(self):
        r = Orgtehnika.total_filled_cells
        Orgtehnika.total_filled_cells = 0
        return f'{r}'


class Printer(Orgtehnika):

    def __init__(self, qty, location, responsible_person, kartridges):
        super().__init__(qty, location, responsible_person)
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person
        self.kart = kartridges

    @property
    def filled_cells(self):
        return (self.qty[0]) * 2


class Skaner(Orgtehnika):

    @property
    def filled_cells(self):
        return (self.qty[0]) * 4


class Xerox(Orgtehnika):

    def __init__(self, qty, location, responsible_person, speed):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person
        self.speed = speed

    @property
    def filled_cells(self):
        return (self.qty[0]) * 1


X=Xerox(20,3,'ggg',4)
P=Printer(23,4,'ggg',5)
P.qty
print (X+P)
Orgtehnika.departments
X.priemka('x',2,'buh')
Orgtehnika.departments


# Задача6

from abc import ABC, abstractmethod


class Orgtehnika(ABC):
    total_filled_cells = 0
    departments = {'buh': {'x': 0, 'p': 0, 's': 0, 'log': {'x': 0, 'p': 0, 's': 0}}}

    def __init__(self, qty, location, responsible_person):

        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person

    @classmethod
    def priemka(cls, name, dep, x):
        y = ExceptPrihod(x).check()
        while y == 0:
            print('введите число, а не текст')
            x = input()
            y = ExceptPrihod(x).check()
        else:
            x = int(x)
            cls.departments[dep][name] = cls.departments[dep][name] + x
            return cls.departments[dep][name]

    @property
    @abstractmethod
    def filled_cells(self):
        pass

    def __add__(self, other):
        Orgtehnika.total_filled_cells += self.filled_cells + other.filled_cells

        return Orgtehnika.total_filled_cells

    def __str__(self):
        r = Orgtehnika.total_filled_cells
        Orgtehnika.total_filled_cells = 0
        return f'{r}'


class Printer(Orgtehnika):

    def __init__(self, qty, location, responsible_person, kartridges):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person
        self.kart = kartridges

    @property
    def filled_cells(self):
        return (self.qty[0]) * 2


class Skaner(Orgtehnika):

    @property
    def filled_cells(self):
        return (self.qty[0]) * 4


class Xerox(Orgtehnika):

    def __init__(self, qty, location, responsible_person, speed):
        self.qty = qty,
        self.location = location,
        self.responsible_person = responsible_person
        self.speed = speed

    @property
    def filled_cells(self):
        return (self.qty[0]) * 1


class ExceptPrihod:

    def __init__(self, text):
        self.text = text

    def check(self):
        h = self.text
        if str(h).isdigit() == True:
            return 1
        elif h == 'stop':
            return 'stop'
        else:

            return 0


Orgtehnika.departments
Orgtehnika.priemka('p','buh','rrr')
Orgtehnika.departments['buh']['p']
Orgtehnika.departments


# Задача7

class ComplexNumber:

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def __str__(self):

        r1 = self.a
        i1 = self.b
        if (r1 > 0 and i1 > 0):
            r1 = str(r1)
            r1 += '+'
            if (abs(i1) != 1):
                i1 = str(i1)
                i1 += 'i'
            else:
                i1 = 'i'
        elif (r1 == 0 and i1 == 0):
            return '0'
        elif (r1 <= 0 and i1 < 0):
            if (r1 == 0):
                r1 = str(r1)
                r1 = ''
            if (i1 == -1):
                i1 = str(i1)
                i1 = '-i'
            else:
                i1 = str(i1)
                i1 += 'i'
        elif (r1 <= 0 and i1 > 0):
            if (r1 == 0):
                r1 = str(r1)
                r1 = ''
            else:
                r1 = str(r1)
                r1 += '+'
            if (i1 == 1):
                i1 = str(i1)
                i1 = 'i'
            else:
                i1 = str(i1)
                i1 += 'i'
        elif (r1 > 0 and i1 < 0):
            i1 = self.im
            i1 = str(i1)
            if (i1 != '-1'):
                i1 += 'i'
            else:
                i1 = '-i'
        if (i1 == 0):
            i1 = ''

        self.__repr__()
        ans = str(r1) + str(i1)
        return ans

    def __add__(self, other):

        ans = ComplexNumber(self.a + other.a, self.b + other.b)
        return ans

    def __mul__(self, other):

        ex1 = (self.a * other.a) - (self.b * other.b)
        ex2 = (self.a * other.b) + (self.b * other.a)
        c = ComplexNumber(ex1, ex2)
        return c

y = ComplexNumber(2, 8)
x = ComplexNumber(2, 7)
print(x + y)
print(x * y)


