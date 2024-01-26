from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = "nkpoker"
socketio = SocketIO(app)  

@app.route("/")
def index():
    html = """<div id="title-container"> 
        <div class="title">
            <img id="title-img" src="../static/images/title.png" alt="タイトル">
        </div>
        <div class="title-nav">
            <img id="title-nav-img" src="../static/images/clickanywhere.png" alt="クリックしてください">
        </div>   
    </div>             
    <video id=switchingbg preload="auto" poster="../static/images/titlebg.png">
        <source src="../static/switchingbg.mp4" type="video/mp4">
    </video>
    <div class="menubg">
    <div class="left-container">
    </div>
    <div class="right-container">
        <div class="btn-container">
            <img class="btn" src="../static/images/rankmatch.png" alt="ランクマッチ">
            <img class="btn" id="friendmatch-btn" src="../static/images/friendmatch.png" alt="フレンドマッチ">
            <img class="btn" src="../static/images/training.png" alt="トレーニング">
        </div>  
    </div>            
</div>"""
    return render_template("index.html", html=html)

if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)