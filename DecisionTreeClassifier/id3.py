# Run this program on your local python
# interpreter, provided you have installed
# the required libraries.

# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
# Function importing Dataset


def importdata():
    balance_data = pd.read_csv('car.data',
                               sep=',', header=None)

    # Printing the dataswet shape
    print("Dataset Lenght: ", len(balance_data))
    print("Dataset Shape: ", balance_data.shape)

    # Printing the dataset obseravtions
    # print("Dataset: ", balance_data.head())
    return balance_data

# Function to split the dataset


def splitdataset(balance_data):

    # Seperating the target variable
    X = balance_data.values[:, 0:6]
    Y = balance_data.values[:, 6]

    labelencoder = LabelEncoder()
    for i in range(6):
        X[:, i] = labelencoder.fit_transform(X[:, i])
    # X[:, 1] = labelencoder.fit_transform(X[:, 1])
    # X[:, 2] = labelencoder.fit_transform(X[:, 2])
    #     X[:, 3] = labelencoder.fit_transform(X[:, 3])
    #     X[:, 4] = labelencoder.fit_transform(X[:, 4])
    #     X[:, 5] = labelencoder.fit_transform(X[:, 5])

    # Spliting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2)

    # change test_size to 0.3 and 0.2 for using train set as 70% and 80% of total data.

    return X, Y, X_train, X_test, y_train, y_test

# Function to perform training with giniIndex.


def train_using_gini(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      max_depth=6, min_samples_leaf=1)

    # Performing training

    clf_gini.fit(X_train, y_train)

    return clf_gini

# Function to perform training with entropy.


def tarin_using_entropy(X_train, X_test, y_train):

    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=6, min_samples_leaf=1)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


# Function to make predictions
def prediction(X_test, clf_object):

    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    # print("Predicted values:")
    # print(y_pred)
    return y_pred

# Function to calculate accuracy


def cal_accuracy(y_test, y_pred):

    print("Confusion Matrix: ",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred)*100)

    print("Report : ",
          classification_report(y_test, y_pred))

    return accuracy_score(y_test, y_pred)*100
# Driver code


def main():
    avg_acc_gini = 0
    av_acc_entropy = 0
    # Building Phase
    data = importdata()

    for i in range(20):
        X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
        # print(X_train, y_train)
        clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
        clf_gini = train_using_gini(X_train, X_test, y_train)

        # Operational Phase
        print("Results Using Gini Index:")

        # Prediction using gini
        y_pred_gini = prediction(X_test, clf_gini)
        avg_acc_gini += cal_accuracy(y_test, y_pred_gini)

        print("Results Using Entropy:")
        # Prediction using entropy
        y_pred_entropy = prediction(X_test, clf_entropy)
        av_acc_entropy += cal_accuracy(y_test, y_pred_entropy)

    avg_acc_gini = avg_acc_gini/20
    av_acc_entropy = av_acc_entropy/20

    print("Average Accuracy using Gini index after 20 iterations: ", avg_acc_gini)
    print("Average Accuracy using Entropy after 20 iterations: ", av_acc_entropy)


# Calling main function
if __name__ == "__main__":
    main()
