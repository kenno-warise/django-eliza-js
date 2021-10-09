from django.shortcuts import render


def index(request):
    return render(request, 'eliza/index.html')


def test(request):
    return render(request, 'eliza/eliza_test.html')