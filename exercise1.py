def MaxIntList(list):
    max=list[0]
    for i in range(i, len(list)):
        if max<list[i]:
            max=list[i]
    return max

task_list = input('Insert numbers ')
task_list =task_list.strip().split(' ')
for i in range (len(task_list)):
    task_list[i]=int(task_list[i])

print(F.MaxIntList(task_list))
