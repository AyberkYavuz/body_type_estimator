from helpers.application_helpers import get_working_directory
from helpers.application_helpers import get_now
from helpers.pandas_dataframe_helpers import feature_descriptions
from helpers.pandas_dataframe_helpers import target
from helpers.pandas_dataframe_helpers import get_most_important_features
from helpers.pandas_dataframe_helpers import get_data
from core.machine_learning_handler import XgboostModelCreator
from core.visualizer import MatplotlibVisualizer
from helpers.pandas_dataframe_helpers import split_dataframe_as_train_and_test_instances

print("feature_selection.py execution begins: " + str(get_now()))
print("Loading Base Xgboost Model")
working_directory = get_working_directory()
base_xgboost_model_path = working_directory + '/models/base_xgboost_model.pickle'
base_xgboost_model = XgboostModelCreator.load_model(base_xgboost_model_path)

print("Visualizing Base Xgboost Model's Feature Importances")
matplotlib_visualizer = MatplotlibVisualizer()
feature_descriptions_values_list = list(feature_descriptions.values())
matplotlib_visualizer.show_feature_importances(base_xgboost_model.feature_importances_,
                                               feature_descriptions_values_list,
                                               16, 8)

print("Creating body_type_estimation_data_selected_columns dataframe")
feature_names = list(feature_descriptions.keys())
selected_columns = get_most_important_features(base_xgboost_model.feature_importances_, feature_names, 12)
data_path = working_directory + "/machine_learning_data/body_type_estimation_data.csv"
body_type_estimation_data = get_data(data_path)
selected_columns.append(target)
body_type_estimation_data_selected_columns = body_type_estimation_data[selected_columns]

print("Saving body_type_estimation_data_selected_columns as a csv file.")
updated_data_path = working_directory + '/machine_learning_data/body_type_estimation_data_selected_columns.csv'
body_type_estimation_data_selected_columns.to_csv(updated_data_path, index=False)

print("Splitting body_type_estimation_data_selected_columns.")
selected_columns = selected_columns[:-1]
X_train, X_test, y_train, y_test = split_dataframe_as_train_and_test_instances(body_type_estimation_data, target,
                                                                               selected_columns, test_size=0.3)

print("Creating Base Xgboost Model with Selected Columns")
xgboost_model_creator = XgboostModelCreator()
xgboost_model_creator.create_base_xgboost_model(X_train, y_train)

print("Saving Base Xgboost Model")
base_xgboost_model_path = working_directory + '/models/base_xgboost_model_with_selected_features.pickle'
xgboost_model_creator.save_model("base_model", base_xgboost_model_path)

print("feature_selection.py execution ends: " + str(get_now()))
