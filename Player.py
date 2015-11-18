import AnimatedObject as ao
import sfml as sf
import Location as loc
import Physics as Phys
import IniFile as ini
import Object as obj

STEP_SIZE = 1

class Player(ao.AnimatedObject):
	def __init__(self, IniPath):
		ao.AnimatedObject.__init__(self, IniPath)
		self.StartAnimate()
		self._clock=sf.Clock()
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
		if step.x > 0:
			self.SetAnimation("walk_right")
		if step.x < 0:
			self.SetAnimation("walk_left")
		if step.y < 0:
			self.SetAnimation("walk_up")
		if step.y > 0:
			self.SetAnimation("walk_down")
		if step.x==0 and step.y==0:
			self._stopCounter += 1
			if self._stopCounter > 10:
				self.StopAnimate()
		else:
			self._stopCounter = 0
			self.StartAnimate()
	def SetLocation(self,location):
		self._location=location
	_location = None
	_stopCounter = 0
	_clock=None
