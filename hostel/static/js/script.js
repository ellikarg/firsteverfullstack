$(document).ready(function() { //DISABLED PAST DATES IN BOOKING DATE
    var dateToday = new Date();
    var month = dateToday.getMonth() + 1;
    var day = dateToday.getDate();
    var year = dateToday.getFullYear();
  
    if (month < 10)
      month = '0' + month.toString();
    if (day < 10)
      day = '0' + day.toString();
  
    var maxDate = year + '-' + month + '-' + day;
  
    $('.datepicker').attr('min', maxDate);
  });
  