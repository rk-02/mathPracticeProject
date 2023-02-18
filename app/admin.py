from django.contrib import admin
from .models import User, Subject, Practice, PracticalTask, AnsPract, StudAnsPract, Exam, ExamTask, AnsExam, StudAnsExam

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Practice)
admin.site.register(PracticalTask)
admin.site.register(AnsPract)
admin.site.register(StudAnsPract)
admin.site.register(Exam)
admin.site.register(ExamTask)
admin.site.register(AnsExam)
admin.site.register(StudAnsExam)


