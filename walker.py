import sfml as sf
from object import Position
import math
from logicObject import LogicObject
from way import Way
import copy

STEP_SIZE = 4
TIME_BETWEEN_STEPS = 0.03

class Walker (LogicObject):
	def __init__(self, objectLogicPath, object):
		LogicObject.__init__(self, objectLogicPath, object)
		self._way = Way(objectLogicPath)
		self._stepBetweenTime = sf.Clock()
	def Walk(self):
		if self._stepBetweenTime.elapsed_time.seconds > TIME_BETWEEN_STEPS:
			self._stepBetweenTime.restart()
			oldWayPoint = self._way.GetPreviousWayPoint()
			nextWayPoint = self._way.GetNextWayPoint()
			pos = self._object.GetPosition()
			pos = Position(pos.x, pos.y)
			dPos = nextWayPoint.GetPosition() - pos
			dPos = Position(dPos.x / math.sqrt(dPos.x * dPos.x + dPos.y * dPos.y), dPos.y / math.sqrt(dPos.x * dPos.x + dPos.y * dPos.y))
			dPos = Position(dPos.x * STEP_SIZE, dPos.y * STEP_SIZE)
			self.SetView(dPos)
			newPos = pos + dPos
			dist = math.sqrt(math.pow((newPos.x - nextWayPoint.GetPosition().x), 2) + math.pow((newPos.y - nextWayPoint.GetPosition().y), 2))
			if dist <= STEP_SIZE:
				self._way.ChangeToNextWayPoint()
			self._object.Move(dPos)
			self._object.SetAnimation("WALK")
	def SetView(self, dPos):
		dPos = copy.copy(dPos)
		dPos.y = dPos.y * (-1)
		if dPos.x == 0 and dPos.y == 0:
			return
		hypotenuze = math.sqrt(dPos.x * dPos.x + dPos.y * dPos.y)
		cos = dPos.x / hypotenuze
		angleBuf = math.degrees(math.acos(cos))
		sin = dPos.y / hypotenuze
		
		if sin >= 0:
			angle = angleBuf
		else:
			angle = -1*angleBuf
		angle = angle - 90
		angle = angle * (-1)
		self._object.SetRotation(angle)
	_way = None
	_stepBetweenTime = None
