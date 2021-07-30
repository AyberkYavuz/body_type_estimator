from xgboost.sklearn import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from core.decorators import execution_time
from core.file_handler import PickleHandler
from sklearn.metrics import classification_report


class XgboostModelCreator:
    """Xgboost Model Creator
    Attributes:
        base_xgboost_classifier: trained XGBClassifier, default=None. This attribute will be initialized,
                                                             when create_base_xgboost_model method is called.
        randomized_search_object: trained RandomizedSearchCV, default=None. This attribute will be initialized,
                                                                   when create_randomized_search_cv_model method is called.
    """
    def __init__(self):
        """Constructs all the necessary attributes for the xgboost_model_creator object.
        """
        self.base_xgboost_classifier = None
        self.randomized_search_object = None

    @execution_time("seconds")
    def create_base_xgboost_model(self, X_train, y_train, n_estimators=200, max_depth=5,
                                  learning_rate=0.01, n_jobs=-1):
        """Trains xgboost classifier and initializes base_xgboost_classifier attribute.
        Args:
            X_train: it can be list, numpy array, scipy-sparse matrix or pandas dataframe.
            y_train: it can be list, numpy array, pandas series.
            n_estimators : int. Number of boosted trees to fit.
            max_depth: int. Maximum tree depth for base learners.
            learning_rate: float. Boosting learning rate (xgb's "eta").
            n_jobs : int. Number of parallel threads used to run xgboost.
        """
        xgb_classifier = XGBClassifier(n_estimators=n_estimators, max_depth=max_depth,
                                       learning_rate=learning_rate, n_jobs=n_jobs)
        model = xgb_classifier.fit(X_train, y_train)
        self.base_xgboost_classifier = model

    @execution_time("minutes")
    def create_randomized_search_cv_model(self, grid, X_train, y_train,
                                          n_jobs=None, n_iter=10, cv=None):
        """Trains RandomizedSearchCV and initializes randomized_search_object attribute.
        Args:
            grid: dict. Parameter grid.
            X_train: it can be list, numpy array, scipy-sparse matrix or pandas dataframe.
            y_train: it can be list, numpy array.
            n_jobs: int, default=None.
                Number of jobs to run in parallel.
                ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
                ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
                for more details.
            n_iter: int, default=10. Number of parameter settings that are produced.
            cv : int, cross-validation generator or an iterable, default=None
                Determines the cross-validation splitting strategy.
                Possible inputs for cv are:
                - None, to use the default 5-fold cross validation,
                - integer, to specify the number of folds in a `(Stratified)KFold`,
                - :term:`CV splitter`,
                - An iterable yielding (train, test) splits as arrays of indices.
                For integer/None inputs, if the estimator is a classifier and ``y`` is
                either binary or multiclass, :class:`StratifiedKFold` is used. In all
                other cases, :class:`KFold` is used.
                Refer :ref:`User Guide <cross_validation>` for the various
                cross-validation strategies that can be used here.
                .. versionchanged:: 0.22
                    ``cv`` default value if None changed from 3-fold to 5-fold.
        """
        classifier = XGBClassifier(n_jobs=n_jobs)
        randomized_search_cv = RandomizedSearchCV(classifier, param_distributions=grid, n_jobs=n_jobs,
                                                  n_iter=n_iter, cv=cv)
        randomized_search_cv_model = randomized_search_cv.fit(X_train, y_train)
        self.randomized_search_object = randomized_search_cv_model

    def save_model(self, model_type, path):
        """Saves the model.
        Args:
            model_type: str. It can be 'base_model' or 'randomized_search_object'.
            path: str. Model path.
        """
        pickle_handler = PickleHandler()
        if model_type == "base_model":
            pickle_handler.save_object(path, self.base_xgboost_classifier)
        elif model_type == "randomized_search_object":
            pickle_handler.save_object(path, self.randomized_search_object)

    @staticmethod
    def load_model(path):
        """Loading Model
        Args:
            path: str. Model path
        Returns:
            Trained model
        """
        pickle_handler = PickleHandler()
        return pickle_handler.load_object(path)

    @staticmethod
    def display_classification_report(model, X_test, y_test):
        """Displays classification report.
        Args:
            model: XGBClassifier or RandomizedSearchCV model
            X_test: it can be list, numpy array, scipy-sparse matrix or pandas dataframe.
            y_test: it can be list, numpy array, pandas series.
        """
        y_pred = model.predict(X_test)
        print(classification_report(y_test, y_pred))

