class MusicalNote:
    def __init__(self,name,pitch):
        self.__name=name
        self.__pitch=pitch

    @property
    def name(self):
        return self.__name
    
    # @name.setter
    # def name(self,name):
    #     raise AttributeError("Can't set attribute")
    
    @property
    def pitch(self):
        return self.__pitch
    
    # @pitch.setter
    # def pitch(self,pitch):
    #     raise AttributeError("Can't set attribute")
    
note=MusicalNote("a4",440)
print(note.name)
print(note.pitch)
# note.name="b4"
# note.pitch=450