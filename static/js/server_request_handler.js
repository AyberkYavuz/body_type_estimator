/*
function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function request_server(first_number_value, second_number_value, url){
    var condition1 = first_number_value == "";
    var condition2 = second_number_value == "";
    if (condition1 || condition2) {
        console.log("Empty values")
    } else {
        console.log("Values are not empty!");
        $.ajax({
              type : 'POST',
              url : url,
              data : {'number1':first_number_value, 'number2': second_number_value},
              success: function(response) {
                console.log(response);
                var operation_name = url.substring(1);
                operation_name = capitalizeFirstLetter(operation_name);
                Materialize.toast(operation_name + ' Prediction: ' + response['prediction'].toString(), 5000)
              },
              error: function(error) {
                console.log(error);
              }
        });
    }

}
*/
$("#add_button").click(function(e) {
    e.preventDefault(); // prevents page refreshing
    var first_number_value = $("#first_number").val();
    var second_number_value = $("#second_number").val();
    url = "/summation";
    //request_server(first_number_value, second_number_value, url);
});

