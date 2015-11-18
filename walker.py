
STEP = 5

class Walker:
	def __init__(self, object):
		logicFileName = object.GetLogicFileName()
		objectLogicPath = object.GetLocationIniDir() + "\\logics\\" + logicFileName
		self._way = Way(objectLogicPath)
	def Walk(self):
		pass
	_way = None
