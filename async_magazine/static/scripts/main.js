/*
var card = document.getElementById('card');

document.getElementById('flip').addEventListener('click', function() {
    card.classList.toggle('flipped');
}, false)
*/
function flipCardFunction(card_id){
    let card = document.getElementById(`card-${card_id}`);
    card.classList.toggle('flipped');
}

function addToCartCardFunction(cl_id){
    let img = document.getElementById(`img-${cl_id}`).src;
    let name = document.getElementById(`name-${cl_id}`).innerHTML;
    let price = document.getElementById(`price-${cl_id}`).innerHTML;
    let color = document.getElementById(`color-${cl_id}`).innerHTML.trim().split(' ');
    let size = document.getElementById(`size-${cl_id}`).innerHTML.trim().split(' ');
    let rand =  Math.ceil(Math.random()*100);
    $('.sh-cart').append(`  
    <div class="product">
        <div class="product-image">
            <img src="${img}">
        </div>
        <div class="product-details">
            <div class="product-title">${name}</div>
        </div>
        <div class="product-price">${price}</div>
        <div class="product-quantity ">
            <input type="number" class="input-count" value="1" min="1">
        </div>
        <div class="product-removal">
        <select id="select-size-${rand}">
        </select>
            </div>
            <div class="product-removal">
            <select id="select-color-${rand}">
            </select>
            </div>
        <div class="product-removal">
            <button class="remove-product">
            Remove
            </button>
        </div>
        <div class="product-line-price">${price}</div>
    </div>
`)
  for(let i in size){
    $(`#select-size-${rand}`).append(
        `<option>${size[i]}</option>`
    )
  }
  for(let i in color){
    $(`#select-color-${rand}`).append(
        `<option>${color[i]}</option>`
    )
  }
}
 
