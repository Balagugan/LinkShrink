from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
import string, random

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()
        URL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, 'linkshrink/index.html', {'short_code': short_code})
    return render(request, 'linkshrink/index.html')

def redirect_to_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)
