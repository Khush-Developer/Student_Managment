from django.db import models

# Create your models here.
class Addcourse(models.Model):
    course= models.CharField(max_length=100)
    fees= models.IntegerField()
    duration=models.CharField(max_length=100)
    desc=models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.course
    
class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=250)

class Addstudent(models.Model):
    sname = models.CharField(max_length=200)
    semail=models.EmailField(max_length=100)
    smobile=models.IntegerField()
    scollege=models.CharField(max_length=225)
    sdegree=models.CharField(max_length=225)
    scourses = models.ForeignKey(Addcourse, on_delete=models.CASCADE,default='0',null=True)
    def __str__(self):
        return self.sname