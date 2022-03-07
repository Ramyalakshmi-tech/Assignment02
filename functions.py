# def add(x,y):
#     z=x+y
#     print(z)
#
# a=9
# b=5
# add(a,b)
#
# def addnum(x,y):
#     z=x+y
#     return z
#
# c=8
# d=5
# result=addnum(c,d)
# print(result)
#
#
# def checkOddorEven(m):
#     if(m%2==0):
#         return "even"
#     else:
#         return "odd"
# n=9
# result=checkOddorEven(n)
# print(result)
#
# def divisiblefun(k):
#     if(k%8==0):
#         return "divisible by 8"
#     else:
#         return "not divisible by 8"
# l=int(input("Enter a number"))
# result=divisiblefun(l)
# print(result)
#
# def smallestnum(r,s,t):
#     if(r<s and r<t):
#         return "r is the smallest"
#     elif(s<r and s<t):
#         return "s is the smallest"
#     else:
#         return "t is the smallest"
# r=int(input("Enter a number"))
# s=int(input("Enter a number"))
# t=int(input("Enter a number"))
# result=smallestnum(r,s,t)
# print(result)
#
# orbitary orbitals
# def add(*num):
#     return num[0]
# r=2
# s=9
# g=8
# result=add(r,s,g)
# print(result)
#
# def printName(*name):
#     for i in name:
#         print(i)
# def test(w):
#     pass
# namelist=["Ramya","Devi","lakshmi"]
# printName(namelist)
#
# a=29.817677
# result=round(a,2)
# print(result)
# b=(2,6,0,7,5)
# print(min(b))
#
# x=int(input("Enter x"))
# y=int(input("Enter y"))
# z=int(input("Enter z"))
# multiply=lambda a,b,c:a+b+c
# print(multiply(x,y,z))
#
# num_list=[1,2,3,4,5,6]
# odd_lists=list(map(lambda x:(x%2)!=0,num_list))
# odd_list=list(filter(lambda x:(x%2)!=0,num_list))
# print(odd_lists)
# print(odd_list)

# new_list=[1,2,3,4,5,6,9,8,5]
new_list=[i for i in range(1,10)]
div=list(filter(lambda x:(x%5)==0,new_list))
square=list(map(lambda a:(a*a),new_list))
square_exponent=list(map(lambda b:(b**2),new_list))
print(div)
print(square)
print(square_exponent)

#zip
a=["Ramya","devi","nandhini"]
b=["engineer","doctor","designer"]
c=zip(a,b)
print(tuple(c))

import calculatorPackages as cp
a=9
b=5
result=cp.addnum(a,b)
result1=cp.multiply(a,b)
print(result)
print(result1)


import json as j
data={"name":"Ramya","age":"kl"}
jsonData=j.dumps(data)
myjsonData=j.loads(jsonData)

print(myjsonData)