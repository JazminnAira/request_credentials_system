from operator import truediv
from unicodedata import name
from unittest.util import *
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
import datetime
from distutils.command.upload import upload

class user_table(AbstractUser):
     
    courses = [
        ('', '--SELECT--'),
        ('BSIE-Information and Communication Technology', 'BSIE-Information and Communication Technology'),
        ('BSIE-Industrial Arts', 'BSIE-Industrial Arts'),
        ('BGT-Architecture Technology', 'BGT-Architecture Technology'),
        ('BET-Civil Technology', 'BET-Civil Technology'),
        ('BET-Electrical Technology', 'BET-Electrical Technology'),
        ('BET-Electronics Engineering Technology', 'BET-Electronics Engineering Technology'),
        ('BET-Computer Engineering Technology', 'BET-Computer Engineering Technology'),
        ('BET-Mechanical & Production Engineering Technology', 'BET-Mechanical & Production Engineering Technology'),
        ('BET-Power Plant Engineering Technology', 'BET-Power Plant Engineering Technology'),
        ('BT-Civil Engineering Technology', 'BT-Civil Engineering Technology'),
        ('BT-Computer Engineering Technology', 'BT-Computer Engineering Technology'),
        ('BT-Electrical Engineering Technology', 'BT-Electrical Engineering Technology'),
        ('BT-Electronics Engineering Technology', 'BT-Electronics Engineering Technology'),
        ('BT-Mechanical & Production Engineering Technology', 'BT-Mechanical & Production Engineering Technology'),
        ('BT-Powerplant Engineering Technology', 'BT-Powerplant Engineering Technology'),
        ('Mechanical & Production Engineering Technology', 'Mechanical & Production Engineering Technology'),
        ('Powerplant Engineering Technology', 'Powerplant Engineering Technology'),
        ('BSIE-Automotive Engineering Technology', 'BSIE-Automotive Engineering Technology'),
        ('BSIE-Mechanical & Production Engineering Technology', 'BSIE-Mechanical & Production Engineering Technology'),
        ('BTTE-Architecture Technology', 'BTTE-Architecture Technology'),
        ('BTTE-Automotive Engineering Technology', 'BTTE-Automotive Engineering Technology'),
        ('BTTE-Civil Engineering Technology', 'BTTE-Civil Engineering Technology'),
        ('BTTE-Computer Engineering Technology', 'BTTE-Computer Engineering Technology'),
        ('BTTE-Electrical Engineering Technology', 'BTTE-Electrical Engineering Technology'),
        ('BTTE-Electronics Engineering Technology', 'BTTE-Electronics Engineering Technology'),
        ('BTTE-Mechanical & Production Engineering Technology', 'BTTE-Mechanical & Production Engineering Technology'),
        ('BTTE-Powerplant Engineering Technology', 'BTTE-Powerplant Engineering Technology'),
        ('BT-Automotive Engineering Technology', 'BT-Automotive Engineering Technology'),
        ('BET-Construction Technology', 'BET-Construction Technology'),
        ('BET-Mechanical Technology', 'BET-Mechanical Technology'),
        ('BET-Automotive Technology', 'BET-Automotive Technology'),
        ('BET-Power Plant Technology', 'BET-Power Plant Technology'),
        ('BSIE-Home Economics', 'BSIE-Home Economics'),
        ('BTTE-Computer Programming', 'BTTE-Computer Programming'),
        ('BTTE-Electrical', 'BTTE-Electrical'),
        ('BS-Civil Engineering', 'BS-Civil Engineering'),
        ('BS-Electrical Engineering', 'BS-Electrical Engineering'),
        ('BS-Mechanical Engineering', 'BS-Mechanical Engineering'),


          
    ]

    graduates_courses = [
        ('', '--SELECT--'),
        ('Bachelor of Science in Industrial Education', 'Bachelor of Science in Industrial Education'),
        ('Architecture Technology', 'Architecture Technology'),
        ('Automotive Engineering Technology', 'Automotive Engineering Technology'),
        ('Computer Engineering Technology', 'Computer Engineering Technology'),
        ('Electronics Engineering Technology', 'Electronics Engineering Technology'),
        ('Electrical Engineering Technology', 'Electrical Engineering Technology'),
        ('Civil Engineering Technology', 'Civil Engineering Technology'),
        ('Mechanical & Production Engineering Technology', 'Mechanical & Production Engineering Technology'),
        ('Power Plant Engineering Technology', 'Power Plant Engineering Technology'),
        ('Bachelor of Technical Teacher Education', 'Bachelor of Technical Teacher Education'),
        ('Associate Marine Engineering', 'Associate Marine Engineering'),
        ('Automotive Technology', 'Automotive Technology'),
        ('BSIE-Architecture Technology', 'BSIE-Architecture Technology'),
        ('BSIE-Automotive Technology', 'BSIE-Automotive Technology'),
        ('BSIE-Civil Engineering Technology', 'BSIE-Civil Engineering Technology'),
        ('BSIE-Civil Technology', 'BSIE-Civil Technology'),
        ('BSIE-Computer Engineering Technology', 'BSIE-Computer Engineering Technology'),
        ('BSIE-Drafting Engineering Technology', 'BSIE-Drafting Engineering Technology'),
        ('BSIE-Electrical Engineering Technology', 'BSIE-Electrical Engineering Technology'),
        ('BSIE-Electrical Technology', 'BSIE-Electrical Technology'),
        ('BSIE-Electronics Engineering Technology', 'BSIE-Electronics Engineering Technology'),
        ('BSIE-Electronics Technology', 'BSIE-Electronics Technology'),
        ('BSIE-Mechanical Engineering Technology', 'BSIE-Mechanical Engineering Technology'),
        ('Bachelor of of Science in Marine Engineering', 'Bachelor of of Science in Marine Engineering'),
        ('Bachelor of Technology', 'Bachelor of Technology'),
        ('Civil Technology', 'Civil Technology'),
        ('Electrical Technology', 'Electrical Technology'),
        ('Electronics Technology', 'Electronics Technology'),
        ('Marine Engineering Technology', 'Marine Engineering Technology'),
        ('Mechanical Engineering Technology', 'Mechanical Engineering Technology'),
        ('Mechanical Technology', 'Mechanical Technology'),
        ('Power Engineering Technology', 'Power Engineering Technology'),
        ('Stationary Marine Engineering', 'Stationary Marine Engineering'),
        ('Automotive Technoloy', 'Automotive Technoloy'),
        ('Drafting Technology', 'Drafting Technology'),
        ('BSIE-Drafting Technology', 'BSIE-Drafting Technology'),
        ('BS-Mechanical & Production Engineering Technology', 'BS-Mechanical & Production Engineering Technology'),
        ('Marine Engineering', 'Marine Engineering'),
       
    ]


    year = [
        ('', '--SELECT--'),
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]

    department = [
        ('', '--SELECT--'),
        ('OCS', 'Accountant (OCS)'),
        ('OGS', 'Guidance Office (OGS)'),
        ('OSA', 'Student Affairs (OSA)'),
        ('ADAA', 'Academic Affairs (ADAA)'),
        ('OES', 'Extension Services (OES)'),
        ('OCL', 'Library (OCL)'),
        ('DMS', 'Math and Science Department (DMS)'),
        ('DPECS', 'Department of Physical Education Culture and Sports (DPECS)'),
        ('DED', 'Industrial Education Department (DED)'),
        ('DIT', 'Industrial Technology Department (DIT)'),
        ('DLA', 'Liberal Arts Department (DLA)'),
        ('DOE', 'Department of Engineering (DOE)'), 
       
    ]

    gender = [
        ('', '--SELECT--'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, verbose_name="Full Name", null=True)
    prefix = models.CharField(max_length=100, verbose_name="Prefix", null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    suffix = models.CharField(max_length=100, verbose_name="Suffix", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Address", null=True, blank=True)
    gender = models.CharField(max_length=100, choices=gender)
    birthday = models.CharField(max_length=8,verbose_name="Birthday")
    id_number = models.CharField(max_length=17, verbose_name="ID Number", 
                validators=[MinLengthValidator(6)], unique=True, null=True)
    course = models.CharField(
            max_length=100, choices=courses, null=True, blank=True)
    course_graduated = models.CharField(
        max_length=100, choices=graduates_courses, null=True, blank=True)
    department = models.CharField(
        max_length=100, choices=department, verbose_name="Department", null=True, blank=True)
    position = models.CharField(
        max_length=100, verbose_name="Position ", null=True, blank=True)
    asigned_position_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    remove_position_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    designation = models.CharField(
        max_length=100, verbose_name="Designation ", null=True, blank=True)
    year_graduated = models.CharField(
        max_length=100, verbose_name="Year Graduated", null=True, blank=True)
    year_and_section = models.CharField(
        max_length=100, choices=year, null=True, blank=True)
    contact_number = models.CharField(
        max_length=13, verbose_name="Contact Number", validators=[MinLengthValidator(13)])
    email = models.EmailField(
        max_length=100, verbose_name="Email Address", unique=True)
    user_type = models.CharField(max_length=100, verbose_name="User Type")
    student_id = models.CharField(max_length=100, verbose_name ="Student ID", null=True)
    username = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='uploads/', default="Media/account.png")
    e_signature = models.ImageField(upload_to='esignatures/',blank=True)# PIP INSTALL PILLOW
    e_signature_timesaved = models.DateTimeField(auto_now_add=True)
    uploaded_signature = models.ImageField(upload_to='uploaded signatures/',blank=True)# PIP INSTALL PILLOW
    uploaded_signature_timesaved = models.DateTimeField(auto_now_add=True)
    no_signature = models.CharField(max_length=100, verbose_name="Approve",default="Approved with Manual Signature Required")
    
    change_password_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    convert_status_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    REQUIRED_FIELDS = ('email',)
    
    # WHAT SHOWS IN ADMIN PAGE
    def __str__(self):
        return self.username
 

class clearance_form_table(models.Model):
    student_id = models.CharField(max_length=100, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    present_address = models.CharField(max_length=100, verbose_name="Present Address")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
     
    date_filed = models.CharField(max_length=20, verbose_name="Date Filed")
    date_admitted_in_tup = models.CharField(
        max_length=20, verbose_name="Date Admitted")
    highschool_graduated = models.TextField(
        max_length=100, verbose_name="High School Graduated")
    tupc_graduate = models.CharField(
        max_length=10, verbose_name="TUPC Graduate", null=True)
    year_graduated_in_tupc = models.CharField(max_length=20,
        verbose_name="Year Graduated", default="NONE", null=True)
    number_of_terms_in_tupc = models.IntegerField(
        verbose_name="Number of Terms in TUPC", null=True)
    amount_paid = models.CharField(
        max_length=100, verbose_name="Amount Paid", default="0")
    have_previously_requested_form = models.CharField(
        max_length=10, verbose_name="Previous Request", default="NONE")
    date_of_previously_requested_form = models.CharField(
        max_length=20, verbose_name="Previous Request Date", default="NONE", null=True)
    last_term_in_tupc = models.IntegerField(
        verbose_name="Last Term in TUPC", default="NONE", null=True)
    purpose_of_request = models.CharField(
        max_length=100, verbose_name="Purpose of Request", default="NONE", null=True)
    purpose_of_request_reason = models.CharField(
        max_length=100, verbose_name="Purpose of Request Reason", default="NONE", null=True)
    semester_enrolled = models.CharField(
        max_length=100, verbose_name="Semester Enrolled in TUPC", default="NONE", null=True)
    or_num = models.CharField(max_length=50, blank=True ,null=True)

    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="0")
    liberal_arts_signature = models.CharField(max_length=100,
        verbose_name="Liberal Art Signature", default="UNAPPROVED")
    liberal_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    accountant_signature = models.CharField(max_length=100,
        verbose_name="Accountant Signature", default="UNAPPROVED")
    accountant_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)    
    
    mathsci_dept_signature = models.CharField(max_length=100,
        verbose_name="Math and Science Signature", default="UNAPPROVED")
    mathsci_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
        
    pe_dept_signature = models.CharField(max_length=100,
        verbose_name="P.E. Signature", default="UNAPPROVED")
    pe_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    ieduc_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Educ. Signature", default="UNAPPROVED")
    ieduc_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    it_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Tech. Signature", default="UNAPPROVED")
    it_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    eng_dept_signature = models.CharField(max_length=100,
        verbose_name="Engineering Signature", default="UNAPPROVED")
    eng_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    library_signature = models.CharField(max_length=100,
        verbose_name="Library Signature", default="UNAPPROVED")
    library_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    guidance_office_signature = models.CharField(max_length=100,
        verbose_name="Guidance Signature", default="UNAPPROVED")
    guidance_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    osa_signature = models.CharField(max_length=100,
        verbose_name="OSA Signature", default="UNAPPROVED")
    osa_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    academic_affairs_signature = models.CharField(max_length=100,
        verbose_name="Academic Affairs Signature", default="UNAPPROVED")
    academic_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    course_adviser = models.CharField(max_length=100,
        verbose_name="Course Adviser", default="NONE")
    course_adviser_signature = models.CharField(max_length=100,
        verbose_name="Course Adviser Signature", default="NONE")
    course_adviser_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    clear_notif = models.CharField(
        max_length=100, verbose_name="Notification", default="NONE", null=True)
    approved_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    time_requested = models.DateTimeField(auto_now_add=True)
    user_removed = models.CharField(max_length=50, blank = True, null= True, default="0")

    def __str__(self):
        return self.student_id


class graduation_form_table(models.Model):

    instructor = [
        ('', '--SELECT--'),
        ('Instructor1', 'Instructor1'),
        ('Instructor2', 'Instructor2'),
        ('Instructor3', 'Instructor3'),
        ('Instructor4', 'Instructor4'),
       
    ]

    add_instructor = [
        ('', '--SELECT--'),
        ('Instructor1', 'Instructor1'),
        ('Instructor2', 'Instructor2'),
        ('Instructor3', 'Instructor3'),
        ('Instructor4', 'Instructor4'),
       
    ]

    
    student_id = models.CharField(max_length=100, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
    purpose_of_request = models.CharField(max_length=100, verbose_name="Purpose of Request",
                                        default="Graduation Form", null=True)
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)

    shift = models.CharField(max_length=20, verbose_name="Shift")
    study_load = models.CharField(max_length=10, verbose_name="Study Load")
    status = models.CharField(max_length=10, verbose_name="Status")
    enrolled_term = models.CharField(max_length=100, verbose_name="Enrolled Term", null=True, default="NONE")
    unenrolled_application_deadline = models.CharField(max_length=20,verbose_name="Deadline", null=True, default="NONE")

    subject1 = models.CharField(max_length=50,verbose_name="Subject1", null=True, blank=True)
    room1 = models.CharField(max_length=50, verbose_name="Room1", null=True, blank=True)
    faculty1 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_1 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    day1_1 = models.CharField(max_length=50, verbose_name="Day1_1", null=True, blank=True)
    subject1_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject2 = models.CharField(max_length=50, verbose_name="Subject2", null=True, blank=True)
    room2 = models.CharField(max_length=50, verbose_name="Room2", null=True, blank=True)
    faculty2 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_2 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    day1_2 = models.CharField(max_length=50, verbose_name="Day1_2", null=True, blank=True)
    subject2_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject3 = models.CharField(max_length=50, verbose_name="Subject3", null=True, blank=True)
    room3 = models.CharField(max_length=50, verbose_name="Room3", null=True, blank=True)
    faculty3 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_3 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    day1_3 = models.CharField(max_length=50, verbose_name="Day1_3", null=True, blank=True)
    subject3_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject4 = models.CharField(max_length=50, verbose_name="Subject4", null=True, blank=True)
    room4 = models.CharField(max_length=50, verbose_name="Room4", null=True, blank=True)
    faculty4 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_4 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    day1_4 = models.CharField(max_length=50, verbose_name="Day1_4", null=True, blank=True)
    subject4_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject5 = models.CharField(max_length=50, verbose_name="Subject5", null=True, blank=True)
    room5 = models.CharField(max_length=50, verbose_name="Room5", null=True, blank=True)
    faculty5 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_5 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    day1_5 = models.CharField(max_length=50, verbose_name="Day1_5", null=True, blank=True)
    subject5_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject6 = models.CharField(max_length=50, verbose_name="Subject6", null=True, blank=True)
    room6 = models.CharField(max_length=50, verbose_name="Room6", null=True, blank=True)
    faculty6 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_6 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_6 = models.TimeField( null=True, blank=True, default='00:00')
    day1_6 = models.CharField(max_length=50, verbose_name="Day1_6", null=True, blank=True)
    subject6_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject7 = models.CharField(max_length=50, verbose_name="Subject7", null=True, blank=True)
    room7 = models.CharField(max_length=50,verbose_name="Room7", null=True, blank=True)
    faculty7 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_7 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_7 = models.TimeField( null=True, blank=True, default='00:00')
    day1_7 = models.CharField(max_length=50, verbose_name="Day1_7", null=True, blank=True)
    subject7_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject8 = models.CharField(max_length=50, verbose_name="Subject8", null=True, blank=True)
    room8 = models.CharField(max_length=50, verbose_name="Room8", null=True, blank=True)
    faculty8  = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_8 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_8 = models.TimeField( null=True, blank=True, default='00:00')
    day1_8 = models.CharField(max_length=50, verbose_name="Day1_8", null=True, blank=True)
    subject8_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    subject9 = models.CharField(max_length=50, verbose_name="Subject9", null=True, blank=True)
    room9 = models.CharField(max_length=50, verbose_name="Room9", null=True, blank=True)
    faculty9 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_9 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_9 = models.TimeField( null=True, blank=True, default='00:00')
    day1_9 = models.CharField(max_length=50, verbose_name="Day1_9", null=True, blank=True)
    subject9_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    subject10 = models.CharField(max_length=50, verbose_name="Subject10", null=True, blank=True)
    room10 = models.CharField(max_length=50, verbose_name="Room10", null=True, blank=True)
    faculty10 = models.CharField(max_length=50, null=True, blank=True, choices=instructor)
    starttime1_10 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_10 = models.TimeField( null=True, blank=True, default='00:00')
    day1_10 = models.CharField(max_length=50, verbose_name="Day1_10", null=True, blank=True)
    subject10_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    addsubject1 = models.CharField(max_length=50, verbose_name="Add Subject1", null=True, blank=True)
    addroom1 = models.CharField(max_length=50,verbose_name="Add Room1", null=True, blank=True)
    addfaculty1 = models.CharField(max_length=50, null=True, blank=True, choices=add_instructor)
    add_starttime1_1 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_1 = models.CharField(max_length=50, verbose_name="Add Day1_1", null=True, blank=True)
    addsubject1_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject2 = models.CharField(max_length=50, verbose_name="Add Subject2", null=True, blank=True)
    addroom2 = models.CharField(max_length=50, verbose_name="Add Room2", null=True, blank=True)
    addfaculty2 = models.CharField(max_length=50, null=True, blank=True, choices=add_instructor)
    add_starttime1_2 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_2 = models.CharField(max_length=50, verbose_name="Add Day1_2", null=True, blank=True)
    addsubject2_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    addsubject3 = models.CharField(max_length=50, verbose_name="Add Subject3", null=True, blank=True)
    addroom3 = models.CharField(max_length=50, verbose_name="Add Room3", null=True, blank=True)
    addfaculty3 = models.CharField(max_length=50, null=True, blank=True, choices=add_instructor)
    add_starttime1_3 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_3 = models.CharField(max_length=50, verbose_name="Add Day1_3", null=True, blank=True)
    addsubject3_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject4 = models.CharField(max_length=50, verbose_name="Add Subject4", null=True, blank=True)
    addroom4 = models.CharField(max_length=50, verbose_name="Add Room4", null=True, blank=True)
    addfaculty4 = models.CharField(max_length=50, null=True, blank=True, choices=add_instructor)
    add_starttime1_4 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_4 = models.CharField(max_length=50, verbose_name="Add Room1_4", null=True, blank=True)
    addsubject4_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject5 = models.CharField(max_length=50, verbose_name="Add Subject5", null=True, blank=True)
    addroom5 = models.CharField(max_length=50, verbose_name="Add Room5", null=True, blank=True)
    addfaculty5 = models.CharField(max_length=50, null=True, blank=True, choices=add_instructor)
    add_starttime1_5 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_5 = models.CharField(max_length=50,verbose_name="Add Day1_5", null=True, blank=True)
    addsubject5_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    trainP_startdate = models.CharField(max_length=30,verbose_name="Start", null=True, default="NONE")
    trainP_enddate = models.CharField(max_length=30,verbose_name="End", null=True, default="NONE")
    instructor_name = models.CharField(max_length=50, verbose_name="SIT Instructor")
    sit_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    approval_status = models.CharField(max_length=15,
                    verbose_name="Approval Status", default="0")
    signature1 = models.CharField(max_length=100)
    signature2 = models.CharField(max_length=100)
    signature3 = models.CharField(max_length=100)
    signature4 = models.CharField(max_length=100)
    signature5 = models.CharField(max_length=100)
    signature6 = models.CharField(max_length=100)
    signature7 = models.CharField(max_length=100)
    signature8 = models.CharField(max_length=100)
    signature9 = models.CharField(max_length=100)
    signature10 = models.CharField(max_length=100)
    
    addsignature1 = models.CharField(max_length=100)
    addsignature2 = models.CharField(max_length=100)
    addsignature3 = models.CharField(max_length=100)
    addsignature4 = models.CharField(max_length=100)
    addsignature5 = models.CharField(max_length=100)

    sitsignature = models.CharField(max_length=100)
    grad_notif = models.CharField(
        max_length=100, verbose_name="Notification", default="NONE", null=True)
    approved_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    time_requested = models.DateTimeField(auto_now_add=True)
    
    user_removed = models.CharField(max_length=50, blank = True, null= True, default="0")

    def __str__(self):
        return self.student_id

class request_form_table(models.Model):
    student_id = models.CharField(max_length=50, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    name2 = models.CharField(max_length=100, verbose_name="2nd Format Student Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
    date = models.CharField(max_length=20, verbose_name="Date")
    control_number = models.CharField(max_length=50, verbose_name="Control Number",null=True,default="NONE")
    contact_number = models.CharField( max_length=13, verbose_name="Contact Number", validators=[MinLengthValidator(13)])
    current_status = models.CharField(max_length=100, verbose_name="Current Status",null=True)
    request = models.CharField(
        max_length=100, verbose_name="Request", default="NONE", null=True)
    purpose_of_request_reason = models.CharField(
        max_length=100, verbose_name="Purpose of Request",null=True)
    amount = models.CharField(max_length=100, verbose_name="Amount", default="0")
    form_137 = models.CharField(max_length=50, default="❌",null=True)
    form_137_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    clearance = models.CharField(max_length=50, default="❌",null=True)
    clearance_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    official_receipt = models.CharField(max_length=50, default="❌",null=True)
    or_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    claim = models.CharField(max_length=50, default="UNCLAIMED", null=True)
    claim_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="UNAPPROVED")
    approval_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    or_num = models.CharField(max_length=50, blank=True ,null=True)
    or_date = models.CharField(max_length=50, blank=True ,null=True, verbose_name="O.R Date")
    
    time_requested = models.DateTimeField(auto_now_add=True)
    
    user_removed = models.CharField(max_length=50, blank = True, null= True, default="0")


    def __str__(self):
        return self.student_id 

#DELETED RECORDS TABLES
#USER DELETED ACCOUNT TABLE
class user_deleted_table(models.Model):
    
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, verbose_name="Full Name", null=True)
    prefix = models.CharField(max_length=100, verbose_name="Prefix", null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", null=True, blank=True, default="None")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    suffix = models.CharField(max_length=100, verbose_name="Suffix", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Address", null=True, blank=True)
    gender = models.CharField(max_length=100)
    birthday = models.CharField(max_length=8,verbose_name="Birthday")
    id_number = models.CharField(max_length=17, verbose_name="ID Number", 
                validators=[MinLengthValidator(6)], null=True)
    course = models.CharField(
            max_length=100, null=True, blank=True)
    course_graduated = models.CharField(
        max_length=100,null=True, blank=True)
    department = models.CharField(
        max_length=100, verbose_name="Department", null=True, blank=True)
    position = models.CharField(
        max_length=100, verbose_name="Position ", null=True, blank=True)
    asigned_position_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    remove_position_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    designation = models.CharField(
        max_length=100, verbose_name="Designation ", null=True, blank=True)
    year_graduated = models.CharField(
        max_length=100, verbose_name="Year Graduated", null=True, blank=True)
    year_and_section = models.CharField(
        max_length=100, null=True, blank=True)
    contact_number = models.CharField(
        max_length=13, verbose_name="Contact Number", validators=[MinLengthValidator(13)])
    email = models.EmailField(
        max_length=100, verbose_name="Email Address")
    user_type = models.CharField(max_length=100, verbose_name="User Type")
    student_id = models.CharField(max_length=100, verbose_name ="Student ID", null=True)
    username = models.CharField(max_length=100, null=True)
    profile_picture = models.CharField(max_length=100, null=True)
    e_signature = models.CharField(max_length=100, null=True)
    e_signature_timesaved = models.DateTimeField(auto_now_add=False)
    uploaded_signature = models.CharField(max_length=100, null=True)
    uploaded_signature_timesaved = models.DateTimeField(auto_now_add=False)
    no_signature = models.CharField(max_length=100, verbose_name="Approve",default="Approved with Manual Signature Required")
    
    change_password_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    convert_status_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    deleted_status = models.CharField(max_length=50, blank = True, null= True, default="0")
    deleted_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    def __str__(self):
        return self.username

#CLEARANCE DELETED FORMS TABLE
class clearance_form_deleted_table(models.Model):
    student_id = models.CharField(max_length=100, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    present_address = models.CharField(max_length=100, verbose_name="Present Address")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
     
    date_filed = models.CharField(max_length=20, verbose_name="Date Filed")
    date_admitted_in_tup = models.CharField(
        max_length=20, verbose_name="Date Admitted")
    highschool_graduated = models.TextField(
        max_length=100, verbose_name="High School Graduated")
    tupc_graduate = models.CharField(
        max_length=10, verbose_name="TUPC Graduate", null=True)
    year_graduated_in_tupc = models.CharField(max_length=20,
        verbose_name="Year Graduated", default="NONE", null=True)
    number_of_terms_in_tupc = models.IntegerField(
        verbose_name="Number of Terms in TUPC", null=True)
    amount_paid = models.CharField(
        max_length=100, verbose_name="Amount Paid", default="0")
    have_previously_requested_form = models.CharField(
        max_length=10, verbose_name="Previous Request", default="NONE")
    date_of_previously_requested_form = models.CharField(
        max_length=20, verbose_name="Previous Request Date", default="NONE", null=True)
    last_term_in_tupc = models.IntegerField(
        verbose_name="Last Term in TUPC", default="NONE", null=True)
    purpose_of_request = models.CharField(
        max_length=100, verbose_name="Purpose of Request", default="NONE", null=True)
    purpose_of_request_reason = models.CharField(
        max_length=100, verbose_name="Purpose of Request Reason", default="NONE", null=True)
    semester_enrolled = models.CharField(
        max_length=100, verbose_name="Semester Enrolled in TUPC", default="NONE", null=True)
    or_num = models.CharField(max_length=50, blank=True ,null=True)

    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="0")
    liberal_arts_signature = models.CharField(max_length=100,
        verbose_name="Liberal Art Signature", default="UNAPPROVED")
    liberal_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    accountant_signature = models.CharField(max_length=100,
        verbose_name="Accountant Signature", default="UNAPPROVED")
    accountant_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    mathsci_dept_signature = models.CharField(max_length=100,
        verbose_name="Math and Science Signature", default="UNAPPROVED")
    mathsci_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    pe_dept_signature = models.CharField(max_length=100,
        verbose_name="P.E. Signature", default="UNAPPROVED")
    pe_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    ieduc_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Educ. Signature", default="UNAPPROVED")
    ieduc_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    it_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Tech. Signature", default="UNAPPROVED")
    it_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    eng_dept_signature = models.CharField(max_length=100,
        verbose_name="Engineering Signature", default="UNAPPROVED")
    eng_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    library_signature = models.CharField(max_length=100,
        verbose_name="Library Signature", default="UNAPPROVED")
    library_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    guidance_office_signature = models.CharField(max_length=100,
        verbose_name="Guidance Signature", default="UNAPPROVED")
    guidance_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    osa_signature = models.CharField(max_length=100,
        verbose_name="OSA Signature", default="UNAPPROVED")
    osa_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    academic_affairs_signature = models.CharField(max_length=100,
        verbose_name="Academic Affairs Signature", default="UNAPPROVED")
    academic_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    course_adviser = models.CharField(max_length=100,
        verbose_name="Course Adviser", default="NONE")
    course_adviser_signature = models.CharField(max_length=100,
        verbose_name="Course Adviser Signature", default="NONE")
    course_adviser_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    clear_notif = models.CharField(
        max_length=100, verbose_name="Notification", default="NONE", null=True)
    approved_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    time_requested = models.DateTimeField(auto_now_add=False)
    deleted_status = models.CharField(max_length=50, blank = True, null= True, default="0")
    deleted_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.student_id
    
#GRADUATION DELETED FORMS TABLE
class graduation_form_deleted_table(models.Model):
    
    student_id = models.CharField(max_length=100, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
    purpose_of_request = models.CharField(max_length=100, verbose_name="Purpose of Request",
                                        default="Graduation Form", null=True)
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)

    shift = models.CharField(max_length=20, verbose_name="Shift")
    study_load = models.CharField(max_length=10, verbose_name="Study Load")
    status = models.CharField(max_length=10, verbose_name="Status")
    enrolled_term = models.CharField(max_length=100, verbose_name="Enrolled Term", null=True, default="NONE")
    unenrolled_application_deadline = models.CharField(max_length=20,verbose_name="Deadline", null=True, default="NONE")

    subject1 = models.CharField(max_length=50,verbose_name="Subject1", null=True, blank=True)
    room1 = models.CharField(max_length=50, verbose_name="Room1", null=True, blank=True)
    faculty1 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_1 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    day1_1 = models.CharField(max_length=50, verbose_name="Day1_1", null=True, blank=True)
    subject1_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject2 = models.CharField(max_length=50, verbose_name="Subject2", null=True, blank=True)
    room2 = models.CharField(max_length=50, verbose_name="Room2", null=True, blank=True)
    faculty2 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_2 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    day1_2 = models.CharField(max_length=50, verbose_name="Day1_2", null=True, blank=True)
    subject2_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject3 = models.CharField(max_length=50, verbose_name="Subject3", null=True, blank=True)
    room3 = models.CharField(max_length=50, verbose_name="Room3", null=True, blank=True)
    faculty3 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_3 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    day1_3 = models.CharField(max_length=50, verbose_name="Day1_3", null=True, blank=True)
    subject3_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject4 = models.CharField(max_length=50, verbose_name="Subject4", null=True, blank=True)
    room4 = models.CharField(max_length=50, verbose_name="Room4", null=True, blank=True)
    faculty4 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_4 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    day1_4 = models.CharField(max_length=50, verbose_name="Day1_4", null=True, blank=True)
    subject4_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject5 = models.CharField(max_length=50, verbose_name="Subject5", null=True, blank=True)
    room5 = models.CharField(max_length=50, verbose_name="Room5", null=True, blank=True)
    faculty5 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_5 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    day1_5 = models.CharField(max_length=50, verbose_name="Day1_5", null=True, blank=True)
    subject5_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject6 = models.CharField(max_length=50, verbose_name="Subject6", null=True, blank=True)
    room6 = models.CharField(max_length=50, verbose_name="Room6", null=True, blank=True)
    faculty6 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_6 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_6 = models.TimeField( null=True, blank=True, default='00:00')
    day1_6 = models.CharField(max_length=50, verbose_name="Day1_6", null=True, blank=True)
    subject6_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject7 = models.CharField(max_length=50, verbose_name="Subject7", null=True, blank=True)
    room7 = models.CharField(max_length=50,verbose_name="Room7", null=True, blank=True)
    faculty7 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_7 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_7 = models.TimeField( null=True, blank=True, default='00:00')
    day1_7 = models.CharField(max_length=50, verbose_name="Day1_7", null=True, blank=True)
    subject7_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject8 = models.CharField(max_length=50, verbose_name="Subject8", null=True, blank=True)
    room8 = models.CharField(max_length=50, verbose_name="Room8", null=True, blank=True)
    faculty8  = models.CharField(max_length=50, null=True, blank=True)
    starttime1_8 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_8 = models.TimeField( null=True, blank=True, default='00:00')
    day1_8 = models.CharField(max_length=50, verbose_name="Day1_8", null=True, blank=True)
    subject8_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject9 = models.CharField(max_length=50, verbose_name="Subject9", null=True, blank=True)
    room9 = models.CharField(max_length=50, verbose_name="Room9", null=True, blank=True)
    faculty9 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_9 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_9 = models.TimeField( null=True, blank=True, default='00:00')
    day1_9 = models.CharField(max_length=50, verbose_name="Day1_9", null=True, blank=True)
    subject9_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    subject10 = models.CharField(max_length=50, verbose_name="Subject10", null=True, blank=True)
    room10 = models.CharField(max_length=50, verbose_name="Room10", null=True, blank=True)
    faculty10 = models.CharField(max_length=50, null=True, blank=True)
    starttime1_10 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_10 = models.TimeField( null=True, blank=True, default='00:00')
    day1_10 = models.CharField(max_length=50, verbose_name="Day1_10", null=True, blank=True)
    subject10_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject1 = models.CharField(max_length=50, verbose_name="Add Subject1", null=True, blank=True)
    addroom1 = models.CharField(max_length=50,verbose_name="Add Room1", null=True, blank=True)
    addfaculty1 = models.CharField(max_length=50, null=True, blank=True)
    add_starttime1_1 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_1 = models.CharField(max_length=50, verbose_name="Add Day1_1", null=True, blank=True)
    addsubject1_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject2 = models.CharField(max_length=50, verbose_name="Add Subject2", null=True, blank=True)
    addroom2 = models.CharField(max_length=50, verbose_name="Add Room2", null=True, blank=True)
    addfaculty2 = models.CharField(max_length=50, null=True, blank=True)
    add_starttime1_2 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_2 = models.CharField(max_length=50, verbose_name="Add Day1_2", null=True, blank=True)
    addsubject2_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject3 = models.CharField(max_length=50, verbose_name="Add Subject3", null=True, blank=True)
    addroom3 = models.CharField(max_length=50, verbose_name="Add Room3", null=True, blank=True)
    addfaculty3 = models.CharField(max_length=50, null=True, blank=True)
    add_starttime1_3 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_3 = models.CharField(max_length=50, verbose_name="Add Day1_3", null=True, blank=True)
    addsubject3_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject4 = models.CharField(max_length=50, verbose_name="Add Subject4", null=True, blank=True)
    addroom4 = models.CharField(max_length=50, verbose_name="Add Room4", null=True, blank=True)
    addfaculty4 = models.CharField(max_length=50, null=True, blank=True)
    add_starttime1_4 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_4 = models.CharField(max_length=50, verbose_name="Add Room1_4", null=True, blank=True)
    addsubject4_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    addsubject5 = models.CharField(max_length=50, verbose_name="Add Subject5", null=True, blank=True)
    addroom5 = models.CharField(max_length=50, verbose_name="Add Room5", null=True, blank=True)
    addfaculty5 = models.CharField(max_length=50, null=True, blank=True)
    add_starttime1_5 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_5 = models.CharField(max_length=50,verbose_name="Add Day1_5", null=True, blank=True)
    addsubject5_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    trainP_startdate = models.CharField(max_length=30,verbose_name="Start", null=True, default="NONE")
    trainP_enddate = models.CharField(max_length=30,verbose_name="End", null=True, default="NONE")
    instructor_name = models.CharField(max_length=50, verbose_name="SIT Instructor")
    sit_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    approval_status = models.CharField(max_length=15,
                    verbose_name="Approval Status", default="0")
    signature1 = models.CharField(max_length=100)
    signature2 = models.CharField(max_length=100)
    signature3 = models.CharField(max_length=100)
    signature4 = models.CharField(max_length=100)
    signature5 = models.CharField(max_length=100)
    signature6 = models.CharField(max_length=100)
    signature7 = models.CharField(max_length=100)
    signature8 = models.CharField(max_length=100)
    signature9 = models.CharField(max_length=100)
    signature10 = models.CharField(max_length=100)
    
    addsignature1 = models.CharField(max_length=100)
    addsignature2 = models.CharField(max_length=100)
    addsignature3 = models.CharField(max_length=100)
    addsignature4 = models.CharField(max_length=100)
    addsignature5 = models.CharField(max_length=100)

    sitsignature = models.CharField(max_length=100)
    grad_notif = models.CharField(
        max_length=100, verbose_name="Notification", default="NONE", null=True)
    approved_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    
    time_requested = models.DateTimeField(auto_now_add=False)
    
    deleted_status = models.CharField(max_length=50, blank = True, null= True, default = "0")
    deleted_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.student_id

#DELETED REQUEST FORMS TABLE
class request_form_deleted_table(models.Model):
    student_id = models.CharField(max_length=50, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    name2 = models.CharField(max_length=100, verbose_name="2nd Format Student Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    course = models.CharField(max_length=100, verbose_name="Student Course",null=True, default="NONE")
    date = models.CharField(max_length=20, verbose_name="Date")
    control_number = models.CharField(max_length=50, verbose_name="Control Number",null=True,default="NONE")
    contact_number = models.CharField( max_length=13, verbose_name="Contact Number", validators=[MinLengthValidator(13)])
    current_status = models.CharField(max_length=100, verbose_name="Current Status",null=True)
    request = models.CharField(
        max_length=100, verbose_name="Request", default="NONE", null=True)
    purpose_of_request_reason = models.CharField(
        max_length=100, verbose_name="Purpose of Request",null=True)
    amount = models.CharField(max_length=100, verbose_name="Amount", default="0")
    form_137 = models.CharField(max_length=50, default="❌",null=True)
    form_137_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    clearance = models.CharField(max_length=50, default="❌",null=True)
    clearance_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    official_receipt = models.CharField(max_length=50, default="❌",null=True)
    or_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    claim = models.CharField(max_length=50, default="UNCLAIMED", null=True)
    claim_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="UNAPPROVED")
    approval_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    or_num = models.CharField(max_length=50, blank=True ,null=True)
    or_date = models.CharField(max_length=50, blank=True ,null=True, verbose_name="O.R Date")
    
    time_requested = models.DateTimeField(auto_now_add=False)
    
    deleted_status = models.CharField(max_length=50, blank=True ,null=True, default ="0")
    deleted_timestamp = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.student_id  