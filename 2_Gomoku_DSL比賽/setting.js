var chessX = 11;
var chessY = 11;
var chessSize = 40;
var player = true;
var online = true;
var cheesspace = new Array(chessX);
var gameover = false;
var maxChess = 0; // 最大可下棋子數
var fightResult = -1;
var fightRecord = null;
var isFirst = false;
var stepNumberL=0;
var stepNumberV=0;

var c = document.getElementById("Chess");
var ctx = c.getContext("2d");
fightRecord = new Array();

//初始化棋盤
function CreateChessBoard(){
	
	//初始化棋盤陣列
	for(var i=0;i<chessX;i++){
		cheesspace[i] = new Array(chessY);
		for(var j=0;j<chessY;j++){
			cheesspace[i][j] = 2;
			maxChess++;
		}
	}
	fightResult = -1;
	gameover = false;
	// 清空畫布
	ctx.clearRect(0, 0, c.width, c.height);
	// c.removeEventListener("mousedown", mouseDownHandler);

	//開始畫棋盤(初始化)
	ctx.beginPath();
	
	//X線
	for(var i = 1;i<chessY+1;i++){
		ctx.moveTo(chessSize, i*chessSize);
		ctx.lineTo(chessX*chessSize, i*chessSize);  
	}
	
	//Y線
	for(var i = 1;i<chessX+1;i++){
		ctx.moveTo(i*chessSize, chessSize);
		ctx.lineTo(i*chessSize, chessY*chessSize);  
	}
	
	//基本框
	for(var i = 0;i<chessX;i++){
		for(var j = 0;j<chessY;j++){	  
			ctx.fillStyle = "#FFF";
			ctx.fillRect((chessSize*0.75)+(i*chessSize),(chessSize*0.75)+(j*chessSize),chessSize/2,chessSize/2);
		}	  
	}
	ctx.stroke();
	// c.addEventListener('mousedown', mouseDownHandler, false);

}

var tt = "";


//繪製目前的棋盤
function replychess(){
	for(var i = 0;i<chessX;i++){
		for(var j = 0;j<chessY;j++){
			ctx.beginPath();
			if(cheesspace[i][j] == 0){
				ctx.arc(chessSize+(i*chessSize),chessSize+(j*chessSize),chessSize/3,0,2*Math.PI);
				ctx.fillStyle = 'white';
				ctx.fill();
			}
			else if(cheesspace[i][j] == 1){
				ctx.arc(chessSize+(i*chessSize),chessSize+(j*chessSize),chessSize/3,0,2*Math.PI);
				ctx.fillStyle = 'black';
				ctx.fill();	
			}
			ctx.stroke();
		}	  
	}
}

//自動下棋
function autorun(){
	var ran = randoms();
	
	ctx.beginPath();
	cheesspace[ran.x][ran.y] = 0;
	ctx.arc(chessSize+(ran.x*chessSize),chessSize+(ran.y*chessSize),chessSize/3,0,2*Math.PI);
	ctx.fillStyle = 'white';
	ctx.fill();
	ctx.stroke();
	SendData(ran.x,ran.y);
	player = !player;
	maxChess--;
}