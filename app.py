from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room
from texasholdem  import ROOMS, Table, Player
from random import choice
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
    emit("after_create_room", {"createroomno":roomno})

@socketio.on("join_room")
def join(data):
    iroomno = data["roomno"]

    #検索した部屋が存在していたら入室する
    for i in range(len(ROOMS)):
        if ROOMS[i].roomno == iroomno:
            join_room(ROOMS[i].roomno, request.sid)
            ROOMS[i].add_player(Player(data["username"], request.sid))
            emit("after_join_room", {"roomno": ROOMS[i].roomno, "username":data["username"]}, room=ROOMS[i].roomno)
            break
    else:
        emit("message", "部屋が見つかりませんでした。")

@socketio.on("leave_room")
def leave():
    pass

@socketio.on("start_game")
def start(data):
    rm = ""
    for i in range(len(ROOMS)):
        if  ROOMS[i].roomno == data["roomno"]:
            rm = ROOMS[i]
            break
    else:
        print("部屋が削除されました。")

    #BTN(親を決める)
    rm.choose_dealer()

    #sb, bbを払う
    rm.pay_sbbb()

    #カードを生存しているプレイヤー全員に配る
    rm.deal_hand()

    print(rm)

    emit("")
    

def choiceroomno():
    roomnolist = list(range(100000))
    return str(choice(roomnolist)).zfill(5)

if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)