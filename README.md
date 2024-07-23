README file to explain the  CI/CD pipeline for building and pushing Docker images. This README also includes a step-by-step guide for ML engineers on how to reuse this repository to build Docker images with their own Python module.

This repository contains a GitHub Actions CI/CD pipeline to automate the process of building Docker images and pushing them to a Docker repository.

The CI/CD pipeline is triggered on every push to the `main` branch and on pull requests to the `main` branch. The pipeline performs the following tasks:

      1, Checks out the code from the repository.
      2, Builds a Docker image using the provided Dockerfile.
      3, Pushes the Docker image to a Docker repository.

Prerequisites:

    Before you begin, ensure you have the following:
    
          1, Docker installed on your local machine.
          2, A Docker Hub account or access to another Docker repository.
          
Checks out the code from the repository and create secret for Docker login
    
          1, git clone https://github.com/your-username/<your-repo.git>
          2, cd <your-repo>
          3, Go to the "Settings" tab of your forked repository on GitHub.
          4, Click on "Secrets" in the sidebar.
          5, Add the following secrets:
             DOCKER_USERNAME: Your Docker Hub username.
             DOCKER_PASSWORD: Your Docker Hub password.

Builds a Docker image using the provided Dockerfile.

      To create your own Docker image using your Python file, follow these steps:
      
          1, Create a Python file: Create a Python file named <name>.py with your ML code.
          2, Modify the Dockerfile: Ensure the Dockerfile is set up to copy your Python file into the image.

                    Dockerfile:
                    
                    FROM python:3.12.4-alpine3.20
                    LABEL Maintainer="Arun"
                    WORKDIR /usr/app/src
                    RUN pip3 install flask
                    COPY ./<name>.py ./
                    EXPOSE 5000
                    CMD ["python3", "./ml.py"]

Pushes the Docker image to a Docker repository:
          
                    git add ml.py Dockerfile
                    git commit -m "Add ML Python file and Dockerfile"
                    git push origin main

           1, Trigger the CI/CD Pipeline: The GitHub Actions pipeline will automatically build and push the Docker image to your Docker repository.
           2, Once the pipeline successfully completes, your Docker image will be available in your Docker repository.

      
