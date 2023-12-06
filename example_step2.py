# **Step 2: Deploy the Model**

# Once the model is trained, you can deploy it as a web service.

pythonCopy code
# Deploy the best model as a web service
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.conda_dependencies import CondaDependencies

# Register the model
model = run.register_model(description='Best AutoML model')

# Create a deployment configuration
aciconfig = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Define dependencies required by the scoring script
myenv = CondaDependencies.create(conda_packages=['scikit-learn'])

# Set runtime to Python
myenv.python.conda_dependencies = ['python=3.6.2']

# Save the environment configuration to a file
env_file_path = 'env.yml'
with open(env_file_path, 'w') as f:
    f.write(myenv.serialize_to_string())

# Deploy the model as a web service
service = Model.deploy(
    workspace=ws,
    name='your-service-name',
    models=[model],
    inference_config=inference_config,
    deployment_config=aciconfig
)

# Wait for the deployment to complete
service.wait_for_deployment(show_output=True)
