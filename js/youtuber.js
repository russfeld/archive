var players = [];
var playing = [];
var starts = [];

$(function() {
  $('.vimeo').each(function(value){
    var videoID = $(this).attr('id');
    var startTime = $(this).data('start') | 0;
    

    var embed = "<iframe id=\'" + videoID + "\' class=\'vimeo\' width=\"920\" height=\"690\" src=\"http://player.vimeo.com/video/" + videoID + "?byline=0&amp;portrait=0&amp;api=1&amp;player_id=" + videoID + " frameborder=\"0\" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>";
    $(this).replaceWith(embed);
    players[videoID] = $f(videoID);
    starts[videoID] = startTime;
    playing[videoID] = false;
  });
  document.addEventListener("keydown", playVid, false);
});

function onYouTubeIframeAPIReady() {
	$('.youtube').each(function(value){
    var div_id = $(this).attr('id');
		var videoID = $(this).data('id');
		var startTime = $(this).data('start') | 0;

		var embed = "<iframe id=\'" + div_id + "\' class=\'youtube\' width=\"920\" height=\"690\" src=\"//www.youtube.com/embed/" + videoID + "?rel=0&html5=1&iv_load_policy=3&enablejsapi=1&start=" + startTime + "\" frameborder=\"0\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe>";
		$(this).replaceWith(embed);
		players[div_id] = new YT.Player(div_id);
    playing[div_id] = false;
	});
}

var playVid = function(e) {
    if (e.keyCode == 66 || e.keyCode == 80) {
        e.preventDefault();
        var source = $('.active .youtube').attr('id');
        if(source == null){
          source = $('.active .vimeo').attr('id');
          if(source == null){
            var player = $('.active video')[0];
            if (player.paused){
              player.play();
              if (player.requestFullscreen) {
                player.requestFullscreen();
              }
              else if (player.mozRequestFullScreen) {
                player.mozRequestFullScreen();
              }
              else if (player.webkitRequestFullScreen) {
                player.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
              }
            }else{
              player.pause(); 
              document.webkitCancelFullScreen();
            }
          }else{
            var vplayer = players[source];
            if(playing[source]){
              vplayer.api('pause');
              playing[source] = false;
              document.webkitCancelFullScreen();
            }else{
              vplayer.api('play');
              var docElm = document.getElementById(source);
              if (docElm.requestFullscreen) {
                docElm.requestFullscreen();
              }
              else if (docElm.mozRequestFullScreen) {
                docElm.mozRequestFullScreen();
              }
              else if (docElm.webkitRequestFullScreen) {
                docElm.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
              }
              if(starts[source] > 0){
                setTimeout(function(){vplayer.api('seekTo', starts[source]); starts[source] = 0;}, "1000");
              }
              playing[source] = true;
            }
          }
        }else{
          var ytplayer = players[source];
          //YT.Player(source, { events: { 'onReady': youtubePlayPause }});
          if(playing[source]){
            ytplayer.pauseVideo();
            playing[source] = false;
            document.webkitCancelFullScreen();
          }else{
            ytplayer.playVideo();
            var docElm = document.getElementById(source);
            if (docElm.requestFullscreen) {
              docElm.requestFullscreen();
            }
            else if (docElm.mozRequestFullScreen) {
              docElm.mozRequestFullScreen();
            }
            else if (docElm.webkitRequestFullScreen) {
              docElm.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
            }
            playing[source] = true;
          }
      }
    }
/*
  var youtubePlayPause(event){
    if(playing[source]){
      ytplayer.pauseVideo();
      playing[source] = false;
      document.webkitCancelFullScreen();
    }else{
      ytplayer.playVideo();
      var docElm = document.getElementById(source);
      if (docElm.requestFullscreen) {
        docElm.requestFullscreen();
      }
      else if (docElm.mozRequestFullScreen) {
        docElm.mozRequestFullScreen();
      }
      else if (docElm.webkitRequestFullScreen) {
        docElm.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
      }
      playing[source] = true;
  }
  */
}

