#challenge 2.2

#define the base class player
class Player:
  def play(self):
      print("The player is playing cricket.")

#define the derived class Batsman
class Batsman(Player):
  def play(self):
      print("The batsman is batting.")

#define the derived class Bowler
class Bowler:
  def play(self):
      print("The bowler is bowling.")

#create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play( ) method for each object
batsman.play()
bowler.play()