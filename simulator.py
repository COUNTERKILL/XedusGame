from anomaly import Anomaly
from npc import Npc
from walker import Walker
import iniFile as ini
from logicPlayer import LogicPlayer
from live import Live
from musiccollection import musicCollection

class Simulator:
	def __init__(self, location):
		self._logicObjects = []
		self._location = location
		for object in location._objects:
			logicFileName = object.GetLogicFileName()
			objectLogicPath = location.GetLocationIniDir() + "\\logics\\" + logicFileName
			logicObject = None
			if type(object).__name__ == "Player":
				logicObject = LogicPlayer(objectLogicPath, object)
				self._player = logicObject
				self._logicObjects.append(logicObject)
				print("Player is finded on location")
				continue
			configFile=ini.IniFile(objectLogicPath)
			unit_type = configFile.ReadString("logic", "type")
			if unit_type == "npc":
				logicObject = Npc(objectLogicPath, object)
			if unit_type == "anomaly":
				logicObject = Anomaly(objectLogicPath,object)
				logicObject._object.SetAnimation("PASSIVE")
			if logicObject == None:
				print("Object time not defined: " + unit_type)
				continue
			self._logicObjects.append(logicObject)
		self._isGameOver = False
	def ProcessFrame(self):
		for logicObject in self._logicObjects:
			if issubclass(logicObject.__class__, Walker):
				logicObject.Walk()
			if issubclass(logicObject.__class__, Live):
				for logicObjectIter in self._logicObjects:
					if issubclass(logicObjectIter.__class__, Anomaly):
						if logicObject.InAnomaly(logicObjectIter):
							logicObjectIter.ActivateTo(logicObject)
		if self._player.GetHealth()==0:
			self._isGameOver = True
			music = musicCollection.GetMusic("ACTOR", "DIE")
			music.play()
			self._player._object.SetAnimation("DIE")
			self._player._object.SetNextAnimation("DIED")
	def IsGameOver(self):
		return self._isGameOver
	def GetPlayer(self):
		return self._player
	_logicObjects = None
	_player = None
	_location = None
	_isGameOver = None
