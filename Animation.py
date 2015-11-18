import sfml as sf
import time
class Animation:
	def __init__(self,framestime,name):
		self.framestime=sf.seconds(framestime)
		self.clock=sf.Clock()
		self.currentframe=0
		self.name=name
		self.frames = []
		self._itersCount = 0
	def AddFrame(self,rect):
		self.frames.append(rect)
	def GetFrame(self):
		if self.started and self.clock.elapsed_time>self.framestime:
			self.clock.restart()
			self.currentframe+=1
			if self.currentframe==len(self.frames):
				self.currentframe=0
				self._itersCount += 1
		if not self.started:
			self.currentframe=0
		return self.frames[self.currentframe]
	def SetSpriteTexture(self,texture):
		self.texture=texture
	def GetSpriteTexture(self):
		return self.texture
	def Stop(self):
		self.started = False
	def Start(self):
		self.started = True
	def GetAnimationItersCount(self):
		return self._itersCount
	name=None
	framestime=None
	clock=None
	frames = None
	currentframe=None
	texture=None
	started = True
	_itersCount = None

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

