import IniFile as ini
import Object as obj
class WayPoint:
    def __init__(self,position,animation):
        self._position=position
        self._animation=animation
    def SetPosition(self,position):
        self._position=position
    def SetAnimation(self,animation):
        self._animation=animation
    def GetPosition(self):
        return self._position
    def GetAnimation(self):
        return self._animation
	_animation = None
	_position = None
    
class Way:
    def __init__(self,LogicFileName):
        IniReader=ini.IniFile(LogicFileName)
        points_count=IniReader.ReadInt("way","points_count")
        self._ways=[]
        for i in range(0,points_count):
            way_point=WayPoint(obj.Position(IniReader.ReadInt("way_point"+str(i),"pos_x"),
                                            IniReader.ReadInt("way_point"+str(i),"pos_y")),
                                            IniReader.ReadString("way_point"+str(i),"animation"))
            self._ways.append(way_point)
        self._currentWayPoint=self._ways[0]
    def GetWayPoint(self):
        return self._ways[self._currentWayPointIndex]      
    def GetNextWayPoint(self):
        if len(self._ways)-1 == self._currentWayPointIndex:
            return 0
        else:
            return self._ways[self._currentWayPointIndex+1]
    def ChangeToNextWayPoint(self):
        if len(self._ways)-1 == self._currentWayPointIndex:
            self._currentWayPointIndex=0
        else:
            self._currentWayPointIndex+=1
    _ways=None
    _currentWayPointIndex=None

Ways=Way("locations\\logics\\test_npc.ini")
