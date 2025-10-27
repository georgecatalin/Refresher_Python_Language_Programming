from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}


def index(request: any) -> HttpResponse:
    list_items = ""
    months = list(monthly_challenges_dictionary.keys())

    for month in months:
        capitalize_month = month.capitalize()
        link_info = reverse("new_challenge_path",args=[month])
        list_items += f"<li><a href=\"{link_info}\">{capitalize_month}</a></li>"
        
        response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "new_challenge/index.html", { "months" : months})

# Create your views here.
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges_dictionary[month]

        # response_data = "<h1>{}</h1>".format(challenge_text) # old version before learning about templates
        # response_data = render_to_string("new_challenge/challenge.html")
        # return HttpResponse(response_data) 

        return render(request, "new_challenge/challenge.html",{"text": challenge_text, "month" : month}) #simplified and shortened the two lines above
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

def monthly_challenge_int(request, month):
    months =list(monthly_challenges_dictionary.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>you added a non-existing month...</h1>")
    
    redirected_month = months[month - 1]
    redirect_url = reverse("new_challenge_path",args = [redirected_month])
    return HttpResponseRedirect(redirect_url)
