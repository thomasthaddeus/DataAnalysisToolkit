# Documentation for `model` Directory of DataAnalysisToolkit

The `model` directory in the DataAnalysisToolkit contains tools for feature engineering and model evaluation, essential for the preparation and assessment of machine learning models.

## Feature Engineer (`feature_engineer.py`)

### Overview

The `FeatureEngineer` class is designed to perform various feature engineering tasks on datasets. Feature engineering enhances the dataset by creating new features from existing ones, improving model performance and providing deeper insights.

### Usage

```python
engineer = FeatureEngineer(df)
engineer.binning('age', bins=[0, 18, 65, 100], labels=['child', 'adult', 'senior'])
engineer.create_interaction('height', 'weight')
```

### Methods

- `__init__(self, data)`: Initialize with a dataset for feature engineering.
- `binning(self, column, bins, labels)`: Perform binning on a specified column, transforming continuous data into categorical bins.
- `create_interaction(self, column1, column2)`: Create an interaction feature by multiplying two columns.

### Example

Binning a Numeric Column and Creating an Interaction Feature:

```python
feature_engineer = FeatureEngineer(df)
feature_engineer.binning('income', bins=[0, 50000, 100000, 150000], labels=['low', 'medium', 'high'])
feature_engineer.create_interaction('age', 'income')
```

---

## Model Evaluator (`model_evaluator.py`)

### Overview Model Evaluator

The `ModelEvaluator` class leverages scikit-learn's metrics to compute key evaluation metrics for machine learning models. This includes metrics like confusion matrix, precision, and recall, essential for understanding a model's performance.

### Usage Model Evaluator

```python
evaluator = ModelEvaluator(model, X_test, y_test)
conf_matrix = evaluator.get_confusion_matrix()
precision = evaluator.get_precision()
recall = evaluator.get_recall()
```

### Methods Model Evaluator

- `__init__(self, model, X_test, y_test)`: Initialize the evaluator with a trained model and test data.
- `get_confusion_matrix(self)`: Compute the confusion matrix for the model's predictions.
- `get_precision(self)`: Compute the precision score for the model's predictions.
- `get_recall(self)`: Compute the recall score for the model's predictions.

### Example Model Evaluator

Evaluating a Classification Model:

```python
model_evaluator = ModelEvaluator(trained_model, X_test, y_test)
print("Confusion Matrix:", model_evaluator.get_confusion_matrix())
print("Precision:", model_evaluator.get_precision())
print("Recall:", model_evaluator.get_recall())
```

---

These tools in the `model` directory facilitate the preparation and evaluation of machine learning models, providing functionality to enhance datasets through feature engineering and to assess model performance with key metrics.
