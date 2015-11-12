import sfml as sf
class Animation:
    def AddFrame(self,rect):
        frames.Append(rect)
    def GetFrame(self):
        return frames
    def SetSpriteTexture(self,texture):
        self.texture=texture
    def GetSpriteTexture(self):
        return texture
    frames=[]
    texture=None


