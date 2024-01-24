from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = "nkpoker"
socketio = SocketIO(app)


@app.route("/")
def index():
    html = '''<div id="title-bg">
                <div id="title-container"> 
                    <div class="title">
                        <img id="title-img" src="../static/images/title.png" alt="タイトル">
                    </div>
                    <div class="title-nav">
                        <img id="title-nav-img" src="../static/images/clickanywhere.png" alt="クリックしてください">
                    </div>   
                </div>             
            </div>'''
    return render_template("index.html", html=html)

@socketio.on("video_request")
def handle_video_request():
    html = """<video id=switchingbg controls autoplay>
    <source src="../videos/switching.mp4" type="video/mp4">
    </video> 
"""



if __name__ == "__main__":
    socketio.run(app, port=50002, debug=True)