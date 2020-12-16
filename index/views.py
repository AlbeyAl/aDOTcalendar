from django.shortcuts import render


def index(request):
    context_dict = {'current_app': 'calendar'}

    return render(request, 'index/index.html', context=context_dict)
