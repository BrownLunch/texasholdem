from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
from texasholdem  import ROOMS, Table, Player, Player_encoder, Table_encoder
from random import choice
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = "pokerio"
socketio = SocketIO(app)  

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("menu")
def handle_menu():
    emit("menu")

@socketio.on("create_room")
def create(data):
    roomno = choiceroomno()
    ROOMS.append(Table(50, 100, int(data["chip"]), int(data["maxplayers"]), roomno))
    emit("echo_create_room", {"createroomno":roomno, "stack":int(data["chip"]), "username":data["username"]})

@socketio.on("join_room")
def join(data):
    iroomno = data["roomno"]

    #検索した部屋が存在していたら入室する
    for i in range(len(ROOMS)):
        if ROOMS[i].roomno == iroomno:
            #部屋に入室
            join_room(ROOMS[i].roomno, request.sid)
            print(data["host"])

            #プレイヤーオブジェクトを作成し、参加させる
            pls = Player(data["username"], request.sid)
            pls.host = data["host"]
            ROOMS[i].add_player(pls)

            # json形式に書き換え
            room = json.dumps(ROOMS[i], default=Table_encoder)
            players = json.dumps(ROOMS[i].players, default=Player_encoder)

            emit("echo_join_room", {"room": room, "players":players}, room=ROOMS[i].roomno)
            break
    else:
        emit("message", "部屋が見つかりませんでした。")

@socketio.on("leave_room")
def leave():
    pass

@socketio.on("start_game")
def start(data):
    #部屋を検索
    rm = searchroom(data["roomno"])

    #BTN(親を決める)
    rm.choose_dealer()

    #sb, bbを払う
    rm.pay_sbbb()

    #カードを生存しているプレイヤー全員に配る
    rm.deal_hand()

    # json形式に書き換え
    room = json.dumps(rm, default=Table_encoder)
    players = json.dumps(rm.players, default=Player_encoder)

    emit("echo_start_game", {"room": room, "players":players}, room=rm.roomno)
    
@socketio.on("preflop")
def preflop(data):
    #部屋を検索
    rm = searchroom(data["roomno"])

    #ラウンドをプリフロップに更新
    rm.round = "preflop"

    #最初に行動を行うプレイヤーを探す(未完成；生存チェック)
    startplayeridx = (rm.bbidx + 1) % len(rm.players)
    startplayer = rm.players[startplayeridx].sessionid

    reqcallamount = rm.maxbet - rm.players[startplayeridx].bet
    reqbetamount = rm.minimumraise - rm.players[startplayeridx].bet

    # json形式に書き換え
    room = json.dumps(rm, default=Table_encoder)
    players = json.dumps(rm.players, default=Player_encoder)
    
    emit("action", {"room":room, "players":players, "reqcallamount":reqcallamount, "reqbetamount": reqbetamount}, room=startplayer)

@socketio.on("bettinground")
def bettinground(data):
    #部屋を検索
    rm = searchroom(data["roomno"])
    #行動したプレイヤーのアクションを記録
    actedplayeridx = rm.search_actedplayeridx(data["sessionid"])
    rm.players[actedplayeridx].action = data["action"]
    #次に行動するプレイヤーを検索

    

def choiceroomno():
    roomnolist = list(range(100000))
    return str(choice(roomnolist)).zfill(5)

def searchroom(roomno):
    rm = ""
    for i in range(len(ROOMS)):
        if ROOMS[i].roomno == roomno:
            rm = ROOMS[i]
            break
    
    return rm


if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)