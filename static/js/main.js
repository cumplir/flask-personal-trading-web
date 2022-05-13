const myPageLink = $('a.my-page');
const myPageInterface = $('.mypage-interface');
const myPageClose = $('.mypage-close');

const setProductLink = $('.set-product');
const productForm = $('.product-form');
const productClose = $('.close-form');


$(document).ready(function(){
    myPageLink.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'60%'});
    });
    myPageClose.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'100%'});
    });

    setProductLink.click(function(e){
        e.preventDefault();
        productForm.fadeIn();
    });

    productClose.click(function(e){
        e.preventDefault();
        productForm.fadeOut();
    })
})
