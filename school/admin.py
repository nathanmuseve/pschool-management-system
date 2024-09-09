from django.contrib import admin
from .models import StudentDetails, Department, Subjects, Staff,NonStaff, Marks, Contact, Feedback

# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(Department)
admin.site.register(Subjects)
admin.site.register(Staff)
admin.site.register(NonStaff)
admin.site.register(Marks)
admin.site.register(Contact)
admin.site.register(Feedback)