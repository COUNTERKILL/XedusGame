class Live:
	def __init__(self):
		self._health = 100
	def GetHealth(self):
		return self._health
	def SetHealth(self, health):
		self._health = health
	def IsLive(self):
		if self._health <= 0:
			return False
		else:
			return True
	_health = None
	