# body_type_estimator
This repository is a tutorial for all levels who want to learn how to develop end to end machine learning system.

## Machine Learning Dataset Details
[Dataset Source](https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+)
<br/>
[Dataset Details](https://www.sciencedirect.com/science/article/pii/S2352340919306985?via%3Dihub)

## Project Structure
```bash
body_type_estimator/
├── core
│   ├── __init__.py
│   ├── decorators.py
│   ├── file_handler.py
│   ├── machine_learning_handler.py
│   └── visualizer.py
├── helpers
│   ├── __init__.py
│   ├── application_helpers.py
│   └── pandas_dataframe_helpers.py
├── machine_learning_data
│   ├── body_type_estimation_data.csv
│   ├── body_type_estimation_data_selected_columns.csv
│   └── ObesityDataSet_raw_and_data_sinthetic.csv
├── models
│   ├── base_xgboost_model.pickle
│   ├── base_xgboost_model_with_selected_features.pickle
│   └── NObeyesdad_label_encoder.pickle
├── static
│   ├── css
│   │   └── materialize.min.css
│   ├── fonts
│   │   └── roboto
│   │       ├── Roboto-Bold.woff
│   │       ├── Roboto-Bold.woff2
│   │       ├── Roboto-Light.woff
│   │       ├── Roboto-Light.woff2
│   │       ├── Roboto-Medium.woff
│   │       ├── Roboto-Medium.woff2
│   │       ├── Roboto-Regular.woff
│   │       ├── Roboto-Regular.woff2
│   │       ├── Roboto-Thin.woff
│   │       └── Roboto-Thin.woff2
│   ├── img
│   │   ├── machine-learning.png
│   │   └── webapp.png
│   └── js
│       ├── initialize_form_components.js
│       ├── materialize.min.js
│       └── server_request_handler.js
├── templates
│   └── main_page.html
├── create_exploratory_data_analysis_html_file.py
├── data_transformation_for_machine_learning_model_training.py
├── feature_selection.py
├── README.md
├── web_application_backend.py
├── xgboost_base_model_creator.py
└── xgboost_base_models_comparison.py
```

## Project Tutorial Video
[Body Type Estimator Project Tutorial](https://www.youtube.com/watch?v=QwGwMftjUYI&ab_channel=AyberkYavuz)

