import AnimatedObject as ao
import Location as loc
import Physics as Phys
import IniFile as ini
import Object as obj

STEP_SIZE = 5

class Player(ao.AnimatedObject):
	def __init__(self, IniPath):
		ao.AnimatedObject.__init__(self, IniPath)
	def Move(self,step):
		self._position.x += step.x
		self._position.y += step.y
		if self._location.CollideTo(self):
			self._position.x -= step.x
			self._position.y -= step.y
		if step.x > 0:
			self.SetAnimation("walk_right")
		if step.x < 0:
			self.SetAnimation("walk_left")
		if step.y < 0:
			self.SetAnimation("walk_up")
		if step.y > 0:
			self.SetAnimation("walk_down")
	def SetLocation(self,location):
		self._location=location
	_location = None
