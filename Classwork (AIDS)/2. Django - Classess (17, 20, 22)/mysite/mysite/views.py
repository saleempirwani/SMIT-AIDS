from django.http import HttpResponse
from django.shortcuts import render

from .textUtils.textUtils import text_utils

def index(request):
    return render(request, 'index.html', {
        'name': 'Saleem'
    })
    # return HttpResponse('Hello World')


def analyzed(request):
    text = request.POST.get('text', '')
    # print(text)
    remove_punc = request.POST.get('removePunc', 'off')
    lower_case = request.POST.get('lowerCase', 'off')
    upper_case = request.POST.get('upperCase', 'off')


    params = text_utils(text, remove_punc,  upper_case, lower_case)

    return render(request, 'analyzed.html', params)
