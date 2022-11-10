from operator import truediv
from unicodedata import name
from unittest.util import *
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
import datetime
from PIL import Image
from distutils.command.upload import upload

class user_table(AbstractUser):

    courses = [
        ('', '--SELECT--'),
        ('BSCE', 'Bachelor of Science in Civil Engineering'),
        ('BSEE', 'Bachelor of Science in Electrical Engineering'),
        ('BSME', 'Bachelor of Science in Mechanical Engineering'),
        ('BSIE-ICT', 'Bachelor of Science in Industrial Education major in Information and Communication Technology'),
        ('BSIE-HE', 'Bachelor of Science in Industrial Education major in Home Economics'),
        ('BTTE-CP', 'Bachelor of Technical Teachers Education major in Computer Programming'),
        ('BTTE-EI', 'Bachelor of Technical Teachers Education major in Electronics'),
        ('BTTE-AU', 'Bachelor of Technical Teachers Education major in Automotive'),
        ('BTTE-HVACT', 'Bachelor of Technical Teachers Education major in Heatingg, Ventilation and Air Conditioning Tecnology'),
        ('BTTE-E', 'Bachelor of Technical Teachers Education major in Electrical'),
        ('BGT-AT', 'Bachelor of Engineering Technolgy major in Architecture Technology'),
        ('BET-CT', 'Bachelor of Engineering Technolgy major in Civil Engineering Technology'),
        ('BET-ET', 'Bachelor of Engineering Technolgy major in Electrical Engineering Technology'),
        ('BET-EsET', 'Bachelor of Engineering Technolgy major in Electronics Engineering Technology'),
        ('BET-CoET', 'Bachelor of Engineering Technolgy major in Computer Engineering Technology'),
        ('BET-MT', 'Bachelor of Engineering Technolgy major in Mechanical & Production Engineering Technology'),
        ('BET-PPT', 'Bachelor of Engineering Technolgy major in Power Plant Engineering Technology'),
        ('BET-AT', 'Bachelor of Engineering Technolgy major in Automotive Engineering Technology'),
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
        ('DED', 'Industrial Educational Department (DED)'),
        ('DIT', 'Industrial Technology Department (DIT)'),
        ('DIE', 'Industrial Engineering Department (DIE)'),
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
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", null=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    gender = models.CharField(
        max_length=100, choices=gender, null=True, blank=True)
    id_number = models.CharField(
        max_length=7, verbose_name="ID Number", validators=[MinLengthValidator(7)],  unique=True)
    course = models.CharField(
        max_length=100, choices=courses, null=True, blank=True)
    department = models.CharField(
        max_length=100, choices=department, verbose_name="Department", null=True, blank=True)
    position = models.CharField(
        max_length=100, verbose_name="Position ", null=True, blank=True)
    designation = models.CharField(
        max_length=100, verbose_name="Designation ", null=True, blank=True)
    course_graduated = models.CharField(
        max_length=100, choices=courses, null=True, blank=True)
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
    profile_picture = models.ImageField(upload_to='uploads/')
    uploaded_signature = models.ImageField(upload_to='signatures/',blank=True)# PIP INSTALL PILLOW
    signature_timesaved = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ('email',)
    
    # WHAT SHOWS IN ADMIN PAGE
    def __str__(self):
        return self.username
 

