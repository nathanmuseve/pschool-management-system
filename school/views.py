from django.shortcuts import render, redirect
from .models import Department, Subjects, StudentDetails, Admission, Staff, NonStaff, Marks
from .forms import StudentRegistrationForm, StudentAdmissionForm, StudentProfileForm, StudentProfilePicForm, StaffRegistrationForm, StaffProfileForm, StaffProfilePicForm, NonStaffRegistrationForm, NonStaffProfileForm, NonStaffProfilePicForm,StudentMarksForm, ContactForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

#1. Create your views here.
def departments(request):
  return render(request, 'school/departments.html')

#2.home
def home(request):
  return render(request, 'school/home.html')

#3.history
def history(request):
  return render(request, 'school/history.html')

#4.philosopy
def philosophy(request):
  return render(request, 'school/philosophy.html')
  
#6.vission
def vission(request):
  return render(request, 'school/vission.html')

#7.goal
def goal(request):
  return render(request, 'school/goal.html')

#8.values
def values(request):
  return render(request, 'school/values.html')

#9.enrollment
def enrollment(request):
  students = StudentDetails.objects.all()
  return render(request, 'school/enrollment.html', { 'students':students })

#10.admission
def admission(request):
  form = StudentAdmissionForm()
  if request.method == "POST":
    form = StudentAdmissionForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return render(request, 'school/admission_success.html', { 'form':form})  
  else:
    form = StudentAdmissionForm()
  return render(request, 'school/admission.html', { 'form':form })

#11.curriculum
def curriculum(request):
  return render(request, 'school/curriculum.html')

#12.subjects
def subjects(request):
  subjects = Subjects.objects.all()
  context = {
    'subjects': subjects,
  }
  return render(request, 'school/subjects.html', context)

#13.departments
def departments(request):
  departments = Department.objects.all()
  return render(request, 'school/departments.html', { 'departments':departments })

#14.student portal
# @login_required(login_url='school:student_login')
# @permission_required(('school.change_StudentDetails', 'school.view_StudentDetails'))
def student_portal(request):
  students = StudentDetails.objects.all()
  users = User.objects.all()
  context = {
    'students': students,
    'users': users,
  }
  return render(request, 'school/students_portal.html', context)

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Profile View and Update
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)

# View Marks/Results
@login_required
def view_marks(request):
    marks = Marks.objects.filter(student=request.user)
    return render(request, 'users/marks.html', {'marks': marks})


#15.student_registration
def student_registration(request):
  student = Admission.objects.all()
  form = StudentRegistrationForm()
  context = {
    'student':student,
    'form':form,
  }
  if request.method == "POST":
    form = StudentRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      login(request, form.save())
      return redirect('school:home')
  else:
    form = StudentRegistrationForm()
  return render(request, 'school/student_registration.html', context)

#16.student login
def student_login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      next_url = request.POST.get('next') or request.GET.get('next') or 'home'
      return redirect('next_url')
  # else:
  #   error_message = "Invalid entries. Confirm that passwords match."
  return render(request, 'school/students_portal.html' )

#17.student_logout
def student_logout(request):
  student = Admission.objects.all()
  if request.method == "POST":
    logout(request)
    return render(request,'school/logout_success.html', { 'student':student })
  
#18.logout_success
def logout_success(request):
  return render(request, 'school/logout_success.html')

#19.Student profile update
def student_profile_update(request):
  form = StudentProfileForm()
  if request.method == "POST":
    form = StudentProfileForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('school:student_portal')
  else:
    form = StudentProfileForm()
  return render(request, 'school/student_profile.html', { 'form':form })

#20 STUDENT_PIC updtae
def student_pic_update(request):
  form = StudentProfilePicForm()
  if request.method == "POST":
    form = StudentProfilePicForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('school:student_portal')
  else:
    form = StudentProfilePicForm()
  return render(request, 'school/student_portal.html', { 'form':form })
    
