window.onload = startupFunctions

function startupFunctions(){
    fadeInCards()
}

function fadeInCards(){
    $(".card").each(function(index, value){
        $(value).fadeIn(index*1000);
    });
}