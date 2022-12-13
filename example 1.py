my_list=[1,2,4,5,] #список
my_tuple =(1,2,4,5)#кортеж
my_set={1,2,3,4,5} #множество 
my_dict= {1:'one', 2:'two',3:'three'} #словарь

print(my_list)
my_list.remove(2) #removes number two from thr list
# my_list.pop(2) removes the element two

#adding elements
print(my_list)
pop_elem = my_list.pop(2)
print(my_list)
my_list.extend(my_list)
print(my_list)
my_list = my_list[::-1]
print(my_list)