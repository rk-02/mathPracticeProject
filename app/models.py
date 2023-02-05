from django.db import models

class User(models.Model):
    name = models.CharField("Имя Фамилия", max_length=150)
    login = models.CharField("Логин", max_length=150)
    password = models.CharField("Пароль", max_length=150)
    classNum = models.IntegerField("Класс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Subject(models.Model):
    name = models.CharField("Название", max_length=150)
    classNum = models.IntegerField("Класс")
    presName = models.CharField("Путь к презентации", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

class Practice(models.Model):
    idSubj = models.ForeignKey(Subject, on_delete=models.CASCADE)

class PracticalTask(models.Model):
    idPractice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    TaskText = models.TextField("Задание")

class AnsPract(models.Model):
    idTask = models.ForeignKey(PracticalTask, on_delete=models.CASCADE)
    ans = models.IntegerField("Ответ")

class StudAnsPract(models.Model):
    idStud = models.ForeignKey(User, on_delete=models.CASCADE)
    idTask = models.ForeignKey(PracticalTask, on_delete=models.CASCADE)
    ans1 = models.IntegerField("Ответ 1")
    ans2 = models.IntegerField("Ответ 2")
    ans3 = models.IntegerField("Ответ 3")
    ans4 = models.IntegerField("Ответ 4")
    rightAns = models.IntegerField("Правильный ответ")

class Exam(models.Model):
    idSubj = models.ForeignKey(Subject, on_delete=models.CASCADE)

class ExamTask(models.Model):
    idExam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    TaskText = models.TextField("Задание")

class AnsExam(models.Model):
    idTask = models.ForeignKey(ExamTask, on_delete=models.CASCADE)
    ans = models.IntegerField("Ответ")

class StudAnsExam(models.Model):
    idStud = models.ForeignKey(User, on_delete=models.CASCADE)
    idTask = models.ForeignKey(ExamTask, on_delete=models.CASCADE)
    ans1 = models.IntegerField("Ответ 1")
    ans2 = models.IntegerField("Ответ 2")
    ans3 = models.IntegerField("Ответ 3")
    ans4 = models.IntegerField("Ответ 4")
    rightAns = models.IntegerField("Правильный ответ")

