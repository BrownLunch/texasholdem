"""
ポーカーのカード、デックの定義を行うプログラムです
"""

import random

# Cardクラスを作成
class Card:
   def __init__(self, suit, rank):
      self.__suit = suit
      self.__rank = rank
   
   def __str__(self) -> str:
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
      random.shuffle(self)

   def deal_card(self, num):
      dealcard = []
      for _ in range(num):
         popcard = self.pop()
         dealcard.append(popcard.suit + popcard.rank)
      return dealcard

class Player:
   def __init__(self, name, sessionid):
      self.__name = name      
      self.__stack = 0
      self.__hand = []
      self.__bet = 0
      self.__status = "Alive"        #プレイヤーが対戦中かすでに負けているか(Alive, Defeted)を管理するプロパティ
      self.__action = ""             #プレイヤーのアクション(call, raise, fold, allin, check)を管理するプロパティ
      self.__sessionid = sessionid
   # nameのゲッター
   def get_name(self):
      return self.__name

   # betする
   def bet(self, amount):
      self.__stack -= amount
      self.__bet += amount

   # 手札を受け取る
   def receive_hand(self, cards):
      self.__hand = cards

   # 管理用
   def __str__(self) -> str:
      return f"name:{self.__name} stack:{self.__stack} bet:{self.__bet} status:{self.__status} hand:{self.__hand} action:{self.__action}"
      

class Table:
   def __init__(self, sb, bb, stack, playerlimit):
      self.__sbamount = sb                     #スモールブラインドを管理
      self.__bbamount = bb                     #ビッグブラインドを管理
      self.__dealeridx = 0                     #ボタンのポジションを管理
      self.__sbidx = 0                         #sbのポジションを管理
      self.__bbidx = 0                         #bbのポジションを管理
      self.__playerlimit = playerlimit         #人数上限を管理
      self.__pot = 0                           #初期ポットを管理   
      self.__community = []                    #コミュニティカード配列を管理
      self.__players = []                      #プレイヤー情報を格納する配列を管理

   # 管理用
   def __str__(self) -> str:
      player_info = "\n".join(str(player) for player in self.__players)
      return f"■テーブル情報\nsb_amount:{self.__sbamount}\nbb_amount:{self.__bbamount}\nBTN:{self.__players[self.__dealeridx].get_name()}\nSB:{self.__players[self.__sbidx].get_name()}\nBB:{self.__players[self.__bbidx].get_name()}\nコミュニティカード:{self.__community}\n人数制限:{self.__playerlimit}\nPOT:{self.__pot}\n■プレイヤー情報\n{player_info}"

   # テーブルにプレイヤーを追加する
   def add_player(self, player):
      if self.__playerlimit > len(self.__players):
         self.__players.append(player)
      else:
         print("人数上限に達しました。")

   #マッチ開始時のBTNを決定する
   def choose_dealer(self):
      self.__dealeridx = random.randint(0, len(self.__players) - 1)
      self.__sbidx = (self.__dealeridx + 1) % len(self.__players)
      self.__bbidx = (self.__dealeridx + 2) % len(self.__players)

   # 強制掛け金を払う
   def pay_sbbb(self):
      self.__players[self.__sbidx].bet(self.__sbamount)
      self.__players[self.__bbidx].bet(self.__bbamount)

   # ゲーム
   def game(self):
      deck = Deck()
      self.preflop(deck)
      self.flop(deck)
      self.turn(deck)
      self.river(deck)
      self.showdown()


   # コミュニティーカードを受け取る
   def recieve_community(self, cards):
      self.__community.extend(cards)

   
   # ベッティングラウンド
   def bettinground(self):
      pass

   # プリフロップ
   def preflop(self, deck):
      #強制掛け金(sb, bb)の支払い
      self.pay_sbbb()

      # ハンドをプレイヤー全員に配る
      for p in self.__players:
         p.receive_hand(deck.deal_card(2))
      self.bettinground()

   # フロップ
   def flop(self, deck):
      self.recieve_community(deck.deal_card(3))
      self.bettinground()

   # ターン
   def turn(self, deck):
      self.recieve_community(deck.deal_card(1))
      self.bettinground()


   # リバー
   def river(self, deck):
      self.recieve_community(deck.deal_card(1))
      self.bettinground()

   #ショーダウン
   def showdown(self):
      pass


if __name__ == "__main__":
   table = Table(50, 100, 6)
   table.add_player(Player("一郎", 10000))
   table.add_player(Player("二郎", 10000))
   table.add_player(Player("三郎", 10000))
   table.add_player(Player("四郎", 10000))
   table.add_player(Player("五郎", 10000))
   table.add_player(Player("六郎", 10000))
   table.choose_dealer()
   table.game()
   print(table)