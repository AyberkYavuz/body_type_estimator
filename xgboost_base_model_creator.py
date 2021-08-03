from helpers.pandas_dataframe_helpers import get_data
from helpers.application_helpers import get_working_directory
from helpers.application_helpers import get_now
from helpers.pandas_dataframe_helpers import target
from helpers.pandas_dataframe_helpers import features
from helpers.pandas_dataframe_helpers import split_dataframe_as_train_and_test_instances
from core.machine_learning_handler import XgboostModelCreator
from core.file_handler import PickleHandler

print("xgboost_base_model_creator.py execution begins: " + str(get_now()))
print("Getting body_type_estimation_data.csv")
working_directory = get_working_directory()
data_path = working_directory + "/machine_learning_data/body_type_estimation_data.csv"
print("Data path: " + data_path)
body_type_estimation_data = get_data(data_path)
print(body_type_estimation_data.head())
print("Splitting data.")
X_train, X_test, y_train, y_test = split_dataframe_as_train_and_test_instances(body_type_estimation_data, target,
                                                                               features, test_size=0.3)
print("Xgboost Base Model Creation")
xgboost_model_creator = XgboostModelCreator()
xgboost_model_creator.create_base_xgboost_model(X_train, y_train)

print("let's have a look at classification report for training set.")
# loading NObeyesdad_label_encoder for classification report
nobeyesdad_label_encoder_path = working_directory + '/models/NObeyesdad_label_encoder.pickle'
pickle_handler = PickleHandler()
nobeyesdad_label_encoder = pickle_handler.load_object(nobeyesdad_label_encoder_path)

XgboostModelCreator.display_classification_report(xgboost_model_creator.base_xgboost_classifier,
                                                  X_train, y_train, target_names=nobeyesdad_label_encoder.classes_)

print("let's have a look at classification report for test set.")
XgboostModelCreator.display_classification_report(xgboost_model_creator.base_xgboost_classifier,
                                                  X_test, y_test, target_names=nobeyesdad_label_encoder.classes_)

print("Saving Base Xgboost Model")
base_xgboost_model_path = working_directory + '/models/base_xgboost_model.pickle'
xgboost_model_creator.save_model("base_model", base_xgboost_model_path)

print("xgboost_base_model_creator.py execution ends: " + str(get_now()))
