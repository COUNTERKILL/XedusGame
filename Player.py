import animatedObject as ao
import sfml as sf
import location as loc
import physics as Phys
import iniFile as ini
import object as obj
from musiccollection import musicCollection
import math

STEP_SIZE = 2

class Player(ao.AnimatedObject):
	def __init__(self, IniPath, window):
		ao.AnimatedObject.__init__(self, IniPath)
		self.StartAnimate()
		self._clock=sf.Clock()
		self._stepBetweenTime = sf.Clock()
		self._window = window
	def Move(self,step):
		if self._clock.elapsed_time < sf.milliseconds(5):
			return
		self._clock.restart()
		self._position.x += step.x
		self._position.y += step.y
		if self._location.CollideTo(self):
			self._position.x -= step.x
			self._position.y -= step.y
		if self._position.x < 0:
			self._position.x = 0
		if self._position.y < 0:
			self._position.y = 0
		if (self._position.x + self.GetWidth()) > self._location.GetWidth():
			self._position.x = self._location.GetWidth() - self.GetWidth()
		if (self._position.y + self.GetHeight()) > self._location.GetHeight():
			self._position.y = self._location.GetHeight() - self.GetHeight()
		if step.x==0 and step.y==0:
			self._stopCounter += 1
			if self._stopCounter > 10:
				self.StopAnimate()
				music = musicCollection.GetMusic("ACTOR", "STEP")
				music.stop()
		else:
			self._stopCounter = 0
			self.SetAnimation("WALK")
			self.StartAnimate()
			music = musicCollection.GetMusic("ACTOR", "STEP")
			if music.status == sf.audio.SoundSource.STOPPED and self._stepBetweenTime.elapsed_time.seconds > 0.4:
				self._stepBetweenTime.restart()
				music.volume = 50
				music.play()
	def SetLocation(self,location):
		self._location=location
	def SetView(self):
		mousePos = sf.Mouse.get_position(self._window)
		dPos = mousePos - sf.Vector2(self._window.width/2, self._window.height/2)
		dPos.y = dPos.y * (-1)
		if dPos.x == 0 and dPos.y == 0:
			return
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
		self.SetRotation(angle)
	_window = None
	_location = None
	_stopCounter = 0
	_clock=None
	_stepBetweenTime = None
