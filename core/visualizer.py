import matplotlib.pyplot as plt
import pandas as pd


class MatplotlibVisualizer:
    def show_horizontal_bar_plot(self, group_names, values, title_text, group_name_text, value_text):
        plt.barh(group_names, values)
        plt.title(title_text)
        plt.ylabel(group_name_text)
        plt.xlabel(value_text)
        plt.show()

    def show_feature_importances(self, importances, feature_names, top_n, font_size):
        plt.rcParams.update({'font.size': font_size})
        feature_importances = pd.Series(importances, index=feature_names)
        feature_importances.nlargest(top_n).plot(kind='barh')
        plt.title(str(top_n) + " Important Features")
        plt.show()

