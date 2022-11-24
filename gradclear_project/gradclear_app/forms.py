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
        fields = ['email', 'first_name', 'last_name', 'middle_name', 'address', 'gender', 'birthday', 'course', 'password1',
                  'contact_number', 'year_and_section', 'id_number', 'password2', 'department', 'profile_picture', 'course_graduated', 'year_graduated', 'uploaded_signature']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No., Street, Subdivision, Brgy., Province'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YY'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'course_graduated': forms.Select(attrs={'class': 'form-control'}),
            'year_and_section': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(09)00-000-0000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'year_graduated': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g.2000'})
        }

class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class Graduation_form_table(ModelForm):
    class Meta(ModelForm):
        model = graduation_form_table
        fields = ['subject1', 'subject2', 'subject3', 'subject4', 'subject5', 'subject6', 'subject7', 'subject8', 'subject9', 'subject10',
                  'room1', 'room2', 'room3', 'room4', 'room5', 'room6', 'room7', 'room8', 'room9', 'room10',
                  'faculty1', 'faculty2', 'faculty3', 'faculty4', 'faculty5', 'faculty6', 'faculty7', 'faculty8', 'faculty9', 'faculty10',
                  'day1_1', 'day1_2', 'day1_3', 'day1_4', 'day1_5', 'day1_6', 'day1_7', 'day1_8', 'day1_9', 'day1_10',
                  'starttime1_1', 'starttime1_2', 'starttime1_3', 'starttime1_4', 'starttime1_5', 'starttime1_6', 'starttime1_7', 'starttime1_8', 'starttime1_9', 'starttime1_10',
                  'endtime1_1', 'endtime1_2', 'endtime1_3', 'endtime1_4', 'endtime1_5', 'endtime1_6', 'endtime1_7', 'endtime1_8', 'endtime1_9', 'endtime1_10',
                  'addsubject1', 'addsubject2', 'addsubject3', 'addsubject4', 'addsubject5','addroom1', 'addroom2', 'addroom3', 'addroom4', 'addroom5',
                  'addfaculty1', 'addfaculty2', 'addfaculty3', 'addfaculty4', 'addfaculty5',
                  'addday1_1', 'addday1_2', 'addday1_3', 'addday1_4', 'addday1_5','add_starttime1_1', 'add_starttime1_2', 'add_starttime1_3', 'add_starttime1_4', 'add_starttime1_5',
                  'add_endtime1_1', 'add_endtime1_2', 'add_endtime1_3', 'add_endtime1_4', 'add_endtime1_5','enrolled_term', 'unenrolled_application_deadline']

        widgets = {
            'subject1': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.CPET16'}),
            'subject2': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.CPET18', 'disabled':'True'}),
            'subject3': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.BET5' , 'disabled':'True'}),
            'subject4': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.BET3', 'disabled':'True'}),
            'subject5': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ELECTIVE', 'disabled':'True'}),
            'subject6': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.GEC3', 'disabled':'True'}),
            'subject7': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.GEC7', 'disabled':'True'}),
            'subject8': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.LAB1', 'disabled':'True'}),
            'subject9': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.LAB2', 'disabled':'True'}),
            'subject10': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.CPET8', 'disabled':'True'}),

            'room1': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM201'}),
            'room2': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM202', 'disabled':'True'}),
            'room3': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM203', 'disabled':'True'}),
            'room4': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM204', 'disabled':'True'}),
            'room5': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM205', 'disabled':'True'}),
            'room6': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM206', 'disabled':'True'}),
            'room7': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM207', 'disabled':'True'}),
            'room8': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM208', 'disabled':'True'}),
            'room9': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM209', 'disabled':'True'}),
            'room10': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM210', 'disabled':'True'}),

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

            'day1_1': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days'}),
            'day1_2': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_3': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_4': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_5': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_6': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_7': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_8': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_9': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'day1_10': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),



            'starttime1_1': TimePickerInput(),
            'endtime1_1': TimePickerInput(),
            'starttime1_2': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_2': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_3': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_3': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_4': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_4': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_5': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_5': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_6': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_6': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_7': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_7': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_8': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_8': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_9': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_9': TimePickerInput(attrs={'disabled':'True'}),
            'starttime1_10': TimePickerInput(attrs={'disabled':'True'}),
            'endtime1_10': TimePickerInput(attrs={'disabled':'True'}),

            'addsubject1': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.CPET16'}),
            'addsubject2': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.CPET18', 'disabled':'True'}),
            'addsubject3': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.BET5', 'disabled':'True'}),
            'addsubject4': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.BET3', 'disabled':'True'}),
            'addsubject5': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ELECTIVE', 'disabled':'True'}),

            'addroom1': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM201'}),
            'addroom2': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM202', 'disabled':'True'}),
            'addroom3': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM203', 'disabled':'True'}),
            'addroom4': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM204', 'disabled':'True'}),
            'addroom5': forms.TextInput(attrs={'class': 'form-control input-add col-m-8', 'placeholder': 'e.g.ROOM205', 'disabled':'True'}),

            'addfaculty1': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty2': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty3': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty4': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),
            'addfaculty5': forms.Select(attrs={'class': 'form-control input-add col-sm-9'}),

            'addday1_1': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days'}),
            'addday1_2': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'addday1_3': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'addday1_4': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),
            'addday1_5': forms.TextInput(attrs={'class': 'form-control input-add col-sm-9', 'placeholder': 'no. of days', 'disabled':'True'}),

            'add_starttime1_1': TimePickerInput(),
            'add_endtime1_1': TimePickerInput(),
            'add_starttime1_2': TimePickerInput(attrs={'disabled':'True'}),
            'add_endtime1_2': TimePickerInput(attrs={'disabled':'True'}),
            'add_starttime1_3': TimePickerInput(attrs={'disabled':'True'}),
            'add_endtime1_3': TimePickerInput(attrs={'disabled':'True'}),
            'add_starttime1_4': TimePickerInput(attrs={'disabled':'True'}),
            'add_endtime1_4': TimePickerInput(attrs={'disabled':'True'}),
            'add_starttime1_5': TimePickerInput(attrs={'disabled':'True'}),
            'add_endtime1_5': TimePickerInput(attrs={'disabled':'True'}),

            'enrolled_term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'}),
            'unenrolled_application_deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00-0000'})
        }
