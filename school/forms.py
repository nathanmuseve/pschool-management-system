from django import forms
from django.contrib.auth.models import User
from .models import StudentDetails, Admission, Subjects, Staff, NonStaff, Department,Marks, Contact

#1.student registration form
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


#2.student admission form 
class StudentAdmissionForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = StudentDetails
        fields = '__all__'

#3.StudentProfile form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['first_name', 'middle_name', 'other_name', 'last_name', 'username', 'gender', 'location', 'country', 'age', 'date_of_birth', 'parent_phone_number',  ]

#4.Student profile Pic Update
class StudentProfilePicForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['profile_picture',]

#5.Staff registration form
class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

#6.Staff Profile Form
class StaffProfileForm(forms.ModelForm):
    departments = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget = forms.CheckboxInput
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Staff
        fields = '__all__'

#7.StaffProfilePic form
class StaffProfilePicForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields =['profile_picture',]

#8.NonStaff registration form
class NonStaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

#9.NonStaff Registration Form
class NonStaffProfileForm(forms.ModelForm):
    
    departments = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget = forms.CheckboxInput
    )
    class Meta:
        model = NonStaff
        fields = '__all__'

#10.NonStaffProfilePic form
class NonStaffProfilePicForm(forms.ModelForm):
    class Meta:
        model = NonStaff
        fields =['profile_picture',]
#11. Student marks
class StudentMarksForm(forms.ModelForm):
    subject = forms.ModelMultipleChoiceField(
        queryset=Marks.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Marks
        fields = '__all__'

#12. Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'