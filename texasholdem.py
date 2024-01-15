"""
ポーカーのカード、デックの定義を行うプログラムです
"""

from random import shuffle

# Cardクラスを作成
class Card:

   def __init__(self, suit, rank):
      self.__suit = suit
      self.__rank = rank
   
   def __str__(self):
      return f"{self.__suit}{self.__rank}"
   
   @property
   def suit(self):
      return self.__suit
   
   @property
   def rank(self):
      return self.__rank

# CardクラスからDeckクラスを作成  
class Deck(list):
   suits = ["S", "H", "D", "C"]
   ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
   scores = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

   def __init__(self):
      super().__init__(
         Card(suit, rank) for suit in __class__.suits for rank in __class__.ranks
      )
      self.shuffle()

   def shuffle(self):
      shuffle(self)

   def deal(self, num):
      dealcards = []
      for _ in range(num):
         popcard = self.pop()
         dealcards.append(popcard.suit + popcard.rank)
      return dealcards
   
class Player:
   def __init__(self, name, stack):
      self.name = name
      self.stack = stack
      self.hand = []



class Table:
   def __init__(self, sb, bb, playerlimit):
      self.sb = sb
      self.bb = bb
      self.playerlimit = playerlimit
      self.pot = 0     
      self.players = []

   def add_player():
      pass

   def start_game():
      pass



