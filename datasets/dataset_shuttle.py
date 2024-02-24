import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from datasets.basic_dataset import AbstractDataset


class DatasetShuttle(AbstractDataset):
    def __init__(self):
        super().__init__()

    def load(self):
        """From DIF"""
        data = pd.read_csv("/Users/andreyageev/PycharmProjects/NAF/dataset_folder/shuttle_16.csv")
        data = data.astype(float)

        data, labels = data.drop("label", axis=1), data["label"]
        fraud = labels[labels==1]
        normal = labels[labels==0]

        # scaler = MinMaxScaler()
        # data = scaler.fit_transform(data)
        self.data = data
        self.labels = labels
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.labels, test_size=0.33, random_state=42)
        self.X_train = X_train
        self.X_test = X_test
        scaler = StandardScaler()
        scaler.fit(self.X_train)
        self.X_train = scaler.transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)
        self.y_train = y_train.values
        self.y_test = y_test.values


    # def cross_validation_split(self, k: int):
    #     X_train, X_test, y_train, y_test = train_test_split(self.data, self.labels, test_size=0.33, random_state=k)
    #     self.X_train = X_train
    #     self.X_test = X_test
    #     scaler = StandardScaler()
    #     scaler.fit(self.X_train)
    #     self.X_train = scaler.transform(self.X_train)
    #     self.X_test = scaler.transform(self.X_test)
    #     self.y_train = y_train.values
    #     self.y_test = y_test.values

    def plot_dataset(self, data, y, save_path):
        pass

    def get_name(self) -> str:
        return "shuttle"

