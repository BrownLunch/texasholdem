"""
ポーカーのカード、デックの定義を行うプログラムです
"""

import random
from determine import cards_score

ROOMS = []

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
      self.__status = "Active"       #プレイヤーが対戦中かすでに負けているか(Active, Defeted)を管理するプロパティ
      self.__action = ""             #プレイヤーのアクション(call, raise, fold, allin, check)を管理するプロパティ
      self.__sessionid = sessionid   #セッションIDを管理するプロパティ
   
   @property
   def name(self):
      return self.__name
   
   @property
   def stack(self):
      return self.__stack
   
   @property
   def hand(self):
      return self.__hand
   
   @property
   def bet(self):
      return self.__bet
   
   @property
   def status(self):
      return self.__status
   
   @property
   def action(self):
      return self.__action
   
   @property
   def sessionid(self):
      return self.__sessionid
   
   @name.setter
   def name(self, value):
      self.__name = value

   @stack.setter
   def stack(self, value):
      self.__stack = value

   @hand.setter
   def hand(self, value):
      self.__hand = value

   @bet.setter
   def bet(self, value):
      self.__bet = value

   @status.setter
   def status(self, value):
      self.__status = value

   @action.setter
   def action(self, value):
      self.__action = value

   @sessionid.setter
   def sessionid(self, value):
      self.__sessionid = value
                            
   # ベットする
   def betting(self, betamount):
      self.stack -= betamount
      self.bet += betamount

   # 手札を受け取る
   def receive_hand(self, cards):
      self.__hand = cards

   # 管理用
   def __str__(self) -> str:
      return f"name:{self.name} stack:{self.stack} bet:{self.bet} status:{self.status} hand:{self.hand} action:{self.action} sessionid:{self.sessionid}"
      
class Table:
   
   def __init__(self, sb, bb, stack, maxplayers, roomno):
      self.__sbamount = sb                     #スモールブラインドを管理
      self.__bbamount = bb                     #ビッグブラインドを管理
      self.__stack = stack                     #スタックを管理
      self.__maxplayers = maxplayers           #人数上限を管理
      self.__dealeridx = 0                     #ボタンのポジションを管理
      self.__sbidx = 0                         #sbのポジションを管理
      self.__bbidx = 0                         #bbのポジションを管理
      self.__pot = 0                           #初期ポットを管理
      self.__minimumraise = 0                  #ミニマムレイズを管理
      self.__community = []                    #コミュニティカード配列を管理
      self.__players = []                      #プレイヤー情報を格納する配列を管理
      self.__deck = Deck()                     #山札を管理
      self.__roomno = roomno                   #ルームナンバーを管理

   @property
   def sbamount(self):
      return self.__sbamount
   
   @property
   def bbamount(self):
      return self.__bbamount
   
   @property
   def stack(self):
      return self.__stack
   
   @property
   def maxplayers(self):
      return self.__maxplayers
   
   @property
   def dealeridx(self):
      return self.__dealeridx
   
   @property
   def sbidx(self):
      return self.__sbidx
   
   @property
   def bbidx(self):
      return self.__bbidx
   
   @property
   def pot(self):
      return self.__pot
   
   @property
   def minimumraise(self):
      return self.__minimumraise
   
   @property
   def community(self):
      return self.__community
   
   @property
   def players(self):
      return self.__players
   
   @property
   def deck(self):
      return self.__deck
   
   @property
   def roomno(self):
      return self.__roomno
   
   @sbamount.setter
   def sbamount(self, value):
      self.__sbamount = value

   @bbamount.setter
   def bbamount(self, value):
      self.__bbamount = value

   @stack.setter
   def stack(self, value):
      self.__stack = value

   @maxplayers.setter
   def maxplayers(self, value):
      self.__maxplayers = value

   @dealeridx.setter
   def dealeridx(self, value):
      self.__dealeridx = value

   @sbidx.setter
   def sbidx(self, value):
      self.__sbidx = value

   @bbidx.setter
   def bbidx(self, value):
      self.__bbidx = value

   @pot.setter
   def pot(self, value):
      self.__pot = value

   @pot.setter
   def minimumraise(self, value):
      self.__pot = value

   @community.setter
   def community(self, value):
      self.__community = value

   @players.setter
   def players(self, value):
      self.__players = value

   @deck.setter
   def deck(self, value):
      self.__deck = value

   @roomno.setter
   def roomno(self, value):
      self.__roomno = value

   # 管理用
   def __str__(self) -> str:
      player_info = "\n".join(str(player) for player in self.players)
      return f"■テーブル情報\nroomno:{self.roomno}\nsb_amount:{self.sbamount}\nbb_amount:{self.bbamount}\nBTN:{self.players[self.dealeridx].name}\nSB:{self.players[self.sbidx].name}\nBB:{self.players[self.bbidx].name}\n初期スタック{self.stack}\n人数制限:{self.maxplayers}\nコミュニティカード:{self.community}\nPOT:{self.pot}\n■プレイヤー情報\n{player_info}"

   # テーブルにプレイヤーを追加する
   def add_player(self, player):
      if self.maxplayers > len(self.players):
         self.players.append(player)
         player.stack = self.stack
      else:
         print("人数上限に達しました。")

   #マッチ開始時のBTNを決定する
   def choose_dealer(self):
      self.dealeridx = random.randint(0, len(self.players) - 1)
      self.sbidx = (self.dealeridx + 1) % len(self.players)
      self.bbidx = (self.dealeridx + 2) % len(self.players)

   # 強制掛け金を払う
   def pay_sbbb(self):
      self.players[self.sbidx].betting(self.sbamount)
      self.players[self.bbidx].betting(self.bbamount)

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
      self.community.extend(cards)

   
   # ベッティングラウンド
   def bettinground(self):
      pass

   # プリフロップ
   def preflop(self, deck):
      #強制掛け金(sb, bb)の支払い
      self.pay_sbbb()

      # ハンドをプレイヤー全員に配る
      for p in self.players:
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
      winneridx = 0
      for i in range(self.maxplayers):
         if self.players[i].status == "Active":
            if cards_score(self.players[winneridx].hand + self.community)[1:] < cards_score(self.players[i].hand + self.community)[1:]:
               winneridx = i
      print(f"{self.players[winneridx].name}の勝利!!!")
   

if __name__ == "__main__":
   table = Table(50, 100, 10000, 6)
   table.add_player(Player("一郎"))
   table.add_player(Player("二郎"))
   table.add_player(Player("三郎"))
   table.add_player(Player("四郎"))
   table.add_player(Player("五郎"))
   table.add_player(Player("六郎"))
   table.choose_dealer() 
   table.game()
   print(table)