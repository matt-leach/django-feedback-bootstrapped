$("document").ready( function() {
  $(".glyphicon-feedback").on('click', function() {
    $(".feedback-container").toggle();
  })

  $("#feedback-form").submit(function(e) {
    e.preventDefault();
    var data = $(this).serialize();
    var formURL = $(this).attr("action");
    $.ajax(
    {
        url : formURL,
        type: "POST",
        data : data,
        success: function(data, textStatus, jqXHR) 
        {   
        	alert("Feedback submitted!");
        	$(".feedback-container").hide();
        },
        error: function(jqXHR, textStatus, errorThrown) 
        {
            alert("Feedback could not be submitted :(");
        }
    });
  });
});
