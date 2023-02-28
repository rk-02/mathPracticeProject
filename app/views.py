from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.base import View
from .models import Subject
from .models import User as us
from .models import Practice, PracticalTask, AnsPract, Exam, ExamTask

def practice_detail(request):
    if request.method == 'POST':
        subjects = Subject.objects.all()
        current_user = us.objects.filter(login=(request.session.get('user_info'))['username'])
        subj_id = request.POST.get('subj_id')
        practice = Practice.objects.get(idSubj=subj_id)
        practical_tasks = PracticalTask.objects.filter(idPractice=practice.id)
        data = []
        for task in practical_tasks:
            ans_pract = AnsPract.objects.get(idTask=task.id)
            task_data = {
                'task_id': task.id,
                'task_text': task.TaskText,
                'ans1': ans_pract.ans1,
                'ans2': ans_pract.ans2,
                'ans3': ans_pract.ans3,
                'ans4': ans_pract.ans4,
                'right_ans': ans_pract.rightAns,
            }
            data.append(task_data)
        return render(request, 'index.html', {"subj_list": subjects,
                                              "currentUser": current_user[0],
                                              'data': data,
                                              'type_data': 'practice'})
    return render(request, 'index.html')

def exam_detail(request):
    subjects = Subject.objects.all()
    current_user = us.objects.filter(login=(request.session.get('user_info'))['username'])
    subj_id = request.POST.get('subj_id')
    exam = Exam.objects.get(idSubj=subj_id)
    exam_tasks =ExamTask.objects.filter(idExam=exam.id)
    data = []
    for task in exam_tasks:
        task_data = {
            'task_id': task.id,
            'task_text': task.TaskText
        }
        data.append(task_data)
    return render(request, 'index.html', {"subj_list": subjects,
                                          "currentUser": current_user[0],
                                          'data': data,
                                          'type_data': 'exam'})

def auth(request):
    if request.method == 'POST':
        name = request.POST.get("login")
        password = request.POST.get("pass")
        if us.objects.filter(login=name, password=password):
            if not User.objects.filter(username=name):
                user = User.objects.create_user(name, '', password)
                user.save()
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                request.session['user_info'] = {'username': name, 'email': user.email}
            return redirect('../index/')
        else:
            return render (request, 'auth.html')
    else:
        return render(request, 'auth.html')

def index(request):
    if request.method == 'GET':
        return redirect('index.html')

class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        current_user = us.objects.filter(login=(request.session.get('user_info'))['username'])
        return render(request, "index.html", {"subj_list": subjects, "currentUser": current_user[0]})
