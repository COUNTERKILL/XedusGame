from logicObject import LogicObject
import iniFile as ini
import sfml as sf
import random
from musiccollection import musicCollection
from logicPlayer import LogicPlayer

class Anomaly(LogicObject):
	def __init__(self, objectLogicPath, object):
		LogicObject.__init__(self, objectLogicPath, object)
		logicFileName = object.GetLogicFileName()
		configFile=ini.IniFile(objectLogicPath)
		self._damage = configFile.ReadInt("anomaly", "damage")
		self._temeReloading = configFile.ReadInt("anomaly", "time_reloading")
		self._music = musicCollection.GetMusic("ANOMALIES", configFile.ReadString("anomaly", "music_active"))
		self._clock = sf.Clock()
	def ActivateTo(self, live):
		if self._clock.elapsed_time.milliseconds < self._temeReloading:
			return
		live.SetHealth(live.GetHealth() - random.randint(self._damage*0.2, self._damage*1.5))
		if issubclass(live.__class__, LogicPlayer):
			music = musicCollection.GetMusic("ACTOR", "HIT")
			music.play()
		self.Activate()
	def Activate(self):
		self._clock.restart()
		self._object.SetAnimation("ACTIVE")
		
		self._music.play()
		self._object.SetNextAnimation("PASSIVE")
	_damage = None
	_temeReloading = None
	_clock = None
	_music = None
