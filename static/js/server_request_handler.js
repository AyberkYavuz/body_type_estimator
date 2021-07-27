

function request_server(formData, url){

    $.ajax({
          type : 'POST',
          url : url,
          data : formData,
          success: function(response) {
            Materialize.toast(response, 5000)
          },
          error: function(error) {
            console.log(error);
          }
    });

}

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
  var url = "/predict_body_type";
  request_server(formData, url);
});

