from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect
# Create your views here.

def hello(request):
    return render(request, 'heollo.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    return render(request, 'result.html', {'total_len':total_len,})

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(" ",""))
    return render(request, 'result.html', {
        'total_len' : total_len
        'text' : text,
        'no_blank_len' : no_blank_len,
    })