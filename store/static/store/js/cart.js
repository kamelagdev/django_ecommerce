console.log('cart.html');
update_btns = document.getElementsByClassName('update-cart');

for (let i=0; i<update_btns.length; i++){
    update_btns[i].addEventListener('click', function () {
        let productId = parseInt(this.dataset.product);
        let action = this.dataset.action;

            updateUserCart(productId, action)

    })
}

function updateUserCart(productId, action) {

    let url = '/update-cart/';
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})

    }).then(response => {
        return response.json()
    })
        .then(data => {
            location.reload()
        })
}