class clearance_form_table(models.Model):
    # form_id = models.ForeignKey(user_table, on_delete=models.CASCADE, primary_key=True, unique=True)
    student_id = models.CharField(max_length=20, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    present_address = models.CharField(max_length=100, verbose_name="Present Address")
    course = models.CharField(max_length=50, verbose_name="Student Course",null=True, default="NONE")
     
    date_filed = models.CharField(max_length=20, verbose_name="Date Filed")
    date_admitted_in_tup = models.CharField(
        max_length=20, verbose_name="Date Admitted")
    highschool_graduated = models.TextField(
        max_length=10, verbose_name="High School Graduated")
    tupc_graduate = models.CharField(
        max_length=10, verbose_name="TUPC Graduate")
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

    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="0")
    liberal_arts_signature = models.CharField(max_length=100,
        verbose_name="Liberal Art Signature", default="UNAPPROVED")
    accountant_signature = models.CharField(max_length=100,
        verbose_name="Accountant Signature", default="UNAPPROVED")
    mathsci_dept_signature = models.CharField(max_length=100,
        verbose_name="Math and Science Signature", default="UNAPPROVED")
    pe_dept_signature = models.CharField(max_length=100,
        verbose_name="P.E. Signature", default="UNAPPROVED")
    ieduc_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Educ. Signature", default="UNAPPROVED")
    it_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Tech. Signature", default="UNAPPROVED")
    ieng_dept_signature = models.CharField(max_length=100,
        verbose_name="Industrial Eng. Signature", default="UNAPPROVED")
    library_signature = models.CharField(max_length=100,
        verbose_name="Library Signature", default="UNAPPROVED")
    guidance_office_signature = models.CharField(max_length=100,
        verbose_name="Guidance Signature", default="UNAPPROVED")
    osa_signature = models.CharField(max_length=100,
        verbose_name="OSA Signature", default="UNAPPROVED")
    academic_affairs_signature = models.CharField(max_length=100,
        verbose_name="Academic Affairs Signature", default="UNAPPROVED")
    course_adviser = models.CharField(max_length=100,
        verbose_name="Course Adviser", default="NONE")
    course_adviser_signature = models.ImageField(upload_to='signature/')
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    
    time_requested = models.DateTimeField(auto_now_add=True)

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

    
    student_id = models.CharField(max_length=20, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    course = models.CharField(max_length=50, verbose_name="Student Course",null=True, default="NONE")
    purpose_of_request = models.CharField(max_length=100, verbose_name="Purpose of Request",
                                        default="Graduation Form", null=True)
    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="0")
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)

    shift = models.CharField(max_length=20, verbose_name="Shift")
    study_load = models.CharField(max_length=10, verbose_name="Study Load")
    status = models.CharField(max_length=10, verbose_name="Status")
    enrolled_term = models.CharField(max_length=100, verbose_name="Enrolled Term", null=True, default="NONE")
    unenrolled_application_deadline = models.CharField(max_length=20,verbose_name="Deadline", null=True, default="NONE")

    subject1 = models.CharField(max_length=100,verbose_name="Subject1", null=True, default="NONE")
    room1 = models.CharField(max_length=100, verbose_name="Room1", null=True, default="NONE")
    faculty1 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_1 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    day1_1 = models.CharField(max_length=100, verbose_name="Day1_1", null=True, default="NONE")

    subject2 = models.CharField(max_length=100, verbose_name="Subject2", null=True, default="NONE")
    room2 = models.CharField(max_length=100, verbose_name="Room2", null=True, default="NONE")
    faculty2 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_2 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    day1_2 = models.CharField(max_length=100, verbose_name="Day1_2", null=True, default="NONE")

    subject3 = models.CharField(max_length=100, verbose_name="Subject3", null=True, default="NONE")
    room3 = models.CharField(max_length=100, verbose_name="Room3", null=True, default="NONE")
    faculty3 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_3 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    day1_3 = models.CharField(max_length=100, verbose_name="Day1_3", null=True, default="NONE")

    subject4 = models.CharField(max_length=100, verbose_name="Subject4", null=True, default="NONE")
    room4 = models.CharField(max_length=100, verbose_name="Room4", null=True, default="NONE")
    faculty4 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_4 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    day1_4 = models.CharField(max_length=100, verbose_name="Day1_4", null=True, default="NONE")

    subject5 = models.CharField(max_length=100, verbose_name="Subject5", null=True, default="NONE")
    room5 = models.CharField(max_length=100, verbose_name="Room5", null=True, default="NONE")
    faculty5 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_5 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    day1_5 = models.CharField(max_length=100, verbose_name="Day1_5", null=True, default="NONE")

    subject6 = models.CharField(max_length=100, verbose_name="Subject6", null=True, default="NONE")
    room6 = models.CharField(max_length=100, verbose_name="Room6", null=True, default="NONE")
    faculty6 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_6 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_6 = models.TimeField( null=True, blank=True, default='00:00')
    day1_6 = models.CharField(max_length=100, verbose_name="Day1_6", null=True, default="NONE")

    subject7 = models.CharField(max_length=100, verbose_name="Subject7", null=True, default="NONE")
    room7 = models.CharField(max_length=100,verbose_name="Room7", null=True, default="NONE")
    faculty7 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_7 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_7 = models.TimeField( null=True, blank=True, default='00:00')
    day1_7 = models.CharField(max_length=100, verbose_name="Day1_7", null=True, default="NONE")

    subject8 = models.CharField(max_length=100, verbose_name="Subject8", null=True, default="NONE")
    room8 = models.CharField(max_length=100, verbose_name="Room8", null=True, default="NONE")
    faculty8  = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_8 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_8 = models.TimeField( null=True, blank=True, default='00:00')
    day1_8 = models.CharField(max_length=100, verbose_name="Day1_8", null=True, default="NONE")

    subject9 = models.CharField(max_length=100, verbose_name="Subject9", null=True, default="NONE")
    room9 = models.CharField(max_length=100, verbose_name="Room9", null=True, default="NONE")
    faculty9 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_9 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_9 = models.TimeField( null=True, blank=True, default='00:00')
    day1_9 = models.CharField(max_length=100, verbose_name="Day1_9", null=True, default="NONE")

    subject10 = models.CharField(max_length=100, verbose_name="Subject10", null=True, default="NONE")
    room10 = models.CharField(max_length=100, verbose_name="Room10", null=True, default="NONE")
    faculty10 = models.CharField(max_length=100, null=True, blank=True, choices=instructor)
    starttime1_10 = models.TimeField( null=True,  blank=True, default='00:00')
    endtime1_10 = models.TimeField( null=True, blank=True, default='00:00')
    day1_10 = models.CharField(max_length=100, verbose_name="Day1_10", null=True, default="NONE")

    addsubject1 = models.CharField(max_length=100, verbose_name="Add Subject1", null=True, default="NONE")
    addroom1 = models.CharField(max_length=100,verbose_name="Add Room1", null=True, default="NONE")
    addfaculty1 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_1 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_1 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_1 = models.CharField(max_length=100, verbose_name="Add Day1_1", null=True, default="NONE")

    addsubject2 = models.CharField(max_length=100, verbose_name="Add Subject2", null=True, default="NONE")
    addroom2 = models.CharField(max_length=100, verbose_name="Add Room2", null=True, default="NONE")
    addfaculty2 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_2 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_2 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_2 = models.CharField(max_length=100, verbose_name="Add Day1_2", null=True, default="NONE")

    addsubject3 = models.CharField(max_length=100, verbose_name="Add Subject3", null=True, default="NONE")
    addroom3 = models.CharField(max_length=100, verbose_name="Add Room3", null=True, default="NONE")
    addfaculty3 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_3 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_3 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_3 = models.CharField(max_length=100, verbose_name="Add Day1_3", null=True, default="NONE")

    addsubject4 = models.CharField(max_length=100, verbose_name="Add Subject4", null=True, default="NONE")
    addroom4 = models.CharField(max_length=100, verbose_name="Add Room4", null=True, default="NONE")
    addfaculty4 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_4 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_4 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_4 = models.CharField(max_length=100, verbose_name="Add Room1_4", null=True, default="NONE")

    addsubject5 = models.CharField(max_length=100, verbose_name="Add Subject5", null=True, default="NONE")
    addroom5 = models.CharField(max_length=100, verbose_name="Add Room5", null=True, default="NONE")
    addfaculty5 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_5 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_5 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_5 = models.CharField(max_length=100,verbose_name="Add Day1_5", null=True, default="NONE")

    addsubject6 = models.CharField(max_length=100, verbose_name="Add Subject6", null=True, default="NONE")
    addroom6 = models.CharField(max_length=100, verbose_name="Add Room6", null=True, default="NONE")
    addfaculty6 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_6 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_6 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_6 = models.CharField(max_length=100, verbose_name="Add Day1_6", null=True, default="NONE")

    addsubject7 = models.CharField(max_length=100, verbose_name="Add Subject7", null=True, default="NONE")
    addroom7 = models.CharField(max_length=100, verbose_name="Add Room7", null=True, default="NONE")
    addfaculty7 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_7 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_7 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_7 = models.CharField(max_length=100, verbose_name="Add Day1_7", null=True, default="NONE")

    addsubject8 = models.CharField(max_length=100,verbose_name="Add Subject8", null=True, default="NONE")
    addroom8 = models.CharField(max_length=100,verbose_name="Add Room8", null=True, default="NONE")
    addfaculty8 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_8 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_8 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_8 = models.CharField(max_length=100, verbose_name="Add Day1_8", null=True, default="NONE")

    addsubject9 = models.CharField(max_length=100, verbose_name="Add Subject9", null=True, default="NONE")
    addroom9 = models.CharField(max_length=100, verbose_name="Add Room9", null=True, default="NONE")
    addfaculty9 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_9 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_9 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_9 = models.CharField(max_length=100, verbose_name="Add Day1_9", null=True, default="NONE")

    addsubject10 = models.CharField(max_length=100, verbose_name="Add Subject10", null=True, default="NONE")
    addroom10 = models.CharField(max_length=100, verbose_name="Add Room10", null=True, default="NONE")
    addfaculty10 = models.CharField(max_length=100, null=True, blank=True, choices=add_instructor)
    add_starttime1_10 = models.TimeField(null=True, blank=True, default='00:00')
    add_endtime1_10 = models.TimeField( null=True, blank=True, default='00:00')
    addday1_10 = models.CharField(max_length=100, verbose_name="Add Day1_10", null=True, default="NONE")
    
    trainP_startdate = models.CharField(max_length=30,verbose_name="Start", null=True, default="NONE")
    trainP_enddate = models.CharField(max_length=30,verbose_name="End", null=True, default="NONE")
    instructor_name = models.CharField(max_length=100, verbose_name="SIT Instructor")
    
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
    addsignature6 = models.CharField(max_length=100)
    addsignature7 = models.CharField(max_length=100)
    addsignature8 = models.CharField(max_length=100)
    addsignature9 = models.CharField(max_length=100)
    addsignature10 = models.CharField(max_length=100)

    sitsignature = models.CharField(max_length=100)
    
    time_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id

