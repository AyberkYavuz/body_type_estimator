$(document).ready(function() {
    //   INIT SELECT LIST
    $('select').material_select();
    $('select[required]').css({
      display: 'inline',
      position: 'absolute',
      float: 'left',
      padding: 0,
      margin: 0,
      border: '1px solid rgba(255,255,255,0)',
      height: 0,
      width: 0,
      top: '2em',
      left: '3em'
    });
});