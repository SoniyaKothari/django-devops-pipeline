# django-devops-pipeline

This repository contains a **Jenkins pipeline** configuration to automate the **build, push, and deployment** of a Dockerized **Django application** using **DockerHub** and **Kubernetes**.

It leverages Jenkins’ **shared libraries** to modularize the pipeline steps and make them reusable across projects.

## 🚀 Features
- Builds the Django app into a Docker image.
- Pushes the image to DockerHub.
- Deploys the app to a Kubernetes cluster.
- Uses a clean and maintainable pipeline structure with shared libraries.

## 📂 What's inside
- `Jenkinsfile`: Defines the CI/CD pipeline stages.
- `libs/`: Contains reusable functions like `build()`, `pushDockerImage()`, and `deployToK8s()`.

## 📈 Why use this?
- Simplifies Django application deployments.
- Promotes best practices in DevOps with Docker and Kubernetes.
- Enables scalability and automation in development workflows.
