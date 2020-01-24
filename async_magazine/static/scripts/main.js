/*
var card = document.getElementById('card');

document.getElementById('flip').addEventListener('click', function() {
    card.classList.toggle('flipped');
}, false)
*/
function flipCardFunction(card_id){
    let card = document.getElementById(card_id);
    card.classList.toggle('flipped');
    console.log(card)
}