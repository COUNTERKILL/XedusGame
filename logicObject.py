from object import Position
import math

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
	def UnderMouse(self, mousePos):
		#print mousePos
		objPos = self._object.GetPosition()
		objCenter = Position(objPos.x + self._object.GetWidth() / 2, objPos.y + self._object.GetHeight()  / 2)
		radius = self._object.GetWidth() / 2
		div = math.sqrt((objCenter.x - mousePos.x) * (objCenter.x - mousePos.x) + (objCenter.y - mousePos.y) * (objCenter.y - mousePos.y))

		if div < radius:
			return True
		else:
			return False
		
	_object = None
	_objectLogicPath = None
	
