from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def help(request):
    my_dict={'help_me':"Help Page"}
    return render(request, 'AppTwo/help.html', context=my_dict)

def index(request):
    return HttpResponse("<em>AppTwo</em>")
