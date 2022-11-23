var socket = null;
	
//送出資料
function SendData(x,y){
	// socket.emit('SendData',x,y,fightID);		
	socket.emit('setPiece',x,y);
}

//Send
function Register(){
	var address = "http://"+document.getElementById("serverIP").value+":3000";
	socket = io.connect(address);
	console.log("connect");
	//初始連線
	socket.on('connect', function(){
	console.log("reg");
		socket.emit('reg', document.getElementById("name").value);	
	});
	//註冊成功
	socket.on('regFinish', function(){
		console.log("註冊成功:");
	});

	//開始對弈
	socket.on('fightStart', function(){
		CreateChessBoard();
		isFirst = false;
	});

	//接收資料
	socket.on('getPiece', function(x,y){
		//console.log("對手下子:"+x+","+y);
		otherData(x,y);
		if(x==-1 && y==-1)
		{
			isFirst = true;
			player = true;
			autorun();
			return;
		}
		// 假設沒有棋可以下了
		if(maxChess<=0)	
		{
			fightResult = 2;
		}
		maxChess--;
		cheesspace[x][y] = 1;
		replychess();
		player = true;
		if(!gameover)
			autorun();
	});

	//結束對弈
	socket.on('fightEnd', function(){
		gameover = true;
		//console.log("對弈結束");
	});

	//接收資料
	socket.on('start', function(){
		//console.log("start");
	});

	//接收資料
	socket.on('ReceiveData', function(x,y){
		cheesspace[x][y] = 1;
		replychess();
		player = true;
		if(!gameover)
			autorun();
	});
}