import email
from genericpath import exists
import profile
import imghdr
from queue import Empty
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, mail_admins, mail_managers, EmailMessage, EmailMultiAlternatives
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core import mail
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from textwrap import wrap
from django.db import connection
import base64
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
import datetime
from datetime import datetime, date, timedelta
import os
import time
import random

# NOTES: PATHS ARE ALL BASED FROM ONLINE DEPLOYMENT, CHANGE IT DEPENDING ON LOCAL COMPUTER PATH

# RENDER PRIVACY POLICY FROM COVER PAGE
def privacy_policy(request):
    return render(request, 'html_files/privacy policy.html')

# PRINT REQUEST FORMS
@login_required(login_url='/')
def req_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = request_form_table.objects.get(id=id)

    textob = p.beginText()

    print(content)
    print("hello world")

    lines = []

# Request Form
    p.setFont("Helvetica", 8)
    p.drawString(78, 775, f'{content.name2}')
    p.drawString(400, 775, f'{content.date}')
    p.drawString(520, 775, f'{content.control_number}')
    p.drawString(445, 760, f'{content.contact_number}')
    p.drawString(110, 635, f'{content.appointment}')


# list of payments
    p.setFont("Helvetica", 9)
    p.drawString(78, 462, f'{content.name2}')

    p.drawString(450, 462, f'{content.date}')


