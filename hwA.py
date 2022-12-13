


import random
import math

k = int(random.randint(0,10))
print(k)

coef_1=(int(random.randint(-100,100)))
coef_2=(int(random.randint(-100,100)))
coef_3=(int(random.randint(-100,100)))
print(coef_1)
print(coef_2)
print(coef_3)
#for i in range (coef):
d=((coef_2)**2)-((4*(coef_1))*((coef_3)))
print (f'Выражение равно {((-coef_2)+d)/ (coef_2*2)} либо {((-coef_2)-d)/ (2*coef_1)}')
   