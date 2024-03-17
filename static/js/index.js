let socket = io();
let sessionid;
let roomno;

socket.on("messege", (msg) =>{
    console.log(msg);
})

socket.on("connect", () => {
    sessionid = socket.id;
    console.log("Hello Poker.io!")
    console.log(sessionid)
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
    socket.emit("create_room", {maxplayers:$(".player-num").text(), chip:$("input[name='chipnum']:checked").val(), thinktime:$("input[name='thinktime']:checked").val(), username:"一郎"});
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
        socket.emit("join_room", {username:"たけし", roomno:$(".roomnum-txt").text(), host:"0"});
        
    }
})

function sort_players(players){
    let myidx
    for (let i = 0; i < players.length; i++){
        if (sessionid == players[i]["sessionid"]){
            myidx = i;
            break;
        }
    }
    sorted_players = []
    for (let i = 0; i < players.length; i++){
        sorted_players.push(players[myidx]);
        if(myidx < players.length - 1){
            myidx++
        }else{
            myidx = 0
        }
    }

    return sorted_players
}

function standby_update_display(rm, pls){
    $(".room-no").text(rm["roomno"])

    //参加人数の分プレイヤーウィンドウを表示する
    $(".player-window:lt("+ pls.length +")").css("display", "block");

    for(let i=0; i < pls.length; i++){
        stack = pls[i]["stack"].toLocaleString()
        $(".stack").eq(i).text(stack);
        $(".username").eq(i).text(pls[i]["username"]);
    }

}

function game_start_update_display(rm, pls){
    $(".start-game").css("display", "none");

    //配られたカードを表示(自分以外は裏面を表示、敗北しているプレイヤーは非表示)
    for(let i = 0; i < pls.length; i++){
        if (pls[i]["status"] == "Active"){           
            if (pls[i]["sessionid"] == sessionid){
                $(".hand").eq(i * 2).attr("src", "../static/images/cards/" + pls[i]["hand"][0] + ".png");
                $(".hand").eq((i * 2) + 1).attr("src", "../static/images/cards/" + pls[i]["hand"][1] + ".png");
            }else{
                $(".hand").eq(i * 2).attr("src", "../static/images/cards/back.png");
                $(".hand").eq((i * 2) + 1).attr("src", "../static/images/cards/back.png");
            }
        }else{
            $(".hand").eq(i * 2).attr("src", "");
            $(".hand").eq((i * 2) + 1).attr("src", "");
        }
    }
    console.log(rm)

    //プレイヤーのスタックを更新
    for(let i = 0; i < pls.length; i++){
        $(".stack").eq(i).text(pls[i]["stack"].toLocaleString());
    }

    //プレイヤーのベットを更新
    for(let i = 0;i < pls.length; i++){
        if (pls[i]["bet"] > 0){
            $(".bet").eq(i).text(pls[i]["bet"].toLocaleString());
        }
    }

    //テーブルのポットを更新
    $(".pot").text("Pot：" + rm["pot"].toLocaleString())

}

$(".start-game").on("click", function(){
    socket.emit("start_game", {"roomno":roomno});
})

socket.on("echo_create_room", (data) =>{
    let createdroomno = data["createroomno"];
    let username = data["username"]
    socket.emit("join_room", {username:username, roomno:createdroomno, host:"1"});
    
})

socket.on("echo_join_room", (data) =>{
    //jsonを受け取りjavascriptの配列に変換
    players = sort_players(JSON.parse(data["players"]));
    room = JSON.parse(data["room"]);

    //メニュー画面からゲーム画面に切り替える
    $(".roomnum-txt").text("");
    $(".modal-content").removeClass("open");
    $(".modal-content").addClass("close");
    $(".modal-overlay").css("display", "none")
    $(".menu-container").css("display", "none");
    $(".game-container").css("display", "block");

    roomno = room["roomno"];

    standby_update_display(room, players);     
})

socket.on("echo_start_game", (data) =>{
    //jsonを受け取りjavascriptの配列に変換
    players = sort_players(JSON.parse(data["players"]));
    room = JSON.parse(data["room"]);

    game_start_update_display(room, players);

    console.log(players)
    //部屋の製作者が代表して送信
    if(players[0]["host"] == "1"){
        socket.emit("preflop", {roomno: roomno});
    }  
})

socket.on("action", (data) => {
    rm = data["room"];
    pls = data["players"];
    console.log("俺の番")
    $(".action-bar").css("display", "grid");
})