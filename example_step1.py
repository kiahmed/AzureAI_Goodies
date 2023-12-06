#In this example, we'll train a machine learning model using Azure Machine Learning,
#deploy the model, and then use it in an Azure Data Factory pipeline for making predictions.

#Step 1: Train a Machine Learning Model using Azure Machine Learning

pythonCopy code
# Python code to train a machine learning model using Azure Machine Learning

from azureml.core import Workspace, Experiment, Dataset
from azureml.train import automl

# Connect to Azure Machine Learning workspace
ws = Workspace.from_config()

# Load dataset
dataset = Dataset.get_by_name(ws, name='your_dataset_name')
train_data = dataset.drop_columns(columns=['target_column'])
label_column = 'target_column'

# Create an experiment
experiment = Experiment(workspace=ws, name='your_experiment_name')

# Configure AutoML settings
automl_settings = {
    "task": "classification",
    "primary_metric": "accuracy",
    "enable_early_stopping": True,
    "iteration_timeout_minutes": 10,
    "iterations": 10,
    "featurization": 'auto',
}

# Run AutoML experiment
automl_config = automl.AutoMLConfig(
    task='classification',
    training_data=train_data,
    label_column_name=label_column,
    **automl_settings
)

run = experiment.submit(automl_config)
run.wait_for_completion(show_output=True)
