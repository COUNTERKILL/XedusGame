import sfml as sf
import time
import IniFile as ini
import Object as obj
import Animation as ani

class AnimationObject(obj.Object):
    def __init__(self,ObjIniPath):
        obj.Object.__init__(self,ObjIniPath)
        load=ini.IniFile(ObjIniPath)
        animation_count=load.ReadInt("animation","count")
        for j in range(0, animation_count):
            frames_count=load.ReadInt("animation"+str(j),"frames_count")
            animation=ani.Animation(load.ReadFloat("animation"+str(j),"frame_time"),
                                    load.ReadString("animation"+str(j),"name"))
            animation.frame_width=load.ReadInt("animation","frame_width")
            animation.frame_height=load.ReadInt("animation","frame_height")
            animation.SetSpriteTexture(self.sprite)
            for i in range(0, frames_count):
                animation.AddFrame(sf.Rectangle
                (sf.Vector2(load.ReadInt("frame"+str(i),"pos_x"),
                                        load.ReadInt("frame"+str(i),"pos_y")),
                             sf.Vector2(animation.frame_width,animation.frame_height)))
                self.Animations[animation.name]=animation
        self.CurrentAnimation=self.Animations[load.ReadString("animation"+str(0),"name")]
    Animations={}
    def draw(self, target, state):
        self.sprite.position=sf.Vector2(self.position.x,self.position.y)
        self.sprite.texture_rectangle=self.CurrentAnimation.GetFrame()
        target.draw(self.sprite,state)
        
    
if __name__=="__main__":
    anim=AnimationObject("C:\\Users\\User\\Desktop\\Repository\\Repository\\locations\\test_loc\\objects\\test_obj_animated_electra.ini")
window = sf.RenderWindow(sf.VideoMode(640, 480), "pySFML Window")
view = sf.View()
view.reset(sf.Rectangle((100, 100), (640, 480)))
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
    while(True):
            time.sleep(1)
            window.draw(anim) # draw the sprite
     # draw the string
    # set the default view back
    #window.view = window.default_view
    window.display() # update the window 
          

                





