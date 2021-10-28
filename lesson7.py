# Задача1

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        strr = str()
        for i in self.matrix:
            for j in i:
                strr = strr + str(j) + '\t'
            strr = strr + '\n'
        return f'{strr}'

    def __add__(self, other):

        summ = list()
        for j in range(len(self.matrix)):
            summ.append([])

            for k in range(len(self.matrix[0])):
                summ[j].append(self.matrix[j][k] + other.matrix[j][k])

        return Matrix(summ)


matrix = [[1, 2],
          [3, 4]]
other = [[4, 2],
         [4, 7]]

ss = Matrix(matrix)
kk = Matrix(other)
print(ss)
print(ss + kk)


# Задача2


class Odezda:

    def __init__(self, name, V, H):
        self._name = name
        self.V = V
        self.H = H

    # @property
    # def name(self):
    # return self._name

    # @name.setter
    # def name(self, value):
    # self._name=value

    @property
    def ras(self):
        if self._name == 'palto':
            try:
                r = (float(self.V) / 6.5 + 0.5)
            except:
                raise ValueError("Not valid number")
            return r
        elif self._name == 'kostum':
            try:
                r = (float(self.H) * 2 + 0.3)
            except:
                raise ValueError("Not valid number")
            return r

    @property
    def name(self):
        return self._name


r = Odezda('kostum', 42, 1.7)
r.ras
r.name


# Задача3

class Kletka:

    def __init__(self, yach):
        self.yach = yach

    def __str__(self):
        print(f'количество ячеек {self.yach}')

    def __add__(self, other):
        return self.yach + other.yach

    def __sub__(self, other):
        r = self.yach - other.yach
        if r > 0:
            return r
        else:
            return 'result is negative'

    def __mul__(self, other):
        return self.yach * other.yach

    def __truediv__(self, other):
        return self.yach // other.yach

    @staticmethod
    def Makeorder(a, d):

        yach = Kletka(a).yach

        st = str()
        print(yach // d)
        for k in range(0, (yach // d)):
            i = 0
            while i < d:
                st = ''.join((st, '*'))

                i += 1
            st = ''.join((st, '/n'))

        for k in range(0, yach % d):
            st = ''.join((st, '*'))

        return st


k1 = Kletka(23)
s = Kletka(5)
k2 = Kletka.Makeorder(23, 5)
print(k2)
k1 / s
k1 * s
