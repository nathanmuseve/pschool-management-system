from django.shortcuts import render
from .models import Department, Subjects, StudentDetails, Admission, Staff, NonStaff, Marks
from .forms import StudentRegistrationForm, StudentAdmissionForm, StudentProfileForm, StudentProfilePic, StaffRegistrationForm, StaffProfileForm, StaffProfilePicForm, NonStaffRegistrationForm, NonStaffProfileForm, NonStaffProfilePicForm

# Create your views here.
def test(request):
  return render(request, 'school/test.html')

#home
def home(request):
  return render(request, 'school/home.html')

#history
def history(request):
  return render(request, 'school/history.html')

#philosopy
def philosopy(request):
  return render(request, 'school/philosopy.html')

#mission
def mission(request):
  return render(request, 'school/mission.html')

#vission
def vission(request):
  return render(request, 'school/vission.html')

#goal
def goal(request):
  return render(request, 'school/goal.html')

#values
def values(request):
  return render(request, 'school/values.html')

#enrollment
def enrollment(request):
  return render(request, 'school/enrollment.html')

#admission
def admission(request):

  return render(request, 'school/admission.html')

#curriculum
def curriculum(request):
  return render(request, 'school/curriculum.html')

#subjects
def subjects(request):
  student = StudentDetails.objects.get(id=1)
  subjects_taken = student.subjects.all()
  context = {
    'student': 'student',
    'subjects_taken':subjects_taken,
  }
  return render(request, 'school/subjects.html', context)

#departments
def departments(request):
  departments = Department.objects.all()
  return render(request, 'school/departments.html', { 'departments':departments })

#student portal
def student_portal(request):
  studentdetails = StudentDetails.objects.all()
  return render(request, 'school/student_portal.html', { 'studentdetails':studentdetails })

#student_registration
def student_registration(request):
  return render(request, 'school/student_registration.html')

#student_logout
def student_logout(request):
  return render(request, 'school/student_logout.html')

#logout_success
def logout_success(request):
  return render(request, 'school/logout_success.html')

#staff_registration
def staff_registration(request):
  return render(request, 'school/staff_registration.html')

#staff_login
def staff_login(request):
  return render(request, 'school/staff_login.html')

#staff_logout
def staff_logout(request):
  return render(request, 'school/staff_logout.html')

#non_staff_registration
def non_staff_registration(request):
  return render(request, 'school/non_staff_registration.html')

#non_staff_login
def non_staff_login(request):
  return render(request, 'school/non_staff_login.html')

#non_staff_logout
def non_staff_logout(request):
  return render(request, 'school/non_staff_logout.html')







