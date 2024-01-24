let socket = io.connect('http://' + document.domain + ':' + location.port);

function switching_menu(){
    console.log(111)
        $(".title-nav").fadeOut(1500); //アニメーション変更の可能性あり
        $(".title").fadeOut(1500); //アニメーション変更の可能性あり
}

$(window).on("load", function(){
    $("#title-bg").on("mouseup", switching_menu)

})





