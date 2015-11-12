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
        for j in range(0, animations_count):
            frames_count=load.ReadInt("animation"+str(j),"frames_count")
            animation=ani(load.ReadInt("animation","frames_time")
            animation.frame_width=load.ReadInt("animation","frames_width")
            animation.frame_height=load.ReadInt("animation","frames_height")
            animation.SetSpriteTexture(self.sprite)
            for i in range(0, frames_count):
			animation.AddFrame(sf.Rectangle
                                           (sf.Vector2(load.ReadInt("frame"+str(i),pos_x),load.ReadInt("frame"+str(i),pos_y)),
                                            sf.Vector2(animation.frame_width,animation.frame_height)))
            self.Animations["animation"+str(j)]=animation
    Animations={}





