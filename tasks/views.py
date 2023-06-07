from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")



# Create your views here.
def index(request):
    if "tasks" not in request.session:
         request.session["tasks"] = []
         
    return render(request,"tasks/index.html",{
        "tasks": request.session["tasks"]
    })
    
def add(request):
    
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))

        

    return render(request, "tasks/add.html",{
        "form":NewTaskForm()
    })