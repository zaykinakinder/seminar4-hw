my_dict= {'one':1, 'two':2,'three':3} #словарь
my_dict_2= {'four':4, 'five':5,'six':6}
my_dict[6]='six'
print (my_dict.get(6))

#my_dict.update(my_dict_2)
#print(my_dict)
for i in my_dict.keys():
    if my_dict.get(i) and my_dict_2.get(i):
        my_dict[i]=my_dict.get(i) + my_dict_2.get(i)
print (my_dict)