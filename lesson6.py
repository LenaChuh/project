# Задача1

import time
import turtle


class TrafficLight:

    # методы
    def __init__(self):
        self.__color = "Red"

    def running(self):
        i=0
        while i<4:
            for _color, t in list(zip(['yellow', 'green', 'yellow', 'red'], [2, 7, 2, 7])):
                print(_color)
                player_one = turtle.Turtle()
                player_one.color(_color)
                player_one.shape("circle")
                time.sleep(t)
                i+=1


a = TrafficLight()
a.running()

# Задача2


class Road:

    # атрибуты
    def __init__(self, _lenth, _width):
        self._lenth = input('_lenth')
        self._width = input('_width')

    def raschet(_lenth, _width):
        m = (_lenth * _width * 25 * 5) / 10000
        return (f'{m} тонн')


a = Road

a.raschet(20, 5000)

# Задача3

class Worker:
    counter = 0

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {x: y for x, y in zip(['wage', 'bonus'], [17, 18])}
        Worker.counter += 1


class Position(Worker):

    def get_full_name(self):
        print(a.__dict__['name'], a.__dict__['surname'])

    def get_total_income(self):
        print(a.__dict__['_income']['wage'] + a.__dict__['_income']['bonus'])


a=Worker('Вася', 'Пупкин', 'продавец')
dictt = a.__dict__

b=Position('Вася', 'Пупкин', 'продавец')
b.get_total_income()
b.get_full_name()

# Задача4


class Car:
    counter = 0

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        Car.counter += 1

    def go(self, speed):
        print(f'go car {self.name} with speed {self.speed}')

    def stop(self):
        print(f'stop car {self.name}')

    def turn(self, direction):
        print(f'turn car {self.name} to {direction}')

    def show_speed(self):
        print(f'our speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('speed exceeded')
        else:
            print(f'our speed is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('speed exceeded')
        else:
            print(f'our speed is {self.speed}')


class PoliceCar(Car):
    pass


a=Car('KIA','red','77',False)
a.go(77)
a.stop()
a.show_speed()
a.turn('right')

b=TownCar('Opel','green','60',False)
b.show_speed()
c=TownCar('Opel','green','63',False)
c.show_speed()
d=WorkCar('Opel','yellow','37',False)
d.show_speed()
d.name
d.color
d.is_police


# Задача5


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print (f"Отрисовка ручкой")
class Handle(Stationery):
    def draw(self):
        print (f"Отрисовка маркером")
class Pencil(Stationery):
    def draw(self):
        print (f"Отрисовка карандашом")

a = Stationery
a.draw('нана')
b=Pen
b.draw('tata')
c=Pencil('опт')
c.draw()