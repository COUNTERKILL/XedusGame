import sfml as sf
from sfml.graphics import RenderStates, BlendMode
import IniFile as ini
import Object as ob
import os
import Physics as Phys
import Player
                                                          
class Location(sf.Drawable):
	def __init__(self, locIniPath):
		self._objects = []
		load=ini.IniFile(locIniPath)
		iniDir = os.path.dirname(locIniPath)
		self._objects_count=load.ReadInt("Location","objects_count")
		texture = sf.Texture.from_file(iniDir+'\\'+load.ReadString("Location","texture"))
		texture.repeated = True
		self._sprite=sf.Sprite(texture)
		self._width=load.ReadInt("Location","width")
		self._height=load.ReadInt("Location","height")
		for i in range(0, self._objects_count):
			objName = load.ReadString("Object"+str(i), "obj")
			self._objects.append(ob.Object(iniDir + '\\' + 'objects\\'+objName))
			pos = ob.Position(load.ReadInt("Object"+str(i), "pos_x"), load.ReadInt("Object"+str(i), "pos_y"))
			self._objects[len(self._objects)-1].SetPosition(pos)
			self._objects[len(self._objects)-1].SetLayer(load.ReadInt("Object"+str(i), "layer"))
		self._objects.sort(key=lambda object: object._layer, reverse=True)
		sf.Drawable.__init__(self)
	def AddObject(self, obj, layer):
		obj.SetLayer(layer)
		if type(obj).__name__=='Player':
			obj.SetLocation(self)
		self._objects.append(obj)
		self._objects.sort(key=lambda object: object._layer, reverse=True)
		self._objects_count+=1                
	def draw(self, target, state):
		self._sprite.position=sf.Vector2(0,0)
		self._sprite.texture_rectangle=sf.Rectangle((0,0),(self._width,self._height))
			
		target.draw(self._sprite, state)
		for obj in self._objects:
			target.draw(obj)
	def CollideTo(self, obj):
		for object in self._objects:
			if (object.GetTypeInteraction()==ob.TYPE_INTERACTION_PHYSICAL):
				if (object.GetLayer()==obj.GetLayer()) and Phys.Collide(obj, object):
					return True
		return False
	_loc_id=None
	_sprite=None
	_objects = None
	_objects_count=0
	_width = 0
	_height = 0
