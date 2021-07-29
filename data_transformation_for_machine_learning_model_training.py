import pandas as pd
from helpers.application_helpers import get_working_directory
from helpers.application_helpers import get_now
from sklearn.preprocessing import LabelEncoder
from core.file_handler import PickleHandler

print("data_transformation_for_machine_learning_model_training.py execution begins: " + str(get_now()))
print("getting data.")
working_directory = get_working_directory()
data_path = working_directory + "/machine_learning_data/ObesityDataSet_raw_and_data_sinthetic.csv"
print("Data path: " + data_path)

data = pd.read_csv(data_path)
print(data.head())

print("Gender Column Values Transformation")
data["Gender"] = data["Gender"].replace({'Male': 0})
data["Gender"] = data["Gender"].replace({'Female': 1})

print("family_history_with_overweight Column Values Transformation")
data["family_history_with_overweight"] = data["family_history_with_overweight"].replace({'yes': 1})
data["family_history_with_overweight"] = data["family_history_with_overweight"].replace({'no': 0})

print("FAVC Column Values Transformation")
data["FAVC"] = data["FAVC"].replace({'yes': 1})
data["FAVC"] = data["FAVC"].replace({'no': 0})

print("CAEC Column Values Transformation")
data["CAEC"] = data["CAEC"].replace({'no': 0})
data["CAEC"] = data["CAEC"].replace({'Sometimes': 1})
data["CAEC"] = data["CAEC"].replace({'Frequently': 3})
data["CAEC"] = data["CAEC"].replace({'Always': 6})

print("SMOKE Column Values Transformation")
data["SMOKE"] = data["SMOKE"].replace({'no': 0})
data["SMOKE"] = data["SMOKE"].replace({'yes': 1})

print("SCC Column Values Transformation")
data["SCC"] = data["SCC"].replace({'no': 0})
data["SCC"] = data["SCC"].replace({'yes': 1})

print("CALC Column Values Transformation")
data["CALC"] = data["CALC"].replace({'no': 0})
data["CALC"] = data["CALC"].replace({'Sometimes': 1})
data["CALC"] = data["CALC"].replace({'Frequently': 3})
data["CALC"] = data["CALC"].replace({'Always': 6})

print("MTRANS Column Values Transformation")
# frequency encoding is used.
data["MTRANS"] = data["MTRANS"].replace({'Public_Transportation': 1580})
data["MTRANS"] = data["MTRANS"].replace({'Automobile': 457})
data["MTRANS"] = data["MTRANS"].replace({'Walking': 56})
data["MTRANS"] = data["MTRANS"].replace({'Motorbike':  11})
data["MTRANS"] = data["MTRANS"].replace({'Bike':  7})

print("NObeyesdad Column Values Transformation")
label_encoder = LabelEncoder()
label_encoder.fit(data["NObeyesdad"])
print(label_encoder.classes_)
data["NObeyesdad"] = label_encoder.transform(data["NObeyesdad"])

print("Saving NObeyesdad label encoder")
label_encoder_path = working_directory + '/models/NObeyesdad_label_encoder.pickle'
pickle_handler = PickleHandler()
pickle_handler.save_object(label_encoder_path, label_encoder)

print("Saving machine learning ready data as body_type_estimation_data.csv")
machine_learning_ready_data_path = working_directory + '/machine_learning_data/body_type_estimation_data.csv'
data.to_csv(machine_learning_ready_data_path, index=False)

print("data_transformation_for_machine_learning_model_training.py execution ends: " + str(get_now()))

