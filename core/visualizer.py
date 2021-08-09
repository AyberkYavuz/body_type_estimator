import matplotlib.pyplot as plt
import pandas as pd


class MatplotlibVisualizer:
    """Container of matplotlib methods.
    """
    def show_feature_importances(self, importances, feature_names, top_n, font_size):
        """Visualizes tree based algorithms feature importances.
        Args:
            importances: numpy array or list. Feature importances of tree based machine learning model.
            feature_names: list. Names of important features
            top_n: int. Feature set size.
            font_size: int. Label font sizes of the plot.
        """
        plt.rcParams.update({'font.size': font_size})
        feature_importances = pd.Series(importances, index=feature_names)
        feature_importances.nlargest(top_n).plot(kind='barh')
        plt.title(str(top_n) + " Feature Columns Importances")
        plt.show()

