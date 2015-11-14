import sfml as sf
import time
import IniFile as ini
import Object as obj
import Animation as ani

class AnimatedObject(obj.Object):
	def __init__(self,ObjIniPath):
		obj.Object.__init__(self, ObjIniPath)
		load=ini.IniFile(ObjIniPath)
		animation_count=load.ReadInt("animation","count")
		frameInd = 0
		for j in range(0, animation_count):
			frames_count=load.ReadInt("animation"+str(j),"frames_count")
			animation=ani.Animation(load.ReadFloat("animation"+str(j),"frame_time"),load.ReadString("animation"+str(j),"name"))
			animation.frame_width=load.ReadInt("animation","frame_width")
			animation.frame_height=load.ReadInt("animation","frame_height")
			animation.SetSpriteTexture(self._sprite)
			for i in range(0, frames_count):
				animation.AddFrame(sf.Rectangle(sf.Vector2(load.ReadInt("frame"+str(frameInd),"pos_x"), load.ReadInt("frame"+str(frameInd),"pos_y")), sf.Vector2(animation.frame_width,animation.frame_height)))
				frameInd+=1
			self._animations[animation.name]=animation
		self._currentAnimation=self._animations[load.ReadString("animation"+str(0),"name")]
	def SetAnimation(self,name):
		self._currentAnimation=self._animations[name]
	def draw(self, target, state):
		self._sprite.position=sf.Vector2(self._position.x,self._position.y)
		self._sprite.texture_rectangle=self._currentAnimation.GetFrame()
		target.draw(self._sprite,state)
	def StopAnimate(self):
		self._currentAnimation.Stop()
	def StartAnimate(self):
		self._currentAnimation.Start()
	_rotationAngle = 0
	_animations={}
	_currentAnimation = None
        
    
if __name__=="__main__":
        anim=AnimatedObject("locations\\test_loc\\objects\\test_obj_animated_electra.ini")
        window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
        view = sf.View()
        view.reset(sf.Rectangle((0, 0), (640, 480)))
        window.view = view
        # start the game loop
        while window.is_open:
                # process events
                for event in window.events:
                        # close window: exit
                        if type(event) is sf.CloseEvent:
                                window.close()
                        if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
                                view.move(-1, 0)
                        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
                                view.move(1, 0)
                        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
                                view.move(0, -1)
                        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
                                view.move(0, 1)
                window.clear() # clear screen
                window.draw(anim)
                window.display() # update the window 
                          

                                        





