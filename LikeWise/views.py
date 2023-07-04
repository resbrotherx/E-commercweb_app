from django.shortcuts import render

def terms(request):
    return render(request, 'terms.html')


def coming_soon(request):
    return render(request, 'coming-soon.html')