#   Claim Stub
    p.setFont("Helvetica", 9)
    p.drawString(90, 233, f'{content.name2}')
    p.drawString(410, 233, f'{content.date}')
    p.drawString(530, 233, f'{content.control_number}')
    p.drawString(439, 135, f'{content.appointment}')

    p.setFont("Helvetica", 5)
    p.drawString(70, 760, f'{content.address}')
    
    # List of Payments
    p.setFont("Helvetica", 6)
    course_get = content.course
    num = len(course_get.split())
    if num > 2:
        result = ' '.join(course_get.split()[:2])
        p.drawString(290, 779, f"""{result}""")
        p.drawString(315, 467, f"""{result}""")
        p.drawString(300, 237, f"""{result}""")
        result1 = ' '.join(course_get.split()[2:])
        p.drawString(290, 775, f"""{result1}""")
        p.drawString(315, 462, f"""{result1}""")
        p.drawString(300, 232, f"""{result1}""")
    else:
        p.drawString(290, 775, f'{content.course}')
        p.drawString(315, 462, f'{content.course}')
        p.drawString(300, 232, f'{content.course}')

    p.setFont("Helvetica", 11)
    fname = content.name
    stats = user_table.objects.get(full_name=fname)
    u_type = stats.user_type

    if u_type == "STUDENT":
        p.drawString(33, 750, '✔')

    elif u_type == "OLD STUDENT":
        p.drawString(187, 750, '✔')
    else:
        p.drawString(308, 750, '✔')
        p.drawString(450, 748, f'{stats.year_graduated}')

    # purpose
    form_purpose = content.request
    word_list = form_purpose.split()  # list of words

    cert = word_list[0]
    cert4 = ' '.join(form_purpose.split()[1:])
    others = ' '.join(form_purpose.split()[1:])

    if form_purpose == "Honorable Dismissal":
        p.drawString(248, 695, '✔')
        p.drawString(255, 180, '✔')
    elif form_purpose == "Verification":
        p.drawString(275, 408, '✔')
    elif form_purpose == "Subject Description":
        p.drawString(282, 723, '✔')
        p.drawString(275, 435, '✔')
        p.drawString(255, 208, '✔')
    elif form_purpose == "CAV":
        p.drawString(30, 680, '✔')
        p.drawString(30, 395, '✔')
        p.drawString(40, 167,  '✔')
    elif form_purpose == "Transcript of Records":
        p.drawString(30, 723, '✔ ')
        p.drawString(30, 435, '✔  ')
        p.drawString(40, 207, '✔ ')
    elif form_purpose == "Authentication/Verification":
        p.drawString(248, 709, '✔')
        p.drawString(275, 420, '✔')
        p.drawString(255, 195, '✔')
    elif form_purpose == "Diploma":
        p.drawString(30, 695, '✔')
        p.drawString(30, 408, '✔')
        p.drawString(40, 180, '✔')
    elif cert == "Certification:":
        p.drawString(30, 709, '✔')
        p.drawString(30, 420, '✔')
        p.drawString(40, 195, '✔')
        p.setFont("Helvetica", 9)
        p.drawString(105, 705, f"""{cert4}""")
        p.drawString(125, 195, f"""{cert4}""")
    else:
        p.setFont("Helvetica", 11)

        p.drawString(248, 680, '✔')
        p.drawString(255, 167, '✔')
        p.setFont("Helvetica", 9)
        p.drawString(375, 680, f"""{others}""")
        p.drawString(385, 170, f"""{others}""")

    f137 = content.form_137
    clearance = content.clearance
    o_r = content.official_receipt

    if o_r == "✔":

        p.drawString(130, 650, '✔')
    else:
        p.drawString(300, 130, '')

    if clearance == "✔":
        p.drawString(210, 650, '✔')
    else:
        p.drawString(210, 650, '')

    if f137 == "✔":
        p.drawString(285, 650, '✔')
    else:
        p.drawString(300, 650, '')

    p.setFont("Helvetica", 7)
    p.drawString(115, 663, f'{content.purpose_of_request_reason}')


    for line in lines:
        textob.textLine(line)

    p.drawText(textob)
    p.showPage()
    p.save()

    # Merging 2 Pdfs
    buffer.seek(0)
    infos = PdfFileReader(buffer)
    clearance_pdf = PdfFileReader(open(
        r'../public_html/static/pdf/Required_Forms.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'../public_html/static/pdf/Request_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'../public_html/static/pdf/Request_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=Required Form.pdf'
        return response

# PRINT GRADUATION FORM
@login_required(login_url='/')
def graduation_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = graduation_form_table.objects.get(id=id)
    fac = user_table.objects.all()
    textob = p.beginText()

    lines = []

    coursess = content.course
    c_len = len(coursess.split())

    if c_len > 4:
        p.setFont("Helvetica", 6)
        result = ' '.join(coursess.split()[:3])
        p.drawString(480, 765, f"""{result}""")
        result1 = ' '.join(coursess.split()[3:])
        p.drawString(480, 758, f"""{result1}""")
    else:
        p.setFont("Helvetica", 6)
        p.drawString(480, 758, f'{content.course}')

    p.setFont("Helvetica", 11)
    p.drawString(80, 757, f'{content.name}')
    p.drawString(175, 720, f'{content.study_load}')

    semester = content.enrolled_term
    if semester == "1st":
        p.drawString(360, 715, '✔')
    elif semester == "2nd":
        p.drawString(430, 715, '✔')
    else:
        p.drawString(525, 715, '✔')

    # revised
    p.setFont("Helvetica", 9)
    p.setFillColorRGB(0, 0, 0)
    sub1 = content.subject1

    if len(sub1) == 0:
        p.drawstring(33, 640, "")
    else:
        p.drawString(35, 630, f'{content.subject1}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 635, f'{content.starttime1_1} -')
        p.drawString(125, 625, f'{content.endtime1_1}')
        
        room1 = content.room1
        
        if room1 is None:
            p.drawString(166, 630, '')
        else:
            num1 = len(room1.split())
            if num1 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room1.split()[:3])
                p.drawString(166, 635, f"""{result}""")
                result1 = ' '.join(room1.split()[3:])
                p.drawString(166, 630, f"""{result1}""")
            else:  
                p.drawString(166, 630, f'{content.room1}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 630, f'{content.day1_1}')

        sig1 = content.signature1
        stat_sig1 = sig1.split(' ')[-1]
        faculty1 = content.faculty1
        fac1 = user_table.objects.get(full_name=faculty1)
        fac1_sig_upload = fac1.uploaded_signature
        str_upload1 = str(fac1_sig_upload)
        fac1_sig_esign = fac1.e_signature
        str_esign1 = str(fac1_sig_esign)
        f1 = fac1.first_name + " " + fac1.last_name

        if stat_sig1 == "ESIGN":
            im = "../public_html/Media/" + str_esign1
            p.drawImage(im, 252, 630, height=15, width=80, mask='auto')

        elif stat_sig1 == "UPLOAD":
            im = "../public_html/Media/" + str_upload1
            p.drawImage(im, 252, 630, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 625, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(252, 625, f"""{f1}""")
        
        
    p.setFont("Helvetica", 9)
    sub2 = content.subject2
    p.setFillColorRGB(0, 0, 0)

    if len(sub2) == 0:
        p.drawString(33, 625, "")

    else:
        p.drawString(33, 610, f'{content.subject2}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 615, f'{content.starttime1_2} -')
        p.drawString(125, 605, f'{content.endtime1_2}')
        
        room2 = content.room2
        if room2 is None:
            p.drawString(166, 610, '')
        else:
            num2 = len(room2.split())
            if num2 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room2.split()[:3])
                p.drawString(166, 610, f"""{result}""")
                result1 = ' '.join(room2.split()[3:])
                p.drawString(166, 605, f"""{result1}""")
            else:    
                p.drawString(166, 610, f'{content.room2}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 610, f'{content.day1_2}')
        sig2 = content.signature2
        stat_sig2 = sig2.split(' ')[-1]
        faculty2 = content.faculty2
        fac2 = user_table.objects.get(full_name=faculty2)
        fac2_sig_upload = fac2.uploaded_signature
        str_upload2 = str(fac2_sig_upload)
        fac2_sig_esign = fac2.e_signature
        str_esign2 = str(fac2_sig_esign)
        f2 = fac2.first_name + " " + fac2.last_name

        if stat_sig2 == "ESIGN":
            im = "../public_html/Media/" + str_esign2
            p.drawImage(im, 254, 602, height=15, width=80, mask='auto')
        elif stat_sig2 == "UPLOAD":
            im = "../public_html/Media/" + str_upload2
            p.drawImage(im, 254, 602, height=13, width=80, mask='auto')

        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 605, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 602, f"""{f2}""")   
            

    p.setFont("Helvetica", 9)
    sub3 = content.subject3
    p.setFillColorRGB(0, 0, 0)

    if len(sub3) == 0:
        p.drawString(33, 611,  "")
    else:
        p.drawString(35, 585, f'{content.subject3}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 590, f'{content.starttime1_3} -')
        p.drawString(125, 580, f'{content.endtime1_3}')
        
        room3 = content.room3
        if room3 is None:
            p.drawString(166, 585, '')
        else:
            num3 = len(room3.split())
            if num3 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room3.split()[:3])
                p.drawString(166, 590, f"""{result}""")
                result1 = ' '.join(room3.split()[3:])
                p.drawString(166, 585, f"""{result1}""")
            else:
                p.drawString(166, 585, f'{content.room3}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 585, f'{content.day1_3}')
        sig3 = content.signature3
        stat_sig3 = sig3.split(' ')[-1]
        faculty3 = content.faculty3
        fac3 = user_table.objects.get(full_name=faculty3)
        fac3_sig_upload = fac3.uploaded_signature
        str_upload3 = str(fac3_sig_upload)
        fac3_sig_esign = fac3.e_signature
        str_esign3 = str(fac3_sig_esign)
        f3 = fac3.first_name + " " + fac3.last_name

        if stat_sig3 == "ESIGN":
            im = "../public_html/Media/" + str_esign3
            p.drawImage(im, 254, 585, height=15, width=80, mask='auto')

        elif stat_sig3 == "UPLOAD":
            im = "../public_html/Media/" + str_upload3
            p.drawImage(im, 254, 585, height=15, width=80, mask='auto')
        else:

            p.setFont("Helvetica", 5.5)
            p.drawString(410, 580, "Approved *Manual Signature Required")
            
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 580, f"""{f3}""")

    p.setFont("Helvetica", 9)
    p.setFillColorRGB(0, 0, 0)
    sub4 = content.subject4

    if len(sub4) == 0:
        p.drawString(33, 597, '')

    else:
        p.drawString(33, 565, f'{content.subject4}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 570, f'{content.starttime1_4} -')
        p.drawString(125, 560, f'{content.endtime1_4}')
        
        
        room4 = content.room4
        if room4 is None:
           p.drawString(166, 565, '') 
        else:
            num4 = len(room4.split())
            if num4 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room4.split()[:3])
                p.drawString(166, 570, f"""{result}""")
                result1 = ' '.join(room4.split()[3:])
                p.drawString(166, 565, f"""{result1}""")
            else:   
                p.drawString(166, 565, f'{content.room4}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 565, f'{content.day1_4}')

        sig4 = content.signature4
        stat_sig4 = sig4.split(' ')[-1]
        faculty4 = content.faculty4
        fac4 = user_table.objects.get(full_name=faculty4)
        fac4_sig_upload = fac4.uploaded_signature
        str_upload4 = str(fac4_sig_upload)
        fac4_sig_esign = fac4.e_signature
        str_esign4 = str(fac4_sig_esign)
        f4 = fac4.first_name + " " + fac4.last_name
        

        if stat_sig4 == "ESIGN":
            im = "../public_html/Media/" + str_esign4
            p.drawImage(im, 254, 560, height=15, width=80, mask='auto')

        elif stat_sig4 == "UPLOAD":
            im = "../public_html/Media/" + str_upload4
            p.drawImage(im, 254, 560, height=15, width=80, mask='auto')
        else:

            p.setFont("Helvetica", 5.5)
            p.drawString(410, 560, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 560, f"""{f4}""")

    p.setFont("Helvetica", 9)
    p.setFillColorRGB(0, 0, 0)
    sub5 = content.subject5

    if len(sub5) == 0:
        p.drawString(33, 584, '')
    else:
        p.drawString(33, 543, f'{content.subject5}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 548, f'{content.starttime1_5} -')
        p.drawString(125, 538, f'{content.endtime1_5}')
        
        room5 = content.room5
        if room5 is None:
            p.drawString(166, 543,'')
        else:
            num5 = len(room5.split())
            if num5 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room5.split()[:3])
                p.drawString(166, 548, f"""{result}""")
                result1 = ' '.join(room5.split()[3:])
                p.drawString(166, 543, f"""{result1}""")
            else: 
                p.drawString(166, 543, f'{content.room5}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 542, f'{content.day1_5}')

        sig5 = content.signature5
        faculty5 = content.faculty5
        stat_sig5 = sig5.split(' ')[-1]
        fac5 = user_table.objects.get(full_name=faculty5)
        fac5_sig_upload = fac5.uploaded_signature
        str_upload5 = str(fac5_sig_upload)
        fac5_sig_esign = fac5.e_signature
        str_esign5 = str(fac5_sig_esign)
        f5 = fac5.first_name + " " + fac5.last_name
        

        if stat_sig5 == "ESIGN":
            im = "../public_html/Media/" + str_esign5
            p.drawImage(im, 254, 538, height=15, width=80, mask='auto')

        elif stat_sig5 == "UPLOAD":
            im = "../public_html/Media/" + str_upload5
            p.drawImage(im, 254, 538, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 535, "Approved *Manual Signature Required")
        
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 535, f"""{f5}""")
            

    p.setFont("Helvetica", 9)
    p.setFillColorRGB(0, 0, 0)
    sub6 = content.subject6

    print(sub6)
    if len(sub6) == 0:
        p.drawString(39, 570, '')
    else:
        p.drawString(33, 520, f'{content.subject6}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 525, f'{content.starttime1_6} -')
        p.drawString(125, 515, f'{content.endtime1_6}')
        
        room6 = content.room6
        if room6 is None:
            p.drawString(166, 520, '')
        else:
            num6 = len(room6.split())
            if num6 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room6.split()[:3])
                p.drawString(166, 525, f"""{result}""")
                result1 = ' '.join(room6.split()[3:])
                p.drawString(166, 520, f"""{result1}""")
            else:    
                p.drawString(166, 520, f'{content.room6}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 520, f'{content.day1_6}')

        sig6 = content.signature6
        stat_sig6 = sig6.split(' ')[-1]
        faculty6 = content.faculty6
        fac6 = user_table.objects.get(full_name=faculty6)
        fac6_sig_upload = fac6.uploaded_signature
        str_upload6 = str(fac6_sig_upload)
        fac6_sig_esign = fac6.e_signature
        str_esign6 = str(fac6_sig_esign)
        f6 = fac6.first_name + " " + fac6.last_name
        

        if stat_sig6 == "ESIGN":
            im = "../public_html/Media/" + str_esign6
            p.drawImage(im, 254, 512, height=15, width=80, mask='auto')

        elif stat_sig6 == "UPLOAD":
            im = "../public_html/Media/" + str_upload6
            p.drawImage(im, 254, 512, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 512, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 512, f"""{f6}""")

    p.setFont("Helvetica", 9)
    p.setFillColorRGB(0, 0, 0)
    sub7 = content.subject7

    if len(sub7) == 0:
        p.drawString(33, 555,  '')

    else:
        p.drawString(33, 495, f'{content.subject7}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 500, f'{content.starttime1_7} -')
        p.drawString(125, 490, f'{content.endtime1_7}')
        
        room7 = content.room7
        if room7 is None:
            p.drawString(166, 495, '')
        else:
            num7 = len(room7.split())
            if num7 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room7.split()[:3])
                p.drawString(166, 500, f"""{result}""")
                result1 = ' '.join(room7.split()[3:])
                p.drawString(166, 495, f"""{result1}""")
            else:    
                p.drawString(166, 495, f'{content.room7}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 495, f'{content.day1_7}')

        sig7 = content.signature7
        stat_sig7 = sig7.split(' ')[-1]
        faculty7 = content.faculty7
        fac7 = user_table.objects.get(full_name=faculty7)
        fac7_sig_upload = fac7.uploaded_signature
        str_upload7 = str(fac7_sig_upload)
        fac7_sig_esign = fac7.e_signature
        str_esign7 = str(fac7_sig_esign)
        f7 = fac7.first_name + " " + fac7.last_name
        

        if stat_sig7 == "ESIGN":
            im = "../public_html/Media/" + str_esign7
            p.drawImage(im, 254, 490, height=15, width=80, mask='auto')

        elif stat_sig7 == "UPLOAD":
            im = "../public_html/Media/" + str_upload7
            p.drawImage(im, 254, 490, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 490, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 490, f"""{f7}""")

    p.setFont("Helvetica", 9)
    sub8 = content.subject8
    p.setFillColorRGB(0, 0, 0)

    if len(sub8) == 0:

        p.drawString(33, 542, '')
    else:
        p.drawString(33, 475, f'{content.subject8}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 480, f'{content.starttime1_8} - ')
        p.drawString(125, 470, f'{content.endtime1_8}')
        
        room8 = content.room8
        if room8 is None:
            p.drawString(166, 475, f'{content.room8}')
        else:
            num8 = len(room8.split())
            if num8 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room8.split()[:3])
                p.drawString(166, 480, f"""{result}""")
                result1 = ' '.join(room8.split()[3:])
                p.drawString(166, 475, f"""{result1}""")
            else:    
                p.drawString(166, 475, f'{content.room8}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 475, f'{content.day1_8}')
        sig8 = content.signature8
        faculty8 = content.faculty8
        stat_sig8 = sig8.split(' ')[-1]
        fac8 = user_table.objects.get(full_name=faculty8)
        fac8_sig_upload = fac8.uploaded_signature
        str_upload8 = str(fac8_sig_upload)
        fac8_sig_esign = fac8.e_signature
        str_esign8 = str(fac8_sig_esign)
        f8 = fac8.first_name + " " + fac8.last_name
        

        if stat_sig8 == "ESIGN":
            im = "../public_html/Media/" + str_esign8
            p.drawImage(im, 254, 470, height=15, width=80, mask='auto')

        elif stat_sig8 == "UPLOAD":
            im = "../public_html/Media/" + str_upload8
            p.drawImage(im, 254, 470, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 470, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 470, f"""{f8}""")    

    p.setFont("Helvetica", 9)
    sub9 = content.subject9
    p.setFillColorRGB(0, 0, 0)

    if len(sub9) == 0:
        p.drawString(33, 529,  '')
    else:
        p.drawString(33, 452, f'{content.subject9}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 457, f'{content.starttime1_9} - ')
        p.drawString(125, 447, f'{content.endtime1_9}')
        
        room9 = content.room9
        if room9 is None:
          p.drawString(166, 452, ' ')  
        else:
            num9 = len(room9.split())
            if num9 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room9.split()[:3])
                p.drawString(166, 457, f"""{result}""")
                result1 = ' '.join(room9.split()[3:])
                p.drawString(166, 452, f"""{result1}""")
            else:   
                p.drawString(166, 452, f'{content.room9}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 447, f'{content.day1_9}')

        sig9 = content.signature9
        stat_sig9 = sig9.split(' ')[-1]
        faculty9 = content.faculty9
        fac9 = user_table.objects.get(full_name=faculty9)
        fac9_sig_upload = fac9.uploaded_signature
        str_upload9 = str(fac9_sig_upload)
        fac9_sig_esign = fac9.e_signature
        str_esign9 = str(fac9_sig_esign)
        f9 = fac9.first_name + " " + fac9.last_name
        

        if stat_sig9 == "ESIGN":
            im = "../public_html/Media/" + str_esign9
            p.drawImage(im, 254, 447, height=15, width=80, mask='auto')

        elif stat_sig1 == "UPLOAD":
            im = "../public_html/Media/" + str_upload9
            p.drawImage(im, 254, 447, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 447, "Approved *Manual Signature Required")
            
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 447, f"""{f9}""")

    p.setFont("Helvetica", 9)
    sub10 = content.subject10
    p.setFillColorRGB(0, 0, 0)

    if len(sub10) == 0:
        p.drawString(33, 515,  '')

    else:
        p.drawString(33, 430, f'{content.subject10}')
        p.setFont("Helvetica", 7)
        p.drawString(125, 435, f'{content.starttime1_10} -')
        p.drawString(125, 425, f'{content.endtime1_10}')
        
        room10 = content.room10
        if room10 is None:
            p.drawString(166, 430,' ')
        else:
            num10 = len(room10.split())
            if num10 > 3:
                p.setFont("Helvetica", 5)
                result = ' '.join(room10.split()[:3])
                p.drawString(166, 435, f"""{result}""")
                result1 = ' '.join(room10.split()[3:])
                p.drawString(166, 430, f"""{result1}""")
            else:   
                p.drawString(166, 430, f'{content.room10}')
        p.setFont("Helvetica", 7)
        p.drawString(215, 430, f'{content.day1_10}')
        sig10 = content.signature10
        stat_sig10 = sig10.split(' ')[-1]
        faculty10 = content.faculty10
        fac10 = user_table.objects.get(full_name=faculty10)
        fac10_sig_upload = fac10.uploaded_signature
        str_upload10 = str(fac10_sig_upload)
        fac10_sig_esign = fac10.e_signature
        str_esign10 = str(fac10_sig_esign)
        f10 = fac10.first_name + " " + fac10.last_name
        

        if stat_sig10 == "ESIGN":
            im = "../public_html/Media/" + str_esign10
            p.drawImage(im, 254, 425, height=15, width=80, mask='auto')

        elif stat_sig10 == "UPLOAD":
            im = "../public_html/Media/" + str_upload10
            p.drawImage(im, 254, 425, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 425, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 425, f"""{f10}""")

    # # #additional subj

    p.setFont("Helvetica", 8)
    p.setFillColorRGB(0, 0, 0)
    addsub1 = content.addsubject1

    if len(addsub1) == 0:
        p.drawString(33, 305, '')

    else:
        p.drawString(33, 255, f'{content.addsubject1}')
        p.setFont("Helvetica", 5)
        p.drawString(125, 260, f'{content.add_starttime1_1} -')
        p.drawString(125, 252, f'{content.add_endtime1_1}')
        
        addroom1 = content.addroom1
        if addroom1 is None:
            p.drawString(166, 255, '')
        else:
            addnum1 = len(addroom1.split())
            if addnum1 > 3:
                p.setFont("Helvetica", 4.5)
                result = ' '.join(addroom1.split()[:3])
                p.drawString(166, 260, f"""{result}""")
                result1 = ' '.join(addroom1.split()[3:])
                p.drawString(166, 255, f"""{result1}""")
            else: 
                p.drawString(166, 255, f'{content.addroom1}')
        p.setFont("Helvetica", 5)
        p.drawString(215, 255, f'{content.addday1_1}')

        addsig1 = content.addsignature1
        stat_addsig1 = addsig1.split(' ')[-1]
        addfaculty1 = content.addfaculty1
        addfac1 = user_table.objects.get(full_name=addfaculty1)
        addfac1_sig_upload = addfac1.uploaded_signature
        add_str_upload1 = str(addfac1_sig_upload)
        addfac1_sig_esign = addfac1.e_signature
        add_str_esign1 = str(addfac1_sig_esign)
        addf1 = addfac1.first_name + " " + addfac1.last_name
        

        if stat_addsig1 == "ESIGN":
            im = "../public_html/Media/" + add_str_esign1
            p.drawImage(im, 254, 252, height=15, width=80, mask='auto')

        elif stat_addsig1 == "UPLOAD":
            im = "../public_html/Media/" + add_str_upload1
            p.drawImage(im, 254, 252, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 252, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 252, f"""{addf1}""")    

    p.setFont("Helvetica", 7)
    p.setFillColorRGB(0, 0, 0)
    addsub2 = content.addsubject2

    if len(addsub2) == 0:
        p.drawString(33, 290, '')
    else:
        p.drawString(33, 242, f'{content.addsubject2}')
        p.setFont("Helvetica", 5)
        p.drawString(125, 245, f'{content.add_starttime1_2} -')
        p.drawString(125, 240, f'{content.add_endtime1_2}')
        
        addroom2 = content.addroom2
        if addroom2 is None:
            p.drawString(166, 242, f'{content.addroom2}')
        else:
            addnum2 = len(addroom2.split())
            if addnum2 > 3:
                p.setFont("Helvetica", 4.5)
                result = ' '.join(addroom2.split()[:3])
                p.drawString(166, 247, f"""{result}""")
                result1 = ' '.join(addroom2.split()[3:])
                p.drawString(166, 242, f"""{result1}""")
            else: 
                p.drawString(166, 242, f'{content.addroom2}')
        p.setFont("Helvetica", 5)
        p.drawString(215, 242, f'{content.addday1_2}')

        addsig2 = content.addsignature2
        stat_addsig2 = addsig2.split(' ')[-1]
        addfaculty2 = content.addfaculty2
        addfac2 = user_table.objects.get(full_name=addfaculty2)
        addfac2_sig_upload = addfac2.uploaded_signature
        add_str_upload2 = str(addfac2_sig_upload)
        addfac2_sig_esign = addfac2.e_signature
        add_str_esign2 = str(addfac2_sig_esign)
        addf2 = addfac2.first_name + " " + addfac2.last_name
        

        if stat_addsig2 == "ESIGN":
            im = "../public_html/Media/" + add_str_esign2
            p.drawImage(im, 254, 238, height=15, width=80, mask='auto')

        elif stat_addsig2 == "UPLOAD":
            im = "../public_html/Media/" + add_str_upload2
            p.drawImage(im, 254, 238, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 238, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 240, f"""{addf2}""")

    p.setFont("Helvetica", 7)
    p.setFillColorRGB(0, 0, 0)
    addsub3 = content.addsubject3
    if len(addsub3) == 0:
        p.drawString(33, 276, '')

    else:
        p.drawString(33, 228, f'{content.addsubject3}')
        p.setFont("Helvetica", 5)
        p.drawString(125, 230, f'{content.add_starttime1_3} -')
        p.drawString(125, 224, f'{content.add_endtime1_3}')
    
        
        addroom3 = content.addroom3
        if addroom3 is None:
            p.drawString(166, 228, '')
        else:
            addnum3 = len(addroom3.split())
            if addnum3 > 3:
                p.setFont("Helvetica", 4.5)
                result = ' '.join(addroom3.split()[:3])
                p.drawString(166, 233, f"""{result}""")
                result1 = ' '.join(addroom3.split()[3:])
                p.drawString(166, 228, f"""{result1}""")
            else: 
                p.drawString(166, 228, f'{content.addroom3}')
        p.setFont("Helvetica", 5)
        p.drawString(215, 228, f'{content.addday1_3}')

        addsig3 = content.addsignature3
        stat_addsig3 = addsig3.split(' ')[-1]
        addfaculty3 = content.addfaculty3
        addfac3 = user_table.objects.get(full_name=addfaculty3)
        addfac3_sig_upload = addfac3.uploaded_signature
        add_str_upload3 = str(addfac3_sig_upload)
        addfac3_sig_esign = addfac3.e_signature
        add_str_esign3 = str(addfac3_sig_esign)
        addf3 = addfac3.first_name + " " + addfac3.last_name
        

        if stat_addsig3 == "ESIGN":
            im = "../public_html/Media/" + add_str_esign3
            p.drawImage(im, 254, 224, height=15, width=80, mask='auto')

        elif stat_addsig3 == "UPLOAD":
            im = "../public_html/Media/" + add_str_upload3
            p.drawImage(im, 254, 224, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 224, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 224, f"""{addf3}""")

    p.setFont("Helvetica", 7)
    p.setFillColorRGB(0, 0, 0)
    addsub4 = content.addsubject4
    if len(addsub4) == 0:
        print("empty")
        p.drawString(33, 262,  '')

    else:
        p.drawString(33, 213, f'{content.addsubject4}')
        p.setFont("Helvetica", 5)
        p.drawString(125, 216, f'{content.add_starttime1_4} -')
        p.drawString(125, 210, f'{content.add_endtime1_4}')
        
        addroom4 = content.addroom4
        if addroom4 is None:
            p.drawString(166, 213, f'{content.addroom4}')
        else:
            addnum4 = len(addroom4.split())
            if addnum4 > 3:
                p.setFont("Helvetica", 4.5)
                result = ' '.join(addroom4.split()[:3])
                p.drawString(166, 218, f"""{result}""")
                result1 = ' '.join(addroom4.split()[3:])
                p.drawString(166, 213, f"""{result1}""")
            else: 
                p.drawString(166, 213, f'{content.addroom4}')
        p.setFont("Helvetica", 5)
        p.drawString(215, 213, f'{content.addday1_4}')

        addsig4 = content.addsignature4
        stat_addsig4 = addsig4.split(' ')[-1]
        addfaculty4 = content.addfaculty4
        addfac4 = user_table.objects.get(full_name=addfaculty4)
        addfac4_sig_upload = addfac4.uploaded_signature
        add_str_upload4 = str(addfac4_sig_upload)
        addfac4_sig_esign = addfac4.e_signature
        add_str_esign4 = str(addfac4_sig_esign)
        addf4 = addfac4.first_name + " " + addfac4.last_name
        

        if stat_addsig4 == "ESIGN":
            im = "../public_html/Media/" + add_str_esign4
            p.drawImage(im, 254, 210, height=15, width=80, mask='auto')

        elif stat_addsig4 == "UPLOAD":
            im = "../public_html/Media/" + add_str_upload4
            p.drawImage(im, 254, 210, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 210, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 210, f"""{addf4}""")

    p.setFont("Helvetica", 7)
    p.setFillColorRGB(0, 0, 0)
    addsub5 = content.addsubject5
    if len(addsub5) == 0:
        p.drawString(33, 249,  '')
    else:
        p.drawString(33, 198, f'{content.addsubject5}')
        p.setFont("Helvetica", 5)
        p.drawString(125, 200, f'{content.add_starttime1_5} -')
        p.drawString(125, 195, f'{content.add_endtime1_5}')
        
        addroom5 = content.addroom5
        if addroom5 is None:
            p.drawString(166, 198, ' ')
        else:
            
            addnum5 = len(addroom5.split())
            if addnum5 > 3:
                p.setFont("Helvetica", 4.5)
                result = ' '.join(addroom5.split()[:3])
                p.drawString(166, 203, f"""{result}""")
                result1 = ' '.join(addroom5.split()[3:])
                p.drawString(166, 198, f"""{result1}""")
            else: 
                p.drawString(166, 198, f'{content.addroom5}')
        p.setFont("Helvetica", 5)
        p.drawString(215, 198, f'{content.addday1_5}')

        addsig5 = content.addsignature5
        stat_addsig5 = addsig5.split(' ')[-1]
        addfaculty5 = content.addfaculty5
        addfac5 = user_table.objects.get(full_name=addfaculty5)
        addfac5_sig_upload = addfac5.uploaded_signature
        add_str_upload5 = str(addfac5_sig_upload)
        addfac5_sig_esign = addfac5.e_signature
        add_str_esign5 = str(addfac5_sig_esign)
        addf5 = addfac5.first_name + " " + addfac5.last_name
        

        if stat_addsig5 == "ESIGN":
            im = "../public_html/Media/" + add_str_esign5
            p.drawImage(im, 254, 196, height=15, width=80, mask='auto')

        elif stat_addsig5 == "UPLOAD":
            im = "../public_html/Media/" + add_str_upload5
            p.drawImage(im, 254, 196, height=15, width=80, mask='auto')
        else:
            p.setFont("Helvetica", 5.5)
            p.drawString(410, 196, "Approved *Manual Signature Required")
            
        p.setFont("Helvetica", 7)
        p.setFillColorRGB(0, 0, 0)
        p.drawString(254, 196, f"""{addf5}""")

    p.setFont("Helvetica", 11)
    dline = content.unenrolled_application_deadline
    if dline is None:
        p.drawString(235, 168, '')
    else:
        p.drawString(235, 168, f'{content.unenrolled_application_deadline}')
    p.drawString(195, 90, f'{content.trainP_startdate}')
    p.drawString(390, 90, f'{content.trainP_enddate}')

    p.setFont("Helvetica", 7)
    sitsig = content.sitsignature
    sit = sitsig.split(' ')[-1]
    ins = content.instructor_name
    fac = user_table.objects.get(full_name=ins)
    sit_upload = fac.uploaded_signature
    sit_str_upload1 = str(sit_upload)
    sit_esign = fac.e_signature
    sit_str_esign1 = str(sit_esign)
    sitins = fac.first_name + " " + fac.last_name
    

    if sit == "ESIGN":
        im = "../public_html/Media/" + sit_str_esign1
        p.drawImage(im, 408, 74, height=15, width=80, mask='auto')

    elif sit == "UPLOAD":
        im = "../public_html/Media/" + sit_str_upload1
        p.drawImage(im, 408, 74, height=15, width=80, mask='auto')
    else:
        p.setFont("Helvetica", 5.5)
        p.drawString(258, 66, "Approved *Manual Signature Required")
        
    p.setFont("Helvetica", 7)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(255, 75, f"""{sitins}""")

    for line in lines:
        textob.textLine(line)

    p.drawText(textob)
    p.showPage()
    p.save()

    # Merging 2 Pdfs
    buffer.seek(0)
    infos = PdfFileReader(buffer)
    clearance_pdf = PdfFileReader(
        open(r'../public_html/static/pdf/Graduation_form.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'../public_html/static/pdf/Graduation_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'../public_html/static/pdf/Graduation_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=Graduation Form.pdf'
        return response

# PRINT CLEARANCE FORM
@login_required(login_url='/')
def clearance_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = clearance_form_table.objects.get(id=id)
    textob = p.beginText()

    print(content)
    print("hello world")

    lines = []

    p.setFont("Helvetica", 9)
    p.drawString(80, 733, f'{content.name}')
    p.drawString(400, 733, f'{content.date_filed}')
    p.setFont("Helvetica", 7)
    p.drawString(130, 690, f'{content.present_address}')
    p.setFont("Helvetica", 10)
    p.drawString(150, 663, f'{content.date_admitted_in_tup}')
    p.setFont("Helvetica", 7)
    p.drawString(120, 638, f'{content.course}')

    hs_grad = content.highschool_graduated
    num = len(hs_grad.split())

    if num > 3:
        p.setFont("Helvetica", 7)
        result = ' '.join(hs_grad.split()[:3])
        p.drawString(180, 613, f"""{result}""")
        result1 = ' '.join(hs_grad.split()[3:])
        p.drawString(43, 587, f"""{result1}""")
    else:
        p.setFont("Helvetica", 7)
        p.drawString(180, 613, f'{content.highschool_graduated}')

    p.setFont("Helvetica", 10)
    amount_paid = content.amount_paid
    last_term = content.last_term_in_tupc
    num_term = content.number_of_terms_in_tupc
    prev_date = content.date_of_previously_requested_form

    if amount_paid != "0.00":

        p.drawString(400, 663, f'{content.amount_paid}')
        p.drawString(429, 639, f'{content.or_num}')
        
    if prev_date is not None:
        p.drawString(370, 540, f'{content.date_of_previously_requested_form}')
        p.drawString(418, 510, f'{content.last_term_in_tupc}')
    
    p.drawString(428, 485, f'{content.purpose_of_request_reason}')
    p.drawString(210, 510, f'{content.number_of_terms_in_tupc}')
    
    tupc_grad = content.tupc_graduate
    if tupc_grad == "YES":
        p.drawString(163, 561, '✔')
        p.drawString(178, 535, f'{content.year_graduated_in_tupc}')
    else:
        p.drawString(220, 561, '✔')

    prev_form = content.have_previously_requested_form
    if prev_form == "YES":
        p.drawString(384, 590, '✔')
        p.drawString(370, 540, f'{content.date_of_previously_requested_form}')

    else:
        p.drawString(415, 592, '✔')

    # purpose
    form_purpose = content.purpose_of_request

    if form_purpose == "Honorable Dismissal":
        p.drawString(37, 415, '✔')
    elif form_purpose == "Transcript of Records":
        p.drawString(37, 385, '✔')
    elif form_purpose == "Diploma":
        p.drawString(208, 415, '✔')
    elif form_purpose == "Certification":
        p.drawString(208, 383, '✔')
    else:
        p.drawString(287, 415, '✔')
        p.drawString(400, 415, f'{content.purpose_of_request}')


# signature
    p.setFont("Helvetica", 7)
    sig_acc = content.accountant_signature
    acc_stat = sig_acc.split(' ')[-1]
    accs = sig_acc.rsplit(' ', 1)[0]
    acc_name = accs.split('_', 1)[0]

    accountant = user_table.objects.get(full_name=acc_name)
    upload_acc_sign = accountant.uploaded_signature
    str_upload_acc = str(upload_acc_sign)
    esign_acc_sign = accountant.e_signature
    str_esign_acc = str(esign_acc_sign)
    p.setFont("Helvetica", 6)
    p.setFillColorRGB(0, 0, 0)
    accname = accountant.first_name + " " + accountant.last_name

    if acc_stat == "ESIGN":
        if  bool(upload_acc_sign) == False:
            im = "../public_html/Media/"+str_esign_acc
            p.drawImage(im, 130, 287, height=25, width=80, mask='auto')
            p.drawString(125, 298, f"""{acc_name}""")
            p.drawString(53, 292, "Approved *Manual Signature Required")
            p.drawString(160, 292, "Signed:" +"f'{accountant.accountant_timestamp}")
        else:
            im = "../public_html/Media/"+str_upload_acc
            p.drawImage(im, 130, 287, height=25, width=80, mask='auto')
            p.drawString(125, 298, f"""{upload_acc_sign}""")

    elif acc_stat == "REGISTRAR":

        p.setFont("Helvetica", 6)
        p.drawString(125, 298, "APPROVED")

    else:
        p.drawString(125, 298, f"""{accname}""")
        p.setFont("Helvetica", 4.5)
        p.setFillColorRGB(1, 0, 0)
        p.drawString(53, 292, "Approved *Manual Signature Required")
        

    # # Liberal arts

    # p.setFont("Helvetica", 7)
    # sig_dla = content.liberal_arts_signature
    # dla_stat = sig_dla.split(' ')[-1]
    # dlas = sig_dla.rsplit(' ', 1)[0]
    # dla_name = dlas.split('_', 1)[0]

    # liberal_arts = user_table.objects.get(full_name=dla_name)
    # upload_dla_sign = liberal_arts.uploaded_signature
    # str_upload_dla = str(upload_dla_sign)
    # esign_dla_sign = liberal_arts.e_signature
    # str_esign_dla = str(esign_dla_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # dlaname = liberal_arts.first_name + " " + liberal_arts.last_name

    # if dla_stat == "ESIGN":
    #     im = "../public_html/Media/"+str_esign_dla
    #     p.drawImage(im, 150, 240, height=25, width=80, mask='auto')
    #     p.drawString(147, 243, f"""{dlaname}""")

    # elif dla_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_dla
    #     p.drawImage(im, 150, 240, height=25, width=80, mask='auto')
    #     p.drawString(147, 243, f"""{dlaname}""")
        
    # elif dla_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(147, 243, "APPROVED")

    # else:
    #     p.drawString(147, 243, f"""{dlaname}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(75, 234, "Approved *Manual Signature Required")
        

    # # # # math and sci
    # p.setFont("Helvetica", 7)
    # sig_dms = content.mathsci_dept_signature
    # dms_stat = sig_dms.split(' ')[-1]
    # dmss = sig_dms.rsplit(' ', 1)[0]
    # dms_name = dmss.split('_', 1)[0]

    # mathsci = user_table.objects.get(full_name=dms_name)
    # upload_dms_sign = mathsci.uploaded_signature
    # str_upload_dms = str(upload_dms_sign)
    # esign_dms_sign = mathsci.e_signature
    # str_esign_dms = str(esign_dms_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # dmsname = mathsci.first_name + " " + mathsci.last_name

    # if dms_stat == "ESIGN":
    #     im = "../public_html/Media/"+str_esign_dms
    #     p.drawImage(im, 170, 215, height=25, width=80, mask='auto')
    #     p.drawString(170, 215, f"""{dmsname}""")

    # elif dms_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_dms
    #     p.drawImage(im, 170, 215, height=25, width=80, mask='auto')
    #     p.drawString(170, 215, f"""{dmsname}""")

    # elif dms_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(170, 215, "APPROVED")

    # else:
    #     p.drawString(170, 215, f"""{dmsname}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(75, 209, "Approved *Manual Signature Required")
        

    # # # # dpecs

    # pe_acc = content.pe_dept_signature
    # pe_stat = pe_acc.split(' ')[-1]
    # dpecs = pe_acc.rsplit(' ', 1)[0]
    # pe_name = dpecs.split('_', 1)[0]

    # pe_dept = user_table.objects.get(full_name=pe_name)
    # upload_pe_sign = pe_dept.uploaded_signature
    # str_upload_pe = str(upload_pe_sign)
    # esign_pe_sign = pe_dept.e_signature
    # str_esign_pe = str(esign_pe_sign)
    # p.setFont("Helvetica", 4.5)
    # p.setFillColorRGB(1, 0, 0)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # pename = pe_dept.first_name + " " + pe_dept.last_name

    # if pe_stat == "ESIGN":
    #     im = "../public_html/Media/"+str_esign_pe
    #     p.drawImage(im, 120, 185, height=25, width=80, mask='auto')
    #     p.drawString(120, 190, f"""{pename}""")

    # elif pe_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_pe
    #     p.drawImage(im, 120, 185, height=25, width=80, mask='auto')
    #     p.drawString(120, 190, f"""{pename}""")

    # elif pe_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(120, 190, "APPROVED")

    # else:
    #     p.drawString(120, 190, f"""{pename}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(75, 183, "Approved *Manual Signature Required")
        

    # # # depts
    # itdept_acc = content.it_dept_signature
    # educ_dept = content.ieduc_dept_signature
    # eng = content.eng_dept_signature
    # if itdept_acc != "_APPROVED":

    #     p.setFont("Helvetica", 7)

    #     itdept_stat = itdept_acc.split(' ')[-1]
    #     itdepartments = itdept_acc.rsplit(' ', 1)[0]
    #     itdept_name = itdepartments.split('_', 1)[0]

    #     itdept_dept = user_table.objects.get(full_name=itdept_name)
    #     upload_itdept_sign = itdept_dept.uploaded_signature
    #     str_upload_itdept = str(upload_itdept_sign)
    #     esign_itdept_sign = itdept_dept.e_signature
    #     str_esign_itdept = str(esign_itdept_sign)
    #     p.setFont("Helvetica", 6)
    #     p.setFillColorRGB(0, 0, 0)
    #     itdeptname = itdept_dept.first_name + " " + itdept_dept.last_name

    #     if itdept_stat == "ESIGN":
    #         im = "../public_html/Media/"+str_esign_itdept
    #         p.drawImage(im, 120, 110, height=25, width=80, mask='auto')
    #         p.drawString(105, 113, f"""{itdeptname}""")


    #     elif itdept_stat == "UPLOAD":
    #         im = "../public_html/Media/"+str_upload_itdept
    #         p.drawImage(im, 120, 110, height=25, width=80, mask='auto')
    #         p.drawString(105, 113, f"""{itdeptname}""")

    #     elif itdept_stat == "REGISTRAR":
    #         p.setFont("Helvetica", 6)
    #         p.drawString(105, 113, "APPROVED")

    #     else:
    #         p.drawString(105, 113, f"""{itdeptname}""")
    #         p.setFont("Helvetica", 4.5)
    #         p.setFillColorRGB(1, 0, 0)
    #         p.drawString(75, 105, "Approved *Manual Signature Required")
            

    # elif educ_dept != "_APPROVED":

    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(0, 0, 0)
    #     educdept_stat = educ_dept.split(' ')[-1]
    #     educdepartments = educ_dept.rsplit(' ', 1)[0]
    #     educdept_name = educdepartments.split('_', 1)[0]

    #     educdept_dept = user_table.objects.get(full_name=educdept_name)
    #     upload_educdept_sign = educdept_dept.uploaded_signature
    #     str_upload_educdept = str(upload_educdept_sign)
    #     esign_educdept_sign = educdept_dept.e_signature
    #     str_esign_educdept = str(esign_educdept_sign)
    #     p.setFont("Helvetica", 6)
    #     p.setFillColorRGB(0, 0, 0)
    #     educdeptname = educdept_dept.first_name + " " + educdept_dept.last_name

    #     if educdept_stat == "ESIGN":
    #         p.drawString(105, 113, f"""{educdeptname}""")
    #         im = "../public_html/Media/"+str_esign_educdept
    #         p.drawImage(im, 120, 110, height=25, width=80, mask='auto')

    #     elif educdept_stat == "UPLOAD":
    #         im = "../public_html/Media/"+str_upload_educdept
    #         p.drawImage(im, 120, 110, height=25, width=80, mask='auto')
    #         p.drawString(105, 113, f"""{educdeptname}""")

    #     elif educdept_stat == "REGISTRAR":
    #         p.setFont("Helvetica", 6)
    #         p.drawString(105, 113, "APPROVED")

    #     else:
    #         p.drawString(105, 113, f"""{educdeptname}""")
    #         p.setFont("Helvetica", 4.5)
    #         p.setFillColorRGB(1, 0, 0)
    #         p.drawString(75, 105, "Approved *Manual Signature Required")

    # elif eng != "_APPROVED":
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(0, 0, 0)

    #     engdept_stat = eng.split(' ')[-1]
    #     engdepartments = eng.rsplit(' ', 1)[0]
    #     engdept_name = engdepartments.split('_', 1)[0]

    #     engdept_dept = user_table.objects.get(full_name=engdept_name)
    #     upload_engdept_sign = engdept_dept.uploaded_signature
    #     str_upload_engdept = str(upload_engdept_sign)
    #     esign_engdept_sign = engdept_dept.e_signature
    #     str_esign_engdept = str(esign_engdept_sign)
    #     p.setFont("Helvetica", 6)
    #     p.setFillColorRGB(0, 0, 0)
    #     engdeptname = engdept_dept.first_name + " " + engdept_dept.last_name

    #     if engdept_stat == "ESIGN":
    #         p.drawString(105, 113, f"""{engdeptname}""")
    #         im = "../public_html/Media/"+str_esign_engdept
    #         p.drawImage(im, 120, 110, height=25, width=80, mask='auto')

    #     elif engdept_stat == "UPLOAD":
    #         im = "../public_html/Media/"+str_upload_engdept
    #         p.drawImage(im, 120, 190, height=25, width=80, mask='auto')
    #         p.drawString(105, 113, f"""{engdeptname}""")

    #     elif engdept_stat == "REGISTRAR":
    #         p.setFont("Helvetica", 6)
    #         p.drawString(105, 113, "APPROVED")

    #     else:
    #         p.drawString(105, 113, f"""{engdeptname}""")
    #         p.setFont("Helvetica", 4.5)
    #         p.setFillColorRGB(1, 0, 0)
    #         p.drawString(75, 105, "Approved *Manual Signature Required")

    # # # shop
    # p.setFont("Helvetica", 7)
    # sig_shop = content.course_adviser_signature
    # shop_stat = sig_shop.split(' ')[-1]
    # shops = sig_shop.rsplit(' ', 1)[0]
    # shop_name = shops.split('_', 1)[0]

    # shop_ad = user_table.objects.get(full_name=shop_name)
    # upload_shop_sign = shop_ad.uploaded_signature
    # str_upload_shop = str(upload_shop_sign)
    # esign_shop_sign = shop_ad.e_signature
    # str_esign_shop = str(esign_shop_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # shopname = shop_ad.first_name + " " + shop_ad.last_name

    # if shop_stat == "ESIGN":
    #     p.drawString(435, 300, f"""{shopname}""")
    #     im = "../public_html/Media/"+str_esign_shop
    #     p.drawImage(im, 435, 290, height=15, width=80, mask='auto')

    # elif shop_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_shop
    #     p.drawImage(im, 435, 290, height=25, width=80, mask='auto')
    #     p.drawString(435, 300, f"""{shopname}""")
        
    # elif shop_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(435, 300, "APPROVED")

    # else:
    #     p.drawString(435, 300, f"""{shopname}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(320, 290, "Approved *Manual Signature Required")

    # # # library
    # p.setFont("Helvetica", 7)
    # sig_lib = content.library_signature
    # lib_stat = sig_lib.split(' ')[-1]
    # libb = sig_lib.rsplit(' ', 1)[0]
    # lib_name = libb.split('_', 1)[0]

    # lib_ad = user_table.objects.get(full_name=lib_name)
    # upload_lib_sign = lib_ad.uploaded_signature
    # str_upload_lib = str(upload_lib_sign)
    # esign_lib_sign = lib_ad.e_signature
    # str_esign_lib = str(esign_lib_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # libname = lib_ad.first_name + " " + lib_ad.last_name

    # if lib_stat == "ESIGN":
    #     p.drawString(425, 269, f"""{libname}""")
    #     im = "../public_html/Media/"+str_esign_lib
    #     p.drawImage(im, 425, 265, height=15, width=80, mask='auto')

    # elif lib_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_lib
    #     p.drawImage(im, 425, 265, height=15, width=80, mask='auto')
    #     p.drawString(425, 269, f"""{libname}""")
        
    # elif lib_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(425, 265, "APPROVED")

    # else:
    #     p.drawString(425, 269, f"""{libname}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(325, 260, "Approved *Manual Signature Required")

    # # guidance

    # sig_guidance = content.guidance_office_signature
    # guidance_stat = sig_guidance.split(' ')[-1]
    # guidances = sig_guidance.rsplit(' ', 1)[0]
    # guidance_name = guidances.split('_', 1)[0]

    # guidance = user_table.objects.get(full_name=guidance_name)
    # upload_guidance_sign = guidance.uploaded_signature
    # str_upload_guidance = str(upload_guidance_sign)
    # esign_guidance_sign = guidance.e_signature
    # str_esign_guidance = str(esign_guidance_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # guidancename = guidance.first_name + " " + guidance.last_name

    # if guidance_stat == "ESIGN":
    #     p.drawString(435, 244, f"""{guidancename}""")
    #     im = "../public_html/Media/"+str_esign_guidance
    #     p.drawImage(im, 435, 240, height=25, width=80, mask='auto')

    # elif guidance_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_guidance
    #     p.drawImage(im, 435, 240, height=25, width=80, mask='auto')
    #     p.drawString(435, 244, f"""{guidancename}""")
        
    # elif guidance_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(435, 244, "APPROVED")

    # else:
    #     p.drawString(435, 244, f"""{guidancename}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(325, 238, "Approved *Manual Signature Required")

    # # osa
    # p.setFont("Helvetica", 7)
    # sig_osa = content.osa_signature
    # osa_stat = sig_osa.split(' ')[-1]
    # osas = sig_osa.rsplit(' ', 1)[0]
    # osa_name = osas.split('_', 1)[0]

    # osa = user_table.objects.get(full_name=osa_name)
    # upload_osa_sign = osa.uploaded_signature
    # str_upload_osa = str(upload_osa_sign)
    # esign_osa_sign = osa.e_signature
    # str_esign_osa = str(esign_osa_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # osaname = osa.first_name + " " + osa.last_name

    # if osa_stat == "ESIGN":
    #     p.drawString(455, 217, f"""{osaname}""")
    #     im = "../public_html/Media/"+str_esign_osa
    #     p.drawImage(im, 455, 210, height=25, width=80, mask='auto')

    # elif osa_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_osa
    #     p.drawImage(im, 455, 215, height=25, width=80, mask='auto')
    #     p.drawString(455, 217, f"""{osaname}""")
        
    # elif osa_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(455, 217, "APPROVED")

    # else:
    #     p.drawString(455, 217, f"""{osaname}""")
    #     p.setFont("Helvetica", 4.5)
    #     p.setFillColorRGB(1, 0, 0)
    #     p.drawString(320, 210, "Approved *Manual Signature Required")

    # # adaa

    # sig_adaa = content.academic_affairs_signature
    # adaa_stat = sig_adaa.split(' ')[-1]
    # adaas = sig_adaa.rsplit(' ', 1)[0]
    # adaa_name = adaas.split('_', 1)[0]

    # adaa = user_table.objects.get(full_name=adaa_name)
    # upload_adaa_sign = adaa.uploaded_signature
    # str_upload_adaa = str(upload_adaa_sign)
    # esign_adaa_sign = adaa.e_signature
    # str_esign_adaa = str(esign_adaa_sign)
    # p.setFont("Helvetica", 6)
    # p.setFillColorRGB(0, 0, 0)
    # adaaname = adaa.first_name + " " + adaa.last_name

    # if adaa_stat == "ESIGN":
    #     p.drawString(482, 190, f"""{adaaname}""")
    #     im = "../public_html/Media/"+str_esign_adaa
    #     p.drawImage(im, 475, 180, height=25, width=80, mask='auto')

    # elif adaa_stat == "UPLOAD":
    #     im = "../public_html/Media/"+str_upload_adaa
    #     p.drawImage(im, 475, 180, height=25, width=80, mask='auto')
    #     p.drawString(482, 190, f"""{adaaname}""")
        
    # elif adaa_stat == "REGISTRAR":
    #     p.setFont("Helvetica", 6)
    #     p.drawString(482, 190, "APPROVED")

    # else:
    #     p.drawString(482, 190, f"""{adaaname}""")
    #     p.setFillColorRGB(1, 0, 0)
    #     p.setFont("Helvetica", 4.5)
    #     p.drawString(325, 185, "Approved *Manual Signature Required")

    for line in lines:
        textob.textLine(line)

    p.drawText(textob)
    p.showPage()
    p.save()

    # Merging 2 Pdfs
    buffer.seek(0)
    infos = PdfFileReader(buffer)
    clearance_pdf = PdfFileReader(open(
        r'../public_html/static/pdf/Clearance_form.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'../public_html/static/pdf/Clearance_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'../public_html/static/pdf/Clearance_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment;filename=Clearance Form.pdf'
        return response

# FOR SETTING APPOINTMENTS ON FACULTY'S SIDE (CLEARANCE ONLY)
@login_required(login_url='/')
def appointment(request, id, form):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        gform = form
        purposerequest = clearance_form_table.objects.filter(
            id=id).values_list('purpose_of_request', flat=True).distinct()
        purpose = purposerequest[0]
        if request.method == 'POST':
            email_temp = clearance_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            email = user_table.objects.filter(
                student_id=email_temp[0]).values_list('email', flat=True).distinct()
            rec_email = email[0]
            recipient_list = [rec_email, ]
            print("RECMAIL:", rec_email)

            name_temp = clearance_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            name = user_table.objects.filter(
                student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
            last_name = name[0]

            gender_temp = clearance_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            gender = user_table.objects.filter(
                student_id=gender_temp[0]).values_list('gender', flat=True).distinct()
            gender_choice = gender[0]
            gender_final = ""
            if gender_choice == "Female":
                gender_final = "Ms."
            else:
                gender_final = "Mr."

            faculty_gender = request.user.gender
            gender_fac = ""
            if faculty_gender == "Female":
                gender_fac = "Ms."
            else:
                gender_fac = "Mr."

            subject = 'Application for Clearance Form '
            message1 = 'Good day, ' + "<strong>" + \
                gender_final + name[0] + ",</strong><br><br>"
            message2 = 'Your Application for Clearance Form has pending concerns with  ' + \
                "<strong>" + gender_fac + request.user.last_name + ".</strong><br><br>"
            message3 = '  An appointment for discussing the said concerns was scheduled. Please arrive at the set date and time of appointment. <br><br>'
            message4 = "<i>"+' Failure to comply may result to declined application.'"</i>"
            message5 = 'For other concerns, please contact the official email of TUPC Registrar:   ' + \
                'tupc_registrar@tup.edu.ph'
            message6 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
                "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br>'
            message7 = "<i>"+'***This is an automated message, do not reply.'+"</i>"

            message = message1 + message2 + message3

            date_appointment = request.POST.get('date_appointment')
            time_appointment = request.POST.get('time_appointment')
            additionalmessage = request.POST.get('additionalmessage')
            email = request.POST.get('email')

            data = {
                'date_appointment': date_appointment,
                'time_appointment': time_appointment,
                'subject': subject,
                'message': message,
                'message4': message4,
                'message5': message5,
                'message6': message6,
                'message7': message7,
                'additionalmessage': additionalmessage,
            }
            message = '''{}
            <strong>Date:</strong>\n\t\t{}\n<br>
            <strong>Time:</strong>\n\t\t{}\n<br><br>
            <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br>
            \n\t\t{}\n<br><br><br><br>
            \n\t\t{}\n<br><br><br>
            \n\t\t{}\n<br>
            \n\t\t{}\n<br>
            
            '''''.format(data['message'], data['date_appointment'], data['time_appointment'], data['additionalmessage'], data['message4'], data['message5'], data['message6'], data['message7'])
            msg = EmailMessage(subject, message, '', email, recipient_list,)
            msg.content_subtype = "html"
            msg.send(fail_silently=True)
            messages.success(request, "Appointment Schedule Sent.")

            return redirect(faculty_dashboard_clearance_list)

        else:
            return render(request, 'html_files/appointment.html', {'gform': gform, 'purpose': purpose})

# FOR SETTING APPOINTMENTS ON FACULTY'S SIDE (GRADUATION ONLY)
@login_required(login_url='/')
def appointmentgrad(request, id, form):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        gform = form
        if request.method == 'POST':
            email_temp = graduation_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            email = user_table.objects.filter(
                student_id=email_temp[0]).values_list('email', flat=True).distinct()
            rec_email = email[0]
            recipient_list = [rec_email, ]

            name_temp = graduation_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            name = user_table.objects.filter(
                student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
            last_name = name[0]

            purpose = graduation_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            purpose_of = graduation_form_table.objects.filter(
                student_id=purpose[0]).values_list('purpose_of_request', flat=True).distinct()
            purpose_of_req = purpose_of[0]

            gender_temp = graduation_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            gender = user_table.objects.filter(
                student_id=gender_temp[0]).values_list('gender', flat=True).distinct()
            gender_choice = gender[0]
            gender_final = ""
            if gender_choice == "Female":
                gender_final = "Ms."
            else:
                gender_final = "Mr."

            faculty_gender = request.user.gender
            gender_fac = ""
            if faculty_gender == "Female":
                gender_fac = "Ms."
            else:
                gender_fac = "Mr."

            subject = 'Application for Graduation Form '
            message1 = 'Good day, ' + "<strong>" + \
                gender_final + name[0] + ",</strong><br><br>"
            message2 = 'Your Application for Graduation Form has pending concerns with  ' + \
                "<strong>" + gender_fac + request.user.last_name + ".</strong><br><br>"
            message3 = '  An appointment for discussing the said concerns was scheduled. Please arrive at the set date and time of appointment. <br><br>'
            message4 = "<i>"+' Failure to comply may result to declined application.'+"</i>"
            message5 = 'For other concerns, please contact the official email of TUPC Registrar:   ' + \
                'tupc_registrar@tup.edu.ph'
            message6 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
                "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br>'
            message7 = "<i>"+'***This is an automated message, do not reply.'+"</i>"

            message = message1 + message2 + message3

            purpose_req = request.POST.get('purpose_of_request')
            date_appointment = request.POST.get('date_appointment')
            time_appointment = request.POST.get('time_appointment')
            additionalmessage = request.POST.get('additionalmessage')
            email = request.POST.get('email')

            data = {
                'date_appointment': date_appointment,
                'time_appointment': time_appointment,
                'subject': subject,
                'message': message,
                'message4': message4,
                'message5': message5,
                'message6': message6,
                'message7': message7,
                'additionalmessage': additionalmessage,
            }
            message = '''{}
            <strong>Date of Appointment:</strong>\n\t\t{}\n<br>
            <strong>Time of Appointment:</strong>\n\t\t{}\n<br><br>
            <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br>
            \n\t\t{}\n<br><br><br><br>
            \n\t\t{}\n<br><br><br>
            \n\t\t{}\n<br>
            \n\t\t{}\n<br>
            
            '''''.format(data['message'], data['date_appointment'], data['time_appointment'], data['additionalmessage'], data['message4'], data['message5'], data['message6'], data['message7'])
            msg = EmailMessage(subject, message, '', email, recipient_list,)
            msg.content_subtype = "html"
            msg.send(fail_silently=True)
            messages.success(request, "Appointment Schedule Sent.")
            return redirect('faculty_dashboard_graduation_list')
        else:
            return render(request, 'html_files/appointment.html', {'gform': gform})

# FOR SETTING APPOINTMENTS FOR REGISTRAR'S SIDE (APPROVED GRADUATION ONLY)
@login_required(login_url='/')
def reggrad_appointment(request, id):
    email_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        student_id=email_temp[0]).values_list('email', flat=True).distinct()
    rec_email = email[0]
    recipient_list = [rec_email, ]

    name_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    name = user_table.objects.filter(student_id=name_temp[0]).values_list(
        'last_name', flat=True).distinct()
    last_name = name[0]

    gender_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    gender = user_table.objects.filter(
        student_id=gender_temp[0]).values_list('gender', flat=True).distinct()
    gender_choice = gender[0]
    gender_final = ""
    if gender_choice == "Female":
        gender_final = "Ms."
    else:
        gender_final = "Mr."

    notification = "NOTIFIED"
    grad_notif = request.POST.get('notification')
    graduation_form_table.objects.filter(
        id=id).update(grad_notif=notification)

    subject = 'Application for Graduation Form'
    message1 = 'Good day,   ' + gender_final + \
        "<strong>" + name[0] + ",</strong><br><br>"
    message2 = 'Your Application for Graduation Form has been approved and is now available for printing. Kindly visit ' + \
        '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>' + \
        ' and follow the guidelines below.<br><br>'
    message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to  ' + '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>'+'<br>'+'2. On your dashboard, view your request form from the table.<br>' + \
        '3. Click the "Print" button to print the form. Please take note that the form should be printed in Folio Size Paper (8.5 x 13 inches).<br>' + \
        '4. Arrive at the appointed date and time for claiming your request.<br>' + \
        '5. Proceed to the Office of the Campus Registrar for the procedures.<br><br><br>'
    message4 = 'For other concerns, please contact the official email of TUPC Registrar:   ' + \
        'tupc_registrar@tup.edu.ph<br><br><br><br>'
    message5 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
        "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br><br>'
    message6 = "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"

    message = message1 + message2 + message3 + message4 + message5 + message6

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send(fail_silently=True)

    messages.success(request, "Email Sent.")
    return redirect('/registrar_dashboard_graduation_list/%20')

# FOR SETTING APPOINTMENTS ON REGISTRAR'S SIDE (APPROVED CLEARANCE ONLY)
@login_required(login_url='/')
def regclear_appointment(request, id):
    email_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        student_id=email_temp[0]).values_list('email', flat=True).distinct()

    rec_email = email[0]

    name_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    name = user_table.objects.filter(
        student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
    last_name = name[0]

    gender_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    gender = user_table.objects.filter(
        student_id=gender_temp[0]).values_list('gender', flat=True).distinct()
    gender_choice = gender[0]
    gender_final = ""
    if gender_choice == "Female":
        gender_final = "Ms."
    else:
        gender_final = "Mr."

    notification = "NOTIFIED"
    clear_notif = request.POST.get('notification')
    clearance_form_table.objects.filter(
        id=id).update(clear_notif=notification)

    subject = 'Application for Clearance Form'
    message1 = 'Good day,   ' + gender_final + \
        "<strong>" + name[0] + ",</strong><br><br>"
    message2 = 'Your Application for Clearance Form has been approved and is now available for printing. Kindly visit ' + \
        '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>' + \
        ' and follow the guidelines below.<br><br>'
    message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to ' + '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>'+'<br>'+'2. On your dashboard, view your request form from the table.<br>' + \
        '3. Click the "Print" button to print the form. Please take note that the form should be printed in Folio Size Paper (8.5 x 13 inches).<br>' + \
        '4. Arrive at the appointed date and time for claiming your request.<br>' + \
        '5. Proceed to the Office of the Campus Registrar for the procedures.<br><br>'
    message4 = 'For other concerns, please contact the official email of TUPC Registrar:   ' + \
        'tupc_registrar@tup.edu.ph<br><br><br><br>'
    message5 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
        "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br><br>'
    message6 = "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"

    message = message1 + message2 + message3 + message4 + message5 + message6

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send(fail_silently=True)

    messages.success(request, "Email Sent.")
    return redirect('/registrar_dashboard_clearance_list/%20')

# FOR SETTING APPOINTMENTS ON REGISTRAR'S SIDE (APPROVED REQUESTS ONLY)
@login_required(login_url='/')
def request_appointment(request, id):
    purposerequest = request_form_table.objects.filter(
        id=id).values_list('request', flat=True).distinct()
    purpose = purposerequest[0]
    daterequest = request_form_table.objects.filter(
        id=id).values_list('date', flat=True).distinct()
    daterequested = daterequest[0]
        
    if request.method == 'POST':
        email_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            student_id=email_temp[0]).values_list('email', flat=True).distinct()
        rec_email = email[0]
        recipient_list = [rec_email, ]

        gender_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        gender = user_table.objects.filter(
            student_id=gender_temp[0]).values_list('gender', flat=True).distinct()
        gender_choice = gender[0]
        gender_final = ""
        if gender_choice == "Female":
            gender_final = "Ms."
        else:
            gender_final = "Mr."

        purpose = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        purpose_of = request_form_table.objects.filter(
            student_id=purpose[0]).values_list('request', flat=True).distinct()
        purpose_of_req = purpose_of[0]
        purpose_of_request = purpose_of_req,

        amount = request_form_table.objects.filter(
            id=id).values_list('amount', flat=True).distinct()
        amount_to = request_form_table.objects.filter(
            amount=amount[0]).values_list('amount', flat=True).distinct()
        amount_to_pay = amount_to[0]

        name_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        name = user_table.objects.filter(
            student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
        last_name = name[0]

        subject = 'Claiming of ' + purpose_of_request[0]
        message1 = "Good day, " + gender_final + \
            "<strong>" + name[0] + ",</strong><br><br>"
        message2 = 'Your request for  ' + "<strong>" + purpose_of_request[0] + "</strong>" +  \
            '   has been approved. Kindly visit ' + '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>' + \
            ' and follow the guidelines below for claiming your requested credentials.<br><br>'
        message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to ' + '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>' + '<br>'+'2. On your dashboard, view your request form from the table.<br>' + \
            '3. Click the "Print" button to print the form. Please take note that the form should be printed in Folio Size Paper (8.5 x 13 inches).<br>' + '4. For credentials with payment required, please prepare the amount to pay.<br>' + \
            '5. Arrive at the appointed date and time for claiming your request.<br>' + \
            '6. Proceed to the Office of the Campus Registrar for the procedures.<br><br>'
        message4 = 'For other concerns, please contact the official email of TUPC Registrar:   ' + \
            'tupc_registrar@tup.edu.ph .'
        message5 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
            "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite'
        message6 = "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"

        message = message1 + message2 + message3

        purpose_req = request.POST.get('purpose_of_request')
        amount_paid = request.POST.get('amount_paid')
        date_appointment = request.POST.get('date_appointment')
        request_form_table.objects.filter(
            id=id).update(appointment=date_appointment)
        request_form_table.objects.filter(
            id=id).update(approval_status="APPROVED")

        time_appointment = request.POST.get('time_appointment')
        additionalmessage = request.POST.get('additionalmessage')
        email = request.POST.get('email')

        data = {
            'amount_paid': amount_to[0],
            'date_appointment': date_appointment,
            'time_appointment': time_appointment,
            'subject': subject,
            'message': message,
            'message4': message4,
            'message5': message5,
            'message6': message6,
            'additionalmessage': additionalmessage,
        }
        message = '''{}
        <strong>Amount to  Pay:</strong>\n\t\t{}\n<br>
        <strong>Date of  Appointment:</strong>\n\t\t{}\n<br>
        <strong>Time of  Appointment:</strong>\n\t\t{}\n<br><br>
        <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br><br>
        \n\t\t{}\n<br><br><br><br>
        \n\t\t{}\n<br><br><br>
        \n\t\t{}\n<br>
        
        '''''.format(data['message'], data['amount_paid'], data['date_appointment'], data['time_appointment'], data['additionalmessage'], data['message4'], data['message5'], data['message6'])

        msg = EmailMessage(subject, message, '', email, recipient_list)
        print("hi", recipient_list)
        msg.content_subtype = "html"

        torletter1 = request.POST.get('file_attach')
        stor = str(torletter1)
        if stor != "":
            torletter = request.FILES['file_attach']
            msg.attach(torletter.name, torletter.file.read(),
                       torletter.content_type)
        msg.send(fail_silently=True)
        messages.success(request, "Appointment Schedule Sent.")

        return redirect('registrar_dashboard_request_list')
    else:
        return render(request, 'html_files/appointment.html', {'purpose': purpose, 'daterequested': daterequested})

# LOGIN ALL USERS IN COVER PAGE
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('email_box_01')
        password = request.POST.get('password_box_01')
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            p = user_table.objects.filter(username=username).values_list(
                'user_type', flat=True).distinct()
            print("P:", p)
            va = p[0]

            if va == "STUDENT":
                return redirect('student_dashboard')
            elif va == "ALUMNUS":
                return redirect('student_dashboard')
            elif va == "OLD STUDENT":
                return redirect('student_dashboard')
            elif va == "FACULTY":
                return redirect('faculty_dashboard')
            elif va == "REGISTRAR":
                return redirect('registrar_dashboard')
            elif va == "STAFF":
                return redirect('registrar_dashboard')
            else:
                return redirect('/')
        else:
            messages.error(request, ("Incorrect Username or Password"))
            return redirect('/')
    else:
        registrar_first = user_table.objects.filter(
            user_type="REGISTRAR").values_list('first_name', flat=True).distinct()
        registrar_last = user_table.objects.filter(
            user_type="REGISTRAR").values_list('last_name', flat=True).distinct()
        registrar_gender = user_table.objects.filter(
            user_type="REGISTRAR").values_list('gender', flat=True).distinct()
        if registrar_first:
            if registrar_gender[0] == "Male":
                name_of_registrar = " Mr. " + \
                    registrar_first[0] + " " + registrar_last[0]
            else:
                name_of_registrar = " Ms. " + \
                    registrar_first[0] + " " + registrar_last[0]
        else:
            name_of_registrar = ""
        return render(request, 'html_files/1Cover Page.html', {'RegistrarName': name_of_registrar})

#  LOGOUT ALL USERS FROM DASHBOARDS
def logout_user(request):
    logout(request)
    return redirect('/')

# SIGNUP FOR STUDENTS
def student_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            id_num = form.cleaned_data.get("id_number")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            last = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            temp = form.cleaned_data.get("profile_picture")

            # middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = email
            if middle is None:
                form.instance.full_name = last + ", " + first
            else:
                form.instance.full_name = last + ", " + first + " " + middle

            form.instance.user_type = "STUDENT"

            form.save()

            # AUTOMATICALLY EMAIL STUDENTS UPON SUCCESSFUL SIGNUP (REMOVED DUE TO EMAIL LIMITATIONS)
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(
                request, 'Account Saved. Keep in mind that your username is: ' + email)
            return redirect('/')
        else:
            messages.error(
                request, form.errors)

    img_object = form.instance
    user_identifier = "STUDENT"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

# SIGNUP FOR OLD STUDENTS/TRANSFEREES
def oldstudent_registration(request):
    form = signup_form()
    print(form.errors)
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            email = form.cleaned_data.get("email")
            # middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = email
            if middle is None:
                form.instance.full_name = last + ", " + first
            else:
                form.instance.full_name = last + ", " + first + " " + middle

            form.instance.user_type = "OLD STUDENT"
            form.save()
            
            # AUTOMATICALLY EMAIL STUDENTS UPON SUCCESSFUL SIGNUP (REMOVED DUE TO EMAIL LIMITATIONS)
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(
                request, 'Account Saved. Keep in mind that your username is: ' + email)
            return redirect('/')
        else:
            messages.error(
                request, form.errors)
    img_object = form.instance
    user_identifier = "OLD STUDENT"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

# SIGNUP FOR FACULTIES/ DEPARTMENT HEADS
def faculty_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("email")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.position = "FACULTY"
            form.instance.username = username
            form.instance.user_type = "FACULTY"
            form.instance.designation = "---"
            if middle is None:
                form.instance.full_name = last + ", " + first
            else:
                form.instance.full_name = last + ", " + first + " " + middle

            form.save()
            messages.success(
                request, 'Account Saved. Keep in mind that your username is: ' + username)

            return redirect('/')
        else:
            messages.error(
                request, form.errors)
    img_object = form.instance
    user_identifier = "FACULTY"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

# SIGNUP FOR ALUMNI
def alumnus_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            year_graduated = form.cleaned_data.get("year_graduated")
            id_num = form.cleaned_data.get("id_number")
            birthday = form.cleaned_data.get("birthday")
            birthdaym = birthday[:2]
            birthdayd = birthday[3:5]
            birthdayy = birthday[6:8]
            username = form.cleaned_data.get("email")
            year = random.randint(0, 18)
            year_grad = year_graduated[2:4]
            randomizer = random.randint(0, 9999)
            print(year_grad)
            id_num = str(year).zfill(2) + "-" + str(randomizer).zfill(4) + \
                "-" + year_grad + "-" + birthdaym + birthdayd + birthdayy

            while id_num in user_table.objects.values_list('id_number'):
                year = random.randint(0, 18)
                year_grad = year_graduated[2:4]
                randomizer = random.randint(0, 9999)
                print(year_grad)
                id_num = str(year).zfill(2) + "-" + str(randomizer).zfill(4) + \
                    "-" + year_grad + "-" + birthdaym + birthdayd + birthdayy

            form.instance.id_number = id_num
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = username
            form.instance.user_type = "ALUMNUS"
            if middle is None:
                form.instance.full_name = last + ", " + first
            else:
                form.instance.full_name = last + ", " + first + " " + middle

            form.save()
            # AUTOMATICALLY EMAIL STUDENTS UPON SUCCESSFUL SIGNUP (REMOVED DUE TO EMAIL LIMITATIONS)
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(
                request, 'Account Saved. Keep in mind that your username is: ' + username)
            return redirect('/')

        else:
            messages.error(
                request, form.errors)
            messages.error(form.errors)
            print(form.errors)
    img_object = form.instance
    user_identifier = "ALUMNUS"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

# SIGNUP FOR STAFFS (AVAILABLE ON REGISTRAR'S SIDE)
def staff_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("email")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")

            form.instance.birthday = "MM/DD/YY"
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = username
            form.instance.user_type = "STAFF"
            if middle is None:
                form.instance.full_name = last + ", " + first
            else:
                form.instance.full_name = last + ", " + first + " " + middle

            form.save()
            messages.success(
                request, "Account Saved. Keep in mind that the staff's username is: " + username)
            return redirect('registrar_dashboard_staff_list')
        else:
            messages.error(request, form.errors)

            return redirect('registrar_dashboard_staff_list')
    img_object = form.instance
    user_identifier = "STAFF"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

# RENDER COVER PAGE
def cover(request):
    return render(request, 'html_files/1Cover Page.html')

# DISPLAY STUDENT DASHBOARD
@login_required(login_url='/')
def student_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT":

        # TO DETERMINE IF STUDENT IS 4TH YEAR OR NOT
        todays_date = date.today()
        id_num = request.user.id_number
        print("id", id_num)
        sliced_id = int(str(id_num)[:2])
        current_year = '"'+str(todays_date.year) + '"'
        temp = int(current_year[2:5])
        graduating = temp - sliced_id

        student_id = request.user.student_id
        full_name = request.user.full_name
        first = request.user.first_name
        last = request.user.last_name
        middle = request.user.middle_name

        if middle is None:
            name2 = last + ", " + first
        else:
            mid = middle[0] + "."
            name2 = last + ", " + first + " " + mid

        print(student_id)

        # FOR RENDERING TABLES ON DASHBOARD
        st0 = request_form_table.objects.filter(student_id=student_id)
        st = graduation_form_table.objects.filter(student_id=student_id)
        st1 = clearance_form_table.objects.filter(student_id=student_id)

        check_form137_inrequest = request_form_table.objects.filter(
            Q(name=full_name) | Q(name=name2)).values_list('form_137', flat=True).distinct()
        check_request = request_form_table.objects.filter(Q(name=full_name) | Q(
            name=name2)).order_by('-time_requested').values_list('claim', flat=True).distinct()
        get_clearance_id = clearance_form_table.objects.filter(name=full_name).order_by(
            '-time_requested').values_list('id', flat=True).distinct()
        check_clearance = clearance_form_table.objects.filter(name=full_name).order_by(
            '-time_requested').values_list('approval_status', flat=True).distinct()
        # document checker
        display = []
        # Form137-A

        # MISSING DOCUMENT CHECKER
        if check_form137_inrequest.exists():
            for i in check_form137_inrequest:
                if i == '❌':
                    print('Missing FORM 137-A')
                    display.append("FORM 137-A")
                else:
                    pass
        else:
            pass
        if check_request:
            claim_note = check_request[0]
        else:
            claim_note = "NONE"

        if check_clearance:
            if check_clearance == "APPROVED":
                clearance_stat = ""
                clearance_id = get_clearance_id[0]
            else:
                clearance_stat = "UNAPPROVED"
                clearance_id = get_clearance_id[0]
        else:
            clearance_stat = ""
            clearance_id = ""

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {'st': st, 'st1': st1, 'st0': st0, 'display': display, 'graduating': graduating,
               'claim_note': claim_note, 'clearance_stat': clearance_stat, 'clearance_id': clearance_id}
    return render(request, 'html_files/4.1Student Dashboard.html', context)


@login_required(login_url='/')
def clearance_form(request, req):
    
    # FACULTY LIST FOR DROPDOWN
    a = user_table.objects.filter(user_type="FACULTY", is_active=True).values_list(
        'full_name', flat=True).distinct()
    
    # FOR DISPLAYING (LASTNAME, FIRSTNAME) FORMAT IN DROPDOWNS
    # faculty_list_clear = []
    # for faculty in a:
    #     splitted=faculty.split()
    #     last = splitted[0]
    #     first = splitted[1]
    #     faculty = last + " " +first
    #     faculty_list_clear.append(faculty)
    # a = faculty_list_clear

    requested = req
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT":
        
        # TO DETERMINE IF STUDENT HAS GRADUATION OR NONE
        todays_date = date.today()
        id_num = request.user.id_number
        sliced_id = int(str(id_num)[:2])
        current_year = '"'+str(todays_date.year) + '"'
        temp = int(current_year[2:5])
        with_graduation = temp - sliced_id
        fullname = request.user.full_name
        alumni_course_adviser = ""

        # DETERMINE WHICH DEPARTMENT EACH COURSE BELONGS
        course = request.user.course_graduated
        if course:
            if course.startswith('BSIE-') or course.startswith('BTTE-'):
                print("ded")
                alumni_course_adviser_temp = user_table.objects.filter(
                    department="HDED").values_list('full_name', flat=True).distinct()
            elif course.startswith('BS-'):
                print("doe")
                alumni_course_adviser_temp = user_table.objects.filter(
                    department="HDOE").values_list('full_name', flat=True).distinct()
            else:
                print("dit")
                alumni_course_adviser_temp = user_table.objects.filter(
                    department="HDIT").values_list('full_name', flat=True).distinct()
            if alumni_course_adviser_temp:
                alumni_course_adviser = alumni_course_adviser_temp[0]
            else:
                alumni_course_adviser = " "
        else:
            pass

        user = request.user.user_type
        if request.method == "POST":
            form = clearance_form

            student_id = request.POST.get('stud_id_420')
            print(student_id)
            last_name = request.POST.get('ln_box_420')
            first_name = request.POST.get('fn_box_420')
            middle_name = request.POST.get('mn_box_420')
            if middle_name == "None":
                name = last_name + ", " + first_name
            else:
                name = last_name + ", " + first_name + " " + middle_name
            name2 = first_name + " " + last_name
            present_address = request.POST.get('padd_box_420')
            course = request.POST.get('course_420')
            date_filed = request.POST.get('dfiled_box_420')
            date_admitted = request.POST.get('dait_box_420')
            highschool_graduated = request.POST.get('hswg_box_420')
            tupc_graduate = request.POST.get('grad_option_420')
            tupc_graduated_date = request.POST.get('iydfiled_box_420')
            terms = request.POST.get('notit_box_420')
            amount = request.POST.get('amountp_box_420')
            last_request = request.POST.get('requested_option_420')
            last_request_date = request.POST.get('dbrtime_box_420')
            last_term = request.POST.get('lasterm_box_420')
            course_adviser = request.POST.get('course_adviser_420')
            semester = request.POST.get('sem_term')
            course_adviser_signature = request.POST.get(
                'course_adviser_420') + "_UNAPPROVED"
            purpose_reason = request.POST.get('preq_box_420')
            purpose = request.POST.get('purpose_request_420')

            unapproved = "UNAPPROVED"
            approved = "_APPROVED"

            # AUTOMATICALLY APPROVE IF COURSE IS NOT UNDER THIS DEPARTMENT
            if course.startswith('BSIE-') or course.startswith('BTTE-'):
                print("ded")
                dit_signature = approved
                doe_signature = approved
                ded_signature = unapproved

            elif course.startswith('BS-'):
                print("doe")
                dit_signature = approved
                doe_signature = unapproved
                ded_signature = approved

            else:
                print("dit")
                dit_signature = unapproved
                doe_signature = approved
                ded_signature = approved

            form = clearance_form_table.objects.create(student_id=student_id, name=name, present_address=present_address, course=course,
                                                       date_filed=date_filed, date_admitted_in_tup=date_admitted,
                                                       highschool_graduated=highschool_graduated, tupc_graduate=tupc_graduate, year_graduated_in_tupc=tupc_graduated_date,
                                                       number_of_terms_in_tupc=terms, amount_paid=amount, have_previously_requested_form=last_request,
                                                       date_of_previously_requested_form=last_request_date, last_term_in_tupc=last_term,
                                                       course_adviser=course_adviser, course_adviser_signature=course_adviser_signature,
                                                       purpose_of_request=purpose, purpose_of_request_reason=purpose_reason, semester_enrolled=semester, ieduc_dept_signature=ded_signature, eng_dept_signature=doe_signature, it_dept_signature=dit_signature)

            form.save()

            return redirect('student_dashboard')
        else:
            
            # CHECKER OF PREVIOUS CLEARANCE
            request_clearance = clearance_form_table.objects.filter(name=fullname).order_by(
                '-time_requested').values_list('approval_status', flat=True).distinct()
            latest_others = request_form_table.objects.filter(name=fullname).order_by(
                '-time_requested').values_list('request', flat=True).distinct()

            if request_clearance:
                if request_clearance[0] == "APPROVED":
                    allow_request = request_clearance[0]
                    if latest_others:
                        latest_data = latest_others[0]
                        if latest_data.__contains__('Others'):
                            requested = "Others"
                            other_data = latest_others[0]
                        else:
                            other_data = latest_others[0]
                    else:
                        other_data = ""
                else:
                    allow_request = "UNAPPROVED"
                    other_data = ""
            else:
                if latest_others:
                    latest_data = latest_others[0]
                    if latest_data.__contains__('Others'):
                        requested = "Others"
                        other_data = latest_others[0]
                        allow_request = ""
                    else:
                        other_data = latest_others[0]
                        allow_request = ""
                else:
                    other_data = ""
                    allow_request = ""

            # GETTING PREVIOUS CLEARANCE
            previous_term = clearance_form_table.objects.filter(name=fullname).order_by(
                '-time_requested').values_list('date_filed', flat=True).distinct()
            if previous_term:
                date_previous = previous_term[0]
            else:
                date_previous = ""
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.2Student Clearance Form.html', {'a': a, 'with_graduation': with_graduation, 'allow': allow_request, 'requested': requested, 'other_data': other_data, 'date_previous': date_previous, 'alumni_course_adviser': alumni_course_adviser})

# VIEW GRADUATION FORM
@login_required(login_url='/')
def graduation_view(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        student_name = request.user.full_name

        check_graduation = graduation_form_table.objects.filter(
            name=student_name).values_list('id', flat=True).distinct()
        if check_graduation:
            id_graduation = str(check_graduation[0])
            print(id_graduation)
            return redirect('display_gradform/' + id_graduation)
        else:
            return redirect('graduation_form')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

# RETURN TO GRADUATION LIST (CONNECTED TO BACK BUTTON)
@login_required(login_url='/')
def reggrad_back(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        return redirect('/registrar_dashboard_graduation_list/%20')

# RETURN TO CLEARANCE LIST (CONNECTED TO BACK BUTTON)
@login_required(login_url='/')
def regclear_back(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        return redirect('/registrar_dashboard_clearance_list/%20')

# GRADUATION FORM
@login_required(login_url='/')
def graduation_form(request):
    # FACULTY LIST FOR DROPDOWN
    a = user_table.objects.filter(user_type="FACULTY", is_active=True).values_list(
        'full_name', flat=True).distinct()
    
    # FOR DISPLAYING (LASTNAME, FIRSTNAME) FORMAT IN DROPDOWNS
    # faculty_list_grad = []
    # for faculty in a:
    #     splitted=faculty.split()
    #     last = splitted[0]
    #     first = splitted[1]
    #     faculty = last + " " +first
    #     faculty_list_grad.append(faculty)
    # a = faculty_list_grad
    context = {}
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        form = graduation_form_table(request.POST or None)
        print('6')
        context = {}
        if request.method == "POST":
            print('10')
            student_id = request.POST.get('id_getter')
            last_name = request.POST.get('ln_box_430')
            first_name = request.POST.get('fn_box_430')
            middle_name = request.POST.get('mn_box_430')
            if middle_name == "None":
                name = last_name + ", " + first_name
            else:
                name = last_name + ", " + first_name + " " + middle_name
                name2 = first_name + " " + last_name
            course = request.POST.get('course_getter')

            d = request.POST.get('shift_option')
            e = request.POST.get('stdfor_option')
            h = request.POST.get('sem_term')
            i = request.POST.get('deadline_box_43')
            if h:
                f = "YES"

            if i:
                f = "NO"

            j = request.POST.get('trainP_startdate')
            k = request.POST.get('trainP_enddate')
            l = request.POST.get('instructor_name')

            m1 = request.POST.get('subject1')
            n1 = request.POST.get('room1')
            s1 = request.POST.get('faculty1')
            u1_1 = request.POST.get('starttime1_1')
            v1_1 = request.POST.get('endtime1_1')
            q1_1 = request.POST.get('day1_1')

            m2 = request.POST.get('subject2')
            n2 = request.POST.get('room2')
            s2 = request.POST.get('faculty2')
            u1_2 = request.POST.get('starttime1_2')
            v1_2 = request.POST.get('endtime1_2')
            q1_2 = request.POST.get('day1_2')

            m3 = request.POST.get('subject3')
            n3 = request.POST.get('room3')
            s3 = request.POST.get('faculty3')
            u1_3 = request.POST.get('starttime1_3')
            v1_3 = request.POST.get('endtime1_3')
            q1_3 = request.POST.get('day1_3')

            m4 = request.POST.get('subject4')
            n4 = request.POST.get('room4')
            s4 = request.POST.get('faculty4')
            u1_4 = request.POST.get('starttime1_4')
            v1_4 = request.POST.get('endtime1_4')
            q1_4 = request.POST.get('day1_4')

            m5 = request.POST.get('subject5')
            n5 = request.POST.get('room5')
            s5 = request.POST.get('faculty5')
            u1_5 = request.POST.get('starttime1_5')
            v1_5 = request.POST.get('endtime1_5')
            q1_5 = request.POST.get('day1_5')

            m6 = request.POST.get('subject6')
            n6 = request.POST.get('room6')
            s6 = request.POST.get('faculty6')
            u1_6 = request.POST.get('starttime1_6')
            v1_6 = request.POST.get('endtime1_6')
            q1_6 = request.POST.get('day1_6')

            m7 = request.POST.get('subject7')
            n7 = request.POST.get('room_7')
            s7 = request.POST.get('faculty7')
            u1_7 = request.POST.get('starttime1_7')
            v1_7 = request.POST.get('endtime1_7')
            q1_7 = request.POST.get('day1_7')

            m8 = request.POST.get('subject8')
            n8 = request.POST.get('room8')
            s8 = request.POST.get('faculty8')
            u1_8 = request.POST.get('starttime1_8')
            v1_8 = request.POST.get('endtime1_8')
            q1_8 = request.POST.get('day1_8')

            m9 = request.POST.get('subject9')
            n9 = request.POST.get('room9')
            s9 = request.POST.get('faculty9')
            u1_9 = request.POST.get('starttime1_9')
            v1_9 = request.POST.get('endtime1_9')
            q1_9 = request.POST.get('day1_9')

            m10 = request.POST.get('subject10')
            n10 = request.POST.get('room10')
            s10 = request.POST.get('faculty10')
            u1_10 = request.POST.get('starttime1_10')
            v1_10 = request.POST.get('endtime1_10')
            q1_10 = request.POST.get('day1_10')

            o1 = request.POST.get('addsubject1')
            p1 = request.POST.get('addroom1')
            t1 = request.POST.get('addfaculty1')
            w1_1 = request.POST.get('add_starttime1_1')
            x1_1 = request.POST.get('add_endtime1_1')
            r1_1 = request.POST.get('addday1_1')

            o2 = request.POST.get('addsubject2')
            p2 = request.POST.get('addroom2')
            t2 = request.POST.get('addfaculty2')
            w1_2 = request.POST.get('add_starttime1_2')
            x1_2 = request.POST.get('add_endtime1_2')
            r1_2 = request.POST.get('addday1_2')

            o3 = request.POST.get('addsubject3')
            p3 = request.POST.get('addroom3')
            t3 = request.POST.get('addfaculty3')
            w1_3 = request.POST.get('add_starttime1_3')
            x1_3 = request.POST.get('add_endtime1_3')
            r1_3 = request.POST.get('addday1_3')

            o4 = request.POST.get('addsubject4')
            p4 = request.POST.get('addroom4')
            t4 = request.POST.get('addfaculty4')
            w1_4 = request.POST.get('add_starttime1_4')
            x1_4 = request.POST.get('add_endtime1_4')
            r1_4 = request.POST.get('addday1_4')

            o5 = request.POST.get('addsubject5')
            p5 = request.POST.get('addroom5')
            t5 = request.POST.get('addfaculty5')
            w1_5 = request.POST.get('add_starttime1_5')
            x1_5 = request.POST.get('add_endtime1_5')
            r1_5 = request.POST.get('addday1_5')

            sig_s1 = ""
            sig_s2 = ""
            sig_s3 = ""
            sig_s4 = ""
            sig_s5 = ""
            sig_s6 = ""
            sig_s7 = ""
            sig_s8 = ""
            sig_s9 = ""
            sig_s10 = ""

            sig_t1 = ""
            sig_t2 = ""
            sig_t3 = ""
            sig_t4 = ""
            sig_t5 = ""

            if s1 == "1":
                s1 = "NO FACULTY"
                sig_s1 = "NO_APPROVED"
            else:
                sig_s1 = s1 + "_UNAPPROVED"

            if s2 == "1":
                s2 = "NO FACULTY"
                sig_s2 = "NO_APPROVED"
            else:
                sig_s2 = s2 + "_UNAPPROVED"
            if s3 == "1":
                s3 = "NO FACULTY"
                sig_s3 = "NO_APPROVED"
            else:
                sig_s3 = s3 + "_UNAPPROVED"
            if s4 == "1":
                s4 = "NO FACULTY"
                sig_s4 = "NO_APPROVED"
            else:
                sig_s4 = s4 + "_UNAPPROVED"
            if s5 == "1":
                s5 = "NO FACULTY"
                sig_s5 = "NO_APPROVED"
            else:
                sig_s5 = s5 + "_UNAPPROVED"
            if s6 == "1":
                s6 = "NO FACULTY"
                sig_s6 = "NO_APPROVED"
            else:
                sig_s6 = s6 + "_UNAPPROVED"
            if s7 == "1":
                s7 = "NO FACULTY"
                sig_s7 = "NO_APPROVED"
            else:
                sig_s7 = s7 + "_UNAPPROVED"
            if s8 == "1":
                s8 = "NO FACULTY"
                sig_s8 = "NO_APPROVED"
            else:
                sig_s8 = s8 + "_UNAPPROVED"
            if s9 == "1":
                s9 = "NO FACULTY"
                sig_s9 = "NO_APPROVED"
            else:
                sig_s9 = s9 + "_UNAPPROVED"
            if s10 == "1":
                s10 = "NO FACULTY"
                sig_s10 = "NO_APPROVED"
            else:
                sig_s10 = s10 + "_UNAPPROVED"

            if t1 == "1":
                t1 = "NO FACULTY"
                sig_t1 = "NO_APPROVED"
            else:
                sig_t1 = t1 + "_UNAPPROVED"
            if t2 == "1":
                t2 = "NO FACULTY"
                sig_t2 = "NO_APPROVED"
            else:
                sig_t2 = t2 + "_UNAPPROVED"
            if t3 == "1":
                t3 = "NO FACULTY"
                sig_t3 = "NO_APPROVED"
            else:
                sig_t3 = t3 + "_UNAPPROVED"
            if t4 == "1":
                t4 = "NO FACULTY"
                sig_t4 = "NO_APPROVED"
            else:
                sig_t4 = t4 + "_UNAPPROVED"
            if t5 == "1":
                t5 = "NO FACULTY"
                sig_t5 = "NO_APPROVED"
            else:
                sig_t5 = t5 + "_UNAPPROVED"

            if l == "1":
                l = "NO FACULTY"
                sig_l = "NO_APPROVED"
            else:
                sig_l = l + "_UNAPPROVED"

            form = graduation_form_table.objects.create(name=name, student_id=student_id, course=course, shift=d,
                                                        study_load=e, status=f, enrolled_term=h, unenrolled_application_deadline=i,
                                                        trainP_startdate=j, trainP_enddate=k, instructor_name=l,

                                                        subject1=m1, room1=n1, faculty1=s1, starttime1_1=u1_1, endtime1_1=v1_1, day1_1=q1_1,
                                                        subject2=m2, room2=n2, faculty2=s2, starttime1_2=u1_2, endtime1_2=v1_2, day1_2=q1_2,
                                                        subject3=m3, room3=n3, faculty3=s3, starttime1_3=u1_3, endtime1_3=v1_3, day1_3=q1_3,
                                                        subject4=m4, room4=n4, faculty4=s4, starttime1_4=u1_4, endtime1_4=v1_4, day1_4=q1_4,
                                                        subject5=m5, room5=n5, faculty5=s5, starttime1_5=u1_5, endtime1_5=v1_5, day1_5=q1_5,
                                                        subject6=m6, room6=n6, faculty6=s6, starttime1_6=u1_6, endtime1_6=v1_6, day1_6=q1_6,
                                                        subject7=m7, room7=n7, faculty7=s7, starttime1_7=u1_7, endtime1_7=v1_7, day1_7=q1_7,
                                                        subject8=m8, room8=n8, faculty8=s8, starttime1_8=u1_8, endtime1_8=v1_8, day1_8=q1_8,
                                                        subject9=m9, room9=n9, faculty9=s9, starttime1_9=u1_9, endtime1_9=v1_9, day1_9=q1_9,
                                                        subject10=m10, room10=n10, faculty10=s10, starttime1_10=u1_10, endtime1_10=v1_10, day1_10=q1_10,

                                                        addsubject1=o1, addroom1=p1, addfaculty1=t1, add_starttime1_1=w1_1, add_endtime1_1=x1_1, addday1_1=r1_1,
                                                        addsubject2=o2, addroom2=p2, addfaculty2=t2, add_starttime1_2=w1_2, add_endtime1_2=x1_2, addday1_2=r1_2,
                                                        addsubject3=o3, addroom3=p3, addfaculty3=t3, add_starttime1_3=w1_3, add_endtime1_3=x1_3, addday1_3=r1_3,
                                                        addsubject4=o4, addroom4=p4, addfaculty4=t4, add_starttime1_4=w1_4, add_endtime1_4=x1_4, addday1_4=r1_4,
                                                        addsubject5=o5, addroom5=p5, addfaculty5=t5, add_starttime1_5=w1_5, add_endtime1_5=x1_5, addday1_5=r1_5,

                                                        signature1=sig_s1, signature2=sig_s2, signature3=sig_s3, signature4=sig_s4, signature5=sig_s5,
                                                        signature6=sig_s6, signature7=sig_s7, signature8=sig_s8, signature9=sig_s9, signature10=sig_s10,
                                                        addsignature1=sig_t1, addsignature2=sig_t2, addsignature3=sig_t3, addsignature4=sig_t4, addsignature5=sig_t5, sitsignature=sig_l)
            form.save()
            print('8')

            return redirect('student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    form = Graduation_form_table(request.POST or None)
    return render(request, 'html_files/4.3Student Graduation Form.html', {'form': form, 'a': a})

# ALUMNUS DASHBOARD
@login_required(login_url='/')
def alumnus_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "ALUMNUS":
        student_id = request.user.student_id
        print(student_id)

        st = graduation_form_table.objects.filter(student_id=student_id)
        st1 = clearance_form_table.objects.filter(student_id=student_id)

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/4.1Student Dashboard.html', {'st': st, 'st1': st1})

# FACULTY DASHBOARD
@login_required(login_url='/')
def faculty_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        unapproved = request.user.full_name + "_UNAPPROVED"
        st1 = ""
        st = graduation_form_table.objects.filter(Q(signature1=unapproved) | Q(signature2=unapproved) | Q(signature3=unapproved) |
                                                  Q(signature4=unapproved) | Q(signature5=unapproved) | Q(signature6=unapproved) |
                                                  Q(signature7=unapproved) | Q(signature8=unapproved) | Q(signature9=unapproved) | Q(signature10=unapproved) |
                                                  Q(addsignature1=unapproved) | Q(addsignature2=unapproved) | Q(addsignature3=unapproved) |
                                                  Q(addsignature4=unapproved) | Q(addsignature5=unapproved) | Q(sitsignature=unapproved)).order_by('-time_requested')
        print(unapproved)

        # CLEARANCE FORM IDENTIFIER FOR DEPARTMENT HEADS
        if request.user.department == "HOCS":
            st1 = clearance_form_table.objects.filter(
                accountant_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDLA":
            st1 = clearance_form_table.objects.filter(
                liberal_arts_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDMS":
            st1 = clearance_form_table.objects.filter(
                mathsci_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDPECS":
            st1 = clearance_form_table.objects.filter(
                pe_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDIT":
            st1 = clearance_form_table.objects.filter(
                it_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDED":
            st1 = clearance_form_table.objects.filter(
                ieduc_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDOE":
            st1 = clearance_form_table.objects.filter(
                eng_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HOCL":
            st1 = clearance_form_table.objects.filter(
                library_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HOGS":
            st1 = clearance_form_table.objects.filter(
                guidance_office_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HOSA":
            st1 = clearance_form_table.objects.filter(
                osa_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HADAA":
            st1 = clearance_form_table.objects.filter(Q(approval_status="9/10"), Q(course_adviser_signature__contains="_APPROVED"),
                Q(academic_affairs_signature="UNAPPROVED")).order_by('-time_requested')

        # CLEARANCE FORM IDENTIFIER FOR COURSE ADVISERS
        if clearance_form_table.objects.filter(course_adviser_signature=unapproved):
            st1 = clearance_form_table.objects.filter(
                course_adviser_signature=unapproved).order_by('-time_requested')
            if request.user.department == "HOCS":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    accountant_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDLA":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    liberal_arts_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDMS":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    mathsci_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDPECS":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    pe_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDIT":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    it_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDOE":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    eng_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDED":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    ieduc_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOCL":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    library_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOGS":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    guidance_office_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOSA":
                st1 = clearance_form_table.objects.filter(Q(course_adviser_signature=unapproved) | Q(
                    osa_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HADAA":
                st1 = clearance_form_table.objects.filter(Q(approval_status="8/10"), Q(course_adviser_signature=unapproved) | Q(
                    academic_affairs_signature="UNAPPROVED")).order_by('-time_requested')

        with_clearance = clearance_form_table.objects.filter(
            course_adviser=request.user.full_name)
        
        # REMOVE "H" IN ACCOUNT SETTINGS IF DEPARTMENT HEAD
        depacc = request.user.department
        if depacc.startswith('H'):
            depacc = depacc[1:]
        return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, 'st1': st1, 'with_clearance': with_clearance, 'depacc': depacc})

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

# APPROVE ALL FOR CLEARANCE LISTS
@login_required(login_url='/')
def faculty_dashboard_clearance_list_all(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        f_n = request.user.full_name
        f_n_approved = request.user.full_name + "_APPROVED"
        id_list = []
        sig = ""
        if request.method == "POST":
            sig = request.POST.get('sig')
            templist = request.POST.get('id_list')
            ilist = templist.split(',')
            print("ilist", ilist)
            for i in ilist:
                id_list.append(i)
                print("this is i:", i)
            comma = ","
            while (comma in id_list):
                id_list.remove(comma)

            print("sadsa", id_list)
        name_temp = clearance_form_table.objects.filter(
            id=int(i)).values_list('name', flat=True).distinct()

        # SIGNATURE COUNTER
        f_n = request.user.full_name
        cursor = connection.cursor()
        query = "SELECT approval_status from `gradclear_app_clearance_form_table` where id=%s"
        val = (int(i),)
        cursor.execute(query, val)

        row = cursor.fetchone()
        rownum = row[0]
        print('rownum', rownum)
        if len(rownum) < 5:
            temp = rownum[0]
            print(temp, "this 1")
        else:
            rownum1 = rownum[0]
            rownum2 = rownum[1]
            full_num = rownum1[0], rownum2[0]
            temp = full_num[0] + full_num[1]
            print("this 2", temp)

        app_status = int(temp)
        print(app_status)
        numerator = app_status + 1
        adder = str(numerator) + "/10"
        dep = request.user.department
        signature_saved = f_n_approved + " " + sig

        print("list:", id_list)
        for i in id_list:

            if dep == "HDLA":
                clearance_form_table.objects.filter(id=int(i)).update(
                    liberal_arts_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HOCS":
                clearance_form_table.objects.filter(id=int(i)).update(
                    accountant_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HDMS":
                clearance_form_table.objects.filter(id=int(i)).update(
                    mathsci_dept_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HDPECS":
                clearance_form_table.objects.filter(id=int(i)).update(
                    pe_dept_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HDED":
                clearance_form_table.objects.filter(id=int(i)).update(
                    ieduc_dept_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HDIT":
                clearance_form_table.objects.filter(id=int(i)).update(
                    it_dept_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HDOE":
                clearance_form_table.objects.filter(id=int(i)).update(
                    eng_dept_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HOCL":
                clearance_form_table.objects.filter(id=int(i)).update(
                    library_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HOGS":
                clearance_form_table.objects.filter(id=int(i)).update(
                    guidance_office_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HOSA":
                clearance_form_table.objects.filter(id=int(i)).update(
                    osa_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if dep == "HADAA":
                clearance_form_table.objects.filter(id=int(i)).update(
                    academic_affairs_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)
            if clearance_form_table.objects.filter(course_adviser_signature=f_n + "_UNAPPROVED", id=int(i)):

                clearance_form_table.objects.filter(id=int(i)).update(
                    course_adviser_signature=signature_saved)
                clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)

            # DETECT IF SIGNATURES ARE COMPLETE, UPDATE APPROVAL STATUS
            approved_text = "_APPROVED"
            approval_status_checker = clearance_form_table.objects.filter(
                Q(liberal_arts_signature__contains=approved_text) &
                Q(accountant_signature__contains=approved_text) &
                Q(mathsci_dept_signature__contains=approved_text) &
                Q(pe_dept_signature__contains=approved_text) &
                Q(ieduc_dept_signature__contains=approved_text) &
                Q(it_dept_signature__contains=approved_text) &
                Q(eng_dept_signature__contains=approved_text) &
                Q(library_signature__contains=approved_text) &
                Q(guidance_office_signature__contains=approved_text) &
                Q(osa_signature__contains=approved_text) &
                Q(academic_affairs_signature__contains=approved_text) &
                Q(course_adviser_signature__contains=approved_text), id=int(i))
            if approval_status_checker:
                clearance_form_table.objects.filter(
                    id=int(i)).update(approval_status="APPROVED")

                for get_i in id_list:
                    getting_names = clearance_form_table.objects.filter(id=int(get_i)).values_list('name', flat=True).distinct()
                    get_requested = clearance_form_table.objects.filter(id=int(get_i)).values_list('purpose_of_request', flat=True).distinct()
                    for get_names in getting_names:
                        for req in get_requested:
                            if req == "Certification":
                                request_form_table.objects.filter(name=str(get_names), request__contains="Certification").update(clearance="✔")
                            else:
                                request_form_table.objects.filter(name=str(get_names), request=str(req)).update(clearance="✔")

            messages.success(request, "Form Approved.")
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return redirect('faculty_dashboard_clearance_list')

# DISPLAY CLEARANCE LIST DEPENDING ON DEPARTMENT
@login_required(login_url='/')
def faculty_dashboard_clearance_list(request):
    esignature = request.user.e_signature
    esignature_datetime = request.user.e_signature_timesaved
    uploaded_signature = request.user.uploaded_signature
    uploaded_signature_datetime = request.user.uploaded_signature_timesaved
    id_Facultynumber = request.user.id
    print(esignature)
    f_n_unapproved = request.user.full_name + "_UNAPPROVED"
    f_n_approved = request.user.full_name + "_APPROVED"
    f_n = request.user.full_name
    st = ""
    dep = request.user.department

    course_adv = clearance_form_table.objects.filter(
        course_adviser=request.user.full_name)
    esign_check = user_table.objects.filter(
        full_name=f_n).values_list('e_signature', flat=True).distinct()
    uploadsig_check = user_table.objects.filter(full_name=f_n).values_list(
        'uploaded_signature', flat=True).distinct()

    if request.user.is_authenticated and request.user.user_type == "FACULTY":

        if course_adv:
            st = clearance_form_table.objects.filter(
                Q(course_adviser_signature=f_n_unapproved)).order_by('-time_requested')

            if request.user.department == "HOCS":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    accountant_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDLA":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    liberal_arts_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDMS":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    mathsci_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDPECS":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    pe_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDIT":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    it_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDOE":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    eng_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HDED":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    ieduc_dept_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOCL":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    library_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOGS":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    guidance_office_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HOSA":
                st = clearance_form_table.objects.filter(Q(course_adviser_signature=f_n_unapproved) | Q(
                    osa_signature="UNAPPROVED")).order_by('-time_requested')

            if request.user.department == "HADAA":
                st = clearance_form_table.objects.filter( Q(approval_status="8/10") , Q(course_adviser_signature=f_n_unapproved) | Q(
                    academic_affairs_signature="UNAPPROVED")).order_by('-time_requested')

        elif request.user.department == "HOCS":
            st = clearance_form_table.objects.filter(
                accountant_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDLA":
            st = clearance_form_table.objects.filter(
                liberal_arts_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDMS":
            st = clearance_form_table.objects.filter(
                mathsci_dept_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDPECS":
            st = clearance_form_table.objects.filter(
                pe_dept_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDIT":
            st = clearance_form_table.objects.filter(
                it_dept_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDED":
            st = clearance_form_table.objects.filter(
                ieduc_dept_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HDOE":
            st = clearance_form_table.objects.filter(
                eng_dept_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HOCL":
            st = clearance_form_table.objects.filter(
                library_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HOGS":
            st = clearance_form_table.objects.filter(
                guidance_office_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HOSA":
            st = clearance_form_table.objects.filter(
                osa_signature="UNAPPROVED").order_by('-time_requested')

        elif request.user.department == "HADAA":
            st = clearance_form_table.objects.filter(Q(approval_status="9/10"), Q(course_adviser_signature__contains="_APPROVED"),
                Q(academic_affairs_signature="UNAPPROVED")).order_by('-time_requested')

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    if esign_check:
        esign_checker = esign_check[0]
    else:
        esign_checker = ""

    if uploadsig_check:
        upload_checker = uploadsig_check[0]
    else:
        upload_checker = ""

    return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'dep': dep, 'f_n_unapproved': f_n_unapproved, 'f_n_approved': f_n_approved, 'course_adv': course_adv, 'e_signature': esignature, 'esignature_datetime': esignature_datetime, 'esign_check': esign_checker, 'uploaded_signature': uploaded_signature, 'uploadsig_check': upload_checker, 'uploaded_datetime': uploaded_signature_datetime,  'id': id_Facultynumber})

# SINGLE APPROVAL IN CLEARANCE LIST
@login_required(login_url='/')
def update_clearance(request, id, dep, sign):
    print(sign)
    name_temp = clearance_form_table.objects.filter(
        id=id).values_list('name', flat=True).distinct()
    email_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        student_id=email_temp[0]).values_list('email', flat=True).distinct()
    rec_email = email[0]
    f_n = request.user.full_name
    f_n_approved = request.user.full_name + "_APPROVED"
    print(rec_email)
    f_n_approved = request.user.full_name + "_APPROVED"

    # SIGNATURE COUNTER
    cursor = connection.cursor()
    query = "SELECT approval_status from `gradclear_app_clearance_form_table` where id=%s"
    val = (id,)
    cursor.execute(query, val)

    row = cursor.fetchone()
    rownum = row[0]
    print('rownum', rownum)
    if len(rownum) < 5:
        temp = rownum[0]
        print(temp, "this 1")
    else:
        rownum1 = rownum[0]
        rownum2 = rownum[1]
        full_num = rownum1[0], rownum2[0]
        temp = full_num[0] + full_num[1]
        print("this 2", temp)

    app_status = int(temp)
    print(app_status)
    numerator = app_status + 1
    adder = str(numerator) + "/10"

    signature_saved = f_n_approved + " " + sign
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if dep == "liberal_arts_signature":
            clearance_form_table.objects.filter(id=id).update(
                liberal_arts_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "accountant_signature":
            clearance_form_table.objects.filter(id=id).update(
                accountant_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "mathsci_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                mathsci_dept_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "pe_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                pe_dept_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "ieduc_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                ieduc_dept_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "it_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                it_dept_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "eng_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                eng_dept_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "library_signature":
            clearance_form_table.objects.filter(id=id).update(
                library_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "guidance_office_signature":
            clearance_form_table.objects.filter(id=id).update(
                guidance_office_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "osa_signature":
            clearance_form_table.objects.filter(id=id).update(
                osa_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "academic_affairs_signature":
            clearance_form_table.objects.filter(id=id).update(
                academic_affairs_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "course_adviser_signature":
            clearance_form_table.objects.filter(id=id).update(
                course_adviser_signature=signature_saved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)

        # DETECT IF SIGNATURES ARE COMPLETE, UPDATE APPROVAL STATUS
        approved_text = "_APPROVED"
        approval_status_checker = clearance_form_table.objects.filter(
            Q(liberal_arts_signature__contains=approved_text) &
            Q(accountant_signature__contains=approved_text) &
            Q(mathsci_dept_signature__contains=approved_text) &
            Q(pe_dept_signature__contains=approved_text) &
            Q(ieduc_dept_signature__contains=approved_text) &
            Q(it_dept_signature__contains=approved_text) &
            Q(eng_dept_signature__contains=approved_text) &
            Q(library_signature__contains=approved_text) &
            Q(guidance_office_signature__contains=approved_text) &
            Q(osa_signature__contains=approved_text) &
            Q(academic_affairs_signature__contains=approved_text) &
            Q(course_adviser_signature__contains=approved_text), id=id)
        if approval_status_checker:
            clearance_form_table.objects.filter(
                id=id).update(approval_status="APPROVED")
            name = name_temp[0]
            requested = clearance_form_table.objects.filter(name=name).order_by(
                '-time_requested').values_list('purpose_of_request', flat=True).distinct()
            request_form_table.objects.filter(
                name=name, request=requested[0]).update(clearance="✔")

        messages.success(request, "Form Approved.")
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return redirect(faculty_dashboard_clearance_list)

# APPROVE ALL FORMS IN GRADUATION LIST
@login_required(login_url='/')
def faculty_dashboard_graduation_list_all(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if request.method == "POST":
            # GET ALL ID'S AND PUT IN A LIST
            id_list = []
            sig = ""
            if request.method == "POST":
                sig = request.POST.get('sig')
                ilist = request.POST.get('id_list')
                templist = request.POST.get('id_list')
                ilist = templist.split(',')
                for i in ilist:
                    id_list.append(i)
                comma = ","
                while (comma in id_list):
                    id_list.remove(comma)

            print("idlist:", id_list)
            for i in id_list:
                name_temp = graduation_form_table.objects.filter(
                    id=int(i)).values_list('name', flat=True).distinct()
                email_temp = graduation_form_table.objects.filter(
                    id=int(i)).values_list('student_id', flat=True).distinct()
                email = user_table.objects.filter(
                    student_id=email_temp[0]).values_list('email', flat=True).distinct()

                # rec_email = email[0]
                # print("new rec_email:", email[0])
                f_n1 = request.user.full_name + '_UNAPPROVED'
                
                # SIGNATURE COUNTER FOR GRADUATION FORM
                approval = request.user.full_name + "_APPROVED"
                c1 = graduation_form_table.objects.filter(
                    id=int(i), signature1__contains="NO_APPROVED").count()
                c2 = graduation_form_table.objects.filter(
                    id=int(i), signature2__contains="NO_APPROVED").count()
                c3 = graduation_form_table.objects.filter(
                    id=int(i), signature3__contains="NO_APPROVED").count()
                c4 = graduation_form_table.objects.filter(
                    id=int(i), signature4__contains="NO_APPROVED").count()
                c5 = graduation_form_table.objects.filter(
                    id=int(i), signature5__contains="NO_APPROVED").count()
                c6 = graduation_form_table.objects.filter(
                    id=int(i), signature6__contains="NO_APPROVED").count()
                c7 = graduation_form_table.objects.filter(
                    id=int(i), signature7__contains="NO_APPROVED").count()
                c8 = graduation_form_table.objects.filter(
                    id=int(i), signature8__contains="NO_APPROVED").count()
                c9 = graduation_form_table.objects.filter(
                    id=int(i), signature9__contains="NO_APPROVED").count()
                c10 = graduation_form_table.objects.filter(
                    id=int(i), signature10__contains="NO_APPROVED").count()
                ac1 = graduation_form_table.objects.filter(
                    id=int(i), addsignature1__contains="NO_APPROVED").count()
                ac2 = graduation_form_table.objects.filter(
                    id=int(i), addsignature2__contains="NO_APPROVED").count()
                ac3 = graduation_form_table.objects.filter(
                    id=int(i), addsignature3__contains="NO_APPROVED").count()
                ac4 = graduation_form_table.objects.filter(
                    id=int(i), addsignature4__contains="NO_APPROVED").count()
                ac5 = graduation_form_table.objects.filter(
                    id=int(i), addsignature5__contains="NO_APPROVED").count()
                sc1 = graduation_form_table.objects.filter(
                    id=int(i), sitsignature__contains="NO_APPROVED").count()

                signature_saved = request.user.full_name + "_APPROVED" + " " + sig
                f_n = request.user.full_name
                
                # FOR SIT INSTRUCTOR
                if graduation_form_table.objects.filter(
                        sitsignature__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(sitsignature=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 1
                if graduation_form_table.objects.filter(
                        signature1__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature1=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 2
                if graduation_form_table.objects.filter(
                        signature2__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature2=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 3
                if graduation_form_table.objects.filter(
                        signature3__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature3=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 4
                if graduation_form_table.objects.filter(
                        signature4__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature4=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                # FOR FACULTY 5
                if graduation_form_table.objects.filter(
                        signature5__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature5=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 6
                if graduation_form_table.objects.filter(
                        signature6__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature6=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 7
                if graduation_form_table.objects.filter(
                        signature7__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature7=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR FACULTY 8
                if graduation_form_table.objects.filter(
                        signature8__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature8=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                # FOR FACULTY 9
                if graduation_form_table.objects.filter(
                        signature9__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature9=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                # FOR FACULTY 10
                if graduation_form_table.objects.filter(
                        signature10__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature10=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR ADD SUBJECT FACULTY 1 
                if graduation_form_table.objects.filter(
                        addsignature1__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature1=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR ADD SUBJECT FACULTY 2
                if graduation_form_table.objects.filter(
                        addsignature2__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature2=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR ADD SUBJECT FACULTY 3
                if graduation_form_table.objects.filter(
                        addsignature3__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature3=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR ADD SUBJECT FACULTY 4
                if graduation_form_table.objects.filter(
                        addsignature4__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature4=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                # FOR ADD SUBJECT FACULTY 5
                if graduation_form_table.objects.filter(
                        addsignature5__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature5=signature_saved)

                    total = 0
                    final_count = [c1, c2, c3, c4, c5, c6, c7,
                                   c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
                    for a in final_count:
                        total += a
                    denominator = 16 - int(total)
                    cursor = connection.cursor()
                    query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val = (int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum = row[0]
                    print('rownum', rownum)
                    if len(rownum) < 5:
                        temp = rownum[0]
                        print(temp, "this 1")
                    else:
                        rownum1 = rownum[0]
                        rownum2 = rownum[1]
                        full_num = rownum1[0], rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2", temp)

                    app_status = int(temp)
                    numerator = app_status + 1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                name_temp = graduation_form_table.objects.filter(
                    id=int(i)).values_list('name', flat=True).distinct()
                email_temp = graduation_form_table.objects.filter(
                    id=int(i)).values_list('student_id', flat=True).distinct()
                email = user_table.objects.filter(
                    student_id=email_temp[0]).values_list('email', flat=True).distinct()

                rec_email = email[0]
                print(rec_email)
                f_n_unapproved = request.user.full_name + '_UNAPPROVED'
                f_n_approved = request.user.full_name + "_APPROVED"

                messages.success(request, "Subject Approved.")

                # DETECT IF SIGNATURES ARE COMPLETE, CHANGE APPROVAL STATUS
                approval_status_checker_2 = graduation_form_table.objects.filter(id=int(i),
                                                                                 signature1__contains='_APPROVED',
                                                                                 signature2__contains='_APPROVED',
                                                                                 signature3__contains='_APPROVED',
                                                                                 signature4__contains='_APPROVED',
                                                                                 signature5__contains='_APPROVED',
                                                                                 signature6__contains='_APPROVED',
                                                                                 signature7__contains='_APPROVED',
                                                                                 signature8__contains='_APPROVED',
                                                                                 signature9__contains='_APPROVED',
                                                                                 signature10__contains='_APPROVED',
                                                                                 addsignature1__contains='_APPROVED',
                                                                                 addsignature2__contains='_APPROVED',
                                                                                 addsignature3__contains='_APPROVED',
                                                                                 addsignature4__contains='_APPROVED',
                                                                                 addsignature5__contains='_APPROVED',
                                                                                 sitsignature__contains='_APPROVED')

                if approval_status_checker_2:
                    print(approval_status_checker_2)
                    graduation_form_table.objects.filter(
                        id=int(i)).update(approval_status="APPROVED")

            return redirect(faculty_dashboard_graduation_list)
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return redirect('faculty_dashboard_graduation_list')

# DISPLAY FORMS IN GRADUATION LIST DEPENDING ON SUBJECTS
@login_required(login_url='/')
def faculty_dashboard_graduation_list(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        # signature
        esignature = request.user.e_signature
        esignature_datetime = request.user.e_signature_timesaved
        uploaded_signature = request.user.uploaded_signature
        uploaded_signature_datetime = request.user.uploaded_signature_timesaved
        id_Facultynumber = request.user.id

        full_name = request.user.full_name
        f_n_unapproved = request.user.full_name + "_UNAPPROVED"
        f_n_approved_esign = request.user.full_name + "_APPROVED" + " " + "ESIGN"
        f_n_approved_upload = request.user.full_name + "_APPROVED" + " " + "UPLOAD"
        f_n_approved_approve = request.user.full_name + "_APPROVED" + " " + "APPROVE"
        todayyear = date.today().year

        st = graduation_form_table.objects.filter(Q(faculty1=full_name) | Q(faculty2=full_name) |
                                                  Q(faculty3=full_name) | Q(faculty4=full_name) | Q(faculty5=full_name) | Q(faculty6=full_name) |
                                                  Q(faculty7=full_name) | Q(faculty8=full_name) | Q(faculty9=full_name) | Q(faculty10=full_name) |
                                                  Q(addfaculty1=full_name) | Q(addfaculty2=full_name) | Q(addfaculty3=full_name) | Q(addfaculty4=full_name) |
                                                  Q(addfaculty5=full_name) | Q(instructor_name=full_name), Q(time_requested__startswith=todayyear)).order_by('-time_requested')

        # signature checker
        esign_check = user_table.objects.filter(
            full_name=full_name).values_list('e_signature', flat=True).distinct()
        uploadsig_check = user_table.objects.filter(full_name=full_name).values_list(
            'uploaded_signature', flat=True).distinct()
        if esign_check:
            esign_checker = esign_check[0]
        else:
            esign_checker = ""

        if uploadsig_check:
            upload_checker = uploadsig_check[0]
        else:
            upload_checker = ""

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.3Faculty Graduation List.html', {'st': st, 'f_n_unapproved': f_n_unapproved, 'f_n_approved_esign': f_n_approved_esign, 'f_n_approved_upload': f_n_approved_upload, 'f_n_approved_approved': f_n_approved_approve, 'e_signature': esignature, 'esignature_datetime': esignature_datetime, 'esign_check': esign_checker, 'uploaded_signature': uploaded_signature, 'uploadsig_check': upload_checker, 'uploaded_datetime': uploaded_signature_datetime, 'id': id_Facultynumber})

# SINGLE APPROVAL IN GRADUATION LIST
@login_required(login_url='/')
def update_graduation(request, id, sub, sig):
    print("starts here")
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print(sub)
        name_temp = graduation_form_table.objects.filter(
            id=id).values_list('name', flat=True).distinct()
        email_temp = graduation_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            student_id=email_temp[0]).values_list('email', flat=True).distinct()

        rec_email = email[0]
        print(rec_email)
        f_n_unapproved = request.user.full_name + '_UNAPPROVED'
        f_n_approved = request.user.full_name + "_APPROVED"
        signature_saved = request.user.full_name + "_APPROVED" + " " + sig

        # SIGNATURE COUNTER
        c1 = graduation_form_table.objects.filter(
            id=id, signature1__contains="NO_APPROVED").count()
        c2 = graduation_form_table.objects.filter(
            id=id, signature2__contains="NO_APPROVED").count()
        c3 = graduation_form_table.objects.filter(
            id=id, signature3__contains="NO_APPROVED").count()
        c4 = graduation_form_table.objects.filter(
            id=id, signature4__contains="NO_APPROVED").count()
        c5 = graduation_form_table.objects.filter(
            id=id, signature5__contains="NO_APPROVED").count()
        c6 = graduation_form_table.objects.filter(
            id=id, signature6__contains="NO_APPROVED").count()
        c7 = graduation_form_table.objects.filter(
            id=id, signature7__contains="NO_APPROVED").count()
        c8 = graduation_form_table.objects.filter(
            id=id, signature8__contains="NO_APPROVED").count()
        c9 = graduation_form_table.objects.filter(
            id=id, signature9__contains="NO_APPROVED").count()
        c10 = graduation_form_table.objects.filter(
            id=id, signature10__contains="NO_APPROVED").count()
        ac1 = graduation_form_table.objects.filter(
            id=id, addsignature1__contains="NO_APPROVED").count()
        ac2 = graduation_form_table.objects.filter(
            id=id, addsignature2__contains="NO_APPROVED").count()
        ac3 = graduation_form_table.objects.filter(
            id=id, addsignature3__contains="NO_APPROVED").count()
        ac4 = graduation_form_table.objects.filter(
            id=id, addsignature4__contains="NO_APPROVED").count()
        ac5 = graduation_form_table.objects.filter(
            id=id, addsignature5__contains="NO_APPROVED").count()
        sc1 = graduation_form_table.objects.filter(
            id=id, sitsignature__contains="NO_APPROVED").count()

        final_count = [c1, c2, c3, c4, c5, c6, c7,
                       c8, c9, c10, ac1, ac2, ac3, ac4, ac5, sc1]
        total = 0
        for i in final_count:
            total += i
        denominator = 16 - int(total)
        cursor = connection.cursor()
        query = "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
        val = (id,)
        cursor.execute(query, val)

        row = cursor.fetchone()
        rownum = row[0]
        print('rownum', rownum)
        if len(rownum) < 5:
            temp = rownum[0]
            print(temp, "this 1")
        else:
            rownum1 = rownum[0]
            rownum2 = rownum[1]
            full_num = rownum1[0], rownum2[0]
            temp = full_num[0] + full_num[1]
            print("this 2", temp)

        app_status = int(temp)
        numerator = app_status + 1
        adder = str(numerator) + "/" + str(denominator)

        if sub == "signature1":
            graduation_form_table.objects.filter(id=id).update(
                signature1=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)

        if sub == "signature2":
            graduation_form_table.objects.filter(id=id).update(
                signature2=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature3":
            graduation_form_table.objects.filter(id=id).update(
                signature3=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature4":
            graduation_form_table.objects.filter(id=id).update(
                signature4=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature5":
            graduation_form_table.objects.filter(id=id).update(
                signature5=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature6":
            graduation_form_table.objects.filter(id=id).update(
                signature6=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature7":
            graduation_form_table.objects.filter(id=id).update(
                signature7=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature8":
            graduation_form_table.objects.filter(id=id).update(
                signature8=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature9":
            graduation_form_table.objects.filter(id=id).update(
                signature9=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "signature10":
            graduation_form_table.objects.filter(id=id).update(
                signature10=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "addsignature1":
            graduation_form_table.objects.filter(id=id).update(
                addsignature1=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "addsignature2":
            graduation_form_table.objects.filter(id=id).update(
                addsignature2=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "addsignature3":
            graduation_form_table.objects.filter(id=id).update(
                addsignature3=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "addsignature4":
            graduation_form_table.objects.filter(id=id).update(
                addsignature4=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "addsignature5":
            graduation_form_table.objects.filter(id=id).update(
                addsignature5=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sub == "sitsignature":
            graduation_form_table.objects.filter(id=id).update(
                sitsignature=signature_saved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)

        messages.success(request, "Subject Approved.")

        # DETECT IF SIGNATURES ARE COMPLETE, CHANGE APPROVAL STATUS
        approval_status_checker_2 = graduation_form_table.objects.filter(id=id,
                                                                         signature1__contains='_APPROVED',
                                                                         signature2__contains='_APPROVED',
                                                                         signature3__contains='_APPROVED',
                                                                         signature4__contains='_APPROVED',
                                                                         signature5__contains='_APPROVED',
                                                                         signature6__contains='_APPROVED',
                                                                         signature7__contains='_APPROVED',
                                                                         signature8__contains='_APPROVED',
                                                                         signature9__contains='_APPROVED',
                                                                         signature10__contains='_APPROVED',
                                                                         addsignature1__contains='_APPROVED',
                                                                         addsignature2__contains='_APPROVED',
                                                                         addsignature3__contains='_APPROVED',
                                                                         addsignature4__contains='_APPROVED',
                                                                         addsignature5__contains='_APPROVED',
                                                                         sitsignature__contains='_APPROVED')

        if approval_status_checker_2:
            print(approval_status_checker_2)
            graduation_form_table.objects.filter(
                id=id).update(approval_status="APPROVED")

        return redirect(faculty_dashboard_graduation_list)

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

# REGISTRAR DASHBOARD
@login_required(login_url='/')
def registrar_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        gradtable = graduation_form_table.objects.all()
        cleartable = clearance_form_table.objects.all()

        # CLEARANCE FORMS
        all = clearance_form_table.objects.all()
        cBSIE_ICT = clearance_form_table.objects.filter(
            course="BSIE-Information and Communication Technology").values().count()
        cBSIE_IA = clearance_form_table.objects.filter(
            course="BSIE-Industrial Arts").values().count()
        cBGT_ART = clearance_form_table.objects.filter(
            course="BGT-Architecture Technology").values().count()
        cBET_CT = clearance_form_table.objects.filter(
            course="BET-Civil Technology").values().count()
        cBET_ET = clearance_form_table.objects.filter(
            course="BET-Electrical Technology").values().count()
        cBET_EsET = clearance_form_table.objects.filter(
            course="BET-Electronics Engineering Technology").values().count()
        cBET_CoET = clearance_form_table.objects.filter(
            course="BET-Computer Engineering Technology").values().count()
        cBET_MT = clearance_form_table.objects.filter(
            course="BET-Mechanical & Production Engineering Technology").values().count()
        cBET_PPT = clearance_form_table.objects.filter(
            course="BET-Power Plant Engineering Technology").values().count()
        cBT_CET = clearance_form_table.objects.filter(
            course="BT-Civil Engineering Technology").values().count()
        cBT_CoET = clearance_form_table.objects.filter(
            course="BT-Computer Engineering Technology").values().count()
        cBT_EET = clearance_form_table.objects.filter(
            course="BT-Electrical Engineering Technology").values().count()
        cBT_EsET = clearance_form_table.objects.filter(
            course="BT-Electronics Engineering Technology").values().count()
        cBT_MPET = clearance_form_table.objects.filter(
            course="BT-Mechanical & Production Engineering Technology").values().count()
        cBT_PPET = clearance_form_table.objects.filter(
            course="BT-Powerplant Engineering Technology").values().count()
        c_MPET = clearance_form_table.objects.filter(
            course="Mechanical & Production Engineering Technology").values().count()
        c_PPET = clearance_form_table.objects.filter(
            course="Powerplant Engineering Technology").values().count()
        cBSIE_AET = clearance_form_table.objects.filter(
            course="BSIE-Automotive Engineering Technology").values().count()
        cBSIE_MPET = clearance_form_table.objects.filter(
            course="BSIE-Mechanical & Production Engineering Technology").values().count()
        cBTTE_ART = clearance_form_table.objects.filter(
            course="BTTE-Architecture Technology").values().count()
        cBTTE_AET = clearance_form_table.objects.filter(
            course="BTTE-Automotive Engineering Technology").values().count()
        cBTTE_CET = clearance_form_table.objects.filter(
            course="BTTE-Civil Engineering Technology").values().count()
        cBTTE_CoET = clearance_form_table.objects.filter(
            course="BTTE-Computer Engineering Technology").values().count()
        cBTTE_EET = clearance_form_table.objects.filter(
            course="BTTE-Electrical Engineering Technology").values().count()
        cBTTE_EsET = clearance_form_table.objects.filter(
            course="BTTE-Electronics Engineering Technology").values().count()
        cBTTE_MPET = clearance_form_table.objects.filter(
            course="BTTE-Mechanical & Production Engineering Technology").values().count()
        cBTTE_PPET = clearance_form_table.objects.filter(
            course="BTTE-Powerplant Engineering Technology").values().count()
        cBT_AET = clearance_form_table.objects.filter(
            course="BT-Automotive Engineering Technology").values().count()

        cBET_CT = clearance_form_table.objects.filter(
            course="BET-Construction Technology").values().count()
        cBET_MT = clearance_form_table.objects.filter(
            course="BET-Mechanical Technology").values().count()
        cBET_AT = clearance_form_table.objects.filter(
            course="BET-Automotive Technology").values().count()
        cBET_PPT = clearance_form_table.objects.filter(
            course="BET-Power Plant Technology").values().count()
        cBSIE_HE = clearance_form_table.objects.filter(
            course="BSIE-Home Economics").values().count()
        cBTTE_CP = clearance_form_table.objects.filter(
            course="BTTE-Computer Programming").values().count()
        cBTTE_E = clearance_form_table.objects.filter(
            course="BTTE-Electrical").values().count()
        cBSCE = clearance_form_table.objects.filter(
            course="BS-Civil Engineering").values().count()
        cBSEE = clearance_form_table.objects.filter(
            course="BS-Electrical Engineering").values().count()
        cBSME = clearance_form_table.objects.filter(
            course="BS-Mechanical Engineering").values().count()

        unapproved_forms_count = clearance_form_table.objects.filter(
            approval_status="APPROVED").count()
        clearance_count = all.count() - unapproved_forms_count
        if clearance_count == 0:
            clearance_badge = ""
        else:
            clearance_badge = clearance_count

        # GRADUATION FORMS
        gBSIE_ICT = graduation_form_table.objects.filter(
            course="BSIE-Information and Communication Technology").values().count()
        gBSIE_IA = graduation_form_table.objects.filter(
            course="BSIE-Industrial Arts").values().count()
        gBGT_ART = graduation_form_table.objects.filter(
            course="BGT-Architecture Technology").values().count()
        gBET_CT = graduation_form_table.objects.filter(
            course="BET-Civil Engineering Technology").values().count()
        gBET_ET = graduation_form_table.objects.filter(
            course="BET-Electrical Technology").values().count()
        gBET_EsET = graduation_form_table.objects.filter(
            course="BET-Electronics Engineering Technology").values().count()
        gBET_CoET = graduation_form_table.objects.filter(
            course="BET-Computer Engineering Technology").values().count()
        gBET_MT = graduation_form_table.objects.filter(
            course="BET-Mechanical & Production Engineering Technology").values().count()
        gBET_PPT = graduation_form_table.objects.filter(
            course="BET-Power Plant Engineering Technology").values().count()
        gBT_CET = graduation_form_table.objects.filter(
            course="BT-Civil Engineering Technology").values().count()
        gBT_CoET = graduation_form_table.objects.filter(
            course="BT-Computer Engineering Technology").values().count()
        gBT_EET = graduation_form_table.objects.filter(
            course="BT-Electrical Engineering Technology").values().count()
        gBT_EsET = graduation_form_table.objects.filter(
            course="BT-Electronics Engineering Technology").values().count()
        gBT_MPET = graduation_form_table.objects.filter(
            course="BT-Mechanical & Production Engineering Technology").values().count()
        gBT_PPET = graduation_form_table.objects.filter(
            course="BT-Powerplant Engineering Technology").values().count()
        g_MPET = graduation_form_table.objects.filter(
            course="Mechanical & Production Engineering Technology").values().count()
        g_PPET = graduation_form_table.objects.filter(
            course="Powerplant Engineering Technology").values().count()
        gBSIE_AET = graduation_form_table.objects.filter(
            course="BSIE-Automotive Engineering Technology").values().count()
        gBSIE_MPET = graduation_form_table.objects.filter(
            course="BSIE-Mechanical & Production Engineering Technology").values().count()
        gBTTE_ART = graduation_form_table.objects.filter(
            course="BTTE-Architecture Technology").values().count()
        gBTTE_AET = graduation_form_table.objects.filter(
            course="BTTE-Automotive Engineering Technology").values().count()
        gBTTE_CET = graduation_form_table.objects.filter(
            course="BTTE-Civil Engineering Technology").values().count()
        gBTTE_CoET = graduation_form_table.objects.filter(
            course="BTTE-Computer Engineering Technology").values().count()
        gBTTE_EET = graduation_form_table.objects.filter(
            course="BTTE-Electrical Engineering Technology").values().count()
        gBTTE_EsET = graduation_form_table.objects.filter(
            course="BTTE-Electronics Engineering Technology").values().count()
        gBTTE_MPET = graduation_form_table.objects.filter(
            course="BTTE-Mechanical & Production Engineering Technology").values().count()
        gBTTE_PPET = graduation_form_table.objects.filter(
            course="BTTE-Powerplant Engineering Technology").values().count()
        gBT_AET = graduation_form_table.objects.filter(
            course="BT-Automotive Engineering Technology").values().count()

        gBET_CT = graduation_form_table.objects.filter(
            course="BET-Construction Technology").values().count()
        gBET_MT = graduation_form_table.objects.filter(
            course="BET-Mechanical Technology").values().count()
        gBET_AT = graduation_form_table.objects.filter(
            course="BET-Automotive Technology").values().count()
        gBET_PPT = graduation_form_table.objects.filter(
            course="BET-Power Plant Technology").values().count()
        gBSIE_HE = graduation_form_table.objects.filter(
            course="BSIE-Home Economics").values().count()
        gBTTE_CP = graduation_form_table.objects.filter(
            course="BTTE-Computer Programming").values().count()
        gBTTE_E = graduation_form_table.objects.filter(
            course="BTTE-Electrical").values().count()
        gBSCE = graduation_form_table.objects.filter(
            course="BS-Civil Engineering").values().count()
        gBSEE = graduation_form_table.objects.filter(
            course="BS-Electrical Engineering").values().count()
        gBSME = graduation_form_table.objects.filter(
            course="BS-Mechanical Engineering").values().count()

        unapproved_forms_count2 = graduation_form_table.objects.filter(
            approval_status="APPROVED").count()
        graduation_count = graduation_form_table.objects.all().count() - \
            unapproved_forms_count2
        if graduation_count == 0:
            graduation_badge = ""
        else:
            graduation_badge = graduation_count

        unapproved_forms_count3 = request_form_table.objects.filter(
            claim="CLAIMED").count()
        request_count = request_form_table.objects.all().count() - \
            unapproved_forms_count3
        if request_count == 0:
            request_badge = ""
        else:
            request_badge = request_count

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/7.1Registrar Dashboard.html',
                  {'all': all, 'cBSIE_ICT': cBSIE_ICT, 'cBSIE_IA': cBSIE_IA, 'cBGT_ART': cBGT_ART, 'cBET_CT': cBET_CT,
                   'cBET_ET': cBET_ET, 'cBET_EsET': cBET_EsET, 'cBET_CoET': cBET_CoET, 'cBET_MT': cBET_MT,
                   'cBET_PPT': cBET_PPT, 'cBT_CET': cBT_CET, 'cBT_CoET': cBT_CoET, 'cBT_EET': cBT_EET,
                   'cBT_EsET': cBT_EsET, 'cBT_MPET': cBT_MPET, 'cBT_PPET': cBT_PPET, 'c_MPET': c_MPET,
                   'c_PPET': c_PPET, 'cBSIE_AET': cBSIE_AET, 'cBSIE_MPET': cBSIE_MPET, 'cBTTE_ART': cBTTE_ART,
                   'cBTTE_AET': cBTTE_AET, 'cBTTE_CET': cBTTE_CET, 'cBTTE_CoET': cBTTE_CoET, 'cBTTE_EET': cBTTE_EET,
                   'cBTTE_EsET': cBTTE_EsET, 'cBTTE_MPET': cBTTE_MPET, 'cBTTE_PPET': cBTTE_PPET, 'cBT_AET': cBT_AET,

                   'cBET_CT': cBET_CT, 'cBET_MT': cBET_MT, 'cBET_AT': cBET_AT, 'cBET_PPT': cBET_PPT,
                   'cBSIE_HE': cBSIE_HE, 'cBTTE_CP': cBTTE_CP, 'cBTTE_E': cBTTE_E, 'cBSCE': cBSCE,
                   'cBSEE': cBSEE, 'cBSME': cBSME,

                   'gBSIE_ICT': gBSIE_ICT, 'gBSIE_IA': gBSIE_IA, 'gBGT_ART': gBGT_ART, 'gBET_CT': gBET_CT,
                   'gBET_ET': gBET_ET, 'gBET_EsET': gBET_EsET, 'gBET_CoET': gBET_CoET, 'gBET_MT': gBET_MT,
                   'gBET_PPT': gBET_PPT, 'gBT_CET': gBT_CET, 'gBT_CoET': gBT_CoET, 'gBT_EET': gBT_EET,
                   'gBT_EsET': gBT_EsET, 'gBT_MPET': gBT_MPET, 'gBT_PPET': gBT_PPET, 'g_MPET': g_MPET,
                   'g_PPET': g_PPET, 'gBSIE_AET': gBSIE_AET, 'gBSIE_MPET': gBSIE_MPET, 'gBTTE_ART': gBTTE_ART,
                   'gBTTE_AET': gBTTE_AET, 'gBTTE_CET': gBTTE_CET, 'gBTTE_CoET': gBTTE_CoET, 'gBTTE_EET': gBTTE_EET,
                   'gBTTE_EsET': gBTTE_EsET, 'gBTTE_MPET': gBTTE_MPET, 'gBTTE_PPET': gBTTE_PPET, 'gBT_AET': gBT_AET,
                   'gBET_CT': gBET_CT, 'gBET_MT': gBET_MT, 'gBET_AT': gBET_AT, 'gBET_PPT': gBET_PPT,
                   'gBSIE_HE': gBSIE_HE, 'gBTTE_CP': gBTTE_CP, 'gBTTE_E': gBTTE_E, 'gBSCE': gBSCE,
                   'gBSEE': gBSEE, 'gBSME': gBSME, 'clearance_badge': clearance_badge, 'graduation_badge': graduation_badge, 'request_badge': request_badge,
                   'gradtable': gradtable, 'cleartable': cleartable})


@login_required(login_url='/')
def name_list(request):
    enteruser = request.POST.get('validator')
    to_edit = request.POST.get('validator')
    p = user_table.objects.filter(student_id=enteruser).values_list(
        to_edit, flat=True).distinct()
    va = p[0]
# UPDATE PASSWORD OF STUDENT USER
@login_required(login_url='/')
def updatePassword(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT":
        if request.method == "POST":
            new_password = request.POST.get('new_pass_041')
            confirm_password = request.POST.get('confirm_pass_041')

            if new_password == confirm_password:
                print("same")
                v = request.POST.get('validator2')
                u = user_table.objects.get(student_id__exact=v)

                u.set_password(new_password)
                u.save()
                messages.success(
                    request, 'You have successfully changed your password. Please log in again.')
                return redirect('/')

            else:
                messages.success(
                    request, 'New and Confirm Password does not match. ')
                return redirect('/student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.1Student Dashboard.html')

# UPDATE PASSWORD OF FACULTY USER
@login_required(login_url='/')
def faculty_updatePassword(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print('here')
        if request.method == "POST":
            new_password = request.POST.get('new_pass_051')
            confirm_password = request.POST.get('confirm_pass_051')

            if new_password == confirm_password:
                print("same")
                v = request.POST.get('validator2')
                u = user_table.objects.get(student_id__exact=v)

                u.set_password(new_password)
                u.save()
                messages.success(
                    request, 'You have successfully changed your password. Please log in again.')
                return redirect('/')

            else:
                messages.success(
                    request, 'New and Confirm Password does not match. ')
                return redirect('/faculty_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.1Faculty Dashboard.html')

# UPDATE NAME OF REGISTRAR
@login_required(login_url='/')
def reg_updateName(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            relast_name = request.POST.get('ln_box_071')
            refirst_name = request.POST.get('fn_box_071')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                last_name=relast_name, first_name=refirst_name,)
            return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# UPDATE ADDRESS OF REGISTRAR
@login_required(login_url='/')
def reg_updateAddress(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            readdress = request.POST.get('address_box_071')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(address=readdress)
            return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# UPDATE EMAIL OF REGISTRAR
@login_required(login_url='/')
def reg_updateEmail(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            reemail = request.POST.get('ea_box_071')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(email=reemail)
            return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# UPDATE PASSWORD OF REGISTRAR
@login_required(login_url='/')
def reg_updatePassword(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            new_password = request.POST.get('new_pass_071')
            confirm_password = request.POST.get('confirm_pass_071')

            if new_password == confirm_password:
                print("same")
                v = request.POST.get('validator2')
                u = user_table.objects.get(student_id__exact=v)

                u.set_password(new_password)
                u.save()
                messages.success(
                    request, 'You have successfully changed your password. Please log in again.')
                return redirect('/')

            else:
                messages.success(
                    request, 'New and Confirm Password does not match. ')
                return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# UPDATE PASSWORD OF STAFF
def staff_updatePassword(request):
    if request.user.is_authenticated and request.user.user_type == "STAFF":
        print('here')
        if request.method == "POST":
            new_password = request.POST.get('new_pass_071')
            confirm_password = request.POST.get('confirm_pass_071')

            if new_password == confirm_password:
                print("same")
                v = request.POST.get('validator2')
                u = user_table.objects.get(student_id__exact=v)

                u.set_password(new_password)
                u.save()
                messages.success(
                    request, 'You have successfully changed your password. Please log in again.')
                return redirect('/')

            else:
                messages.success(
                    request, 'New and Confirm Password does not match. ')
                return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# UPDATE CONTACT NUMBER OF REGISTRAR
@login_required(login_url='/')
def reg_updateContact(request):

    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            recontact = request.POST.get('cnum_box_071')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                contact_number=recontact)
            return redirect('/registrar_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    print('running')
    return render(request, 'html_files/7.1Registrar Dashboard.html')

# CLEARANCE FORM DISPLAY
@login_required(login_url='/')
def display_clearform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT" or request.user.user_type == "FACULTY" or request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        clearance = clearance_form_table.objects.filter(id=id).values()
        others_data = clearance_form_table.objects.filter(
            id=id).values_list('purpose_of_request', flat=True).distinct()

        if others_data:
            o_data = others_data[0]
            if o_data.__contains__("Others"):
                requested = "Others"
                others = others_data[0]
            else:
                requested = ""
                others = ""
        else:
            others = ""
            requested = ""

        # Signature Display
        # ACCOUNTANT
        check_status = clearance_form_table.objects.filter(
            id=id, accountant_signature__icontains='UNAPPROVED')
        if check_status:
            accountant = "UNAPPROVED"
            accountant_name = " "
            signature_type1 = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('accountant_signature', flat=True).distinct()
            acc_sig = str(faculty_approved[0])
            fac_name_get = acc_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    account_sig = up_sig[0]
                else:
                    account_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                accountant = account_sig
                accountant_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type1 = "ESIGN"

            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                accountant = ""
                accountant_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type1 = "REG"
            else:
                account_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                accountant = account_sig[0]
                accountant_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type1 = "APPROVE"

        # COURSE ADVISER
        check_status = clearance_form_table.objects.filter(
            id=id, course_adviser_signature__icontains='UNAPPROVED')
        if check_status:
            course_adviser = "UNAPPROVED"
            adviser_name = " "
            signature_type2 = ""
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('course_adviser_signature', flat=True).distinct()
            adviser_sig = str(faculty_approved[0])
            fac_name_get = adviser_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                print("esign laman",e_sig)
                print("upload laman",up_sig)
                if e_sig[0] == "" :
                    ca_sig = up_sig[0]
                else:
                    ca_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                course_adviser = ca_sig
                adviser_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type2 = "ESIGN"

            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                course_adviser = ""
                adviser_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type2 = "REG"
            else:
                ca_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                course_adviser = ca_sig[0]
                adviser_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type2 = "APPROVE"

        # LIBERAL ARTS
        check_status = clearance_form_table.objects.filter(
            id=id, liberal_arts_signature__icontains='UNAPPROVED')
        if check_status:
            liberal_arts = "UNAPPROVED"
            liberal_artsName = " "
            signature_type3 = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('liberal_arts_signature', flat=True).distinct()
            lib_sig = str(faculty_approved[0])
            fac_name_get = lib_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    libart_sig = up_sig[0]
                else:
                    libart_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                liberal_arts = libart_sig
                liberal_artsName = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type3 = "ESIGN"
                
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                liberal_arts = ""
                liberal_artsName = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type3 = "REG"
            else:
                libart_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                liberal_arts = libart_sig[0]
                liberal_artsName = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type3 = "APPROVE"

        # CAMPUS LIBRARIAN
        check_status = clearance_form_table.objects.filter(
            id=id, library_signature__icontains='UNAPPROVED')
        if check_status:
            campus_library = "UNAPPROVED"
            librarian_name = " "
            signature_type4 = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('library_signature', flat=True).distinct()
            camlib_sig = str(faculty_approved[0])
            fac_name_get = camlib_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    cam_lib_sig = up_sig[0]
                else:
                    cam_lib_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                campus_library = cam_lib_sig
                librarian_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type4 = "ESIGN"
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                campus_library = ""
                librarian_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type4 = "REG"
            else:
                cam_lib_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                campus_library = cam_lib_sig[0]
                librarian_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type4 = "APPROVE"

        #MATH & SCIENCES
        check_status = clearance_form_table.objects.filter(
            id=id, mathsci_dept_signature__icontains='UNAPPROVED')
        if check_status:
            math_and_science = "UNAPPROVED"
            math_and_science_name = " "
            signature_type5 = ""
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('mathsci_dept_signature', flat=True).distinct()
            mas_sig = str(faculty_approved[0])
            fac_name_get = mas_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    mathsci_sig = up_sig[0]
                else:
                    mathsci_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                math_and_science = mathsci_sig
                math_and_science_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type5 = "ESIGN"
            
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                math_and_science = ""
                math_and_science_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type5 = "REG"
            else:
                mathsci_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                math_and_science = mathsci_sig[0]
                math_and_science_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type5 = "APPROVE"

        # GUIDANCE COUNCELOR
        check_status = clearance_form_table.objects.filter(
            id=id, guidance_office_signature__icontains='UNAPPROVED')
        if check_status:
            guidance = "UNAPPROVED"
            guidance_councelor = " "
            signature_type6 = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('guidance_office_signature', flat=True).distinct()
            guid_sig = str(faculty_approved[0])
            fac_name_get = guid_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    gui_sig = up_sig[0]
                else:
                    gui_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                guidance = gui_sig
                guidance_councelor = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type6 = "ESIGN"
           
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                guidance = ""
                guidance_councelor = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type6 = "REG"
            else:
                gui_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                guidance = gui_sig[0]
                guidance_councelor = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                signature_type6 = "APPROVE"

        # DPECS
        check_status = clearance_form_table.objects.filter(
            id=id, pe_dept_signature__icontains='UNAPPROVED')
        if check_status:
            dpecs = "UNAPPROVED"
            dpecs_name = " "
            signature_type7 = ""
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('pe_dept_signature', flat=True).distinct()
            pe_sig = str(faculty_approved[0])
            fac_name_get = pe_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    pe_dept_sig = up_sig[0]
                else:
                    pe_dept_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                dpecs = pe_dept_sig
                dpecs_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type7 = "ESIGN"
            
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                dpecs = ""
                dpecs_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type7 = "REG"
            else:
                pe_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                dpecs = pe_dept_sig[0]
                dpecs_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type7 = "APPROVE"

        # OSA
        check_status = clearance_form_table.objects.filter(
            id=id, osa_signature__icontains='UNAPPROVED')
        if check_status:
            osa = "UNAPPROVED"
            osa_name = " "
            signature_type8 = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('osa_signature', flat=True).distinct()
            student_osa_sig = str(faculty_approved[0])
            fac_name_get = student_osa_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    student_affairs_sig = up_sig[0]
                else:
                    student_affairs_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                osa = student_affairs_sig
                osa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type8 = "ESIGN"
            
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                osa = ""
                osa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type8 = "REG"
            else:
                student_affairs_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                osa = student_affairs_sig[0]
                osa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type8 = "APPROVE"

        # ADAA
        check_status = clearance_form_table.objects.filter(
            id=id, academic_affairs_signature__icontains='UNAPPROVED')
        if check_status:
            adaa = "UNAPPROVED"
            adaa_name = " "
            signature_type9 = ""
        else:
            faculty_approved = clearance_form_table.objects.filter(
                id=id).values_list('academic_affairs_signature', flat=True).distinct()
            asst_dir_acad_sig = str(faculty_approved[0])
            fac_name_get = asst_dir_acad_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    adaa_sig = up_sig[0]
                else:
                    adaa_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                adaa = adaa_sig
                adaa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type9 = "ESIGN"
           
            elif faculty_approved[0].__contains__('REGISTRAR'):
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                adaa = ""
                adaa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type9 = "REG"
            else:
                adaa_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                    'no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                adaa = adaa_sig[0]
                adaa_name = faculty_firstName[0] + " " + faculty_lastName[0]
                signature_type9 = "APPROVE"

        # INDUSTRIAL
        check_status = clearance_form_table.objects.filter(Q(id=id), Q(ieduc_dept_signature='UNAPPROVED') | Q(
            it_dept_signature='UNAPPROVED') | Q(eng_dept_signature='UNAPPROVED'))
        ded = clearance_form_table.objects.filter(
            id=id, ieduc_dept_signature='_APPROVED')
        doe = clearance_form_table.objects.filter(
            id=id, eng_dept_signature='_APPROVED')
        dit = clearance_form_table.objects.filter(
            id=id, it_dept_signature='_APPROVED')

        if check_status.exists():
            industrial = "UNAPPROVED"
            it_department = "NONE"
            it_name = " "
            signature_type10 = ""
            print(check_status[0])
        else:
            # INDUSTRIAL EDUCATION
            if doe.exists() and dit.exists():
                faculty_approved = clearance_form_table.objects.filter(
                    id=id).values_list('ieduc_dept_signature', flat=True).distinct()
                ieduc = str(faculty_approved[0])
                fac_name_get = ieduc.split('_', 1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)

                if faculty_approved[0].__contains__('ESIGN'):
                    e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                    up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                    if e_sig[0] == "":
                        ieduc_sig = up_sig[0]
                    else:
                        ieduc_sig = e_sig[0]
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = ieduc_sig
                    it_department = "EDUCATOR"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "ESIGN"
                
                elif faculty_approved[0].__contains__('REGISTRAR'):
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = ""
                    it_department = "EDUCATOR"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "REG"
                else:
                    ieduc_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                        'no_signature', flat=True).distinct()
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = ieduc_sig[0]
                    it_department = "EDUCATOR"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "APPROVE"

            # INDUSTRIAL TECHNOLOGY
            if doe.exists() and ded.exists():
                faculty_approved = clearance_form_table.objects.filter(
                    id=id).values_list('it_dept_signature', flat=True).distinct()
                it = str(faculty_approved[0])
                fac_name_get = it.split('_', 1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)

                if faculty_approved[0].__contains__('ESIGN'):
                    e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                    up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                    if e_sig[0] == "":
                        it_dept_sig = up_sig[0]
                    else:
                        it_dept_sig = e_sig[0]
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = it_dept_sig
                    it_department = "TECHNOLOGIES"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "ESIGN"
                
                elif faculty_approved[0].__contains__('REGISTRAR'):
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = ""
                    it_department = "TECHNOLOGIES"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "REG"
                else:
                    it_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list(
                        'no_signature', flat=True).distinct()
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = it_dept_sig[0]
                    it_department = "TECHNOLOGIES"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "APPROVE"

            # ENGINEERING
            if dit.exists() and ded.exists():
                faculty_approved = clearance_form_table.objects.filter(
                    id=id).values_list('eng_dept_signature', flat=True).distinct()
                eng = str(faculty_approved[0])
                fac_name_get = eng.split('_', 1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)

                if faculty_approved[0].__contains__('ESIGN'):
                    e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                    up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                    if e_sig[0] == "":
                        eng_dept_sig = up_sig[0]
                    else:
                        eng_dept_sig = e_sig[0]
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = eng_dept_sig
                    it_department = "ENGINEERS"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "ESIGN"
                
                elif faculty_approved[0].__contains__('REGISTRAR'):
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = ""
                    it_department = "ENGINEERS"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "REG"
                else:
                    eng_dept_sig = user_table.objects.filter(
                        full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                    faculty_firstName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                    faculty_lastName = user_table.objects.filter(
                        full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                    industrial = eng_dept_sig[0]
                    it_department = "ENGINEERS"
                    it_name = faculty_firstName[0] + " " + faculty_lastName[0]
                    signature_type10 = "APPROVE"

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {
        'clearance': clearance,
        'accountant': accountant,
        'liberal_arts': liberal_arts,
        'math_and_science': math_and_science,
        'dpecs': dpecs,
        'industrial': industrial,
        'it_department': it_department,
        'course_adviser': course_adviser,
        'campus_library': campus_library,
        'guidance': guidance,
        'osa': osa,
        'adaa': adaa,
        'accountant_name': accountant_name,
        'adviser_name': adviser_name,
        'liberal_artsName': liberal_artsName,
        'librarian_name': librarian_name,
        'math_and_science_name': math_and_science_name,
        'guidance_councelor': guidance_councelor,
        'dpecs_name': dpecs_name,
        'osa_name': osa_name,
        'adaa_name': adaa_name,
        'it_name': it_name,
        'others': others,
        'requested': requested,
        'signature_type1': signature_type1,
        'signature_type2': signature_type2,
        'signature_type3': signature_type3,
        'signature_type4': signature_type4,
        'signature_type5': signature_type5,
        'signature_type6': signature_type6,
        'signature_type7': signature_type7,
        'signature_type8': signature_type8,
        'signature_type9': signature_type9,
        'signature_type10': signature_type10
    }

    print('running')
    return render(request, 'html_files/clearance_form_display.html', context)

# GRADUATION FORM DISPLAY
@login_required(login_url='/')
def display_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "OLD STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "FACULTY" or request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        graduation = graduation_form_table.objects.filter(id=id).values()

        # SIT
        check_status = graduation_form_table.objects.filter(
            id=id, sitsignature__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, sitsignature='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('instructor_name', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            sit = "UNAPPROVED"
            sit_type = ""
            sit_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            sit = "NONE"
            sit_type = ""
            sit_name = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('sitsignature', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "" :
                    faculty1_sig = up_sig[0]
                else:
                    faculty1_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                sit_name = faculty_firstName[0] + " " + faculty_lastName[0]
                sit = faculty1_sig
                sit_type = "ESIGN"

            else:
                faculty1_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                sit_name = faculty_firstName[0] + " " + faculty_lastName[0]
                sit = faculty1_sig[0]
                sit_type = "APPROVE"

        # SUBJECT #1
        check_status = graduation_form_table.objects.filter(
            id=id, signature1__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature1='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty1', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_1 = "UNAPPROVED"
            signature_type1 = ""
            subject1_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_1 = ""
            signature_type1 = ""
            subject1_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature1', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty1_sig = up_sig[0]
                else:
                    faculty1_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject1_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_1 = faculty1_sig
                signature_type1 = "ESIGN"

            else:
                faculty1_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject1_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_1 = faculty1_sig[0]
                signature_type1 = "APPROVE"

        # SUBJECT #2
        check_status = graduation_form_table.objects.filter(
            id=id, signature2__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature2='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty2', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_2 = "UNAPPROVED"
            signature_type2 = ""
            subject2_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_2 = ""
            signature_type2 = ""
            subject2_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature2', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty2_sig = up_sig[0]
                else:
                    faculty2_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject2_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_2 = faculty2_sig
                signature_type2 = "ESIGN"

            else:
                faculty2_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject2_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_2 = faculty2_sig[0]
                signature_type2 = "APPROVE"

        # SUBJECT #3
        check_status = graduation_form_table.objects.filter(
            id=id, signature3__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature3='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty3', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_3 = "UNAPPROVED"
            signature_type3 = ""
            subject3_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_3 = ""
            signature_type3 = ""
            subject3_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature3', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty3_sig = up_sig[0]
                else:
                    faculty3_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject3_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_3 = faculty3_sig
                signature_type3 = "ESIGN"

            else:
                faculty3_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject3_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_3 = faculty3_sig[0]
                signature_type3 = "APPROVE"

        # SUBJECT #4
        check_status = graduation_form_table.objects.filter(
            id=id, signature4__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature4='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty4', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_4 = "UNAPPROVED"
            signature_type4 = ""
            subject4_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_4 = ""
            signature_type4 = ""
            subject4_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature4', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty4_sig = up_sig[0]
                else:
                    faculty4_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject4_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_4 = faculty4_sig
                signature_type4 = "ESIGN"

            else:
                faculty4_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject4_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_4 = faculty4_sig[0]
                signature_type4 = "APPROVE"

        # SUBJECT #5
        check_status = graduation_form_table.objects.filter(
            id=id, signature5__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature5='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty5', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_5 = "UNAPPROVED"
            signature_type5 = ""
            subject5_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_5 = ""
            signature_type5 = ""
            subject5_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature5', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty5_sig = up_sig[0]
                else:
                    faculty5_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject5_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_5 = faculty5_sig
                signature_type5 = "ESIGN"

            else:
                faculty5_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject5_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_5 = faculty5_sig[0]
                signature_type5 = "APPROVE"

        # SUBJECT #6
        check_status = graduation_form_table.objects.filter(
            id=id, signature6__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature6='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty6', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_6 = "UNAPPROVED"
            signature_type6 = ""
            subject6_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_6 = ""
            signature_type6 = ""
            subject6_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature6', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty6_sig = up_sig[0]
                else:
                    faculty6_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject6_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_6 = faculty6_sig
                signature_type6 = "ESIGN"

            else:
                faculty6_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject6_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_6 = faculty6_sig[0]
                signature_type6 = "APPROVE"

        # SUBJECT #7
        check_status = graduation_form_table.objects.filter(
            id=id, signature7__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature7='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty7', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_7 = "UNAPPROVED"
            signature_type7 = ""
            subject7_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_7 = ""
            signature_type7 = ""
            subject7_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature7', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty7_sig = up_sig[0]
                else:
                    faculty7_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject7_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_7 = faculty7_sig
                signature_type7 = "ESIGN"

            else:
                faculty7_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject7_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_7 = faculty7_sig[0]
                signature_type7 = "APPROVE"

        # SUBJECT #8
        check_status = graduation_form_table.objects.filter(
            id=id, signature8__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature8='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty8', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_8 = "UNAPPROVED"
            signature_type8 = ""
            subject8_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_8 = ""
            signature_type8 = ""
            subject8_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature8', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty8_sig = up_sig[0]
                else:
                    faculty8_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject8_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_8 = faculty8_sig
                signature_type8 = "ESIGN"

            else:
                faculty8_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject8_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_8 = faculty8_sig[0]
                signature_type8 = "APPROVE"

        # SUBJECT #9
        check_status = graduation_form_table.objects.filter(
            id=id, signature9__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature9='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty9', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_9 = "UNAPPROVED"
            signature_type9 = ""
            subject9_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_9 = ""
            signature_type9 = ""
            subject9_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature9', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty9_sig = up_sig[0]
                else:
                    faculty9_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject9_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_9 = faculty9_sig
                signature_type9 = "ESIGN"

            else:
                faculty9_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject9_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_9 = faculty9_sig[0]
                signature_type9 = "APPROVE"

        # SUBJECT #10
        check_status = graduation_form_table.objects.filter(
            id=id, signature10__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, signature10='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('faculty10', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            subject_10 = "UNAPPROVED"
            signature_type10 = ""
            subject10_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            subject_10 = ""
            signature_type10 = ""
            subject10_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('signature10', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    faculty10_sig = up_sig[0]
                else:
                    faculty10_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject10_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_10 = faculty10_sig
                signature_type10 = "ESIGN"

            else:
                faculty10_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                subject10_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                subject_10 = faculty10_sig[0]
                signature_type10 = "APPROVE"

        # ADD SUBJECT #1
        check_status = graduation_form_table.objects.filter(
            id=id, addsignature1__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, addsignature1='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('addfaculty1', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            addsubject_1 = "UNAPPROVED"
            signature_type11 = ""
            addsubject1_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            addsubject_1 = ""
            signature_type11 = ""
            addsubject1_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('addsignature1', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    addfaculty1_sig = up_sig[0]
                else:
                    addfaculty1_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject1_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_1 = addfaculty1_sig
                signature_type11 = "ESIGN"

            else:
                addfaculty1_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject1_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_1 = addfaculty1_sig[0]
                signature_type11 = "APPROVE"

        # ADD SUBJECT #2
        check_status = graduation_form_table.objects.filter(
            id=id, addsignature2__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, addsignature2='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('addfaculty2', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            addsubject_2 = "UNAPPROVED"
            signature_type12 = ""
            addsubject2_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            addsubject_2 = ""
            signature_type12 = ""
            addsubject2_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('addsignature2', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    addfaculty2_sig = up_sig[0]
                else:
                    addfaculty2_sig= e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject2_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_2 = addfaculty2_sig
                signature_type12 = "ESIGN"

            else:
                addfaculty2_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject2_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_2 = addfaculty2_sig[0]
                signature_type12 = "APPROVE"

        # ADD SUBJECT #3
        check_status = graduation_form_table.objects.filter(
            id=id, addsignature3__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, addsignature3='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('addfaculty3', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            addsubject_3 = "UNAPPROVED"
            signature_type13 = ""
            addsubject3_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            addsubject_3 = ""
            signature_type13 = ""
            addsubject3_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('addsignature3', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    addfaculty3_sig = up_sig[0]
                else:
                    addfaculty3_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject3_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_3 = addfaculty3_sig
                signature_type13 = "ESIGN"

            else:
                addfaculty3_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject3_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_3 = addfaculty3_sig[0]
                signature_type13 = "APPROVE"

        # ADD SUBJECT #4
        check_status = graduation_form_table.objects.filter(
            id=id, addsignature4__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, addsignature4='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('addfaculty4', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            addsubject_4 = "UNAPPROVED"
            signature_type14 = ""
            addsubject4_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            addsubject_4 = ""
            signature_type14 = ""
            addsubject4_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('addsignature4', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    addfaculty4_sig = up_sig[0]
                else:
                    addfaculty4_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject4_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_4 = addfaculty4_sig
                signature_type14 = "ESIGN"

            else:
                addfaculty4_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject4_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_4 = addfaculty4_sig[0]
                signature_type14 = "APPROVE"

        # ADD SUBJECT #5
        check_status = graduation_form_table.objects.filter(
            id=id, addsignature5__icontains='UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(
            id=id, addsignature5='NO_APPROVED')
        if check_status:
            faculty_name = graduation_form_table.objects.filter(
                id=id).values_list('addfaculty5', flat=True).distinct()
            str_fac_name = str(faculty_name[0])
            faculty_firstName = user_table.objects.filter(
                full_name=str_fac_name).values_list('first_name', flat=True).distinct()
            faculty_lastName = user_table.objects.filter(
                full_name=str_fac_name).values_list('last_name', flat=True).distinct()
            addsubject_5 = "UNAPPROVED"
            signature_type15 = ""
            addsubject5_name = faculty_firstName[0] + " " + faculty_lastName[0]
        elif check_signature:
            addsubject_5 = ""
            signature_type15 = ""
            addsubject5_name = "NONE"
        else:
            faculty_approved = graduation_form_table.objects.filter(
                id=id).values_list('addsignature5', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_', 1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)

            if faculty_approved[0].__contains__('ESIGN'):
                e_sig = user_table.objects.filter(full_name=str_fac_name).values_list('e_signature', flat=True).distinct()
                up_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                if e_sig[0] == "":
                    addfaculty5_sig = up_sig[0]
                else:
                    addfaculty5_sig = e_sig[0]
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject5_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_5 = addfaculty5_sig
                signature_type15 = "ESIGN"

            else:
                addfaculty5_sig = user_table.objects.filter(
                    full_name=str_fac_name).values_list('no_signature', flat=True).distinct()
                faculty_firstName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('first_name', flat=True).distinct()
                faculty_lastName = user_table.objects.filter(
                    full_name=str_fac_name).values_list('last_name', flat=True).distinct()
                addsubject5_name = faculty_firstName[0] + \
                    " " + faculty_lastName[0]
                addsubject_5 = addfaculty5_sig[0]
                signature_type15 = "APPROVE"

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    context = {
        'graduation': graduation,
        'subject_1': subject_1,
        'subject_2': subject_2,
        'subject_3': subject_3,
        'subject_4': subject_4,
        'subject_5': subject_5,
        'subject_6': subject_6,
        'subject_7': subject_7,
        'subject_8': subject_8,
        'subject_9': subject_9,
        'subject_10': subject_10,
        'addsubject_1': addsubject_1,
        'addsubject_2': addsubject_2,
        'addsubject_3': addsubject_3,
        'addsubject_4': addsubject_4,
        'addsubject_5': addsubject_5,
        'signature_type1': signature_type1,
        'signature_type2': signature_type2,
        'signature_type3': signature_type3,
        'signature_type4': signature_type4,
        'signature_type5': signature_type5,
        'signature_type6': signature_type6,
        'signature_type7': signature_type7,
        'signature_type8': signature_type8,
        'signature_type9': signature_type9,
        'signature_type10': signature_type10,
        'signature_type11': signature_type11,
        'signature_type12': signature_type12,
        'signature_type13': signature_type13,
        'signature_type14': signature_type14,
        'signature_type15': signature_type15,
        'sit_name': sit_name,
        'subject1_name': subject1_name,
        'subject2_name': subject2_name,
        'subject3_name': subject3_name,
        'subject4_name': subject4_name,
        'subject5_name': subject5_name,
        'subject6_name': subject6_name,
        'subject7_name': subject7_name,
        'subject8_name': subject8_name,
        'subject9_name': subject9_name,
        'subject10_name': subject10_name,
        'addsubject1_name': addsubject1_name,
        'addsubject2_name': addsubject2_name,
        'addsubject3_name': addsubject3_name,
        'addsubject4_name': addsubject4_name,
        'addsubject5_name': addsubject5_name,
        'sit': sit,
        'sit_type': sit_type
    }
    print('running')
    return render(request, 'html_files/graduation_form_display.html', context)

# CLEARANCE LIST ON REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_clearance_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        # DEFAULT/ GENERAL LIST
        if id == "%20":
            all = clearance_form_table.objects.all().order_by('-time_requested')
            return render(request,  'html_files/7.2Registrar Clearance List.html', {'all': all})
        else:
            string = id.replace('%20', ' ')
            all = clearance_form_table.objects.filter(course=string).order_by('-time_requested').values()
            return render(request,  'html_files/7.2Registrar Clearance List.html', {'all': all})
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request,  'html_files/7.2Registrar Clearance List.html', {'all': all})

# GRADUATION LIST ON REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_graduation_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        if id == "%20":
            all = graduation_form_table.objects.all().order_by('-time_requested')
            all_list = graduation_form_table.objects.filter(
                approval_status="APPROVED")
            return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all, 'all_list': all_list})
        else:
            string = id.replace('%20', ' ')
            all = graduation_form_table.objects.filter(course=string).order_by('-time_requested')
            all_list = graduation_form_table.objects.filter(
                course=string, approval_status="APPROVED")
            return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all, 'all_list': all_list})

        return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all})
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all})

# FACULTY LIST FOR REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_faculty_list(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        all_faculty = user_table.objects.filter(
            user_type="FACULTY", is_active=True)
        faculty_data = {
            'all': all_faculty,
        }
        return render(request,  'html_files/7.4Registrar Faculty List.html', faculty_data)

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    # return render(request,  'html_files/7.4Registrar Faculty List.html', {'all': all_faculty})

# CHANGE ACTIVE STATUS OF FACULTY INSTEAD OF DELETE (MIGHT AFFECT SAVED SIGNATURES IF DELETED)
@login_required(login_url='/')
def faculty_list_remove(request, id):
    print("hey")
    delete_faculty = user_table.objects.get(id=id)
    # delete_faculty.delete()
    delete_faculty.is_active = False
    delete_faculty.save()
    messages.success(request, "Faculty has been deleted.")

    return redirect(registrar_dashboard_faculty_list)

# UPDATE DESIGNATION LIST FOR DEPARTMENT HEADS
@login_required(login_url='/')
def faculty_designation_update(request, id):
    form_change = request.POST.get('designationSelect')

    if form_change == "---":
        user_table.objects.filter(id=id).update(position="FACULTY")
        temp = user_table.objects.filter(id=id).values_list(
            'department', flat=True).distinct()
        dep = temp[0]
        hremover = dep[1:]
        print(dep)
        print(hremover)
        user_table.objects.filter(id=id).update(department=hremover)
    else:
        user_table.objects.filter(id=id).update(position="HEAD")
        user_table.objects.filter(id=id).update(department=form_change)

    if form_change == "HOCS":
        user_table.objects.filter(id=id).update(designation="ACCOUNTANT")
    elif form_change == "HDLA":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF LIBERAL ARTS")
    elif form_change == "HDMS":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF MATH AND SCIENCES")
    elif form_change == "HDPECS":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF PHYSICAL EDUCATION")
    elif form_change == "HDIT":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF INDUSTRIAL TECHNOLOGY")
    elif form_change == "HDED":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF INDUSTRIAL EDUCATION")
    elif form_change == "HDOE":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF ENGINEERING")
    elif form_change == "HOCL":
        user_table.objects.filter(id=id).update(designation="CAMPUS LIBRARIAN")
    elif form_change == "HOGS":
        user_table.objects.filter(id=id).update(
            designation="GUIDANCE COUNCELOR")
    elif form_change == "HOSA":
        user_table.objects.filter(id=id).update(
            designation="HEAD OF STUDENT AFFAIRS")
    elif form_change == "HADAA":
        user_table.objects.filter(id=id).update(
            designation="ASST. DIRECTOR FOR ACADEMIC AFFAIRS")
    else:
        user_table.objects.filter(id=id).update(designation="---")

    return redirect(registrar_dashboard_faculty_list)

# STUDENT LIST ON REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_student_list(request, id):
    # declaring template
    template = "html_files/Student list.html"
    
    if id == "student":
        student_data = user_table.objects.filter(
            user_type="STUDENT").values()
    elif id == "old":
        student_data = user_table.objects.filter(
            user_type="OLD STUDENT").values()
    elif id == "alumni":
        student_data = user_table.objects.filter(
        user_type="ALMUNUS").values()
    elif id == "4th":
        student_data = user_table.objects.filter(
        year_and_section__contains="4").values()
    elif id == "3rd":
        student_data = user_table.objects.filter(
        year_and_section__contains="3").values()
    elif id == "2nd":
        student_data = user_table.objects.filter(
        year_and_section__contains="2").values()
    elif id == "1st":
        student_data = user_table.objects.filter(
        year_and_section__contains="1").values()
    elif id =="oldest":
        student_data = user_table.objects.filter(
        year_graduated__isnull=False).order_by('year_graduated').values()
    elif id =="latest":
        student_data = user_table.objects.filter(
        year_graduated__isnull=False).order_by('-year_graduated').values()
    else:    
        student_data = user_table.objects.filter(Q(user_type='STUDENT') | Q(
            user_type='OLD STUDENT') | Q(user_type='ALUMNUS'))

    context = {'data': student_data}
    return render(request, template, context)

# STAFF LIST ON REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_staff_list(request):
    # declaring template
    staff_data = user_table.objects.filter(Q(user_type='STAFF'))

    context = {'data': staff_data}
    return render(request, 'html_files/7.5Registrar Staff List.html', context)

# DELETE STUDENT/REQUESTER ON REGISTRAR'S SIDE
@login_required(login_url='/')
def student_list_remove(request, id):
    print("hey")
    delete_student = user_table.objects.get(id=id)
    delete_student.delete()
    messages.success(request, "Student has been deleted.")

    return redirect('All')

# DELETE STAFF ON REGISTRAR'S SIDE
@login_required(login_url='/')
def staff_list_remove(request, id):
    delete_staff = user_table.objects.get(id=id)
    delete_staff.delete()
    messages.success(request, "Staff has been deleted.")

    return redirect(registrar_dashboard_staff_list)

# REQUEST LIST AND DOCUMENT CHECKER LIST
# REQUEST LIST WITH ORGANIZER
@login_required(login_url='/')
def registrar_dashboard_organize_request_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        sorter = id

        if id == "CLAIMED":
            requests = request_form_table.objects.filter(
                claim="CLAIMED").order_by('-time_requested').values()
        elif id == "UNCLAIMED":
            requests = request_form_table.objects.filter(
                claim="UNCLAIMED").order_by('-time_requested').values()
        elif id == "Honorable":
            requests = request_form_table.objects.filter(
                request="Honorable Dismissal").order_by('-time_requested').values()
        elif id == "Subject":
            requests = request_form_table.objects.filter(
            request="Subject Description").order_by('-time_requested').values()
        elif id == "Certification":
            requests = request_form_table.objects.filter(
                request__startswith = "Certification:").values()
        elif id == "Authentication":
            requests = request_form_table.objects.filter(
            request="Authentication").order_by('-time_requested').values()
        elif id == "Diploma":
            requests = request_form_table.objects.filter(
            request="Diploma").order_by('-time_requested').values()
        elif id == "Transcript":
            requests = request_form_table.objects.filter(
            request="Transcript").order_by('-time_requested').values()
        elif id == "CAV":
            requests = request_form_table.objects.filter(
            request="CAV").order_by('-time_requested').values()
        elif id == "Others":
            requests = request_form_table.objects.filter(
                request__startswith="Others:").order_by('-time_requested').values()
        elif id == "Student":
            requests = request_form_table.objects.filter(
                current_status="STUDENT").order_by('-time_requested').values()
        elif id == "Old":
            requests = request_form_table.objects.filter(
                current_status="OLD STUDENT").order_by('-time_requested').values()
        elif id == "Alumni":
            requests = request_form_table.objects.filter(
                current_status="ALMUNUS").order_by('-time_requested').values()
        elif id == "OLDEST":
            requests = request_form_table.objects.all().order_by('time_requested').values()
        elif id == "LATEST":
            requests = request_form_table.objects.all().order_by('-time_requested').values()
        else:
            requests = request_form_table.objects.all().order_by('-time_requested').values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/Request List.html', {'data': requests, 'sorter_type': sorter})


# CLEARANCE LIST AND DOCUMENT CHECKER LIST
# CLEARANCE LIST WITH ORGANIZER
@login_required(login_url='/')
def registrar_dashboard_organize_clearance_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        sorter = id

        if id == "Honorable":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="Honorable Dismissal").order_by('-time_requested').values()
        elif id == "Subject":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="Subject Description").order_by('-time_requested').values()
        elif id == "Certification":
            requests = clearance_form_table.objects.filter(
                purpose_of_request__startswith = "Certification:").values()
        elif id == "Authentication":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="Authentication").order_by('-time_requested').values()
        elif id == "Diploma":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="Diploma").order_by('-time_requested').values()
        elif id == "Transcript":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="Transcript").order_by('-time_requested').values()
        elif id == "CAV":
            requests = clearance_form_table.objects.filter(
            purpose_of_request="CAV").order_by('-time_requested').values()
        elif id == "Others":
            requests = clearance_form_table.objects.filter(
                purpose_of_request__startswith="Others:").order_by('-time_requested').values()
        elif id == "approved":
            requests = clearance_form_table.objects.filter(
                approval_status="APPROVED").order_by('-time_requested').values()

        else:
            requests = clearance_form_table.objects.all().order_by('-time_requested').values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/7.2Registrar Clearance List.html', {'all': requests, 'sorter_type': sorter})

# FACULTY LIST AND DOCUMENT CHECKER LIST
# FACULTY LIST WITH ORGANIZER
@login_required(login_url='/')
def registrar_dashboard_organize_faculty_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":

        sorter = id

        if id == "OCL":
            requests = user_table.objects.filter(department__contains="OCL").values()
        elif id == "OCS":
            requests = user_table.objects.filter(department__contains="OCS").values()
        elif id == "OGS":
            requests = user_table.objects.filter(department__contains="OGS").values()
        elif id == "OSA":
            requests = user_table.objects.filter(department__contains="OSA").values()
        elif id == "ADAA":
            requests = user_table.objects.filter(department__contains="ADAA").values()
        elif id == "OES":
            requests = user_table.objects.filter(department__contains="OES").values()
        elif id == "DMS":
            requests = user_table.objects.filter(department__contains="DMS").values()
        elif id == "DPECS":
            requests = user_table.objects.filter(department__contains="DPECS").values()
        elif id == "DED":
            requests = user_table.objects.filter(department__contains="DED").values()
        elif id == "DIT":
            requests = user_table.objects.filter(department__contains="DIT").values()
        elif id == "DLA":
            requests = user_table.objects.filter(department__contains="DLA").values()
        elif id == "DOE":
            requests = user_table.objects.filter(department__contains="DOE").values()
        else:
            requests = user_table.objects.filter(user_type="FACULTY") .values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/7.4Registrar Faculty List.html', {'all': requests, 'sorter_type': sorter})



# REQUEST LIST ON REGISTRAR'S SIDE
@login_required(login_url='/')
def registrar_dashboard_request_list(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        requests = request_form_table.objects.all().order_by('-time_requested').values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/Request List.html', {'data': requests})

# UPDATE OR RECEIPT, OR NUMBER, OR DATE ON REQUEST FORM ON REGISTRAR'S SIDE
@login_required(login_url='/')
def request_official_update(request, id):
    form_change = request.POST.get('or_select')
    request_form_table.objects.filter(
        id=id).update(official_receipt=form_change)
    or_number = request.POST.get('or_number')
    request_form_table.objects.filter(id=id).update(or_num=or_number)
    or_date = request.POST.get('or_date')
    request_form_table.objects.filter(id=id).update(or_date=or_date)
    get_name = request_form_table.objects.filter(
        id=id).values_list('name', flat=True).distinct()
    get_request = request_form_table.objects.filter(
        id=id).values_list('request', flat=True).distinct()
    if get_name:
        clearance_form_table.objects.filter(
            name=get_name[0], purpose_of_request=get_request[0]).update(or_num=or_number)
    return redirect(registrar_dashboard_request_list)

# UPDATE FORM 137 STATUS ON REQUEST FORM ON REGISTRAR'S SIDE
@login_required(login_url='/')
def request_form137_update(request, id):
    form_change = request.POST.get('form137_select')
    request_form_table.objects.filter(id=id).update(form_137=form_change)
    return redirect(registrar_dashboard_request_list)

# UPDATE CLAIM STATUS OF REQUEST FORM ON REGISTRAR'S SIDE
def request_claim_update(request, id):
    form_change = request.POST.get('claim_select')
    request_form_table.objects.filter(id=id).update(claim=form_change)
    return redirect(registrar_dashboard_request_list)

# REQUEST FORM
@login_required(login_url='/')
def request_form(request):
    context = {}
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT":
        user = request.user.user_type
        student_name = request.user.full_name

        # DETERMINE UNDERGRADUATE STUDENTS
        today_date = date.today()
        id_num = request.user.id_number
        sliced_id = int(str(id_num)[:2])
        current_year = '"'+str(today_date.year) + '"'
        temp = int(current_year[2:5])
        with_graduation = temp - sliced_id
        year_today = today_date.year

        if request.method == "POST":
            form = request_form
            student_id = request.POST.get('stud_id_pre')
            amount = request.POST.get('amount_paid')
            last_name = request.POST.get('ln_box_pre')
            first_name = request.POST.get('fn_box_pre')
            middle_name = request.POST.get('mn_box_pre')
            course = request.POST.get('course_pre')
            date_today = request.POST.get('date_pre')
            semester = request.POST.get('sem_term')
            control_num = request.POST.get('control_pre')
            address = request.POST.get('add_box_pre')
            contact_num = request.POST.get('contact_pre')
            purpose = request.POST.get('purpose')
            request = request.POST.get('purpose_request_pre')
            current_stat = user

            if middle_name == "None":
                full_name = last_name + ", " + first_name
                name2 = last_name + ", " + first_name
            else:
                full_name = last_name + ", " + first_name + " " + middle_name
                mid = middle_name[0] + "."
                name2 = last_name + ", " + first_name + " " + mid

            print(name2)

            check_form137 = request_form_table.objects.filter(
                name=full_name, form_137="✔").values_list('form_137', flat=True).distinct()
            if check_form137:
                have_form137 = "✔"
                form = request_form_table.objects.create(student_id=student_id, name=full_name, name2=name2,
                                                         address=address, course=course, date=date_today, control_number=control_num, amount=amount, contact_number=contact_num, current_status=current_stat, purpose_of_request_reason=purpose,
                                                         request=request, form_137=have_form137)
            else:
                form = request_form_table.objects.create(student_id=student_id, name=full_name, name2=name2,
                                                         address=address, course=course, date=date_today, control_number=control_num, amount=amount, contact_number=contact_num, current_status=current_stat, purpose_of_request_reason=purpose,
                                                         request=request)
            form.save()

            if user == "STUDENT" or user == "ALUMNUS" or user == "OLD STUDENT":
                # CHECK REQUESTED DOCUMENT BY SEMESTER
                semester_check = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request)).order_by(
                    '-time_requested').values_list('semester_enrolled', flat=True).distinct()
                term_check = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request)).order_by(
                    '-time_requested').values_list('date_filed', flat=True).distinct()
                if request == 'Honorable Dismissal':
                    check_clearance = clearance_form_table.objects.filter(
                        Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        year_then = str(term_check[0].split('-', 1)[0])
                        if semester_check[0] == semester and str(year_then) == str(year_today):
                            return redirect('student_dashboard')
                        else:
                            return redirect('clearance_form/HonorableDismissal')
                    else:
                        return redirect('clearance_form/HonorableDismissal')

                elif request == 'Transcript of Records':
                    check_clearance = clearance_form_table.objects.filter(
                        Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        year_then = str(term_check[0].split('-', 1)[0])
                        if semester_check[0] == semester and str(year_then) == str(year_today):
                            return redirect('student_dashboard')
                        else:
                            return redirect('clearance_form/TrascriptOfRecords')
                    else:
                        return redirect('clearance_form/TrascriptOfRecords')
                elif request == 'Diploma':
                    check_clearance = clearance_form_table.objects.filter(
                        Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        year_then = str(term_check[0].split('-', 1)[0])
                        if semester_check[0] == semester and str(year_then) == str(year_today):
                            return redirect('student_dashboard')
                        else:
                            return redirect('clearance_form/Diploma')
                    else:
                        return redirect('clearance_form/Diploma')
                elif request.__contains__('Certification'):
                    check_clearance = clearance_form_table.objects.filter(
                        Q(name=full_name), Q(purpose_of_request="Certification"))
                    if check_clearance:
                        semester_check_clear = clearance_form_table.objects.filter(Q(name=full_name), Q(
                            purpose_of_request="Certification")).order_by('-time_requested').values_list('semester_enrolled', flat=True).distinct()
                        term_check_clear = clearance_form_table.objects.filter(Q(name=full_name), Q(
                            purpose_of_request="Certification")).order_by('-time_requested').values_list('date_filed', flat=True).distinct()
                        year_then = str(term_check_clear[0].split('-', 1)[0])
                        if semester_check_clear[0] == semester and str(year_then) == str(year_today):
                            return redirect('student_dashboard')
                        else:
                            return redirect('clearance_form/Certification')
                    else:
                        return redirect('clearance_form/Certification')
                elif request.__contains__('Others'):
                    check_clearance = clearance_form_table.objects.filter(
                        Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        year_then = str(term_check[0].split('-', 1)[0])
                        if semester_check[0] == semester and str(year_then) == str(year_today):
                            return redirect('student_dashboard')
                        else:
                            return redirect('clearance_form/Others')
                    else:
                        return redirect('clearance_form/Others')
                else:
                    return redirect('student_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            unclaim_request = request_form_table.objects.filter(name=student_name).order_by(
                '-time_requested').values_list('claim', flat=True).distinct()
            latest_request = request_form_table.objects.filter(name=student_name, approval_status="UNAPPROVED").order_by(
                '-time_requested').values_list('request', flat=True).distinct()
            latest_purpose = request_form_table.objects.filter(name=student_name).order_by(
                '-time_requested').values_list('purpose_of_request_reason', flat=True).distinct()
            if latest_purpose:
                request_pur = latest_purpose[0]
            else:
                request_pur = ""
            if unclaim_request:
                allow_request = unclaim_request[0]
                if latest_request:
                    latest = latest_request[0]
                    if latest.__contains__('Certification'):
                        latest_req = "Certification"
                        request_cert = latest
                        request_other = ""
                        print("CERT")
                    elif latest.__contains__('Others'):
                        latest_req = "Others"
                        request_other = latest
                        request_cert = ""

                    else:
                        latest_req = latest_request[0]
                        request_other = ""
                        request_cert = ""
                else:
                    request_other = ""
                    request_cert = ""
                    latest_req = ""

            else:
                allow_request = ""
                latest_req = ""
                request_other = ""
                request_cert = ""

            context = {'with_graduation': with_graduation, 'allow': allow_request, 'latest_request': latest_req,
                       'request_purpose': request_pur, 'request_other': request_other, 'request_cert': request_cert}

    else:
        today_date = ""
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/Request form.html', context)

# UPDATE SIGNATURE FOR CLEARANCE LIST ON FACULTY'S SIDE
@login_required(login_url='/')
def update_clearance_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        create_signature = request.POST.get('image_encoded')
        uploaded_signature = request.FILES.get('new_upload_signature', False)
        signature_timesaved = datetime.now()
        full_name = request.user.full_name

        if create_signature == "":
            if bool(uploaded_signature) == False:
                messages.error(
                    request, "No New Signature Saved. Please Try Again.")
            else:
                recent_upload_sig = request.user.uploaded_signature
                recent_create_sig = request.user.e_signature
                if recent_upload_sig:
                    if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_upload_sig)):
                        os.remove('/home/tupclget/public_html/Media/' + str(recent_upload_sig))
                        user_table.objects.filter(id=id).update(uploaded_signature="")
                    else:
                        pass
                elif recent_create_sig:
                    
                    if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_create_sig)):
                        os.remove('/home/tupclget/public_html/Media/' + str(recent_create_sig))
                        user_table.objects.filter(id=id).update(e_signature="")
                        
                    else:
                        pass
                else: 
                    pass

                file_name = "uploaded signatures/" + str(uploaded_signature)

                fs = FileSystemStorage()

                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)

                user_table.objects.filter(id=id).update(
                    uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(
                    uploaded_signature_timesaved=signature_timesaved)

                messages.success(
                    request, "Your Signature has been updated. It may take a few minutes to update accross the site.")
        else:
            # remove recent signature
            recent_upload_sig = request.user.uploaded_signature
            recent_create_sig = request.user.e_signature
            if recent_upload_sig:
                if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_upload_sig)):
                    os.remove('/home/tupclget/public_html/Media/' + str(recent_upload_sig))
                    user_table.objects.filter(id=id).update(uploaded_signature="")
                else:
                    pass
            elif recent_create_sig:
                if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_create_sig)):
                    os.remove('/home/tupclget/public_html/Media/' + str(recent_create_sig))
                    user_table.objects.filter(id=id).update(e_signature="")
                else:
                    pass
            else: 
                pass

            # save signature in the storage
            image_decode = ContentFile(base64.b64decode(
                create_signature.replace('data:image/png;base64,', '')))
            file_name = 'esignatures/' + full_name + \
                str(datetime.now()) + '.png'
            fs = FileSystemStorage()
            filename = fs.save(file_name, image_decode)

            user_table.objects.filter(id=id).update(e_signature=file_name)
            user_table.objects.filter(id=id).update(
                e_signature_timesaved=signature_timesaved)
            messages.success(
                request, "Your Signature has been updated. It may take a few minutes to update accross the site.")

    return redirect(faculty_dashboard_clearance_list)

# UPDATE SIGNATURE FOR GRADUATION LIST IN FACULTY'S SIDE
@login_required(login_url='/')
def update_grad_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        create_signature = request.POST.get('image_encoded')
        uploaded_signature = request.FILES.get('new_upload_signature', False)
        signature_timesaved = datetime.now()
        full_name = request.user.full_name

        if create_signature == "":
            if bool(uploaded_signature) == False:
                messages.error(
                    request, "No New Signature Saved. Please Try Again.")
            else:
                recent_upload_sig = request.user.uploaded_signature
                recent_create_sig = request.user.e_signature
                if recent_upload_sig:
                    if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_upload_sig)):
                        os.remove('/home/tupclget/public_html/Media/' + str(recent_upload_sig))
                        user_table.objects.filter(id=id).update(uploaded_signature="")
                    else:
                        pass
                        
                elif recent_create_sig:
                    if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_create_sig)):
                        os.remove('/home/tupclget/public_html/Media/' + str(recent_create_sig))
                        user_table.objects.filter(id=id).update(e_signature="")
                    else:
                        pass
                else: 
                    pass

                file_name = "uploaded signatures/" + \
                    str(datetime.now()) + str(uploaded_signature)

                fs = FileSystemStorage()

                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)

                user_table.objects.filter(id=id).update(
                    uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(
                    uploaded_signature_timesaved=signature_timesaved)
                messages.success(
                    request, "Your Signature has been updated. It may take a few minutes to update accross the site.")
        else:
            # remove recent signature
            recent_upload_sig = request.user.uploaded_signature
            recent_create_sig = request.user.e_signature
            if recent_upload_sig:
                if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_upload_sig)):
                    os.remove('/home/tupclget/public_html/Media/' + str(recent_upload_sig))
                    user_table.objects.filter(id=id).update(uploaded_signature="")
                else:
                    pass
            elif recent_create_sig:
                if os.path.exists('/home/tupclget/public_html/Media/' + str(recent_create_sig)):
                    os.remove('/home/tupclget/public_html/Media/' + str(recent_create_sig))
                    user_table.objects.filter(id=id).update(e_signature="")
                else:
                    pass
            else: 
                pass

            # save signature in the storage
            image_decode = ContentFile(base64.b64decode(
                create_signature.replace('data:image/png;base64,', '')))
            file_name = 'esignatures/' + full_name + \
                str(datetime.now()) + '.png'

            fs = FileSystemStorage()
            filename = fs.save(file_name, image_decode)

            user_table.objects.filter(id=id).update(e_signature=file_name)
            user_table.objects.filter(id=id).update(
                e_signature_timesaved=signature_timesaved)
            messages.success(
                request, "Your Signature has been updated. It may take a few minutes to update accross the site.")

    return redirect(faculty_dashboard_graduation_list)

# DISPLAY REQUEST FORM
@login_required(login_url='/')
def display_reqform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or request.user.user_type == "ALUMNUS" or request.user.user_type == "OLD STUDENT" or request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        reqs = request_form_table.objects.filter(id=id).values()
        certification_data = request_form_table.objects.filter(id=id).values_list('request', flat=True).distinct()
        others_data = request_form_table.objects.filter(id=id).values_list('request', flat=True).distinct()
        if certification_data:
            c = certification_data[0]
            print(c)
            if c.__contains__('Certification'):
                latest_req = "Certification"
                request_cert = str(certification_data[0])
                request_other = ""
            else:
                if others_data:
                    o = others_data[0]
                    print(o)
                    if o.__contains__('Others'):
                        latest_req = "Others"
                        request_other = str(others_data[0])
                        print(request_other)
                        request_cert = ""
                    else:
                        request_other = ""
                        latest_req = ""
                        request_cert = ""
                else:
                    request_other = ""
                    latest_req = ""
                    request_cert = ""
        else:
            request_cert = ""
            latest_req = ""
            request_other = ""

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {
        "reqs": reqs,
        "request_cert": request_cert,
        "request_other": request_other,
        "latest_req": latest_req,

    }

    print('running')
    return render(request, 'html_files/Request_form_display.html', context)

# DELETE GRADUATION FORM ON REGISTRAR'S SIDE
@login_required(login_url='/')
def delete_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        delete_grad = graduation_form_table.objects.get(id=id)
        delete_grad.delete()
        messages.success(request, "Form has been deleted.")
        return redirect('/registrar_dashboard_graduation_list/%20')

# DELETE CLEARANCE FORM ON REGISTRAR'S SIDE
@login_required(login_url='/')
def delete_clearform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        delete_clear = clearance_form_table.objects.get(id=id)
        delete_clear.delete()
        messages.success(request, "Form has been deleted.")
        return redirect('/registrar_dashboard_clearance_list/%20')

# DELETE REQUEST FORM ON REGISTRAR'S SIDE
@login_required(login_url='/')
def delete_reqform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR" or request.user.user_type == "STAFF":
        delete_req = request_form_table.objects.get(id=id)
        delete_req.delete()
        messages.success(request, "Form has been deleted.")
        return redirect('registrar_dashboard_request_list')

# CONVERT STUDENT INTO ALUMNUS OR OLD STUDENT/TRANSFEREE
# AUTO UPDATE ALL SCHOOL-RELATED INFOS
@login_required(login_url='/')
def student_status_update(request, id):
    student_update = request.POST.get('status_select')
    user_table.objects.filter(id=id).update(user_type=student_update)
    

    getter = user_table.objects.get(id=id)
    today = date.today().year
    getter = user_table.objects.get(id=id)

    user_table.objects.filter(id=id).update(year_graduated=today)
    cur_course = getter.course
    user_table.objects.filter(id=id).update(course_graduated=cur_course)
    user_table.objects.filter(id=id).update(course=None)
    user_table.objects.filter(id=id).update(year_and_section=None)
    user_id = getter.id_number
    user_id2 = getter.student_id
    userbday = getter.birthday
    mbday = userbday[:2]
    dbday = userbday[3:5]
    ybday = userbday[6:]
    year_id = str(today)
    id_year = year_id[2:]
    
    request_form_table.objects.filter(student_id=user_id2).update(current_status=student_update)
    if student_update == "ALUMNUS":
        
        update_id = "TUPC-" + user_id+"-"+id_year+"-"+mbday+dbday+ybday
        update_idnum = user_id+"-"+id_year+"-"+mbday+dbday+ybday
        user_table.objects.filter(id=id).update(id_number=update_idnum)
        user_table.objects.filter(id=id).update(student_id=update_id)
        clearance_form_table.objects.filter(
            student_id=user_id2).update(student_id=update_id)
        graduation_form_table.objects.filter(
            student_id=user_id2).update(student_id=update_id)
        request_form_table.objects.filter(
            student_id=user_id2).update(student_id=update_id)

    return redirect('All')

# DECLARE NEW SCHOOL YEAR ON STUDENTS LIST
# APPLICABLE TO UNDERGRADUATE STUDENTS ONLY
# STOPS AT 4TH YEAR
@login_required(login_url='/')
def school_year_update(request):
    id_num = user_table.objects.filter(~Q(year_and_section__startswith="4"), Q(
        user_type="STUDENT")).values_list('id', flat=True).distinct()
    yands = user_table.objects.filter(~Q(year_and_section__startswith="4"), Q(
        user_type="STUDENT")).values_list('year_and_section', flat=True).distinct()
    print("idNum:", id_num)
    print("yands:", yands)

    for x in id_num:
        year_num = user_table.objects.filter(id=x).values_list(
            'year_and_section', flat=True).distinct()

        print("yearnum:", year_num)
        year_num = year_num[0]
        year_num = int(year_num[:1]) + 1
        if year_num == 2:
            user_table.objects.filter(id=int(x)).update(
                year_and_section="2nd Year")
        elif year_num == 3:
            user_table.objects.filter(id=int(x)).update(
                year_and_section="3rd Year")
        elif year_num == 4:
            user_table.objects.filter(id=int(x)).update(
                year_and_section="4th Year")

    return redirect('All')

# SEND EMAIL NOTIFICATIONS ON ALL SIGNATORIES WITH APPLICATION FORMS TO SIGN
# SCHEDULED EVERY WEEKDAYS AT 4PM
# CONNECTED TO SETTINGS.PY CRONJOBS AND CRON.PY
def send_email_all():
    date_today = datetime.now().date()
    print("Date Today: ",date_today)
    faculties = []
    cleartable = clearance_form_table.objects.filter(
        time_requested__contains=date_today).all()
    if cleartable:
        all_course_adviser = clearance_form_table.objects.filter(
            time_requested__contains=date_today).values_list('course_adviser', flat=True).distinct()
        for course_adviser in all_course_adviser:
            if course_adviser in faculties:
                pass
            else:
                faculties.append(course_adviser)

        all_dep_head = user_table.objects.filter(Q(department="HOCS") | Q(department="HDLA")
                                                 | Q(department="HDMS") | Q(department="HDPECS") | Q(department="HDIT") |
                                                 Q(department="HDED") | Q(department="HDOE") | Q(department="HOCL") |
                                                 Q(department="HOGS") | Q(department="HOSA") |
                                                 Q(department="HADAA") & Q(user_type="FACULTY")).values_list('full_name', flat=True).distinct()

        for dephead in all_dep_head:
            if dephead in faculties:
                pass
            else:
                faculties.append(dephead)

    all_faculty_grad = list(graduation_form_table.objects.filter(time_requested__contains=date_today).all().values_list('faculty1', 'faculty2',
                                                                                                                        'faculty3', 'faculty4', 'faculty5', 'faculty6', 'faculty7', 'faculty8', 'faculty9', 'faculty10',
                                                                                                                        'addfaculty1', 'addfaculty2', 'addfaculty3', 'addfaculty4', 'addfaculty5', 'instructor_name').distinct())

    for i in all_faculty_grad:
        for faculty in i:
            if faculty != "NO FACULTY":
                if faculty in faculties:
                    pass
                else:
                    faculties.append(faculty)
            else:
                pass

    recipient_list = []
    for recipient in faculties:
        email_found = user_table.objects.filter(
            full_name=recipient).values_list('username', flat=True).distinct()
        for emails in email_found:
            recipient_list.append(emails)

    subject = 'Application Form Received'
    message1 = 'Greetings! This email is to inform you that an application form has been sent to your account. Please check ' + \
        '<a href="tupcaviteregistrar.site/">tupcaviteregistrar.site</a>' + \
        ' for full details. Thank you!<br><br><br>'
    message2 = "<strong>"+'Technological University of the Philippines-Cavite Campus' + \
        "</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br><br>'
    message3 = "<i>"+'***This is an automated message from the Office of the Campus Registrar, do not reply.<br><br>'+"</i>"

    message = message1 + message2 + message3
    email_from = settings.EMAIL_HOST_USER

    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send(fail_silently=True)
    if recipient_list:
        print("This is to inform you that email notifications has been sent to the signatories.")
    else:
        print("This is to inform you that no email notifications for signatories to send today. Thank you!")

# APPROVE CLEARANCE FORMS ON REGISTRAR'S SIDE
# FOR ALUMNI WITH EXISTING CLEARANCE RECORD IN THE OFFICE
@login_required(login_url='/')
def approve_clearform(request, id):
    registrar_name = user_table.objects.filter(
        user_type="REGISTRAR").values_list('full_name', flat=True).distinct()
    registrar_approval = registrar_name[0] + "_APPROVED REGISTRAR"
    
    student_name = clearance_form_table.objects.filter(id=id).values_list('name', flat=True).distinct()

    clearance_form_table.objects.filter(id=id).update(
        liberal_arts_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        accountant_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        mathsci_dept_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        pe_dept_signature=registrar_approval)

    clearance_form_table.objects.filter(id=id).update(
        library_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        guidance_office_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        osa_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        academic_affairs_signature=registrar_approval)
    clearance_form_table.objects.filter(id=id).update(
        course_adviser=registrar_name[0])
    clearance_form_table.objects.filter(id=id).update(
        course_adviser_signature=registrar_approval)

    ieduc_dept_signature = clearance_form_table.objects.filter(
        id=id).values_list('ieduc_dept_signature', flat=True).distinct()
    it_dept_signature = clearance_form_table.objects.filter(
        id=id).values_list('it_dept_signature', flat=True).distinct()
    eng_dept_signature = clearance_form_table.objects.filter(
        id=id).values_list('eng_dept_signature', flat=True).distinct()
    if ieduc_dept_signature[0] == "_APPROVED" and it_dept_signature[0] == "_APPROVED":
        clearance_form_table.objects.filter(id=id).update(
            eng_dept_signature=registrar_approval)
    elif ieduc_dept_signature[0] == "_APPROVED" and eng_dept_signature[0] == "_APPROVED":
        clearance_form_table.objects.filter(id=id).update(
            it_dept_signature=registrar_approval)
    else:
        clearance_form_table.objects.filter(id=id).update(
            ieduc_dept_signature=registrar_approval)

    clearance_form_table.objects.filter(
        id=id).update(approval_status="APPROVED")
        
    request_form_table.objects.filter(name=student_name[0]).update(clearance="✔")

    return redirect('/registrar_dashboard_clearance_list/%20')
