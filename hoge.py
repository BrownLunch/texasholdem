from random import shuffle

suits = ["S", "H", "D", "C"]
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

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
   
class Deck(list):

   def __init__(self):
      super().__init__(
         Card(suit, rank) for suit in suits for rank in ranks
      )
      self.shuffle()

   def shuffle(self):
      shuffle(self)

   def deal(self, num):
      return [self.pop().suit + self.pop().rank for _ in range(num)]

def royal_straight_flash(d_cards):
   return all_in(d_cards, ["SA", "SK", "SQ", "SJ", "ST"]) > 0 or all_in(d_cards, ["HA", "HK", "HQ", "HJ", "HT"]) > 0\
   or all_in(d_cards, ["DA", "DK", "DQ", "DJ", "DT"]) > 0 or all_in(d_cards, ["CA", "CK", "CQ", "CJ", "CT"]) > 0

def create_pairs(d_cards):
   r = []
   for rank in ranks:
      n = d_cards.count(rank)
      if n > 1:
         r += [(n, rank)]
   return sorted(r)

def straight_flash(d_cards):
   req_cards = ranks + ["A"]
   for i in range(10):
      for suit in suits:
         score = all_in(d_cards, " ".join(s + r for s, r in zip(suit*5, req_cards[i:i+5])))
      if score > 0:
         return score
      return False
   
def flash(d_cards):
   for suit in suits:
      if d_cards.count(suit) > 4:
         return score(d_cards, suit)
   return 0

def straight(d_cards):
   req_cards = ranks + ["A"]
   for i in range(10):
      score = all_in(d_cards, " ".join(req_card for req_card in req_cards[i: i + 5]))
      if score > 0:
         return score
      return 0

def all_in(d_cards, req_cards):
   for req_card in req_cards:
      if d_cards.count(req_card) == 0:
         return 0
   return score(req_cards)

def score(s, m=""):
   for score, rank in zip([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2], ranks):
      if s.count(rank + m) in s:
         return score
      return 0

def cards_score(d_cards):
   pairs = create_pairs(d_cards) + [(0, 0)]
   #ロイヤルストレートフラッシュ
   if royal_straight_flash(d_cards): 
      return 1000
   #ストレートフラッシュ
   score = straight_flash(d_cards)
   if score > 0:
      return 900 + score
   #フォーカード
   if pairs[0][0] == 4:
      return 800 + pairs[0][1]
   #フルハウス
   if pairs[0][0] == 3:
      if len(pairs) > 2:
         return 700 + pairs[0][1]
   #フラッシュ
   score = flash(d_cards)
   if score > 0:
      return 600 + score
   #ストレート
   score = straight(d_cards)
   if score > 0:
      return 500 + score
   #スリーカード
   if pairs[0][0] == 3:
      return 400 + int(pairs[0][1])
   #ツーペア
   if len(pairs)>2:
      return 300 + int(pairs[0][1])
   #ワンペア
   if len(pairs)>1:
      return 200 + int(pairs[0][1])
   #ハイカード
   return score(d_cards)
      
deck = Deck()
num = 7
cards = deck.deal(num)
print(cards)
print(cards_score(" ".join(cards)))
