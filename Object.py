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
	x = None
	y = None
		
class Object(sf.Drawable):
	def __init__(self, ObjIniPath):
		load=ini.IniFile(ObjIniPath)
		iniDir = os.path.dirname(ObjIniPath)
		self.width=load.ReadInt("Object","width")
		self.height=load.ReadInt("Object","height")
		self._type_interaction=load.ReadInt("Object","type_interaction")
		self._type_logic=load.ReadInt("Object","type_logic")
		self._sprite=sf.Sprite(sf.Texture.from_file(iniDir+'\\images\\'+load.ReadString("Object","texture")))
		sf.Drawable.__init__(self)        
	def SetLayer(self,layer):
		self._layer=layer
	def SetPosition(self,pos):
		self._position=pos;
	def GetPosition(self):
		return self._position
	def draw(self, target, state):
		self._sprite.position=sf.Vector2(self._position.x,self._position.y)
		self._sprite.texture_rectangle=sf.Rectangle((0,0),(self._width,self._height))
		target.draw(self._sprite, state)
	def GetTypeInteraction(self):
		return self._type_interaction
	def GetLayer(self):
		return self._layer
	_position=Position(0,0)
	_obj_id = None
	_type_interaction = None
	_type_logic = None
	_sprite = None    
	_layer = 0
	_width = 0
	_height = 0

