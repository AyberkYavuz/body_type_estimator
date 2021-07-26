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
/*
$("#predictBodyTypeButton").click(function(e) {
    //e.preventDefault(); // prevents page refreshing
    console.log("predictBodyTypeButton was clicked!");
    e.preventDefault(); // prevents page refreshing
    //var first_number_value = $("#first_number").val();
    //var second_number_value = $("#second_number").val();
    //url = "/summation";
    //request_server(first_number_value, second_number_value, url);
});
*/

function getFormData() {
    var genderValue = null;
    var isMaleChecked = $("#male").is(":checked");
    if (isMaleChecked) {
        genderValue = "Male"
    } else {
        genderValue = "Female"
    }

    var ageValue = $("#age").val();
    var heightValue = $("#height").val();
    var weightValue = $("#weight").val();

    var familyHistoryWithOverweight = null;
    var familyHistoryWithOverweightYesChecked = $("#familyHistoryWithOverweightYes").is(":checked");
    if (familyHistoryWithOverweightYesChecked) {
        familyHistoryWithOverweight = "yes"
    } else {
        familyHistoryWithOverweight = "no"
    }

    var favc = null;
    var FAVC_yes_checked = $("#FAVC_yes").is(":checked");
    if (FAVC_yes_checked) {
        favc = "yes"
    } else {
        favc = "no"
    }

    var FCVC_value = $("#FCVC").val();

    var formData = {
    "gender": genderValue,
    "age": ageValue,
    "height": heightValue,
    "weight": weightValue,
    "family_history_with_overweight": familyHistoryWithOverweight,
    "FAVC": favc,
    "FCVC": FCVC_value
    }
    return formData;
}

jQuery("form").submit(function(e){
  e.preventDefault();
  // console.log("predictBodyTypeButton was clicked!");
  formData = getFormData();
  console.log(formData);

});

