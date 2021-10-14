from random import seed
from random import randint


# Задача1
my_list=[1, 2.3, False, [3,45,12,4.5],{'d':567,'g':4453,'s':4,'t':2},(3,4,5,6)]
for el in my_list:
    print(type(el))
_______________________________________________________________________________
# Задача2
list1=[]
x=0
while x<randint(5, 14):
    print ('Please, enter element of list')
    list1.append(input())
    x+=1
    print(list1)
for inx in range(0,len(list1),2):
    print (inx,inx+1)
    for inx in range(0,len(list1)-1,2)
    list1[inx],list1[inx+1]=list1[inx+1],list1[inx]
print(f'list1')
______________________________________________________________________________
# Задача3
dict2={'1':'зима',\n",
    "      '2':'зима',\n",
    "     '3':'весна',\n",
    "     '4':'весна',\n",
    "     '5':'весна',\n",
    "     '6':'лето',\n",
    "     '7':'лето',\n",
    "     '8':'лето',\n",
    "      '9':'осень',\n",
    "      '10':'осень',\n",
    "      '11':'осень',\n",
    "      '12':'зима'}\n",

print ('Enter number of month from 1 to 12')\n",
    "inx=str(input())\n",
    "while inx not in dict2.keys():\n",
    "    print ('please, enter correct number')\n",
    "    inx=str(input())\n",
    "else:\n",
    "    print (dict2[inx])\n"
