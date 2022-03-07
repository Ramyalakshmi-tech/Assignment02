nums=[25,12,36,95,14]
print(nums)
print(nums[0])
print(nums[2: ])

names=["Ramya","Devi","nandhini"]
print(names)
values=[9.5,"Navin",25]
mil=[nums,names]
print(mil)

nums.append(45)
print(nums)
nums.insert(2,77)
print(nums)
nums.remove(14)
print(nums)
nums.pop(1)
print(nums)
nums.pop()
print(nums)
del nums[2: ]
print(nums)

nums.extend([29,90,89,70])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
print(nums)
nums.sort()
print(nums)

# ________________________________________________________________________

tuple1=(10,20,30,40,50,60)
print(tuple1)
count=0
for i in tuple1:
    print("tuple1[%d]=%d"%(count,i))
    count=count+1


tuple2=tuple(input("Enter the tuple elements"))
print(tuple2)
count=0
for i in tuple2:
    print("tuple2[%d]=%d" % (count, i))
    count = count + 1


# _________________________________-
Days={"Monday","Tuesday","Wednesday"}
print(Days)
print(type(Days))
print("looping through the set elements...")
for i in Days:
    print(i)

# Empty curly braces will create dictionary
set3 = {}
print(type(set3))

# Empty set using set() function
set4 = set()
print(type(set4))

set1={1,2,3,"Javapoint",20.15,14}
print(type(set1))

set2={1,2,3,["3"]}
print(type(set2))



# Empty curly braces will create dictionary
set3 = {}
print(type(set3))

# Empty set using set() function
set4 = set()
print(type(set4))



set5 = {1,2,4,4,5,8,9,9,10}
print("Return set with unique elements:",set5)



months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(months)
print("\nAdding other months to the set...")
months.add("July")
months.add("August")
print("\nPrinting the modified set...")
print(months)
print("\nlooping through the set elements ... ")
for i in months:
    print(i)

Months = set(["January", "February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(Months)
print("\nupdating the original set ... ")
Months.update(["July", "August", "September", "October"]);
print("\nprinting the modified set ... ")
print(Months)

months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(months)
print("\nRemoving some months from the set...");
months.remove("January");
months.remove("May");
print("\nPrinting the modified set...");
print(months)

