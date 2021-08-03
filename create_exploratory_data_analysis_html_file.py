from helpers.pandas_dataframe_helpers import get_data
import pandas_profiling
from helpers.application_helpers import get_working_directory
from helpers.application_helpers import get_now

print("create_exploratory_data_analysis_html_file.py execution begins: " + str(get_now()))
print("getting data.")
working_directory = get_working_directory()
data_path = working_directory + "/machine_learning_data/ObesityDataSet_raw_and_data_sinthetic.csv"
print("Data path: " + data_path)
data = get_data(data_path)

print("creating exploratory_data_analysis.html file.")
profile = pandas_profiling.ProfileReport(data, title="Pandas Profiling Report", explorative=True)

html_file_path = working_directory + '/templates/exploratory_data_analysis.html'
profile.to_file(html_file_path)

print("create_exploratory_data_analysis_html_file.py execution ends: " + str(get_now()))
