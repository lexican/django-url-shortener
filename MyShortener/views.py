from django.shortcuts import render, redirect
from .models import Short_urls
from .forms import UrlForm
from .shortener import shortener


def index(request, token):
    long_url = Short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)


def make(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if Short_urls.objects.filter(long_url = request.POST['long_url']):
            short_url = Short_urls.objects.get(long_url = request.POST['long_url'])
            context = {
                'form': form,
                'a': short_url.short_url,
            }
            return render(request, 'index.html', context)
        else:
            if form.is_valid():
                NewUrl = form.save(commit=False)
                a = shortener().issue_token()
                NewUrl.short_url = a
                NewUrl.save()
            else:
                form = UrlForm()
                a = "Invalid Url"
    context = {
        'form': form,
        'a': a,
    }
    return render(request, 'index.html', context)