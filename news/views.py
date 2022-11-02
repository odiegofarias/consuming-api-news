from django.shortcuts import render
import requests
import os


API_KEY = str(os.getenv('API_KEY'))


def home(request):
    template = 'news/home.html'
    url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}'
    resp = requests.get(url)
    data = resp.json()
    articles = data['articles']

    context = {'articles': articles}

    return render(request, template, context)
