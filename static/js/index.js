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

function slide_in(){
    $(".btn1").removeClass("slide-out");
    $("#rankmatch-btn").addClass("slide-in1")
    $("#friendmatch-btn").addClass("slide-in2")
    $("#training-btn").addClass("slide-in3")
}

function slide_out(){
    $(".btn1").removeClass("slide-in1 slide-in2 slide-in3");
    $(".btn1").addClass("slide-out");
}

$("body").on("mouseup", switching_menu);
$("#friendmatch-btn").on("mouseup", function(){
    slide_out()
    $(".friendmatch-container").fadeIn(500)
    $(".friendmatch-container").css("display", "flex");
});
$(".back-btn").on("mousedown", function(){
    $(".back-btn").css("height", "70%");  
})
$(".back-btn").on("mouseup", function(){
    $(".back-btn").css("height", "60%");
})
$(".back-btn").on("click", function(){
    $(".friendmatch-container").fadeOut(500, slide_in);
})



