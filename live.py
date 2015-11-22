from logicObject import LogicObject
import physics as Phys

class Live(LogicObject):
	def __init__(self, objectLogicPath, object):
		LogicObject.__init__(self, objectLogicPath, object)
		self._health = 100
	def GetHealth(self):
		return self._health
	def SetHealth(self, health):
		if health < 0:
			health = 0
		self._health = health
	def IsLive(self):
		if self._health <= 0:
			return False
		else:
			return True
	def InAnomaly(self, anomaly):
		anomalyPos = anomaly.GetPosition()
		anomalyWidth = anomaly.GetWidth()
		anomalyHeight = anomaly.GetHeight()
		return Phys.Collide(self._object, anomaly._object)
	_health = None
	