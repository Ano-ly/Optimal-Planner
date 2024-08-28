$(document).ready(function () {
  $.ajax({
    url: `http://0.0.0.0:5000/api/v1/event/user/{window.userId}`,
    method: 'GET',
    dataType: 'json',
    success: function (response) {
      for (let event of response) {

      }
    }
  });
});

