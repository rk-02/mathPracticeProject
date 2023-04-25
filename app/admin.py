from django.contrib import admin
from .models import User, Subject, Practice, PracticalTask, Exam, ExamTask, StudAnsExam

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Practice)
admin.site.register(PracticalTask)
admin.site.register(Exam)
admin.site.register(ExamTask)
admin.site.register(StudAnsExam)


