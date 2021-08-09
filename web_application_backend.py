from flask import Flask
from flask import render_template
from flask import request
import time
from flask.views import MethodView
from helpers.application_helpers import BackendHelper
import pandas as pd
from helpers.application_helpers import get_working_directory
from core.file_handler import PickleHandler

working_directory = get_working_directory()
pickle_handler = PickleHandler()


app = Flask(__name__)
app.secret_key = BackendHelper.create_random_aplhanumeric_string()


class MainPageSenderAPI(MethodView):
    """API for '/' url.
    """
    def get(self):
        """Handles GET requests for '/' url.
        Returns:
            html_file: Main page html file.
        """
        html_file = "main_page.html"
        return render_template(html_file)


class ExploratoryDataAnalysisHTMLSenderAPI(MethodView):
    """API for '/exploratory_data_analysis' url. To use this API,
    you need to run create_exploratory_data_analysis_html_file.py
    first.
    """
    def get(self):
        """Handles GET requests for '/exploratory_data_analysis' url.
        Returns:
            response: tuple or html. Server response to clients.
        """
        response = None
        try:
            html_file = "exploratory_data_analysis.html"
            response = render_template(html_file)
        except Exception:
            response = "To use '/exploratory_data_analysis' service, first you need to " \
                       "run create_exploratory_data_analysis_html_file.py", 500
        return response


class BodyTypeMachineLearningModelAPI(MethodView):
    """API for '/predict_body_type' url.
    """
    def get(self):
        """Handles GET requests for '/predict_body_type' url.
        Returns:
            message: tuple. Welcome message.
        """
        message = "Welcome to Body Type Machine Learning Model API!", 200
        return message

    def __get_features_dataframe(self):
        """Converts client request parameters to features_dataframe
        Returns:
            features_dataframe: dataframe. It will be used for producing prediction.
        """
        gender = request.form["gender"]
        fcvc = request.form["FCVC"]
        weight = request.form["weight"]
        calc = request.form["CALC"]
        favc = request.form["FAVC"]
        height = request.form["height"]
        ch2o = request.form["CH2O"]
        features_values = [[gender, fcvc, weight, calc, favc, height, ch2o]]
        feature_names = ["Gender", "FCVC", "Weight", "CALC", "FAVC", "Height", "CH2O"]
        features_dataframe = pd.DataFrame(features_values, columns=feature_names)
        return features_dataframe

    def __load_production_machine_learning_model(self):
        """Loading production machine learning model.
        Returns:
            production_machine_learning_model: XGBClassifier. It will produce predictions.
        """
        production_machine_learning_model_path = working_directory + '/models' \
                                                                     '/base_xgboost_model_with_selected_features.pickle'
        production_machine_learning_model = pickle_handler.load_object(production_machine_learning_model_path)
        return production_machine_learning_model

    def __load_target_label_encoder(self):
        """Loading target label encoder.
        Returns:
            target_label_encoder: LabelEncoder. It will convert numeric prediction to string value.
        """
        target_label_encoder_path = working_directory + '/models/NObeyesdad_label_encoder.pickle'
        target_label_encoder = pickle_handler.load_object(target_label_encoder_path)
        return target_label_encoder

    def post(self):
        """Handles POST requests for '/predict_body_type' url.
        Returns:
            message: tuple. Server response to clients.
        """
        print("BodyTypeMachineLearningModelAPI POST Method")
        message = None
        parameter_list = ["gender", "height", "weight",
                          "FAVC", "FCVC", "CALC", "CH2O"]
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
                time.sleep(2)  # this line is for user interface test.
                print("Converting client request parameters to features_dataframe.")
                features_dataframe = self.__get_features_dataframe()
                features_dataframe = features_dataframe.astype(float)
                print(features_dataframe.head())
                print("Loading production machine learning model.")
                production_machine_learning_model = self.__load_production_machine_learning_model()
                print("Making a prediction.")
                prediction = production_machine_learning_model.predict(features_dataframe)[0]
                print(prediction)
                print("Loading target label encoder.")
                target_label_encoder = self.__load_target_label_encoder()
                prediction = target_label_encoder.inverse_transform([int(prediction)])[0]
                print(prediction)
                message = prediction, 200
            except Exception as ex:
                print("Exception : " + str(ex))
                message = "Something went wrong!", 500
        return message


main_page_sender_view = MainPageSenderAPI.as_view('main_page_sender_api')
app.add_url_rule('/', view_func=main_page_sender_view, methods=['GET'])

exploratory_data_analysis_html_sender_view = ExploratoryDataAnalysisHTMLSenderAPI.as_view('exploratory_data_analysis_html_sender_api')
app.add_url_rule('/exploratory_data_analysis', view_func=exploratory_data_analysis_html_sender_view, methods=['GET'])

body_type_machine_learning_model_view = BodyTypeMachineLearningModelAPI.as_view('body_type_machine_learning_model_api')
app.add_url_rule('/predict_body_type', view_func=body_type_machine_learning_model_view, methods=['POST', 'GET'])

if __name__ == "__main__":
    # for local host
    app.run(debug=True)
    # You need to run the app with your IPv4 address in order to test UI with
    # your mobile phone which is connected to the same WiFi that your PC is connected to.
    # app.run(debug=True, host='your IPv4 address')
