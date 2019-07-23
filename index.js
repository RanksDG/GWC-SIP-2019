console.log("suppie")
// var i = 0;
// // set i to zero, then adds 2 to i each time, and runs when i is less than or equal to 20
// for(i = 0; i < 21; i += 2){
//   console.log(i);
// }
//
// var i = 0;
// while(i <=20){
//   console.log(i);
//   i += 2;
// }
//
// i = 0;
// while(i <= 20){
//   if(i % 2 == 0){
//     console.log(i);
//   }
//   i +=1;
// }
//
// function getTemp(){
//   return 22.5;
// }
//
// var temperature = getTemp();
//
// console.log(temperature);
//
// function getTemp2(type){
//   if(type == "c"){
//     return 22.5;
//   }
//   if (type == "f"){
//     return 100;
//   }
// }
//
// console.log(getTemp2("f"))
// console.log(getTemp2("c"))

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
