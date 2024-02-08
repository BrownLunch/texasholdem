let socket = io();

socket.on("menu", () => {
    $("#title-container").css("display", "none")
    $("#menu-container").css("display", "flex")
})

function switching_menu(){
    $(".title-nav").fadeOut(1000); //アニメーション変更の可能性あり
    $(".title").fadeOut(1000); //アニメーション変更の可能性あり
    $("#bg").removeClass("start");
    $("#bg").addClass("end");
    setTimeout(() => {
        socket.emit("menu");
    }, 3500);    
    $("body").off("mouseup", switching_menu);
}

function slide_out(){
    $(".btn1").addClass("slide-out");
}

$("body").on("mouseup", switching_menu);
$("#friendmatch-btn").on("mouseup", function(){
    slide_out()
    $(".friendmatch-container").fadeIn(1000)
    $(".friendmatch-container").css("display", "flex")
});





