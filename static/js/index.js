let socket = io();

socket.on("menu", () => {
    $("#title-container").css("display", "none")
    $("#menu-container").css("display", "flex")
})

function switching_menu(){
    $(".title-nav").fadeOut(1000); //アニメーション変更の可能性あり
    $(".title").fadeOut(1000); //アニメーション変更の可能性あり
    $("#bg").removeClass("start")
    $("#bg").addClass("end")
    setTimeout(() => {
        socket.emit("menu")
    }, 3500);    
    $("body").off("mouseup", switching_menu);
}

function slide_out(){
    $(".btn").addClass("slide-out")
}

$("body").on("mouseup", switching_menu);
$(".btn").on("animationend", function(){
    $(".btn").css("right", "0%")
})
$("#friendmatch-btn").on("mouseup", slide_out)





