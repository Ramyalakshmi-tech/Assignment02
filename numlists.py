# lists=[]
# num=1
# while num<=10:
#     lists.append(num)
#     num+=1
# print(lists)
# ---------------------------------------------
lists=[]
num=1
while num<=10:
    if(num%2==0):
        lists.append(num)
    num+=1
print(lists)

list=[]
nums=2
while nums<=100:
    if(nums%7==0):
        list.append(nums)
    nums+=1
print(list)


list1=[i for i in range(1,101) if(i%7==0)]


print(list1)

