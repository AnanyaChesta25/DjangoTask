from django.shortcuts import render
from .models import Student
# Create your views here.

def homepage(request):
     students = Student.objects.all()
     print(students)
     # my_name="Ananya"
     # food=["Dosa","Golgappa","chicken","Burger","FiredChicken","Noddles"]
     return render(request, 'homepage.html', context={ "students": students})











