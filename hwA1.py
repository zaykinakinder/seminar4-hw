

import random

size = int(input('Введите максимальную степень:'))

koef={}
for i in range (size+1):
    koef[i]=random.randint(0,5)
print (koef)

equation = ''

for i in range (size, -1,-1):
    print(koef[i])
    if koef[i]!=0:
        equation +=f'{koef[i]}*x**{i} + '
    elif i ==1:
        equation +=f'{koef[i]}*x + '
    elif i == 0:
        equation += f'{koef[i]} + '

print (equation)
     