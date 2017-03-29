// http://eonasdan.github.io/bootstrap-datetimepicker/#linked-pickers
$(function() {
  var common_options = {
    collapse: false,
    sideBySide: true,
    calendarWeeks: false, // default. it's there! :)
    allowInputToggle: true,
    format: 'YYYY-MM-DD HH:mm' // http://momentjs.com/docs/#/displaying/format/
  };
  var $start_dt = $('#start_dt_input_group');
  var $end_dt = $('#end_dt_input_group');
  $start_dt.datetimepicker(common_options);
  $end_dt.datetimepicker($.extend({}, common_options, {
    useCurrent: false //Important! See issue #1075
  }));
  $start_dt.on("dp.change", function(e) {
    $end_dt.data("DateTimePicker").minDate(e.date);
  });
  $end_dt.on("dp.change", function(e) {
    $start_dt.data("DateTimePicker").maxDate(e.date);
  });

  $('#delete').click(function(e) {
    $.ajax({
      type: 'DELETE',
      success: function(data) {
        alert("Success: " + data);
      },
      error: function(data) {
        if (data.status === 404) {
          console.log('already clear. refresh form.');
          window.location = window.location;
        } else {
          console.log('error deleting:', data);
        }
      }
    });
  })
});
