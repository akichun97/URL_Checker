from django.shortcuts import render, redirect
from myapp.models import * 
import requests

def index(request):
    urls = URL.objects.all()
    context = {'urls': urls}
    return render(request, 'index.html', context)


def url_check(request):
    if request.method == 'POST':
        url_check = request.POST.get('url')
        try:
            response = requests.get(url_check, timeout=200)
            if response.status_code == 200:
                new_url = URL.objects.create(url=url_check, is_available=True)
                return redirect('/')
            else:
                new_url = URL.objects.create(url=url_check, is_available=False)
                return redirect('/')
        except requests.exceptions.RequestException:
            new_url = URL.objects.create(url=url_check, is_available=False)
            return redirect('/')
    return render(request, '/', {'urls': URL.objects.all()})


def all_urls_check(request):
    urls = URL.objects.all()
    for url in urls:
        try:
            response = request.get(url.url, timeout=5)
            if response.ststus_code == 200:
                url.is_available = True
                url.save()
        except requests.exceptions.RequestException:
            url.is_available = False
            url.save()
    return redirect('index.html')                


# def url_add(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         new_url = URL.objects.create(url=url)
#         return redirect('index')
    
#     return render(request, 'index')