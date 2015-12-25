from anomaly import Anomaly
from npc import Npc
from walker import Walker
import iniFile as ini
from logicPlayer import LogicPlayer
from live import Live
from musiccollection import musicCollection
from object import Position
import sfml as sf

ZOOM = 2
TIME_BETWEEN_FIRES = 0.1

class Simulator:
	def __init__(self, location, window):
		self._window = window
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
		self._firesBetweenTime = sf.Clock()
		self._isGameOver = False
	def ProcessFrame(self):
		for logicObject in self._logicObjects:
			if issubclass(logicObject.__class__, Walker):
				if issubclass(logicObject.__class__, Live):
					if logicObject.IsLive():
						logicObject.Walk()
				else:
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
			self._player._object.SetAnimation("DIED")
			#self._player._object.SetNextAnimation("DIED")
	def IsGameOver(self):
		return self._isGameOver
	def GetPlayer(self):
		return self._player
	def Fire(self):
		if self._firesBetweenTime.elapsed_time.seconds > TIME_BETWEEN_FIRES:
			mousePos = sf.Mouse.get_position(self._window) * ZOOM + self._window.view.center - self._window.view.size / 2 + sf.Vector2(100, 100)
			music = musicCollection.GetMusic("ACTOR", "FIRE")
			music.play()
			
			for logicObject in self._logicObjects:
				if issubclass(logicObject.__class__, Live):
					if not logicObject is self._player:
						if logicObject.UnderMouse(mousePos):
							logicObject.SetHealth(logicObject.GetHealth() - 10)
							if not self._oldMusic:
								self._oldMusic = musicCollection.GetRandomInGroup("NPC_HIT")
							if self._oldMusic and self._oldMusic.status==sf.SoundStream.STOPPED:
								music = musicCollection.GetRandomInGroup("NPC_HIT")
								music.play()
								self._oldMusic = music
							if not logicObject.IsLive():
								logicObject._object.SetAnimation("DIED")
								logicObject._object.SetLayer(1)
			self._firesBetweenTime.restart()
					
		
	def GetAngle(self, dPos):
		dPos.y = dPos.y * (-1)
		if dPos.x == 0 and dPos.y == 0:
			return 0

		hypotenuze = math.sqrt(dPos.x * dPos.x + dPos.y * dPos.y)
		cos = dPos.x / hypotenuze
		angleBuf = math.degrees(math.acos(cos))
		sin = dPos.y / hypotenuze
		
		if sin >= 0:
			angle = angleBuf
		else:
			angle = -1*angleBuf
		angle = angle - 90
		angle = angle * (-1)
		return angle
		
	_oldMusic = None
	_logicObjects = None
	_player = None
	_location = None
	_isGameOver = None
	_window		= None
	_firesBetweenTime = None
