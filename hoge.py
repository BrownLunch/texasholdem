from random import shuffle

class Card:

   def __init__(self, suit, number):
      self.__suit = suit
      self.__number = number
   
   @property
   def suit(self):
      return self.__suit
   
   @property
   def number(self):
      return self.__number
   
class Deck(list):

   def __init__(self):
      super().__init__(
         Card(suit, number) for suit in suits for number in range(1, 14)
      )
      self.shuffle()

   def shuffle(self):
      shuffle(self)

   def draw(self):
      return self.pop()

suits = ["s", "h", "d", "c"]

def Determine():
   pass

deck = Deck()

