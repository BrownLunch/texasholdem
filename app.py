from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = "nkpoker"
socketio = SocketIO(app)  

@app.route("/")
def index():
    html = """<div id="bg">
                <div id="title-container"> 
                    <div class="title">
                        <img id="title-img" src="../static/images/title.png" alt="タイトル">
                    </div>
                    <div class="title-nav">
                        <img id="title-nav-img" src="../static/images/clickanywhere.png" alt="クリックしてください">
                    </div>   
                </div>             
            </div>"""
    return render_template("index.html", html=html)

#クライアントとのコネクション確立
@socketio.on('connect')
def handle_connect():
    emit('client_echo',{'msg': 'server connected!'})


#クライアントからのメッセージを出力する関数
@socketio.on('server_echo')
def handle_server_echo(msg):
    print('echo: ' + str(msg))


if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)