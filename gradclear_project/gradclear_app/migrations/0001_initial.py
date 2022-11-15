# Generated by Django 4.0.1 on 2022-11-15 23:26

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='clearance_form_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, verbose_name='Student Id')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('present_address', models.CharField(max_length=100, verbose_name='Present Address')),
                ('course', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Student Course')),
                ('date_filed', models.CharField(max_length=20, verbose_name='Date Filed')),
                ('date_admitted_in_tup', models.CharField(max_length=20, verbose_name='Date Admitted')),
                ('highschool_graduated', models.TextField(max_length=10, verbose_name='High School Graduated')),
                ('tupc_graduate', models.CharField(max_length=10, verbose_name='TUPC Graduate')),
                ('year_graduated_in_tupc', models.CharField(default='NONE', max_length=20, null=True, verbose_name='Year Graduated')),
                ('number_of_terms_in_tupc', models.IntegerField(null=True, verbose_name='Number of Terms in TUPC')),
                ('amount_paid', models.CharField(default='0', max_length=100, verbose_name='Amount Paid')),
                ('have_previously_requested_form', models.CharField(default='NONE', max_length=10, verbose_name='Previous Request')),
                ('date_of_previously_requested_form', models.CharField(default='NONE', max_length=20, null=True, verbose_name='Previous Request Date')),
                ('last_term_in_tupc', models.IntegerField(default='NONE', null=True, verbose_name='Last Term in TUPC')),
                ('purpose_of_request', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Purpose of Request')),
                ('purpose_of_request_reason', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Purpose of Request Reason')),
                ('approval_status', models.CharField(default='0', max_length=15, verbose_name='Approval Status')),
                ('liberal_arts_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Liberal Art Signature')),
                ('accountant_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Accountant Signature')),
                ('mathsci_dept_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Math and Science Signature')),
                ('pe_dept_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='P.E. Signature')),
                ('ieduc_dept_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Industrial Educ. Signature')),
                ('it_dept_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Industrial Tech. Signature')),
                ('eng_dept_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Engineering Signature')),
                ('library_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Library Signature')),
                ('guidance_office_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Guidance Signature')),
                ('osa_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='OSA Signature')),
                ('academic_affairs_signature', models.CharField(default='UNAPPROVED', max_length=100, verbose_name='Academic Affairs Signature')),
                ('course_adviser', models.CharField(default='NONE', max_length=100, verbose_name='Course Adviser')),
                ('course_adviser_signature', models.ImageField(upload_to='signature/')),
                ('appointment', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Appointment')),
                ('clear_notif', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Notification')),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document_checker_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('TOR', models.CharField(max_length=50)),
                ('form_137', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='graduation_form_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, verbose_name='Student Id')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('course', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Student Course')),
                ('purpose_of_request', models.CharField(default='Graduation Form', max_length=100, null=True, verbose_name='Purpose of Request')),
                ('approval_status', models.CharField(default='0', max_length=15, verbose_name='Approval Status')),
                ('appointment', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Appointment')),
                ('shift', models.CharField(max_length=20, verbose_name='Shift')),
                ('study_load', models.CharField(max_length=10, verbose_name='Study Load')),
                ('status', models.CharField(max_length=10, verbose_name='Status')),
                ('enrolled_term', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Enrolled Term')),
                ('unenrolled_application_deadline', models.CharField(default='NONE', max_length=20, null=True, verbose_name='Deadline')),
                ('subject1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject1')),
                ('room1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room1')),
                ('faculty1', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_1', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_1', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_1')),
                ('subject2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject2')),
                ('room2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room2')),
                ('faculty2', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_2', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_2', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_2')),
                ('subject3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject3')),
                ('room3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room3')),
                ('faculty3', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_3', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_3', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_3')),
                ('subject4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject4')),
                ('room4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room4')),
                ('faculty4', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_4', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_4', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_4')),
                ('subject5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject5')),
                ('room5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room5')),
                ('faculty5', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_5', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_5', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_5')),
                ('subject6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject6')),
                ('room6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room6')),
                ('faculty6', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_6', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_6', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_6')),
                ('subject7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject7')),
                ('room7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room7')),
                ('faculty7', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_7', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_7', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_7')),
                ('subject8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject8')),
                ('room8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room8')),
                ('faculty8', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_8', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_8', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_8')),
                ('subject9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject9')),
                ('room9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room9')),
                ('faculty9', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_9', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_9', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_9')),
                ('subject10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Subject10')),
                ('room10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Room10')),
                ('faculty10', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('starttime1_10', models.TimeField(blank=True, default='00:00', null=True)),
                ('endtime1_10', models.TimeField(blank=True, default='00:00', null=True)),
                ('day1_10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Day1_10')),
                ('addsubject1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject1')),
                ('addroom1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room1')),
                ('addfaculty1', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_1', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_1', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_1')),
                ('addsubject2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject2')),
                ('addroom2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room2')),
                ('addfaculty2', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_2', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_2', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_2')),
                ('addsubject3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject3')),
                ('addroom3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room3')),
                ('addfaculty3', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_3', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_3', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_3')),
                ('addsubject4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject4')),
                ('addroom4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room4')),
                ('addfaculty4', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_4', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_4', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room1_4')),
                ('addsubject5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject5')),
                ('addroom5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room5')),
                ('addfaculty5', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_5', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_5', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_5')),
                ('addsubject6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject6')),
                ('addroom6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room6')),
                ('addfaculty6', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_6', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_6', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_6', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_6')),
                ('addsubject7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject7')),
                ('addroom7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room7')),
                ('addfaculty7', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_7', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_7', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_7')),
                ('addsubject8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject8')),
                ('addroom8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room8')),
                ('addfaculty8', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_8', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_8', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_8', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_8')),
                ('addsubject9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject9')),
                ('addroom9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room9')),
                ('addfaculty9', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_9', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_9', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_9', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_9')),
                ('addsubject10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Subject10')),
                ('addroom10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Room10')),
                ('addfaculty10', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Instructor1', 'Instructor1'), ('Instructor2', 'Instructor2'), ('Instructor3', 'Instructor3'), ('Instructor4', 'Instructor4')], max_length=50, null=True)),
                ('add_starttime1_10', models.TimeField(blank=True, default='00:00', null=True)),
                ('add_endtime1_10', models.TimeField(blank=True, default='00:00', null=True)),
                ('addday1_10', models.CharField(blank=True, max_length=50, null=True, verbose_name='Add Day1_10')),
                ('trainP_startdate', models.CharField(default='NONE', max_length=30, null=True, verbose_name='Start')),
                ('trainP_enddate', models.CharField(default='NONE', max_length=30, null=True, verbose_name='End')),
                ('instructor_name', models.CharField(max_length=50, verbose_name='SIT Instructor')),
                ('signature1', models.CharField(max_length=100)),
                ('signature2', models.CharField(max_length=100)),
                ('signature3', models.CharField(max_length=100)),
                ('signature4', models.CharField(max_length=100)),
                ('signature5', models.CharField(max_length=100)),
                ('signature6', models.CharField(max_length=100)),
                ('signature7', models.CharField(max_length=100)),
                ('signature8', models.CharField(max_length=100)),
                ('signature9', models.CharField(max_length=100)),
                ('signature10', models.CharField(max_length=100)),
                ('addsignature1', models.CharField(max_length=100)),
                ('addsignature2', models.CharField(max_length=100)),
                ('addsignature3', models.CharField(max_length=100)),
                ('addsignature4', models.CharField(max_length=100)),
                ('addsignature5', models.CharField(max_length=100)),
                ('addsignature6', models.CharField(max_length=100)),
                ('addsignature7', models.CharField(max_length=100)),
                ('addsignature8', models.CharField(max_length=100)),
                ('addsignature9', models.CharField(max_length=100)),
                ('addsignature10', models.CharField(max_length=100)),
                ('sitsignature', models.CharField(max_length=100)),
                ('grad_notif', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Notification')),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='request_form_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20, verbose_name='Student Id')),
                ('name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('name2', models.CharField(max_length=100, verbose_name='2nd Format Student Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('course', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Student Course')),
                ('date', models.CharField(max_length=20, verbose_name='Date')),
                ('control_number', models.CharField(default='NONE', max_length=50, null=True, verbose_name='Control Number')),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)], verbose_name='Contact Number')),
                ('current_status', models.CharField(max_length=100, null=True, verbose_name='Current Status')),
                ('request', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Request')),
                ('purpose_of_request_reason', models.CharField(max_length=100, null=True, verbose_name='Purpose of Request')),
                ('amount', models.CharField(default='0', max_length=100, verbose_name='Amount')),
                ('form_137', models.CharField(default='❌', max_length=50, null=True)),
                ('clearance', models.CharField(default='❌', max_length=50, null=True)),
                ('official_receipt', models.CharField(default='❌', max_length=50, null=True)),
                ('claim', models.CharField(default='UNCLAIMED', max_length=50, null=True)),
                ('approval_status', models.CharField(default='UNAPPROVED', max_length=15, verbose_name='Approval Status')),
                ('appointment', models.CharField(default='NONE', max_length=100, null=True, verbose_name='Appointment')),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, null=True, verbose_name='Full Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('gender', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True)),
                ('id_number', models.CharField(blank=True, max_length=7, unique=True, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='ID Number')),
                ('course', models.CharField(blank=True, choices=[('', '--SELECT--'), ('BSIE-Information and Communication Technology', 'BSIE-Information and Communication Technology'), ('BSIE-Industrial Arts', 'BSIE-Industrial Arts'), ('BGT-Architecture Technology', 'BGT-Architecture Technology'), ('BET-Civil Technology', 'BET-Civil Technology'), ('BET-Electrical Technology', 'BET-Electrical Technology'), ('BET-Electronics Engineering Technology', 'BET-Electronics Engineering Technology'), ('BET-Computer Engineering Technology', 'BET-Computer Engineering Technology'), ('BET-Mechanical & Production Engineering Technology', 'BET-Mechanical & Production Engineering Technology'), ('BET-Power Plant Engineering Technology', 'BET-Power Plant Engineering Technology'), ('BT-Civil Engineering Technology', 'BT-Civil Engineering Technology'), ('BT-Computer Engineering Technology', 'BT-Computer Engineering Technology'), ('BT-Electrical Engineering Technology', 'BT-Electrical Engineering Technology'), ('BT-Electronics Engineering Technology', 'BT-Electronics Engineering Technology'), ('BT-Mechanical & Production Engineering Technology', 'BT-Mechanical & Production Engineering Technology'), ('BT-Powerplant Engineering Technology', 'BT-Powerplant Engineering Technology'), ('Mechanical & Production Engineering Technology', 'Mechanical & Production Engineering Technology'), ('Powerplant Engineering Technology', 'Powerplant Engineering Technology'), ('BSIE-Automotive Engineering Technology', 'BSIE-Automotive Engineering Technology'), ('BSIE-Mechanical & Production Engineering Technology', 'BSIE-Mechanical & Production Engineering Technology'), ('BTTE-Architecture Technology', 'BTTE-Architecture Technology'), ('BTTE-Automotive Engineering Technology', 'BTTE-Automotive Engineering Technology'), ('BTTE-Civil Engineering Technology', 'BTTE-Civil Engineering Technology'), ('BTTE-Computer Engineering Technology', 'BTTE-Computer Engineering Technology'), ('BTTE-Electrical Engineering Technology', 'BTTE-Electrical Engineering Technology'), ('BTTE-Electronics Engineering Technology', 'BTTE-Electronics Engineering Technology'), ('BTTE-Mechanical & Production Engineering Technology', 'BTTE-Mechanical & Production Engineering Technology'), ('BTTE-Powerplant Engineering Technology', 'BTTE-Powerplant Engineering Technology'), ('BT-Automotive Engineering Technology', 'BT-Automotive Engineering Technology')], max_length=100, null=True)),
                ('course_graduated', models.CharField(blank=True, choices=[('', '--SELECT--'), ('Bachelor of Science in Industrial Education', 'Bachelor of Science in Industrial Education'), ('Architecture Technology', 'Architecture Technology'), ('Automotive Engineering Technology', 'Automotive Engineering Technology'), ('Computer Engineering Technology', 'Computer Engineering Technology'), ('Electronics Engineering Technology', 'Electronics Engineering Technology'), ('Electrical Engineering Technology', 'Electrical Engineering Technology'), ('Civil Engineering Technology', 'Civil Engineering Technology'), ('Mechanical & Production Engineering Technology', 'Mechanical & Production Engineering Technology'), ('Power Plant Engineering Technology', 'Power Plant Engineering Technology'), ('Bachelor of Technical Teacher Education', 'Bachelor of Technical Teacher Education'), ('Associate Marine Engineering', 'Associate Marine Engineering'), ('Automotive Technology', 'Automotive Technology'), ('BSIE-Architecture Technology', 'BSIE-Architecture Technology'), ('BSIE-Automotive Engineering Technology', 'BSIE-Automotive Engineering Technology'), ('BSIE-Civil Engineering Technology', 'BSIE-Civil Engineering Technology'), ('BSIE-Civil Technology', 'BSIE-Civil Technology'), ('BSIE-Computer Engineering Technology', 'BSIE-Computer Engineering Technology'), ('BSIE-Drafting Engineering Technology', 'BSIE-Drafting Engineering Technology'), ('BSIE-Electrical Engineering Technology', 'BSIE-Electrical Engineering Technology'), ('BSIE-Electrical Technology', 'BSIE-Electrical Technology'), ('BSIE-Electronics Engineering Technology', 'BSIE-Electronics Engineering Technology'), ('BSIE-Electronics Technology', 'BSIE-Electronics Technology'), ('BSIE-Mechanical Engineering Technology', 'BSIE-Mechanical Engineering Technology'), ('Bachelor of of Science in Marine Engineering', 'Bachelor of of Science in Marine Engineering'), ('Bachelor of Technology', 'Bachelor of Technology'), ('Civil Technology', 'Civil Technology'), ('Electrical Technology', 'Electrical Technology'), ('Electronics Technology', 'Electronics Technology'), ('Marine Engineering Technology', 'Marine Engineering Technology'), ('Mechanical Engineering Technology', 'Mechanical Engineering Technology'), ('Mechanical Technology', 'Mechanical Technology'), ('Power Engineering Technology', 'Power Engineering Technology'), ('Stationary Marine Engineering', 'Stationary Marine Engineering')], max_length=100, null=True)),
                ('department', models.CharField(blank=True, choices=[('', '--SELECT--'), ('OCS', 'Accountant (OCS)'), ('OGS', 'Guidance Office (OGS)'), ('OSA', 'Student Affairs (OSA)'), ('ADAA', 'Academic Affairs (ADAA)'), ('OES', 'Extension Services (OES)'), ('OCL', 'Library (OCL)'), ('DMS', 'Math and Science Department (DMS)'), ('DPECS', 'Department of Physical Education Culture and Sports (DPECS)'), ('DED', 'Industrial Education Department (DED)'), ('DIT', 'Industrial Technology Department (DIT)'), ('DLA', 'Liberal Arts Department (DLA)'), ('DOE', 'Department of Engineering (DOE)')], max_length=100, null=True, verbose_name='Department')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position ')),
                ('designation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Designation ')),
                ('year_graduated', models.CharField(blank=True, max_length=100, null=True, verbose_name='Year Graduated')),
                ('year_and_section', models.CharField(blank=True, choices=[('', '--SELECT--'), ('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=100, null=True)),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)], verbose_name='Contact Number')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email Address')),
                ('user_type', models.CharField(max_length=100, verbose_name='User Type')),
                ('student_id', models.CharField(max_length=100, null=True, verbose_name='Student ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('profile_picture', models.ImageField(upload_to='uploads/')),
                ('e_signature', models.ImageField(blank=True, upload_to='esignatures/')),
                ('e_signature_timesaved', models.DateTimeField(auto_now_add=True)),
                ('uploaded_signature', models.ImageField(blank=True, upload_to='uploaded signatures/')),
                ('uploaded_signature_timesaved', models.DateTimeField(auto_now_add=True)),
                ('no_signature', models.CharField(default='APPROVED *Required Live Signature', max_length=100, verbose_name='Approve')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
