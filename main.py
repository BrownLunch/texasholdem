"""
テキサスホールデム役判定プログラム
TODO: CPU作成, オンラインゲーム作成
"""

from random import shuffle

suits = ["S", "H", "D", "C"]
ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
scores = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

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
      r = []
      for _ in range(num):
         c = self.pop()
         r.append(c.suit + c.rank)
      return r

def royal_straight_flash(d_cards):
   return check_req(d_cards, "SA SK SQ SJ ST") > 0 or check_req(d_cards, "HA HK HQ HJ HT") > 0\
   or check_req(d_cards, "DA DK DQ DJ DT") > 0 or check_req(d_cards, "CA CK CQ CJ CT") > 0

def create_pairs(d_cards):
   r = []
   for score, rank in zip(scores, ranks):
      n = d_cards.count(rank)
      if n > 1:
         r += [(n, score)]
   return sorted(r, key=lambda x:(x[0], x[1]), reverse=True)

def straight_flash(d_cards):
   req_cards = ranks + ["A"]
   for i in range(10):
      for suit in suits:
         score = check_req(d_cards, list(s + r for s, r in zip(suit*5, req_cards[i:i + 5])))
         if score > 0:       
            return score
   return 0
   
def flash(d_cards):
   for suit in suits:
      if d_cards.count(suit) > 4:
         return cal_score(d_cards, suit)
   return 0

def straight(d_cards):
   req_cards = ranks + ["A"]
   for i in range(10):
      score = check_req(d_cards, "".join(req_card for req_card in req_cards[i: i + 5]))
      if score > 0:
         return score
   return 0

def check_req(d_cards, req_cards):
   for req_card in req_cards:
      if d_cards.count(req_card) == 0:
         return 0
   return cal_score(req_cards)

def cal_score(d_cards, m=""):
   if isinstance(d_cards, list):
      d_cards = " ".join(d_cards)
   for score, rank in zip(scores, ranks):
      if d_cards.count(m + rank) > 0:
         return score
   return 0

def cards_score(d_cards):
   d_cards = " ".join(d_cards)
   pairs = create_pairs(d_cards) + [(0, 0)]
   #ロイヤルストレートフラッシュ
   if royal_straight_flash(d_cards): 
      return "ロイヤルストレートフラッシュ", 1000
   #ストレートフラッシュ
   score = straight_flash(d_cards)
   if score > 0:
      return "ストレートフラッシュ", 900 + score
   #フォーカード
   if pairs[0][0] == 4:
      return "フォーカード", 800 + pairs[0][1]
   #フルハウス
   if pairs[0][0] == 3:
      if len(pairs) > 2:
         return "フルハウス", 700 + pairs[0][1], 700 + pairs[1][1]
   #フラッシュ
   score = flash(d_cards)
   if score > 0:
      return "フラッシュ", 600 + score
   #ストレート
   score = straight(d_cards)
   if score > 0:
      return "ストレート", 500 + score
   #スリーカード
   if pairs[0][0] == 3:
      return "スリーカード", 400 + pairs[0][1]
   #ツーペア
   if len(pairs) > 2:
      return "ツーペア", 300 + pairs[0][1]
   #ワンペア
   if len(pairs) > 1:
      return "ワンペア", 200 + pairs[0][1]
   #ハイカード
   return "ハイカード", cal_score(d_cards)

def test():
   print("ロイヤルストレートフラッシュ：", cards_score(["SA", "SK", "SQ", "SJ", "ST", "S9"]))
   print("ストレートフラッシュ：", cards_score(["H2", "H3", "H4", "H5", "H6", "H7", "H8"]))
   print("フォーカード：", cards_score(["SK", "HK", "DK", "CK"]))
   # print("フルハウス：", cards_score(["", "", "", "", ""]))
      
if __name__ == "__main__":
   deck = Deck()
   num = 7
   cards = deck.deal(num)
   # print(cards)
   # print(cards_score(cards))
   test()
  