#Add Appened in list

mList = []
a = input("Enter your input index a : ")
mList.insert(0,a)

b = input("Enter your input index a : ")
mList.insert(1,b)

c = input("Enter your input index a : ")
mList.insert(2,c)

d = input("Enter your input index a : ")
mList.insert(3,d)

print mList

mList.append(["a", "true"])

print mList
print mList[4]

#Output
'''Enter your input index a : 25
Enter your input index a : 25
Enter your input index a : 25
Enter your input index a : 24
[25, 25, 25, 24]
[25, 25, 25, 24, ['a', 'true']]
['a', 'true']'''
