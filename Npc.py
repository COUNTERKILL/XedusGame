from live import Live
import iniFile as ini
from way import Way
import sfml as sf
from object import Position
from walker import Walker

FRIEND = 1
ENEMY = -1
NEUTRAL = 0

ALARM_TIME = 10 # alarm time in seconds

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
	
class Npc(Live, Walker):
	def __init__(self, simulation, object):
		Live.__init__(self, simulation, object)
		Walker.__init__(object)
		logicFileName = object.GetLogicFileName()
		objectLogicPath = object.GetLocationIniDir() + "\\logics\\" + logicFileName
		configFile=ini.IniFile(objectLogicPath)
		configFile.ReadString("npc", "group")
		self.SetHealth(configFile.ReadInt("npc", "health"))
		self._clock = sf.Clock()
		self._alarm = False
	def IsAlarm(self):
		if self._alarm:
			if self._clock.elapsed_time.seconds < ALARM_TIME:
				return True
			else:
				self._alarm = False
		return False
	_group = None
	_clock = None
	_alarm = None
	
