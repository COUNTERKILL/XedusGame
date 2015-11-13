import sfml as sf
import time
class Animation:
	def __init__(self,framestime,name):
		self.framestime=sf.seconds(framestime)
		self.clock=sf.Clock()
		self.currentframe=0
		self.name=name
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
			return self.frames[self.currentframe]
	def SetSpriteTexture(self,texture):
		self.texture=texture
	def GetSpriteTexture(self):
		return self.texture
	name=None
	framestime=None
	clock=None
	frames=[]
	currentframe=None
	texture=None


if __name__=="__main__":
    b=Animation(1,"lol")
    b.AddFrame(1);
    b.AddFrame(2);
    b.AddFrame(3);
    b.AddFrame(4);
    while(True):
        time.sleep(1)
        print(b.GetFrame())
        print(b.clock.elapsed_time)

