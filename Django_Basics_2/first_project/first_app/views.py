from django.http import HttpResponse
from django.shortcuts import render

from .models import AccessRecord, Topic, Webpage


# Create your views here.
def index(request):

    my_dict={'insert_me':"I am from first_app/views.py"}
    access_records = AccessRecord.objects.all()
    access_data = {'access_records': access_records}
    
    return render(request,'first_app/index.html', context=access_data)
