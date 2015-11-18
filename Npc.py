import IniFile as ini

FRIEND = 1
ENEMY = -1
NEUTRAL = 0

iniReader=ini.IniFile("configs\\relations_test.ini")

def GetRelation(group1,group2):
	value=iniReader.ReadInt(group1,group2)
	if(value>999):
		return FRIEND
	elif(value<999):
		return ENEMY
	else:
		return NEUTRAL
def SetRelation(group1,group2,value):
	if value<=-5000:
		value=-5000
	elif value>=5000:
		value=5000        
	iniReader.Write(group1,group2,value)
	
SetRelation("stalker", "zombie", -3500)


    
