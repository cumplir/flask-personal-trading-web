const myPageLink = $('a.my-page');
const myPageInterface = $('.mypage-interface');
const myPageClose = $('.mypage-close');

const setProductLink = $('.set-product');
const productForm = $('.post');
const productClose = $('.post .close-form');

const updateProductLink = $('.updateLink');
const updateForm = $('.update');
const product_updateClose = $('.update .close-form');


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

    updateProductLink.click(function(e){
        e.preventDefault();
        updateForm.fadeIn();
    })

    product_updateClose.click(function(e){
        e.preventDefault();
        updateForm.fadeOut();
    })
})
