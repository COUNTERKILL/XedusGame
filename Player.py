import AnimatedObject as ao
import Location as loc
import Physics as Phys
import IniFile as ini
import Object as obj
class Player(ao.AnimatedObject):
    def __init__(self,IniPath):
        ao.AnimatedObject.__init__(self,IniPath)
    def Move(self,step):
        valid=True
        for obj in self._location.objects:
            print(Phys.Collide(self,obj))
            if Phys.Collide(self,obj)==True:
                valid=False
        if(valid):
            self.position.x=step.x
            self.position.y=step.y
    def SetLocation(self,location):
        self._location=location

        
