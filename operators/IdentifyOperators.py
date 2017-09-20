#This is the example of identify operators
name = str(raw_input("Enter your number name "))
myName = name
print myName is name

number  = int(input("Enter your number : "))
checkNumber  = number
print number is checkNumber

# is not example

floatNumber  = float(input("Enter your float number : "))
getFloatNumber = floatNumber
print floatNumber is not getFloatNumber


#Output
'''Enter your number name Shankar Pilli
True
Enter your number : 20
True
Enter your float number : 2.5
False'''
