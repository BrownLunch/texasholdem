let socket = io();

function switching_menu(){
    $(".title-nav").fadeOut(1000); //アニメーション変更の可能性あり
    $(".title").fadeOut(1000); //アニメーション変更の可能性あり
    $("#bg").removeClass("start")
    $("#bg").addClass("end")
    $("#bg").html()
    $("body").off("mouseup", switching_menu);
}

$("body").on("mouseup", switching_menu);