class request_form_table(models.Model):
    student_id = models.CharField(max_length=20, verbose_name="Student Id")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    name2 = models.CharField(max_length=100, verbose_name="2nd Format Student Name")
    address = models.CharField(max_length=100, verbose_name="Address")
    course = models.CharField(max_length=50, verbose_name="Student Course",null=True, default="NONE")
    date = models.CharField(max_length=20, verbose_name="Date")
    control_number = models.CharField(max_length=50, verbose_name="Control Number",null=True,default="NONE")
    contact_number = models.CharField( max_length=13, verbose_name="Contact Number", validators=[MinLengthValidator(13)])
    current_status = models.CharField(max_length=100, verbose_name="Current Status",null=True)
    request = models.CharField(
        max_length=100, verbose_name="Request", default="NONE", null=True)
    purpose_of_request_reason = models.CharField(
        max_length=100, verbose_name="Purpose of Request",null=True)
    
    TOR = models.CharField(max_length=50,default="❌",null=True)
    form_137 = models.CharField(max_length=50, default="❌",null=True)
    clearance = models.CharField(max_length=50, default="❌",null=True)
    official_receipt = models.CharField(max_length=50, default="❌",null=True)
    claim = models.CharField(max_length=50, default="UNCLAIMED", null=True)
    approval_status = models.CharField(max_length=15,
        verbose_name="Approval Status", default="UNAPPROVED")
    appointment = models.CharField(
        max_length=100, verbose_name="Appointment", default="NONE", null=True)
    
    time_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id    
class Document_checker_table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    TOR = models.CharField(max_length=50)
    form_137 = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name