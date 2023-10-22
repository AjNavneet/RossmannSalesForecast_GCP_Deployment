# Rossmann Sales Forecast and GCP Deployment

## Project Description

Rossmann, a chain of over 3,000 drug stores across 7 European countries, faces the challenge of predicting daily sales up to six weeks in advance. 

## Objective
This project focuses on forecasting store sales, taking into account various influencing factors, such as promotions, competition, holidays, seasonality, and locality.

---

## Tech Stack

- Language: `Python`
- Cloud: `Google Cloud Platform (GCP)`
- UI: `Flask`
- Libraries: `scikit-learn`, `pandas`, `numpy`
- Code Management: `Git`, `Github`

---

## Model Deployment

We deploy the model created using Google Cloud Platform (GCP). We explore two deployment approaches:

1. Traditional Approach
2. Dockerized Approach

### Traditional Approach

In the traditional approach, we rent a cloud server, set up the necessary environment, deploy the model interface (Flask/Streamlit), and expose the required components for model deployment.

### Dockerized Approach

The Dockerized approach involves packaging the model code and configurations into a Docker image, simplifying deployment and ensuring consistency across environments.

---

## Deployment Steps

To deploy the model using GCP, follow these steps:

1. Create a source repository in GCP.
2. Set up a cloud build trigger for the GCP repository.
3. Create a Virtual Machine (VM) in GCP under "VM Instances."
4. Clone the repository in the VM.
5. Install Docker on the VM.
6. Choose one of the following deployment methods:
   
   - **Setting up a Server Inside the VM:**
     - Execute the provided commands to create and set up the server environment within the VM.
   
   - **Setting up a Server Using Docker:**
     - Pull the Docker image from GCP Container Registry.
     - Run the Docker image to deploy the model.

The necessary shell scripts are included for convenience:
- `install-docker.sh`: Installs Docker on the VM.
- `setup-new-vm.sh`: Sets up a new server inside the VM or deploys the model using Docker.

---

