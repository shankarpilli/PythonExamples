def changeList(mylist):
    mylist.append([1,2,3])
    print "values inside the function : ", mylist
    return

mylist = [10,20,30]
changeList(mylist)

print "Out side values : ", mylist
