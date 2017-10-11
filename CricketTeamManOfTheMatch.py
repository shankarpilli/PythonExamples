'''Take two teams from the user. Enter some
players data. In that take heighest score, catches, wickets.
Calculate Man fof the match'''
import ast

mTeamA = raw_input("Enter team A name: ")
mTeamB = raw_input("Enter team B name: ")

mTeamAData = raw_input("Enter team a data: ")
mTeamBData = raw_input("Enter team b data: ")

mTeamADataAsDict = ast.literal_eval(mTeamAData)
mTeamBDataAsDict = ast.literal_eval(mTeamBData)

mKey="";
mIsSameTeam = True;

if(mTeamA=="IND" or mTeamB == "AUS"):
    if((mTeamADataAsDict["kohili"][0]>mTeamADataAsDict["dhoni"][0] and
       mTeamADataAsDict["kohili"][1]>mTeamADataAsDict["dhoni"][1]) or
       (mTeamADataAsDict["kohili"][1]>mTeamADataAsDict["dhoni"][1] and
       mTeamADataAsDict["kohili"][2]>mTeamADataAsDict["dhoni"][2])or
       (mTeamADataAsDict["kohili"][0]>mTeamADataAsDict["dhoni"][0] and
       mTeamADataAsDict["kohili"][2]>mTeamADataAsDict["dhoni"][2])):
        mKey = "kohili"
    else:
        mKey = "dhoni"
    if((mTeamADataAsDict[mKey][0]>mTeamBDataAsDict["smith"][0] and
       mTeamADataAsDict[mKey][1]>mTeamBDataAsDict["smith"][1]) or
       (mTeamADataAsDict[mKey][1]>mTeamBDataAsDict["smith"][1] and
       mTeamADataAsDict[mKey][2]>mTeamBDataAsDict["smith"][2])or
       (mTeamADataAsDict[mKey][0]>mTeamBDataAsDict["smith"][0] and
       mTeamADataAsDict[mKey][2]>mTeamBDataAsDict["smith"][2])):
        mKey = mKey
    else:
        mKey = "smith"
        mIsSameTeam = False;
    if(mIsSameTeam):
        if((mTeamADataAsDict[mKey][0]>mTeamBDataAsDict["warner"][0] and
           mTeamADataAsDict[mKey][1]>mTeamBDataAsDict["warner"][1]) or
           (mTeamADataAsDict[mKey][1]>mTeamBDataAsDict["warner"][1] and
           mTeamADataAsDict[mKey][2]>mTeamBDataAsDict["warner"][2])or
           (mTeamADataAsDict[mKey][0]>mTeamBDataAsDict["warner"][0] and
           mTeamADataAsDict[mKey][2]>mTeamBDataAsDict["warner"][2])):
            mKey = mKey
        else:
            mKey = "warner"
    else:
        if((mTeamBDataAsDict[mKey][0]>mTeamBDataAsDict["warner"][0] and
           mTeamBDataAsDict[mKey][1]>mTeamBDataAsDict["warner"][1]) or
           (mTeamBDataAsDict[mKey][1]>mTeamBDataAsDict["warner"][1] and
           mTeamBDataAsDict[mKey][2]>mTeamBDataAsDict["warner"][2])or
           (mTeamBDataAsDict[mKey][0]>mTeamBDataAsDict["warner"][0] and
           mTeamBDataAsDict[mKey][2]>mTeamBDataAsDict["warner"][2])):
            mKey = mKey
        else:
            mKey = "warner"
print "Here is the Final Man of the Match : "+str(mKey)


#Out put
'''Enter team A name: IND
Enter team B name: AUS
Enter team a data: {"kohili":[50,2,6],"dhoni":[78,1,4]}
Enter team b data: {"smith":[32,2,0],"warner":[45,0,0]}
Here is the Final Man of the Match : kohili
>>> 
=========== RESTART: D:\PythonWorkout\CricketTeamManOfTheMatch.py ===========
Enter team A name: IND
Enter team B name: AUS
Enter team a data: {"kohili":[50,2,6],"dhoni":[78,1,4]}
Enter team b data: {"smith":[32,2,0],"warner":[85,22,30]}
Here is the Final Man of the Match : warner'''
