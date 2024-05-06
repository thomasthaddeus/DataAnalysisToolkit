"""model_evaluator.py

This module provides a class, ModelEvaluator, for evaluating the performance of
machine learning models. It leverages scikit-learn's metrics to compute key
evaluation metrics such as confusion matrix, precision, and recall.

ModelEvaluator is designed to be initialized with a trained model and a test
dataset (features and labels). It can compute and return the confusion matrix,
precision score, and recall score of the model based on its predictions on the
test dataset. These metrics are crucial for understanding the model's
performance, particularly in classification tasks.

Returns:
    None: This module does not return anything but provides a class that can be
    instantiated for model evaluation.
"""

from sklearn.metrics import confusion_matrix, precision_score, recall_score


class ModelEvaluator:
    """
    A class for evaluating machine learning models.

    This class provides methods to compute key evaluation metrics for a given
    machine learning model. It is initialized with a model and test data and
    can compute the confusion matrix, precision, and recall of the model.

    Attributes:
        model (estimator): The machine learning model to be evaluated.
        X_test (array-like): The test features.
        y_test (array-like): The true labels for the test data.
        predictions (array-like): Predictions made by the model on the test
        features.
    """

    def __init__(self, model, X_test, y_test):
        """
        Constructs all the necessary attributes for the ModelEvaluator object.

        Args:
            model (estimator): The machine learning model to be evaluated.
            X_test (array-like): The test features.
            y_test (array-like): The true labels for the test data.
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.predictions = model.predict(X_test)

    def get_confusion_matrix(self):
        """
        Computes the confusion matrix for the model's predictions.

        The confusion matrix is a useful tool to understand the performance of
        a classification model, showing the correct and incorrect predictions
        across different classes.

        Returns:
            numpy.ndarray: A confusion matrix of shape (n_classes, n_classes),
            where n_classes is the number of unique classes in the test data.
        """
        return confusion_matrix(self.y_test, self.predictions)

    def get_precision(self):
        """
        Computes the precision score for the model's predictions.

        Precision is the ratio of correctly predicted positive observations to
        the total predicted positives. It is a measure of a classifier's
        exactness.

        Returns:
            float: The precision score of the model for the test data.
        """
        return precision_score(self.y_test, self.predictions)

    def get_recall(self):
        """
        Computes the recall score for the model's predictions.

        Recall (also known as sensitivity) is the ratio of correctly predicted
        positive observations to all observations in the actual class. It is a
        measure of a classifier's completeness.

        Returns:
            float: The recall score of the model for the test data.
        """
        return recall_score(self.y_test, self.predictions)
