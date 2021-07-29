import pickle


class PickleHandler:
    """PickleHandler which is used for saving, loading and dumping python objects.
    """
    def save_object(self, path, obj):
        """Saves the python object.
        Args:
            path: str. Saving location of the python object.
            obj: object. Python object to be saved.
        """
        with open(path, 'wb') as handle:
            pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_object(self, path):
        """Loads the pickle file as python object.
        Args:
            path: str. Location of the pickle file.
        Returns:
            python_object: object. Python object.
        """
        with open(path, 'rb') as handle:
            python_object = pickle.load(handle)
            return python_object
