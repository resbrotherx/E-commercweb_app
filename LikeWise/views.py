from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


def terms(request):
    return render(request, 'terms.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')