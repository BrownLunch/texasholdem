let socket = io();

// 接続時の処理
socket.on('connect', () => {      
    console.log('hello');
});

socket.on("menu", (html) => {
    $("#bg").html(html)
})

function switching_menu(){
    $(".title-nav").fadeOut(1000); //アニメーション変更の可能性あり
    $(".title").fadeOut(1000); //アニメーション変更の可能性あり
    $("#bg").removeClass("start")
    $("#bg").addClass("end")
    $("body").off("mouseup", switching_menu);
    socket.emit()
    
}

$("body").on("mouseup", switching_menu);





