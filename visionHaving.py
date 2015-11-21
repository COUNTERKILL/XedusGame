

class VisionHaving:
	def __init__(self):
		pass
	def SetVisionAngle(self, angle):
		self._object.SetRotation(angle)
	def GetVisionAngle(self):
		return self._object.GetRotation()