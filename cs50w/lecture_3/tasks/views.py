from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskFrom(forms.Form):
    task = forms.CharField(label='New Task')

# Create your views here.
def index(request):
    # check if there is no session in our session and ..
    # if there is none add a new one
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })

def add(request):
    if request.method == "POST":
        form = NewTaskFrom(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))
    return render(request, 'tasks/add.html', {
        # plugs in a form value to be used in my html 
        "form": NewTaskFrom()
    })