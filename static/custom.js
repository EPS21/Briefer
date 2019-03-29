// Text Area Detect Entities button function
var myFileName = '';

$( document ).ready(function() {
    console.log( "ready!!" );

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

    // add numbers script
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

    // get textarea text pass into analyze text area function
    $(function() {
        $('#text-area-btn').on('click', function() {
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

    // get file name string from filename
    $('input[type="file"]').change(function(e){
        var fileName = e.target.files[0].name;
        myFileName = fileName;
        alert('The file "' + fileName +  '" has been selected.');
        console.log(myFileName)
    });

//    $(function() {
//        $('#upload-form').change(function() {
//            $.post($SCRIPT_ROOT + '/upload', function(data) {
//                $("#result").html( data );
//            })
//        })
//    })


    // file upload function after user selects a file
//    $(function() {
//        $('#upload').change(function() {
//            alert($('#upload').val());
//            $.getJSON($SCRIPT_ROOT + '/upload', {
//                filename: $('#upload').val()
//              }, function(data) {
//                    $("#result").text(data.filename);
//              });
//              return false;
//        });
//    });

}); // end of document ready

