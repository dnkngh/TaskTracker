from django.shortcuts import render


def index(request):
    template = 'core/index.html'
    return render(request, template)


def index_yandex(request):
    template = 'core/index_yandex.html'
    return render(request, template)
