console.log(suppie)

var adjectives = ["brave", "smart", "mama seh mamasha mamamakcoosa", "happy", "amazing"];

var pos = 0

var loc = document.getElementById("adjective")

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0
  }
}

function zoomin(){
  var myImg = document.getElementById("pic")
  var currWidth = myImg.clientWidth;
  var currHeight = myImg.clientWidth;
  myImg.style.width = (currWidth + 5) + "px";
  myImg.style.height = (currHeight + 5) + "px";
}
