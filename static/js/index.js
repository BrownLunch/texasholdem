let socket = io();

function switching_menu(){
    $(".title-nav").fadeOut(1500); //アニメーション変更の可能性あり
    $(".title").fadeOut(1500); //アニメーション変更の可能性あり
    
    //サーバとのコネクション確立
    socket.on('connect', function() {
        socket.emit('server_echo', {data: 'client connected!'});
    });


    //サーバからのメッセージを出力する関数
    socket.on('client_echo', function(data) {
        console.log("echo" + ': ' + data.msg);
    });
        
    $("#bg").off("mouseup", switching_menu);    
}

$("#bg").on("mouseup", switching_menu);





