$(document).ready(function(){       
   var scroll_start = 0;
   var startchange = $('#startPoint');
   var offset = startchange.offset();
    if (startchange.length){
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
      if(scroll_start > offset.top) {
          $(".navbar-custom").css({'background-color':'rgba(1, 69, 142, 0.8)', 'transition':'background-color 700ms linear'});
       } else {
          $('.navbar-custom').css('background-color', 'transparent');
       }
   });
    }
});