var playing = [];

$(function() {
  $('<audio id="doneAudio"><source src="/~russfeld/js/jeopardy.mp3" type="audio/mpeg"></audio>').appendTo('body');
  $('.timer').each(function(value){
    var ID = $(this).attr('id');
    var textsize = 40;
    if($(this).data('textsize')){
      textsize = $(this).data('textsize');
    }

    var embed = "<div style=\"text-align: center;\"><button class=\"btn btn-success start" + ID + "\" style=\"font-size: " + textsize + "px\">Start</button>&nbsp;&nbsp;&nbsp;<button class=\"btn btn-danger stop" + ID + "\" style=\"font-size: " + textsize + "px\">Stop</button>&nbsp;&nbsp;&nbsp;<button class=\"btn btn-info restart" + ID + "\" style=\"font-size: " + textsize + "px\">Reset</button></div>";
    $("#"+ID).before(embed);
    $("#"+ID).TimeCircles({start: false, time: {Days: {show: false}, Hours: {show: false}}, count_past_zero: false}).restart().stop();
    $(".start"+ID).click(function(){ $("#"+ID).TimeCircles().start(); }); 
    $(".stop"+ID).click(function(){ $("#"+ID).TimeCircles().stop(); }); 
    $(".restart"+ID).click(function(){ $("#"+ID).TimeCircles().restart().stop(); });
    $("#"+ID).TimeCircles().addListener(function(unit, value, total){
      if(total == 0){
        $('#doneAudio')[0].play();
      }
    });
    playing[ID] = false;
  });
  document.addEventListener("keydown", startTimer, false);
});

var startTimer = function(e) {
    if (e.keyCode == 66 || e.keyCode == 80) {
        e.preventDefault();
        var source = $('.active .timer').attr('id');
        if(source != null){
          var ytplayer = $("#"+source);
          //YT.Player(source, { events: { 'onReady': youtubePlayPause }});
          if(playing[source]){
            ytplayer.TimeCircles().restart().stop();
            playing[source] = false;
          }else{
            ytplayer.TimeCircles().start();
            playing[source] = true;
          }
      }
    }
};

