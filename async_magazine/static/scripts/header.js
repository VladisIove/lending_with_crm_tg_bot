// New date
var countDownDate = new Date("Feb 28, 2020 00:00:00").getTime()
// Update timer every one second
let countDownFunction = setInterval(function(){
    let now = new Date().getTime();
    let distance = countDownDate - now;
    let days = Math.floor(distance/(1000*60*60*24));
    let hours = Math.floor((distance%(1000*60*60*24))/(1000*60*60));
    let minutes = Math.floor((distance%(1000*60*60))/(1000*60));
    let seconds = Math.floor((distance%(1000*60))/(1000));
    document.getElementById("timer").innerHTML = days + "д "+ hours + "ч " + minutes + "м " + seconds + "c ";
    if(distance<0){
        clearInterval(countDownFunction);
        document.getElementById("timer").innerHTML = "Время истекло";
    }
}, 1000)