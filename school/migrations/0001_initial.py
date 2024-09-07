# Generated by Django 5.1.1 on 2024-09-07 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('copy_to_myself', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('LANGUAGES', 'Languages'), ('SCIENCES', 'Sciences'), ('HUMANITIES_AND_ARTS', 'Humanities and Arts'), ('PHYSICAL_EDUCATION', 'Physical Education'), ('MATHEMATICS', 'Mathematics')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('admin_number', models.BigAutoField(primary_key=True, serialize=False, unique=True, verbose_name='Admission Number')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('other_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('parent_phone_number', models.PositiveIntegerField(null=True)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(choices=[('MATHEMATICS', 'Mathematics'), ('ENGLISH', 'English'), ('MOTHER_TONGUE', 'Mother Tongue'), ('GENERAL_SCIENCES', 'General Sciences'), ('HOME_SCIENCE', 'Home Science'), ('HISTORY', 'History'), ('GEOGRAPHY', 'Geography'), ('CIVICS', 'Civics'), ('CRE', 'Christian Religious Education'), ('ISLAMIC', 'Islamic'), ('FRENCH', 'French'), ('GERMAN', 'German'), ('ART_AND_CRAFT', 'Art and Craft'), ('GAMES_AND_SPORTS', 'Games and Sports'), ('FITNESS_AND_HEALTH', 'Fitness and Health')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NonStaff',
            fields=[
                ('job_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(choices=[('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('SINGLE', 'Single')], default='SINGLE', max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_admitted', models.CharField(choices=[('GRADE_ONE', 'One'), ('GRADE_TWO', 'Two'), ('GRADE_THREE', 'Three'), ('GRADE_FOUR', 'Four'), ('GRADE_FIVE', 'Five'), ('GRADE_SIX', 'Six'), ('GRADE_SEVEN', 'Seven'), ('GRADE_EIGHT', 'Eight'), ('GRADE_NINE', 'Nine')], default='GRADE_ONE', max_length=30)),
                ('date_admitted', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentdetails')),
            ],
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='subjects',
            field=models.ManyToManyField(to='school.subjects'),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('t_s_c_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(choices=[('MARRIED', 'Married'), ('DIVORCED', 'Divorced'), ('SINGLE', 'Single')], default='SINGLE', max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.PositiveIntegerField(null=True)),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('departments', models.ManyToManyField(related_name='staff_members', to='school.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(related_name='staff_subjects', to='school.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.PositiveIntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentdetails')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subjects')),
            ],
        ),
    ]
