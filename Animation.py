import sfml as sf
import time
class Animation:
    def __init__(self,framestime):
        self.framestime=framestime
        self.clock=sf.Clock()
        self.currentframe=0
    def AddFrame(self,rect):
        self.frames.append(rect)
    def GetFrame(self):
        if self.clock.elapsed_time>self.framestime:
            self.clock.restart()
            self.currentframe+=1
            if self.currentframe==len(self.frames):
                self.currentframe=0
                return self.frames[self.currentframe]
            return self.frames[self.currentframe]
        else:
            self.clock.restart()
            return self.frames[self.currentframe]
    def SetSpriteTexture(self,texture):
        self.texture=texture
    def GetSpriteTexture(self):
        return self.texture
    framestime=None
    clock=None
    frames=[]
    currentframe=None
    texture=None
clock=sf.Clock()
elapsed1=clock.elapsed_time
print(elapsed1.seconds)
#clock.restart()
elapsed2=clock.elapsed_time
print(elapsed2.seconds)
t2=sf.seconds(1)
print(t2)
b=Animation(sf.seconds(1))
b.AddFrame(1);
b.AddFrame(2);
b.AddFrame(3);
b.AddFrame(4);
framess=[]
framess.append(1)
print(framess[0])
while(True):
    time.sleep(1)
    s=b.GetFrame()
    print(str(s))
    print(b.clock.elapsed_time)





