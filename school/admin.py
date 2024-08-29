from django.contrib import admin
from .models import Student, Department, Subject, Staff, CourseRegistration,Marks

# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Staff)
admin.site.register(CourseRegistration)
admin.site.register(Marks)