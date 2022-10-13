from django.shortcuts import render

from . import forms


# Create your views here.
def index(request):
    return render(request, "basicapp/index.html", context={'hello':'hello'})


def formpage(request):
    form = forms.BasicForm()
    print(request)

    if request.method == 'POST':
        form = forms.BasicForm(request.POST)

        if form.is_valid():
            print('NAME: ', form.cleaned_data['name'])
            print("EMAIL: ", form.cleaned_data['email'])
            print("TEXT:", form.cleaned_data['text'])

    return render(request, "basicapp/form_page.html", context={'forms': form})
