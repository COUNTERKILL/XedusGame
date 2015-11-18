class LogicObject:
	def __init__(self, simulator, object):
		self._simulator = simulator
		self._object = object
	def GetWidth(self):
			return self._object.GetWidth()
	def GetHeight(self):
		return self._object.GetHeight()
	def GetPosition(self):
		return self._object.GetPosition()
	_simulator = None
	_object = None
	
