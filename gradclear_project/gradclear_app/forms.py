from dataclasses import field
import imp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class signup_form(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}))

    class Meta(UserCreationForm):
        model = user_table
        fields = ['email', 'first_name', 'last_name', 'middle_name','address', 'gender', 'course', 'password1',
                  'contact_number', 'year_and_section', 'id_number', 'password2', 'department','profile_picture','course_graduated','year_graduated']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TUPC-00-0000'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No., Street, Subdivision, Brgy., Province'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'year_and_section': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(09)00-000-0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'firstname.lastname@gsfe.tupcavite.edu.ph'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course_graduated': forms.Select(attrs={'class': 'form-control'}),
            'year_graduated': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2000-2001'})
        }

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class Graduation_form_table(ModelForm):
    class Meta(ModelForm):
        model = graduation_form_table
        fields = ['subject1','subject2','subject3','subject4','subject5','subject6','subject7','subject8','subject9','subject10', 
        'room1', 'room2','room3','room4','room5','room6','room7','room8','room9','room10',
        'faculty1','faculty2','faculty3','faculty4','faculty5', 'faculty6', 'faculty7','faculty8','faculty9','faculty10', 
        'day1_1','day1_2','day1_3','day1_4','day1_5','day1_6','day1_7','day1_8','day1_9','day1_10','day2','day3', 
        'starttime1_1','starttime1_2','starttime1_3','starttime1_4','starttime1_5','starttime1_6','starttime1_7','starttime1_8','starttime1_9','starttime1_10',
        'endtime1_1','endtime1_2','endtime1_3','endtime1_4','endtime1_5','endtime1_6','endtime1_7','endtime1_8','endtime1_9','endtime1_10',
        'addsubject1','addsubject2','addsubject3','addsubject4','addsubject5','addsubject6','addsubject7','addsubject8','addsubject9','addsubject10',
        'addroom1','addroom2','addroom3','addroom4','addroom5','addroom6','addroom7','addroom8','addroom9','addroom10',
        'addfaculty1','addfaculty2','addfaculty3','addfaculty4','addfaculty5','addfaculty6','addfaculty7','addfaculty8','addfaculty9','addfaculty10',
        'addday1_1','addday1_2','addday1_3','addday1_4','addday1_5','addday1_6','addday1_7','addday1_8','addday1_9','addday1_10',
        'add_starttime1_1','add_starttime1_2','add_starttime1_3','add_starttime1_4','add_starttime1_5','add_starttime1_6','add_starttime1_7','add_starttime1_8','add_starttime1_9','add_starttime1_10',
        'add_endtime1_1','add_endtime1_2','add_endtime1_3','add_endtime1_4','add_endtime1_5','add_endtime1_6','add_endtime1_7','add_endtime1_8','add_endtime1_9','add_endtime1_10',
        'addday2', 'addday3', 'enrolled_term', 'unenrolled_application_deadline']

        widgets = {
            'subject1': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject2': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject3': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject4': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject5': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject6': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject7': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject8': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject9': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'subject10': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),

            'room1': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room2': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room3': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room4': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room5': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room6': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room7': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room8': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room9': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),
            'room10': forms.Select(attrs={'class': 'form-control input-add col-m-8'}),

            'faculty1': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty2': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty3': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty4': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty5': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty6': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty7': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty8': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty9': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),
            'faculty10': forms.Select(attrs={'class': 'form-control input-add col-m-9'}),

            'day1_1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_6': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_7': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_8': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_9': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day1_10': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'day2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'day3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'starttime1_1': TimePickerInput(),
            'endtime1_1': TimePickerInput(),
            'starttime1_2': TimePickerInput(),
            'endtime1_2': TimePickerInput(),
            'starttime1_3': TimePickerInput(),
            'endtime1_3': TimePickerInput(),
            'starttime1_4': TimePickerInput(),
            'endtime1_4': TimePickerInput(),
            'starttime1_5': TimePickerInput(),
            'endtime1_5': TimePickerInput(),
            'starttime1_6': TimePickerInput(),
            'endtime1_6': TimePickerInput(),
            'starttime1_7': TimePickerInput(),
            'endtime1_7': TimePickerInput(),
            'starttime1_8': TimePickerInput(),
            'endtime1_8': TimePickerInput(),
            'starttime1_9': TimePickerInput(),
            'endtime1_9': TimePickerInput(),
            'starttime1_10':TimePickerInput(),
            'endtime1_10': TimePickerInput(),

            'addsubject1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject6': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject7': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject8': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject9': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addsubject10': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'addroom1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom6': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom7': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom8': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom9': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addroom10': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'addfaculty1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty6': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty7': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty8': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty9': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty10': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'addday1_1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_6': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_7': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_8': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_9': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday1_10': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'addday2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addday3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'add_starttime1_1': TimePickerInput(),
            'add_endtime1_1': TimePickerInput(),
            'add_starttime1_2': TimePickerInput(),
            'add_endtime1_2': TimePickerInput(),
            'add_starttime1_3': TimePickerInput(),
            'add_endtime1_3': TimePickerInput(),
            'add_starttime1_4':TimePickerInput(),
            'add_endtime1_4': TimePickerInput(),
            'add_starttime1_5': TimePickerInput(),
            'add_endtime1_5': TimePickerInput(),
            'add_starttime1_6': TimePickerInput(),
            'add_endtime1_6': TimePickerInput(),
            'add_starttime1_7': TimePickerInput(),
            'add_endtime1_7': TimePickerInput(),
            'add_starttime1_8': TimePickerInput(),
            'add_endtime1_8': TimePickerInput(),
            'add_starttime1_9': TimePickerInput(),
            'add_endtime1_9': TimePickerInput(),
            'add_starttime1_10': TimePickerInput(),
            'add_endtime1_10': TimePickerInput(),

            'enrolled_term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'}), 
            'unenrolled_application_deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'})
        }

