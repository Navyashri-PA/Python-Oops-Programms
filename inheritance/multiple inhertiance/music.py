class musicplayer:
#<-----user can give values----->
   def __init__(self):
      self.playlist=[]

#    def add_song(self):
#       user_input=input("enter the list of songs seperated by space:")
#       self.playlist=[x for x in user_input.split()]

#<-----we can give vales in obj---->  
#    def __init__(self,playlist=None):
#       if playlist==None:
#          self.playlist=[]
#       else:
#          self.playlist=playlist

#<---to add to an existing list--->
   def add_song(self,song):
        # self.playlist.extend(song)
        # self.playlist.append(song)#<--don't use append it adds value as list-->

# music=musicplayer(["s1","s2"])
music=musicplayer()
music.add_song(["23","aa"])
print(music.playlist)
