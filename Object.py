import sfml as sf
import IniFile as ini
import os
TYPE_INTERACTION_PHYSICAL=0
TYPE__INTERACTION_VISUAL=1
TYPE__LOGIC_IMPASSABLE_AREA=0
TYPE_LOGIC_PASSABLE_AREA=1
TYPE_LOGIC_ANOMALY=2
TYPE_LOGIC_ARTEFACT=3
TYPE_LOGIC_NPC=4


class Position:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		strx=str(self.x)
		stry=str(self.y)
		return strx+' '+stry
		
class Object(sf.Drawable):
	def __init__(self, ObjIniPath):
		load=ini.IniFile(ObjIniPath)
		iniDir = os.path.dirname(ObjIniPath)
		self.width=load.ReadInt("Object","width")
		self.height=load.ReadInt("Object","height")
		self.type_interaction=load.ReadInt("Object","type_interaction")
		self.type_logic=load.ReadInt("Object","type_logic")
		self.sprite=sf.Sprite(sf.Texture.from_file(iniDir+'\\images\\'+load.ReadString("Object","texture")))
		sf.Drawable.__init__(self)        
	position=Position(0,0)
	obj_id = None
	type_interatction = None
	type_logic = None
	sprite = None    
	layer = 0
	def SetPosition(self,pos):
		self.position=pos;
	def GetPosition(self):
		return self.position
	def draw(self, target, state):
		self.sprite.position=sf.Vector2(self.position.x,self.position.y)
		self.sprite.texture_rectangle=sf.Rectangle((0,0),(self.width,self.height))
		target.draw(self.sprite, state)