#21.Staff portal
@login_required(login_url='school:staff_login')
@permission_required(('school.view_Admission', 'school.add_Admission', 'school.change_Admission', 'school.view_Marks','school.add_Marks','school.change_Marks', 'school.delete_delete'))
def staff_portal(request):
  staff = Staff.objects.all()
  return render(request, 'school/staff_portal.html', { 'staff':staff })

#22.staff_registration
def staff_registration(request):
  staff = Staff.objects.all()
  form = StaffRegistrationForm()
  context = {
    'staff':staff,
    'form':form,
  }
  if request.method == "POST":
    form = StaffRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      login(request, form.save())
      return redirect('school:home')
  else:
    form = StaffRegistrationForm()
  return render(request, 'school/staff_registration.html', context)

#23.staff_login
def staff_login(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
      login(request, user)
      # return redirect('school:staff_portal')
  else:
    error_message = "Invalid entries. Confirm that passwords match."
  return render(request, 'school/staff_portal.html',{ 'error_message':error_message } )

#23.staff_logout
def staff_logout(request):
  staff = Staff.objects.all()
  if request.method == "POST":
    logout(request)
    return render(request,'school/logout_success.html', { 'staff':staff })

#24.staff profile update
def staff_profile_update(request):
  form = StaffProfileForm()
  if request.method == "POST":
    form = StaffProfileForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('school:staff_portal')
  else:
    form = StaffProfileForm()
  return render(request, 'school/staff_portal.html', { 'form':form })

#25 staff pic updtae
def staff_pic_update(request):
  form = StaffProfilePicForm()
  if request.method == "POST":
    form = StaffProfilePicForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('school:staff_portal')
  else:
    form = StaffProfilePicForm()
  return render(request, 'school/staff_portal.html', { 'form':form })

#26.non staff portal
@login_required(login_url='school:non_staff_login')
def non_staff_portal(request):
  return render(request, 'school/non_staff_portal.html')

#27.non_staff_registration
def non_staff_registration(request):
  staff = NonStaff.objects.all()
  form = NonStaffRegistrationForm()
  context = {
    'staff':staff,
    'form':form,
  }
  if request.method == "POST":
    form = NonStaffRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      login(request, form.save())
      return redirect('school:home')
  else:
    form = NonStaffRegistrationForm()
  return render(request, 'school/non_staff_registration.html',context)

#28.non_staff_login
def non_staff_login(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
      login(request, user)
      # return redirect('school:staff_portal')
  else:
    error_message = "Invalid entries. Confirm that passwords match."
  return render(request, 'school/non_staff_portal.html',{ 'error_message':error_message } )

#29.non_staff_logout
def non_staff_logout(request):
  nonstaff = NonStaff.objects.all()
  if request.method == "POST":
    logout(request)
    return render(request,'school/logout_success.html', { 'nonstaff':nonstaff })

#30.Non staff profile update
def non_staff_profile_update(request):
  form = NonStaffProfileForm()
  if request.method == "POST":
    form = NonStaffProfileForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('school:non_staff_portal')
  else:
    form = NonStaffProfileForm()
  return render(request, 'school/non_staff_portal.html', { 'form':form })

#31 non staff pic updtae
def non_staff_pic_update(request):
  form = NonStaffProfilePicForm()
  if request.method == "POST":
    form = NonStaffProfilePicForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('school:non_staff_portal')
  else:
    form = NonStaffProfilePicForm()
  return render(request, 'school/non_staff_portal.html', { 'form':form })

#32. Marks 
@login_required(login_url='school:staff_login')
def marks(request):
  marks = Marks.objects.all()
  form = StudentMarksForm()
  context = {
    'marks':marks,
    'form':form,
  }
  if request.method == "POST":
    form = StudentMarksForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form = StudentMarksForm()
  return render(request, 'school/marks.html', context)
#33.Contact Form
def contact(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('school:home')
  else:
    form = ContactForm()
  return render(request, 'school/contact.html', { 'form':form })