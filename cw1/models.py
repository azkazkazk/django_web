from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    def __str__(self):
        return u'%s  ' % self.name


class Module(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    year = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)
    teacher = models.CharField(max_length=128)

    class Meta:
        unique_together = ('teacher', 'code', 'year', 'semester')


class Rate(models.Model):
    student_name = models.CharField(max_length=126)
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    year = models.CharField(max_length=256)
    semester = models.CharField(max_length=256)
    teacher = models.CharField(max_length=128)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ('student_name', 'code', 'year','semester','teacher')


class Professor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    lecture = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    rate = models.CharField(max_length=256)
