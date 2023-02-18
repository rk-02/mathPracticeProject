from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from .models import Subject

user = ''

def auth(request):
    if request.method == 'POST':
        name = request.POST.get("login")
        password = request.POST.get("pass")
        user = User.objects.create_user(name, '', password)
        return redirect('../index/')
    else:
        return render(request, 'auth.html')

def index(request):
    if request.method == 'GET':
        return redirect('index.html')

class SubjectView(View):

    def get(self, request):
        subjects = Subject.objects.all()
        return render(request, "index.html", {"subj_list": subjects})