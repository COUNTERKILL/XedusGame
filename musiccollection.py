import iniFile as ini
import sfml as sf
import random
class MusicCollection:
    def __init__(self,IniPath):
        IniReader=ini.IniFile(IniPath)
        groups_count=IniReader.ReadInt("music","groups_count")
        music_index=0
        for i in range(0,groups_count):
            music_count=IniReader.ReadInt("group"+str(i),"music_count")
            Music={}
            for j in range(0,music_count):
                Music[IniReader.ReadString("music"+str(music_index),"name")] \
                =sf.Music.from_file\
                (IniReader.ReadString("music"+str(music_index),"path")) 
                music_index+=1
            self._collection[IniReader.ReadString("group"+str(i),"name")]=Music
    def GetMusicByName(self,name):
        for key in self._collection.keys():
            if name in self._collection[key].keys():
                return self._collection[key][name]
    def GetRandomInGroup(self,group):
        return random.choice(self._collection[group].values())
    def AddMusic(self,group,name,path):
        self._collection[group][name]=sf.Music.from_file(path)
    _collection={}

        
        
musicCollection = MusicCollection("configs\\music.ini")
        
        
    
