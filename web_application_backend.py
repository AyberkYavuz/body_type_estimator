from flask import Flask
from flask import render_template
from flask import request
from flask.views import MethodView
from helpers.application_helpers import BackendHelper


app = Flask(__name__)
app.secret_key = BackendHelper.create_random_aplhanumeric_string()


class MainPageSenderAPI(MethodView):
    def get(self):
        return render_template("main_page.html")


class BodyTypeMachineLearningModelAPI(MethodView):

    def get(self):
        return "Welcome to Body Type Machine Learning Model API!", 200

    def post(self):
        print("BodyTypeMachineLearningModelAPI POST Method")
        message = None
        parameter_list = ["gender", "age", "height", "weight",
                          "family_history_with_overweight",
                          "FAVC", "FCVC"]
        result_list = []
        for parameter in parameter_list:
            result = parameter not in request.form
            result_list.append(result)
        condition = True in result_list
        print(condition)
        if condition:
            message = "422", 422
        else:
            try:
                import time
                time.sleep(5)  # this line is for user interface test
                message = "development message", 200
            except Exception as ex:
                print("Exception : " + str(ex))
                message = "Something went wrong!", 500
        return message


main_page_sender_view = MainPageSenderAPI.as_view('main_page_sender_api')
app.add_url_rule('/', view_func=main_page_sender_view, methods=['GET'])

body_type_machine_learning_model_view = BodyTypeMachineLearningModelAPI.as_view('body_type_machine_learning_model_api')
app.add_url_rule('/predict_body_type', view_func=body_type_machine_learning_model_view, methods=['POST', 'GET'])

app.run(debug=True)
