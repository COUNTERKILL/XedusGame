import sfml as sf

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
    def __init__(self,texture,width,height):
        self.width=width
        self.height=height
        self.texture=texture
        sf.Drawable.__init__(self)
    position=Position(0,0)
    obj_id=None
    type_interatction=None
    type_logic=None
    texture=sf.Texture
    def setposition(self,pos):
        self.position=pos;
    def getposition(self):
        return self.position


