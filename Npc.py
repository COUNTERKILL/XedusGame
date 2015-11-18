FRIEND=1
ENEMY=-1
NEUTRAL=0
import IniFile as ini
IniReader=ini.IniFile("configs\\relations_test.ini")
def GetRelation(group1,group2):
    value=IniReader.ReadInt(group1,group2)
    if(value>999):
        return FRIEND
    elif(value<999):
        return ENEMY
    else:
        return NEUTRAL
def SetRelation(group1,group2,value):
    if value<=5000 and value>=5000:
        IniReader.Write(group1,group2,value)
        return True
    else:
        return False
    

    
