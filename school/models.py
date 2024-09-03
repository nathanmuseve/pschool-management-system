from django.db import models
from django.contrib.auth.models import User

# MODELS
# 1. StudentDetails model
class StudentDetails(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    admin_number = models.BigAutoField(unique=True, primary_key=True, verbose_name="Admission Number")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    other_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    parent_phone_number = models.PositiveIntegerField(null=True)
    date_registered = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.admin_number} {self.first_name} {self.last_name} {self.date_registered}"

# 2. Department model
class Department(models.Model):
    DEPARTMENTS_CHOICES = (
        ('LANGUAGES', 'Languages'),
        ('SCIENCES', 'Sciences'),
        ('HUMANITIES_AND_ARTS', 'Humanities and Arts'),
        ('PHYSICAL_EDUCATION', 'Physical Education'),
        ('MATHEMATICS', 'Mathematics'),
    )
    department_name = models.CharField(max_length=30, choices=DEPARTMENTS_CHOICES)

    def __str__(self):
        return self.department_name

# 3. Subjects model
class Subjects(models.Model):
    SUBJECTS_CHOICES = (
        ('MATHEMATICS', 'Mathematics'),
        ('ENGLISH', 'English'),
        ('MOTHER_TONGUE', 'Mother Tongue'),
        ('GENERAL_SCIENCES', 'General Sciences'),
        ('HOME_SCIENCE', 'Home Science'),
        ('HISTORY', 'History'),
        ('GEOGRAPHY', 'Geography'),
        ('CIVICS', 'Civics'),
        ('CRE', 'Christian Religious Education'),
        ('ISLAMIC', 'Islamic'),
        ('FRENCH', 'French'),
        ('GERMAN', 'German'),
        ('ART_AND_CRAFT', 'Art and Craft'),
        ('GAMES_AND_SPORTS', 'Games and Sports'),
        ('FITNESS_AND_HEALTH', 'Fitness and Health'),
    )
    subject_name = models.CharField(max_length=30, choices=SUBJECTS_CHOICES)
    students = models.ManyToManyField(StudentDetails)

    def __str__(self):
        return self.subject_name

# 4. Admission model
class Admission(models.Model):
    CLASS_CHOICES = (
        ('GRADE_ONE', 'One'),
        ('GRADE_TWO', 'Two'),
        ('GRADE_THREE', 'Three'),
        ('GRADE_FOUR', 'Four'),
        ('GRADE_FIVE', 'Five'),
        ('GRADE_SIX', 'Six'),
        ('GRADE_SEVEN', 'Seven'),
        ('GRADE_EIGHT', 'Eight'),
        ('GRADE_NINE', 'Nine'),
    )
    grade_admitted = models.CharField(max_length=30, choices=CLASS_CHOICES, default="GRADE_ONE")
    date_admitted = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subjects)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"

# 5. Staff model
class Staff(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STATUS_CHOICES = (
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('SINGLE', 'Single'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    t_s_c_no = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="SINGLE")
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField(null=True)
    date_registered = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    departments = models.ManyToManyField(Department, related_name='staff_members')
    subjects = models.ManyToManyField(Subjects, related_name='staff_subjects')

    def __str__(self):
        return f"{self.t_s_c_no} {self.user.first_name} {self.user.last_name}"

# 6. Non_Staff model
class NonStaff(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    STATUS_CHOICES = (
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('SINGLE', 'Single'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="SINGLE")
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField(null=True)
    date_registered = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.job_id} {self.user.first_name} {self.user.last_name}"

# 7. Marks model
class Marks(models.Model):
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    def __str__(self):
        return f"{self.student.admin_number} {self.student.first_name} {self.student.last_name}"
