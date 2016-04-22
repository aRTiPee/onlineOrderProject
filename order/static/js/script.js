$(document).ready(function(){
  $('#form').submit(function(){
    var msg = "go to next page?";
    return confirm(msg);
  });
});