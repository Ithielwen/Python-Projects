class Display:
  #The images for the different levels, showing the player how many guesses they have left
    _jumper_pics = ["""
  ___
 /___\ 
 \   /
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """

 /___\ 
 \   /
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """

 /___ 
 \   /
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """

 / 
 \   /
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """
 
 \   /
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """
 
 \   
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """
  
  \ /
   O
  /|\ 
  / \ 

^^^^^^^""", """

  \ 
   O
  /|\ 
  / \ 

^^^^^^^""", """

   X
  /|\ 
  / \ 

^^^^^^^"""]

  #Initialize the class with the word being used to play
    def __init__(self):
        self._incorrectCount = 0

    #Getters

    #Returns the jumper pic based on the number of incorrect guesses the player has
    def get_display_image(self):
      return self._jumper_pics[self._incorrectCount]

    def get_guesses_left(self):
      return 8 - self._incorrectCount

    #Setters

    #Add one to the number of incorrect guesses
    def add_incorrect_letter(self):
      self._incorrectCount+=1