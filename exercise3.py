f_nums = input('Insert numbers: ')
f_nums =f_nums.string().split(' ')

for i in range (len(f_nums)):
    f_nums[i]=int(f_nums[i])
    
max_num= F.MaxIntList(f_nums)
count = max_num


if count % f_nums[0]==0 and f_nums[1]==0:
    print (count)

for i in range (max_num, f_nums[0]+f_nums[i]+1):
     if i % f_nums[0]==0 and i% f_nums[1]==0:
         print (i)

