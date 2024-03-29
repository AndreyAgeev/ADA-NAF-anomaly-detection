import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from datasets.basic_dataset import AbstractDataset

from pylab import rcParams
rcParams['figure.figsize'] = 14, 8


class DatasetIonosphere(AbstractDataset):
    def __init__(self):
        super().__init__()
        self._path = "/Users/andreyageev/PycharmProjects/ATIF/datasets/ionosphere_data.csv"

    def load(self):
        """https://www.kaggle.com/code/zymzym/classification-of-the-ionosphere-dataset-by-knn"""
        df = pd.read_csv(self._path)
        df.drop(columns=['column_b'], inplace=True)
        df.rename(columns={'column_ai': 'label'}, inplace=True)
        df['label'] = df.label.astype('category')
        encoding = {'g': 0, 'b': 1}
        df.label.replace(encoding, inplace=True)
        df['column_a'] = df.column_a.astype('float64')

        # fraud_data = df[df['label'] == 1]
        # norm_data = df[df['label'] == 0]
        ###########
        # import matplotlib.pyplot as plt
        # count_class = pd.value_counts(df['label'])
        # count_class.plot(kind='bar', rot=0)
        # plt.title("Class Distribution")
        # plt.xticks(range(2), ["Normal", "Fraud"])
        # plt.xlabel("Class")
        # plt.ylabel("Frequency")
        # plt.savefig("/Users/andreyageev/PycharmProjects/ATIF/image/ionosphere_dataset.jpg")
        ###############
        data, labels = df.drop('label', axis=1), df['label']
        # scaler = StandardScaler()
        # data = scaler.fit_transform(data)
        self.data = data
        self.labels = labels
        counts = pd.value_counts(labels)
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
        return "ionosphere"
