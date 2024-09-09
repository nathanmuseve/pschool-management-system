from django import forms
from django.contrib.auth.models import User
from .models import StudentDetails, Subjects, Staff, NonStaff, Department,Marks, Contact, Feedback


class StudentRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg Nelson'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg. Joram'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg.nelson89 and will be used for login'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg. example@gmail.com'}), label='Email (optinal)', required=False, empty_value=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

#2.StudentProfile form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['user', 'middle_name', 'other_name', 'gender', 'location', 'country', 'age', 'date_of_birth', 'parent_phone_number', 'bio' ]

#3.Student profile Pic Update
class StudentProfilePicForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ['profile_picture',]

#4.Staff registration form
class StaffRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg Nelson'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg. Joram'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg. example@gmail.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg.nelson89 and will be used for login'}))
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password']

#5.Staff Profile Form
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

#6.StaffProfilePic form
class StaffProfilePicForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields =['profile_picture',]

#7.NonStaff registration form
class NonStaffRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg Nelson'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg. Joram'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg. example@gmail.com'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg.nelson89 and will be used for login'}))
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = fields = ['first_name', 'last_name', 'email', 'username','password']

#8.NonStaff Registration Form
class NonStaffProfileForm(forms.ModelForm):
    
    departments = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget = forms.SelectMultiple
    )
    class Meta:
        model = NonStaff
        fields = '__all__'

#9.NonStaffProfilePic form
class NonStaffProfilePicForm(forms.ModelForm):
    class Meta:
        model = NonStaff
        fields =['profile_picture',]
#10. Student marks
class StudentMarksForm(forms.ModelForm):
    subject = forms.ModelMultipleChoiceField(
        queryset=Marks.objects.all(),
        widget=forms.SelectMultiple
    )
    class Meta:
        model = Marks
        fields = '__all__'

#11. Contact Form
class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg Nelson Kamau'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'eg example@gmail.com'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg .Job Inquiry'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write Your message'}))
    class Meta:
        model = Contact
        fields = '__all__'
        
#12. Feedback Form
class Feedback(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg Joho Kamau'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'eg .Quick Resposnse'}))
    feedback = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write Your Feedback message here.'}))
    rating = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':0}))
    class Meta:
        model = Feedback
        fields = ['name', 'subject','feedback', 'rating']