$(document).ready(function () {
  $('loginuser').submit(function (event) {
    event.preventDefault();
    const userLoginForm = new FormData(this);
    let userId;
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/auth'
      method: 'POST',
      data: userLoginForm,
      contentType: false,
      processData: false,
      success: function (response) {
        window.location.href = "/events"
        userid = response
      },
      error: function (xhr, err, errStr) {
        $('formdiv').text(errStr);
      }
    });
  });
  $.ajax({
    url: `http://0.0.0.0:5000/api/v1/event/user/{userId}`
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      for (let event of response) {

      }
    }
  })
});
