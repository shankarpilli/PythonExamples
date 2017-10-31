#This program will check the given year is leap year or not

def isLeepYear(year):
    if(year%4==0):
        return True;
    else:
        return False;

yourNumber = int(input("Enter your year : "))
if(isLeepYear(yourNumber)):
    print "Leep year"
else:
    print "No this is not leep year"
