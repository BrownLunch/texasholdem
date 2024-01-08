"""
ポーカーのカード、デックの定義を行うプログラムです
"""

from random import shuffle

# トランプのマーク：右からスペード、ハート、ダイヤ、クラブ
suits = ["S", "H", "D", "C"]

# トランプの数字：右からA(エース)、K(キング)、Q(クイーン)、J(ジャック)、10, 9, 8, 7, 6, 5, 4, 3, 2)
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# トランプの数字のスコア：Aが一番高く2が一番低い
scores = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

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

   def __init__(self):
      super().__init__(
         Card(suit, rank) for suit in suits for rank in ranks
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