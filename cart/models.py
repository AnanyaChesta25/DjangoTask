from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):

      student_name = models.CharField(max_length=100)
      date_of_birth = models.DateField(null=True,blank=True)
      email = models.EmailField(default="example@gmail.com")
      s_address = models.TextField(default="")
      assigned_to = models.ForeignKey(User,on_delete=models.DO_NOTHING, null=True )
      

def __str__(self):
    return f"Student {self.id}-{self.student_name}"


      