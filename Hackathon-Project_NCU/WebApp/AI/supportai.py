import pandas as pd
from kmodes.kmodes import KModes
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
form_data = pd.read_csv(os.path.join(current_directory, "testdata.csv"))


def run_clustering():
    form_data_matrix = form_data.to_numpy()
    kmodes = KModes(n_clusters=2, random_state=0)
    global predictions
    predictions = kmodes.fit_predict(form_data_matrix)


def train_classifier():

    # encoder to convert categorical data.
    encode_label = preprocessing.LabelEncoder()

    for column in form_data:
        form_data[column] = encode_label.fit_transform(form_data[column])

    X_train, X_test, y_train, y_test = train_test_split(
        form_data, predictions, test_size=0.2, random_state=0)

    global logistic_regression_model
    logistic_regression_model = LogisticRegression()
    logistic_regression_model.fit(X_train, y_train)


def assign_support_group(answers: dict):
    sample = np.array([int(answers["one"]), int(answers["two"]), int(answers["three"]), int(answers["four"]),
                       int(answers["five"]), int(answers["six"]), int(answers["seven"]), int(answers["eight"]), int(answers["nine"])])

    group = logistic_regression_model.predict([sample])

    return group
