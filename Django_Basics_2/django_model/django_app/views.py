from django.shortcuts import render


# Create your views here.
def index(request):
    my_dict={'insert_content':"HELLO FROM DJANGO APP"}

    return render(request, 'django_app/index.html' , context=my_dict)
