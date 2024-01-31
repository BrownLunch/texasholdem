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

   def deal_card(self, num):
      dealcard = []
      for _ in range(num):
         popcard = self.pop()
         dealcard.append(popcard.suit + popcard.rank)
      return dealcard

class Player:
   def __init__(self, name, stack):
      self.name = name      
      self.stack = stack
      self.hand = []
      self.bet = 0
      self.status = "Alive" #プレイヤーが対戦中かすでに負けているか(Alive, Defeted)を管理するプロパティ
      self.action = "" #プレイヤーのアクション(call, raise, fold, allin, check)を管理するプロパティ

   def receive_hand(self, cards):
      self.hand = cards

   def __str__(self):
      return f"プレイヤー情報 name:{self.name} stack:{self.stack} bet:{self.bet} status:{self.status} hand:{self.hand}"
      

class Table:
   def __init__(self, sb, bb, playerlimit):
      self.sb = sb                           #スモールブラインドを設定
      self.bb = bb                           #ビッグブラインドを設定
      self.playerlimit = playerlimit         #人数上限を設定
      self.pot = 0                           #初期ポットを設定   
      self.community = []                    #コミュニティカード配列を設定
      self.players = []                      #プレイヤー情報を格納する配列

   def __str__(self) -> str:
      return f"テーブル情報 SB:{self.sb} BB:{self.bb} コミュニティカード:{self.community} 人数制限:{self.playerlimit} POT:{self.pot} プレイヤー:{self.players}"

   # テーブルにプレイヤーを追加するメソッド
   def add_player(self, player):
      if self.playerlimit > len(self.players):
         self.players.append(player)
      else:
         print("人数上限に達しました。")

   def recieve_community(self, cards):
      self.community.extend(cards)

   # ベッティングラウンド
   def bettinground(self, startpos):
      pass

   # プリフロップ
   def prefrop(self, opencard):
      self.recieve_community(opencard)
      self.bettinground()

   # フロップ
   def frop(self, opencard):
      self.recieve_community(opencard)
      self.bettinground()

   # ターン
   def turn(self, opencard):
      self.recieve_community(opencard)
      self.bettinground()


   # リバー
   def river(self, opencard):
      self.recieve_community(opencard)
      self.bettinground()

   #ショーダウン
   def show_down(self, players):
      pass


if __name__ == "__main__":
   d = Deck()
   t1 = Table(50, 100, 6)
   p1 = Player("一郎", 10000)
   p2 = Player("次郎", 10000)
   t1.add_player(p1)
   t1.add_player(p2)
   p1.receive_hand(d.deal_card(2))
   p2.receive_hand(d.deal_card(2))
   print(p1)
   print(p2)
   print(t1)
   



