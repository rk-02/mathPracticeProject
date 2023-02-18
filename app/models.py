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

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практики"

class PracticalTask(models.Model):
    idPractice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    TaskText = models.TextField("Задание")

    class Meta:
        verbose_name = "Практическое задание"
        verbose_name_plural = "Практические задания"

class StudAnsPract(models.Model):
    idStud = models.ForeignKey(User, on_delete=models.CASCADE)
    idTask = models.ForeignKey(PracticalTask, on_delete=models.CASCADE)
    ans = models.IntegerField("Ответ")

    class Meta:
        verbose_name = "Ответ ученика на практическое задание"
        verbose_name_plural = "Ответы ученика на практические задания"


class AnsPract(models.Model):
    idTask = models.ForeignKey(PracticalTask, on_delete=models.CASCADE)
    ans1 = models.IntegerField("Ответ 1")
    ans2 = models.IntegerField("Ответ 2")
    ans3 = models.IntegerField("Ответ 3")
    ans4 = models.IntegerField("Ответ 4")
    rightAns = models.IntegerField("Правильный ответ")
    class Meta:
        verbose_name = "Ответ на практическое задание"
        verbose_name_plural = "Ответы на практические задания"

class Exam(models.Model):
    idSubj = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"

class ExamTask(models.Model):
    idExam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    TaskText = models.TextField("Задание")

    class Meta:
        verbose_name = "Задание экзамена"
        verbose_name_plural = "Задания экзамена"

class StudAnsExam(models.Model):
    idStud = models.ForeignKey(User, on_delete=models.CASCADE)
    idTask = models.ForeignKey(ExamTask, on_delete=models.CASCADE)
    ans = models.IntegerField("Ответ")

    class Meta:
        verbose_name = "Ответ студента на экзаменационное задание"
        verbose_name_plural = "Ответы студента на экзаменационные задания"


class AnsExam(models.Model):
    idTask = models.ForeignKey(ExamTask, on_delete=models.CASCADE)
    ans1 = models.IntegerField("Ответ 1")
    ans2 = models.IntegerField("Ответ 2")
    ans3 = models.IntegerField("Ответ 3")
    ans4 = models.IntegerField("Ответ 4")
    rightAns = models.IntegerField("Правильный ответ")

    class Meta:
        verbose_name = "Ответ на экзаменационное задание"
        verbose_name_plural = "Ответы на экзаменационные задания"

