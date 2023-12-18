# Azure ML + ADF: Streamlining Predictive Analytics

## Overview

This repository demonstrates the integration of Azure Machine Learning (Azure ML) with Azure Data Factory (ADF) to streamline predictive analytics workflows. The solution involves training a machine learning model using Azure ML, deploying it as a web service, and seamlessly integrating it into data pipelines orchestrated by Azure Data Factory.

## Getting Started

### Prerequisites

- An Azure subscription
- Azure Machine Learning workspace
- Azure Data Factory instance

### Training the Model

1. Open the `train_model.py` script in the `azure_ml` folder.
2. Configure Azure ML workspace connection in the script.
```python
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
```

3. Adjust dataset names, labels, and AutoML settings.
4. Run the script to train the model.

### Deploying the Model

1. Open the `deploy_model.py` script in the `azure_ml` folder.
2. Update the model registration details and deployment configuration.
3. Execute the script to deploy the model as a web service.

### Integrating with ADF

1. Configure your ADF pipeline using the pseudocode provided in the `adf_pipeline.json` file.
2. Ensure that the necessary permissions and linked services are set up.
3. Run the ADF pipeline to invoke the Azure ML web service within your data workflow.

## File Structure

- `azure_ml/`: Contains scripts for training and deploying the Azure ML model.
  - `train_model.py`: Script for training the machine learning model.
  - `deploy_model.py`: Script for deploying the trained model as a web service.
- `adf_pipeline.json`: ADF pipeline pseudocode for integrating the Azure ML web service into data workflows.

## Contributing

Feel free to contribute to enhance and expand the functionality of this repository. Follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
