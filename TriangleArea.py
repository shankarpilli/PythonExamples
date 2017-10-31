#Area of a triangle.
import math

height = int(input("Enter your triangle height : "))
base = int(input("Enter your traangle base : "))

print "Your Triangle Area : " + str(0.5*height*base)

#OutPut
##Enter your triangle height : 12
##Enter your traangle base : 13
##Your Triangle Area : 78.0

a = int(input("Triangle a coordinate : "))
b = int(input("Triangle a coordinate : "))
c = int(input("Triangle a coordinate : "))

parimater = (a+b+c)/2

area = math.sqrt(parimater*(parimater-a)*(parimater-b)*(parimater-c))

print str(area)


///Enter your triangle height : 12
Enter your traangle base : 13
Your Triangle Area : 78.0
Triangle a coordinate : 2
Triangle a coordinate : 2
Triangle a coordinate : 2
1.73205080757///
