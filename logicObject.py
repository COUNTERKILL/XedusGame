class LogicObject:
	def __init__(self, objectLogicPath, object):
		self._object = object
		self._objectLogicPath = objectLogicPath
	def GetWidth(self):
			return self._object.GetWidth()
	def GetHeight(self):
		return self._object.GetHeight()
	def GetPosition(self):
		return self._object.GetPosition()
	_object = None
	_objectLogicPath = None
	
