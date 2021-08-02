from helpers.application_helpers import get_working_directory
from helpers.pandas_dataframe_helpers import get_data
from helpers.application_helpers import get_now
from helpers.pandas_dataframe_helpers import target
from helpers.pandas_dataframe_helpers import features
from helpers.pandas_dataframe_helpers import split_dataframe_as_train_and_test_instances
from helpers.pandas_dataframe_helpers import get_most_important_features
from core.machine_learning_handler import XgboostModelCreator
from core.file_handler import PickleHandler

print("xgboost_base_models_comparison.py execution begins: " + str(get_now()))
print("Loading body_type_estimation_data.csv")
working_directory = get_working_directory()
data_path = working_directory + "/machine_learning_data/body_type_estimation_data.csv"
body_type_estimation_data = get_data(data_path)

print("Splitting original data.")
X_train, X_test, y_train, y_test = split_dataframe_as_train_and_test_instances(body_type_estimation_data, target,
                                                                               features, test_size=0.3)
print("Loading Base Xgboost Model")
base_model_path = working_directory + '/models/base_xgboost_model.pickle'
base_model = XgboostModelCreator.load_model(base_model_path)

print("Base model classification report for training set.")
# loading NObeyesdad_label_encoder for classification report
nobeyesdad_label_encoder_path = working_directory + '/models/NObeyesdad_label_encoder.pickle'
pickle_handler = PickleHandler()
nobeyesdad_label_encoder = pickle_handler.load_object(nobeyesdad_label_encoder_path)

XgboostModelCreator.display_classification_report(base_model, X_train, y_train,
                                                  target_names=nobeyesdad_label_encoder.classes_)

print("Base model classification report for test set.")
XgboostModelCreator.display_classification_report(base_model, X_test, y_test,
                                                  target_names=nobeyesdad_label_encoder.classes_)

print("Loading Base Xgboost Model with Selected Features")
base_xgboost_model_with_selected_features_path = working_directory + '/models/' \
                                                                     'base_xgboost_model_with_selected_features.pickle'
base_xgboost_model_with_selected_features = XgboostModelCreator.load_model(base_xgboost_model_with_selected_features_path)


print("xgboost_base_models_comparison.py execution ends: " + str(get_now()))
