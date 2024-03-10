let socket = io();

let roomno;

socket.on("messege", (msg) =>{
    console.log(msg);
})

socket.on("menu", () => {
    $(".title-container").css("display", "none")
    $(".menu-container").css("display", "flex")
})

function switching_menu(){
    $(".title-nav").fadeOut(1000); //アニメーション変更の可能性あり
    $(".title").fadeOut(1000); //アニメーション変更の可能性あり
    $(".bg").removeClass("start");
    $(".bg").addClass("end");
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

function fade_in_createroom(){
    $(".createroom-container").fadeIn(500)
}

function fade_in_menu(){
    $(".menu-container").fadeIn(500)
}

//タイトル画面からメニュー画面への遷移
$("body").on("mouseup", switching_menu);

//フレンドマッチからメニュー画面への遷移
$("#friendmatch-btn").on("mouseup", function(){
    slide_out()
    $(".friendmatch-container").fadeIn(500)
    $(".friendmatch-container").css("display", "flex");
});
$("#friendmatchback-btn").on("mousedown", function(){
    $("#friendmatchback-btn").css("height", "70%");  
})
$("#friendmatchback-btn").on("mouseup", function(){
    $("#friendmatchback-btn").css("height", "60%");
})
$("#friendmatchback-btn").on("click", function(){
    $(".friendmatch-container").fadeOut(500, slide_in);
})

// 部屋作成画面への遷移
$("#createroom-btn").on("mousedown", function(){
    $(".menu-container").fadeOut(500, fade_in_createroom)
    initchipbtn();
    initthinkbtn();
})
$("#createroomback-btn").on("mousedown", function(){
    $("#createroomback-btn").css("height", "60%");  
})
$("#createroomback-btn").on("mouseup", function(){
    $("#createroomback-btn").css("height", "50%");
})
$("#createroomback-btn").on("click", function(){
    $(".createroom-container").fadeOut(500, fade_in_menu);
})

//部屋作成画面の人数上限系処理
$(".plus").on("mousedown", function(){
    let player_num = $(".player-num").text();
    if(player_num < 6){
        player_num++;
        $(".player-num").text(player_num);
    }
})
$(".minus").on("mousedown", function(){
    let player_num = $(".player-num").text();
    if(player_num > 2){
        player_num--;
        $(".player-num").text(player_num);
    }
})

//部屋作成ボタンのラジオボタン系処理

//初期スタック数のラジオボタン処理
$("#chip10000-btn").on("mousedown", function(){
    $("input[value='10000']").prop("checked", true);
    changechipbtn();
})
$("#chip15000-btn").on("mousedown", function(){
    $("input[value='15000']").prop("checked", true);
    changechipbtn();
})
$("#chip20000-btn").on("mousedown", function(){
    $("input[value='20000']").prop("checked", true);
    changechipbtn();
})
$("#chip30000-btn").on("mousedown", function(){
    $("input[value='30000']").prop("checked", true);
    changechipbtn();
})

//長考時間のラジオボタン処理
$("#think15-btn").on("mousedown", function(){
    $("input[value='15']").prop("checked", true);
    changethinkbtn();
})
$("#think30-btn").on("mousedown", function(){
    $("input[value='30']").prop("checked", true);
    changethinkbtn();
})
$("#think60-btn").on("mousedown", function(){
    $("input[value='60']").prop("checked", true);
    changethinkbtn();
})
$("#think120-btn").on("mousedown", function(){
    $("input[value='120']").prop("checked", true);
    changethinkbtn();
})
$("#think300-btn").on("mousedown", function(){
    $("input[value='300']").prop("checked", true);
    changethinkbtn();
})

//ゲーム＆待機画面への遷移
$(".create-btn").on("mousedown", function(){
    socket.emit("create_room", {maxplayers:$(".player-num").text(), chip:$("input[name='chipnum']:checked").val(), thinktime:$("input[name='thinktime']:checked").val()});
    $(".createroom-container").css("display", "none");
    $(".menu-container").css("display", "none");
    $(".game-container").css("display", "block");
})

//初期スタック数の初期化
function initchipbtn(){
    $("#chip10000").prop("checked", true);
    $("input[name='chipnum']").each(function(idx){
        if(idx < 1){
            $(".createroom-choose-chip").eq(idx).attr("src", "../static/images/createroomchoosed.png")           
        }else{
            $(".createroom-choose-chip").eq(idx).attr("src", "../static/images/createroomchoose.png") 
        }
    })
}

//長考時間の初期化
function initthinkbtn(){
    $("#think15").prop("checked", true);
    $("input[name='thinktime']").each(function(idx){
        if(idx < 1){
            $(".createroom-choose-think").eq(idx).attr("src", "../static/images/createroomchoosed.png")           
        }else{
            $(".createroom-choose-think").eq(idx).attr("src", "../static/images/createroomchoose.png") 
        }
    })
}

//初期スタック数の選択
function changechipbtn(){
    $("input[name='chipnum']").each(function(idx){
        if($(this).prop("checked")){
            $(".createroom-choose-chip").eq(idx).attr("src", "../static/images/createroomchoosed.png")           
        }else{
            $(".createroom-choose-chip").eq(idx).attr("src", "../static/images/createroomchoose.png") 
        }
    })
}

//長考時間の選択
function changethinkbtn(){
    $("input[name='thinktime']").each(function(idx){
        if($(this).prop("checked")){
            $(".createroom-choose-think").eq(idx).attr("src", "../static/images/createroomchoosed.png")           
        }else{
            $(".createroom-choose-think").eq(idx).attr("src", "../static/images/createroomchoose.png") 
        }
    })
}

//部屋参加モーダル関連
$("#joinroom-btn").on("mousedown", function(){
    $(".modal-overlay").css("display", "block");
    $(".modal-content").css("display", "block");
    $(".modal-content").removeClass("close");
    $(".modal-content").addClass("open");
})

$(".modal-overlay").on("mousedown", function(){
    $(".roomnum-txt").text("");
    $(".modal-overlay").css("display", "none");
    $(".modal-content").removeClass("open");
    $(".modal-content").addClass("close");
})

$(".modalclose-btn").on("mousedown", function(){
    $(".modalclose").css("width", "12%");
})

$(".modalclose-btn").on("mouseup", function(){
    $(".modalclose").css("width", "11%");
})

$(".modalclose-btn").on("click", function(){
    $(".roomnum-txt").text("");
    $(".modal-overlay").css("display", "none");
    $(".modal-content").removeClass("open");
    $(".modal-content").addClass("close");
})

//部屋参加キーパッド関連

//数字
$(".keypad-digit").on("mousedown", function(){
    if($(".roomnum-txt").text().length < 5){
        $(".roomnum-txt").append($(this).text());
    }
})

//Cボタン
$(".keypad-clear").on("mousedown", function(){
    $(".roomnum-txt").text("");
})

//一文字消すボタン
$(".keypad-back").on("mousedown", function(){
    if($(".roomnum-txt").text().length > 0){
        $(".roomnum-txt").text($(".roomnum-txt").text().slice(0, -1))
    }
})

$(".join-btn").on("mousedown", function(){
    if ($(".roomnum-txt").text().length == 5){
        socket.emit("join_room", {username:"たけし", roomno:$(".roomnum-txt").text()});
        
    }
})

socket.on("after_create_room", (data) =>{
    let createdroomno = data["createroomno"];
    socket.emit("join_room", {username:"いちろう", roomno:createdroomno});
    
})

socket.on("after_join_room", (data) =>{
    roomno = data["roomno"];

    //メニュー画面からゲーム画面に切り替える
    $(".roomnum-txt").text("");
    $(".modal-content").removeClass("open");
    $(".modal-content").addClass("close");
    $(".menu-container").css("display", "none");
    $(".game-container").css("display", "block");


    $(".room-no").text(roomno);     
    console.log(data["username"] + "が" + roomno + "に入室しました。")
})
