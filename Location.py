import sfml as sf
from sfml.graphics import RenderStates, BlendMode
import IniFile as ini
import Object as ob
import os
									  
class Location(sf.Drawable):
	def __init__(self, locIniPath):
		load=ini.IniFile(locIniPath)
		iniDir = os.path.dirname(locIniPath)
		self.objects_count=load.ReadInt("Location","objects_count")
		texture = sf.Texture.from_file(iniDir+'\\'+load.ReadString("Location","texture"))
		texture.repeated = True
		self.sprite=sf.Sprite(texture)
		self.width=load.ReadInt("Location","width")
		self.height=load.ReadInt("Location","height")
		for i in range(0, self.objects_count):
			objName = load.ReadString("Object"+str(i), "obj")
			self.objects.append(ob.Object(iniDir + '\\' + 'objects\\'+objName))
			pos = ob.Position(load.ReadInt("Object"+str(i), "pos_x"), load.ReadInt("Object"+str(i), "pos_y"))
			self.objects[len(self.objects)-1].SetPosition(pos)
		sf.Drawable.__init__(self)
	loc_id=None
	sprite=None
	objects=[]
	objects_count=0
	def addobjects(self,*objects):
		for obj in objects:
			self.objects.append(obj)
			self.objects_count+=1
		pass
	def printobjects(self):
		for obj in self.objects:
			print(obj.width,obj.height,obj.position.x,obj.position.y)
		pass
	def draw(self, target, state):
		self.sprite.position=sf.Vector2(0,0)
		self.sprite.texture_rectangle=sf.Rectangle((0,0),(self.width,self.height))
		
		target.draw(self.sprite, state)
		for obj in self.objects:
			target.draw(obj)

