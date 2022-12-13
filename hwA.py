


import random
import math

k = int(random.randint(0,10))
print(f'степень = {k}')
coef_list=[]
coef_1=(int(random.randint(-100,100)))
coef_2=(int(random.randint(-100,100)))
coef_3=(int(random.randint(-100,100)))
print(f'a= {coef_1}')
print(f'b= {coef_2}')
print(f'c= {coef_3}')

coef_list=[coef_1, coef_2,coef_3]
print(coef_list)
#for i in range (coef):
print (f'{coef_1}*(x^2) + {coef_2}*x + {coef_3}=0')
d=((coef_2)**2)-((4*(coef_1))*((coef_3)))
print (f'Выражение равно {((-coef_2)+d)/ (coef_2*2)} либо {((-coef_2)-d)/ (2*coef_1)}')

f=open ('result_hwA.txt', 'w') #запись в отдельный файл
f.write(str(coef_list))
f.close()