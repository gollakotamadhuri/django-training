from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)

from basic_app.models import School, Student


# Create your views here.
class IndexView(TemplateView):
    template_name = "basic_app/index.html"


class HelpView(TemplateView):
    template_name = "basic_app/help.html"


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetailsView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = "basic_app/school_details.html"

class SchoolCreateView(CreateView):
    model = School
    fields = ['name','principal','location']
    template_name = "basic_app/school_form.html"

class SchoolUpdateView(UpdateView):
    model = School
    fields= ['name','principal']

class SchoolDeleteView(DeleteView):
    model= School
    success_url = reverse_lazy("basic_app:schools")
