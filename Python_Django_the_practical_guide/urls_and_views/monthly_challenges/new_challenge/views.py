from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges_dictionary = {
    "january":"Build a CLI tool (e.g., a task tracker) using argparse, pathlib, and OOP best practices.",
    "february":"Analyze a real dataset (e.g., from Kaggle). Use pandas, numpy, and matplotlib to produce an insightful report.",
    "march":"Build an asynchronous REST API with FastAPI and async SQLAlchemy. Add JWT auth and testing with pytest.",
    "april": "Design a PostgreSQL schema, use Alembic migrations, and connect with SQLAlchemy ORM.",
    "may" : "Write a CI/CD pipeline (GitHub Actions or GitLab CI) that runs tests, builds Docker images, and pushes to a registry.",
    "june": "Containerize your app with Docker, write a production-grade Dockerfile, and deploy on AWS ECS or GCP Cloud Run.",
    "july": "Train a scikit-learn model on structured data. Evaluate, tune hyperparameters, and serialize with joblib.",
    "august": "Fine-tune a small Hugging Face model (e.g., sentiment classifier) and serve via FastAPI.",
    "september": "Connect a React (or Svelte) frontend to your FastAPI backend using REST/GraphQL.",
    "october": "Add full coverage testing, use pytest-cov, tox, and mypy for type checking.",
    "november": "Define your infra using Terraform (provision EC2, RDS, S3, etc.), and automate with Ansible.",
    "december": "Create a model deployment pipeline (MLflow + Docker + CI/CD). Deploy a live endpoint."
}


# Create your views here.
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges_dictionary[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported, pal!")

def monthly_challenge_int(request, month):
    return HttpResponse(month)