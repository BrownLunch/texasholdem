from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import texasholdem 
app = Flask(__name__)
app.config['SECRET_KEY'] = "pokerio"
socketio = SocketIO(app)  

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("menu")
def handle_menu():
    emit("menu")

@socketio.on("join")
def join_room():
    pass

if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)