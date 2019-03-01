// Text Area Detect Entities button function
$( document ).ready(function() {
    console.log( "ready!" );

//    $("#text-area-btn").on("click", function() {
//      var text = $("textarea").val();
//      alert(text);
//      $.ajax({
//        type: "POST",
//        url: "/hello", // url to flask detect entities method
//        data: text,
//        success: function (json) {
//          // on success we get the json object
//          alert('success');
//        },
//        error: function() {
//          alert('failed');
//          $("#result-section").html(`
//            <div class="container">
//              <p>This is some container para after the button section, using the jquery after method thing</p>
//            </div>
//          `);
//        }
//      });
//    });

    // Detect entities from uploaded base
    // maybe we'll want to get a result, after hitting a submit file btn?
    $("#upload-detect-btn").on("click", function() {
      // maybe another ajax, or part of below to grab text
      alert(text);
      $.ajax({
        type: "GET",
        url: "@approuteflaskmethodthing", // url to flask detect entities method
        data: text,
        success: function (json) {
          // on success we get the json object
          alert('success');
        },
        error: function() {
          alert('failed');
          $("#result-section").html(`
            <div class="container">
              <p>This is some container para after the button section, using the jquery after method thing</p>
            </div>
          `);
        }
      });
    });

    $(function() {
        $('a#calculate').on('click', function() {
          $.getJSON($SCRIPT_ROOT + '/add_numbers', {
            a: $('input[name="a"]').val(),
            b: $('input[name="b"]').val()
          }, function(data) {
            $("#result").text(data.result);
          });
          return false;
        });
    });

    $(function() {
        $('#text-area-btn').on('click', function() {
            console.log($("textarea").val());
            $.getJSON($SCRIPT_ROOT + '/analyze_text_area', {
                text: $("textarea").val()
              }, function(data) {
                $("#result-section").html(`
                    <div class="container">
                      <p>${data.textresult}</p>
                    </div>
                  `);
              });
              return false;

        });
    });

}); // end of document ready

