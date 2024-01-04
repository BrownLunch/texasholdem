"""
テキサスホールデム役判定プログラム(カードは1組[52枚]想定)
TODO:ゲームの進行をマネジメントするプログラム, CPUの行動アルゴリズム(bet額設定のアルゴリズム),  オンライン機能の追加, ログイン機能の追加
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
      r = []
      for _ in range(num):
         c = self.pop()
         r.append(c.suit + c.rank)
      return r

# ロイヤルストレートを判定する関数
def royal_straight_flash(d_cards):
   return check_req(d_cards, "SA SK SQ SJ ST") > 0 or check_req(d_cards, "HA HK HQ HJ HT") > 0\
   or check_req(d_cards, "DA DK DQ DJ DT") > 0 or check_req(d_cards, "CA CK CQ CJ CT") > 0

# ペアを作成する関数
def create_pairs(d_cards):
   pairs = []
   for score, rank in zip(scores, ranks):
      n = " ".join(d_cards).count(rank)
      if n > 1:
         pairs += [(n, score)]
   return sorted(pairs, key=lambda x:(x[0], x[1]), reverse=True)

# キッカーを作成する関数
def create_kickers(d_cards, suit=""):
   kickers = []
   for score, rank in zip(scores, ranks):
      if " ".join(d_cards).count(suit + rank) > 0:
         kickers.append(score)
   return kickers

#ストレートフラッシュを判定する関数
def straight_flash(d_cards):
   for i in range(9):
      for suit in suits:
         score = check_req(d_cards, [suit + rank for suit, rank in zip(suit*5, ranks[i:i + 5])])
         if score > 0:       
            return score
   else:
      for suit in suits:
         if check_req(d_cards, [suit + rank for suit, rank in zip(suit*5, ranks[-4:] + ranks[:1])]) > 0:
            return 5
      else:
         return 0
  
#フラッシュを判定する関数
def flash(d_cards):
   for suit in suits:
      if " ".join(d_cards).count(suit) > 4:
         return create_kickers(d_cards, suit)
   return 0

#ストレートを判定する関数
def straight(d_cards):
   for i in range(9):
      score = check_req(d_cards, ranks[i: i + 5])
      if score > 0:
         return score
   else:
      if check_req(d_cards, ranks[-4:] + ranks[:1]) > 0:
         return 5
      else:
         return 0

#　役を完成させるために必要なカードが入っているかを判定する関数
def check_req(d_cards, req_cards):
   for req_card in req_cards:
      if " ".join(d_cards).count(req_card) == 0:
         return 0
   return cal_score(req_cards)

# スコアを計算する関数
def cal_score(cal_cards, suit=""):
   for score, rank in zip(scores, ranks):
      if " ".join(cal_cards).count(suit + rank) > 0:
         return score
   return 0

#引数に入れられたカードの役とスコアを返す関数
def cards_score(d_cards):
   pairs = create_pairs(d_cards) + [(0, 0)]
   checkrank = dict(zip(scores, ranks))
   #ロイヤルストレートフラッシュ
   if royal_straight_flash(d_cards): 
      return ["ロイヤルストレートフラッシュ", 1000]
   #ストレートフラッシュ
   score = straight_flash(d_cards)
   if score > 0:
      return ["ストレートフラッシュ", 900 + score]
   #フォーカード
   if pairs[0][0] == 4:
      return ["フォーカード", 800 + pairs[0][1]]
   #フルハウス
   if pairs[0][0] == 3:
      if len(pairs) > 2:
         return ["フルハウス", 700 + pairs[0][1]]
   #フラッシュ
   if flash(d_cards):
      result = ["フラッシュ"] + [x + 600 for x in flash(d_cards)]
      return result
   #ストレート
   score = straight(d_cards)
   if score > 0:
      return ["ストレート", 500 + score]
   #スリーカード
   if pairs[0][0] == 3:
      return ["スリーカード", 400 + pairs[0][1]]
   #ツーペア
   if len(pairs) > 2:
      d_cards = [x for x in d_cards if (checkrank[pairs[0][1]] not in x) and (checkrank[pairs[1][1]] not in x)]
      return (["ツーペア", 300 + pairs[0][1], 300 + pairs[1][1]] + create_kickers(d_cards))[:4]
   #ワンペア
   if len(pairs) > 1:
      d_cards = [x for x in d_cards if checkrank[pairs[0][1]] not in x]
      return (["ワンペア", 200 + pairs[0][1]] + create_kickers(d_cards))[:5]
   #ハイカード  
   return (["ハイカード"] + create_kickers(d_cards))[:6]

# テストケース
def test():
   print("ロイヤルストレートフラッシュ：", cards_score(["SA", "SK", "SQ", "SJ", "ST", "S9"]))
   print("ストレートフラッシュ：", cards_score(["H2", "H3", "H4", "H5", "HA", "DT", "H8"]))
   print("フォーカード：", cards_score(["SK", "HK", "DK", "CK", "S9", "HT", "D3"]))
   print("フルハウス：", cards_score(["S9", "D9", "H9", "H5", "D5", "H3"]))
   print("フラッシュ：", cards_score(["HA", "H5", "H2", "HT", "H9", "DT", "D4"]))
   print("ストレート：", cards_score(["H2", "D3", "C4", "H5", "S6", "DT"]))
   print("スリーカード：", cards_score(["H2", "D3", "C2", "H5", "S2", "DT"]))
   print("ツーペア：", cards_score(["H2", "D3", "C2", "H5", "S3", "D5", "HK"]))
   print("ワンペア：", cards_score(["H2", "D3", "C2", "H5", "S9", "DT"]))
   print("ハイカード：", cards_score(["H2", "D8", "HA", "DT", "S3", "H9"]))


      
if __name__ == "__main__":
   # deck = Deck()
   # num = 2
   # p1 = deck.deal(2)
   # p2 = deck.deal(2)
   # com = deck.deal(5)
   # print(p1 + com, cards_score(p1 + com))
   # print(p2 + com, cards_score(p2 + com))
   # if cards_score(p1 + com)[1] > cards_score(p2 + com)[1]:
   #    print("プレイヤー１の勝利")
   # else:
   #    print("プレイヤー２の勝利")
   test()
  