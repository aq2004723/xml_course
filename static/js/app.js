(function($) {
  'use strict';

  $(function() {
    var $fullText = $('.admin-fullText');
    $('#admin-fullscreen').on('click', function() {
      $.AMUI.fullscreen.toggle();
    });

    $(document).on($.AMUI.fullscreen.raw.fullscreenchange, function() {
      $.AMUI.fullscreen.isFullscreen ? $fullText.text('关闭全屏') : $fullText.text('开启全屏');
    });

    $("#br-header").hide();//隐藏go to top按钮
    $(function(){
      $(window).scroll(function(){
        if($(this).scrollTop()>1){
          //当window的scrolltop距离大于1时，go to top按钮淡出，反之淡入
          $("#br-header").fadeIn();
        } else {
          $("#br-header").fadeOut();
        }
      });
    });

    $("#br-btn-login").click(function(){
      var username = $("#username").val();
      var password =$("#password").val();
      var ts = "<span  class=\"am-icon-times\"></span>"
      $.post("/auth/login",
      {
        username:username,
        password:password
      },function(res){
        if(res=="success"){
           window.location.href="/";
        }
        else{
          $("#br-login-box").addClass("am-form-error");
        }
      });
    }
    );

    $("#br-com-sub").click(function(){
      var title = $("#br-com-title").val();
      var markdown = $("#br-com-context").val();
      $.post("/compose",
        {
          title:title,
          markdown:markdown
        },function(state){
          alert("ok");
        });
    });
  });
})(jQuery);
