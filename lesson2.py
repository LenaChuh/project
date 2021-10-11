# Задача1

my_list=[1, 2.3, False, [3,45,12,4.5],{'d':567,'g':4453,'s':4,'t':2},(3,4,5,6)]
for el in my_list:
    print (type(el))

from random import seed
from random import randint

# Задача2
list1 = []
x = 0

while x < randint(5, 14):
    print('Please, enter element of list')
    list1.append(input())
    x += 1
print(list1)

for inx in range(0, len(list1), 2):
    print(inx, inx + 1)

for inx in range(0, len(list1) - 1, 2):
    list1[inx], list1[inx + 1] = list1[inx + 1], list1[inx]

list1

# Задача3

dict2={'1':'зима',
      '2':'зима',
     '3':'весна',
     '4':'весна',
     '5':'весна',
     '6':'лето',
     '7':'лето',
     '8':'лето',
      '9':'осень',
      '10':'осень',
      '11':'осень',
      '12':'зима'}

print ('Enter number of month from 1 to 12')
inx=str(input())
while inx not in dict2.keys():
    print ('please, enter correct number')
    inx=str(input())
else:
    print (dict2[inx])


list2=[None,'зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима','зима']


print ('Enter number of month from 1 to 12')
inx=int(input())
while inx not in range(1,len(list2)-1):
    print ('please, enter correct number')
    inx=int(input())
else:
    print (list2[inx])

# Задача4

print ('Enter words separated by spaces')
string=str(input())
st=string.split()

for i,v in enumerate(st):
    print (i+1,v[0:10])

# Задача5

r=[7,5,3,3,2]
print ('Enter your rate!')
r_new=int(input())

if r_new>max(r):
    r.insert(0,r_new)
elif r_new<min(r):
    r.insert(-1,r_new)
else:
    r.insert(len(r)-r[::-1].index(r_new),r_new)

print (r)

# Задача6


i = 0
list6 = []

while i < 2:
    print('Please, enter info about new product')
    name, price, quantity, unit = str(input()), int(input()), int(input()), str(input())
    list6.append((i + 1, {'наименование': name, 'цена': price, 'количество': quantity, 'ед.': unit}))
    i += 1

analytics = {}

analytics['наименование'] = [i[1]["наименование"] for i in list6]
analytics['цена'] = [i[1]["цена"] for i in list6]
analytics['количество'] = [i[1]["количество"] for i in list6]
analytics['ед.'] = [i[1]["ед."] for i in list6]

analytics