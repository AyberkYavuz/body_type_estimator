from sklearn.model_selection import train_test_split as sk_train_test_split
import pandas as pd


def get_data(data_path):
    data = pd.read_csv(data_path)
    return data


def split_dataframe_as_train_and_test_instances(dataframe, target_column, feature_columns, test_size=0.2):
    """Splits pandas dataframe as X_train, X_test, y_train, y_test.
    Parameters:
        dataframe: pandas dataframe. The dataframe to be splitted.
        target_column: str. Target variable.
        feature_columns: list. Feature variables.
        test_size: float. Ratio of test set instances.
    Returns:
        splitting: X_train, X_test, y_train, y_test.
    """
    X = dataframe[feature_columns]
    y = dataframe[target_column]
    X_train, X_test, y_train, y_test = sk_train_test_split(X, y, test_size=test_size)
    X_train = X_train.astype(float)
    X_test = X_test.astype(float)
    y_train = y_train.astype(float)
    y_test = y_test.astype(float)
    return X_train, X_test, y_train, y_test


target = 'NObeyesdad'

features = [
    "Gender",
    "Age",
    "Height",
    "Weight",
    "family_history_with_overweight",
    "FAVC",
    "FCVC",
    "NCP",
    "CAEC",
    "SMOKE",
    "CH2O",
    "SCC",
    "FAF",
    "TUE",
    "CALC",
    "MTRANS"
]

feature_descriptions = {
    "Gender": "Gender",
    "Age": "Age",
    "Height": "Height",
    "Weight": "Weight",
    "family_history_with_overweight": "Family Overweight",
    "FAVC": "Eating High Caloric Food",
    "FCVC": "Eating Vegetables",
    "NCP": "Daily Meals Count",
    "CAEC": "Eating Between Meals",
    "SMOKE": "Smoke",
    "CH2O": "Drinking Water Daily",
    "SCC": "Monitoring Calories Daily",
    "FAF": "Physical Activity",
    "TUE": "Time Spending with Technology",
    "CALC": "Alcohol Consumption",
    "MTRANS": "Transportation Type"
}


def get_most_important_features(importances, feature_names, top_n):
    feature_importances = pd.Series(importances, index=feature_names)
    most_important_top_n_features = list(feature_importances.nlargest(top_n).to_dict().keys())
    return most_important_top_n_features


