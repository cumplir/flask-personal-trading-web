console.log('hello');

const myPageLink = $('a.my-page');
const myPageInterface = $('.mypage-interface');
const myPageClose = $('.mypage-close');

const myFollowerLink = $('a.myfollower');
const myfollowerInterface = $('.myfollower-interface');
const myFollowerClose= $('.myfollower-close');

$(document).ready(function(){
    myFollowerLink.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'60%'});
    });
    myFollowerClose.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'100%'});
    })
})

$(document).ready(function(){
    myPageLink.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'60%'});
    });
    myPageClose.click(function(e){
        e.preventDefault();
        myPageInterface.animate({left:'100%'});
    })
})