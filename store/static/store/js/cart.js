console.log('cart.html');
update_btns = document.getElementsByClassName('update-cart');

for (let i=0; i<update_btns.length; i++){
    update_btns[i].addEventListener('click', function () {
        console.log('ok')

    })
}