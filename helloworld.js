console.log(" Hello World");

// var h1tag = document.getElementsByTagName("h1")[0];
// var loc = document.getElementsByClassName("headings")[3];
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
