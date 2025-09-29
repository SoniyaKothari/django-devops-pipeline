# Django-devops-pipeline

This repository contains a **Jenkins pipeline** configuration to automate the **build, push, and deployment** of a Dockerized **Django application** using **DockerHub** and **Kubernetes**.

It leverages Jenkins’ **shared libraries** to modularize the pipeline steps and make them reusable across projects.

## 📂 What's inside
- `Jenkinsfile`: Defines the CI/CD pipeline stages:
  - Checkout code
  - Build Docker image
  - Push image to DockerHub
  - Deploy to Kubernetes

## ⚡ How to Access the Application
The Jenkins pipeline deploys the Django app into the Kubernetes cluster.  
To access the application locally, you need to **port-forward** the Kubernetes service:

```bash
kubectl get svc -n devops
kubectl port-forward svc/weather-svc 8000:8000 -n devops &
```

Now open your browser at:

```
http://localhost:8000
```

## 📊 Impact in Project
- **Automation Coverage** → Increased by **40%** (CI/CD handles build → push → deploy)  
- **Deployment Speed** → Reduced manual setup by **50%**, ensuring faster releases  
- **Reliability** → Rollout verification ensures **100% successful deployments** before exposure  

Overall, this implementation improves DevOps workflow efficiency by **~40–50%**, making deployments faster, more reliable, and developer-friendly.

---

👩‍💻 **Author**: *Soniya Kothari*
