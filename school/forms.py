from django import forms
from django.contrib.auth.models import User
from .models import StudentDetails, Admission, Subjects, Staff, NonStaff, Department

#1.student registration form
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

#2.student admission form 
class StudentAdmissionForm(forms.ModelForm):
    gender = forms.ModelMultipleChoiceField(
        queryset=StudentDetails.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Admission
        fields = '__all__'

#3.StudentProfile form
class StudentProfileForm(forms.ModelForm):
    gender = forms.ModelMultipleChoiceField(
        queryset=StudentDetails.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = StudentDetails
        fields = ['first_name', 'middle_name', 'other_name', 'last_name', 'gender', 'location', 'country', 'age', 'date_of_birth', 'parent_phone_number', 'subjects', ]

#4.Student profile Pic Update
class StudentProfilePic(forms.ModelForm):
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
    gender = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    marital_status = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
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
    gender = forms.ModelMultipleChoiceField(
        queryset=NonStaff.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    marital_status = forms.ModelMultipleChoiceField(
        queryset=NonStaff.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
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
