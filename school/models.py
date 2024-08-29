from django.db import models
from django.contrib.auth.models import User

#MODELS
#1.Students model
class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  admin_number = models.CharField(unique=True, blank=False, null=False)
  last_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50, blank=True, required=False)
  first_name = models.CharField(max_length=50)
  age = models.IntegerField(max=30, min=1)
  date_of_birth = models.DateField(null=False, blank=False, required=True)
  phone_number = models.PositiveIntegerField(required=False, null=True)
  date_admitted = models.DateField(auto_now=True)
  # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

  def __str__(self):
    return f"{self.admin_number} {self.first_name} {self.last_name}"

#2.Department
class Department(models.Model):
  department_name = models.CharField(max_length=100, unique=True)
  def __str__(self):
    return self.department_name
  
#3.Subject Model
class Subject(models.Model):
  subject_name = models.CharField(max_length=100, unique=True)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  def __str__(self):
    return self.subject_name
#4.Staff Model
class Staff(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  is_teaching_staff = models.BooleanField(default=True)
  departments = models.ManyToManyField(Department, related_name='registrations')

#5.CourseRegistration Model
class CourseRegistration(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
  date_registered = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.student.admin_number} {self.subjects.subject_name} {self.date_registered}"
  
  #MARKS model
class Marks(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
  marks_obtained = models.IntegerField(max=100, min=0)
    
  def __str__(self):
    return f"{self.student.admin_number} {self.subject.subject_name} {self.marks_obtained}"