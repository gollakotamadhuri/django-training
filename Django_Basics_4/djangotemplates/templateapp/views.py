from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'templateapp/index.html',context={'name':"hermoine granger",'age':'26','job':'Potions Hogwards'})


def other(request):
    return render(request, 'templateapp/other.html')


def relative(request):
    return render(request, 'templateapp/relative_url_templates.html')
