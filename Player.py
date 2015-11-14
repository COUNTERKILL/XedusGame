import AnimatedObject as ao
import Location as loc
import Physics as Phys
import IniFile as ini
import Object as obj
class Player(ao.AnimatedObject):
	def __init__(self,IniPath):
		ao.AnimatedObject.__init__(self,IniPath)
    def Move(self,step):
		self.position.x += step.x
		self.position.y += step.y
        if self._location.CollideTo(self):
			self.position.x -= step.x
			self.position.y -= step.y
	def SetLocation(self,location):
		self._location=location
