import email
from genericpath import exists
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
from django.core import mail
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import my_csv, csv,  io
from textwrap import wrap
import base64
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
import datetime
from datetime import datetime
import os


def graduation_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = graduation_form_table.objects.get(id=id)
    textob = p.beginText()

    lines = []

    day_eve = content.shift
    if day_eve == "DAY":
        p.drawString(65, 805, '/')
    else:
        p.drawString(65, 792, '/')

    p.drawString(80, 755, f'{content.name}')
    p.drawString(500, 755, f'{content.course}')
    p.drawString(120, 710, f'{content.study_load}')
    stat = content.status
    if stat == "YES":
        p.drawString(390, 670, '/')
    else:
        p.drawString(490, 670, '/')
    p.drawString(220, 670, f'{content.enrolled_term}')
    
    #revised
    p.setFont("Helvetica", 10)
    sub1 = content.subject1
    if len(sub1) == 0:
        p.drawString(33, 640, ' ')
        p.drawString(204, 640,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279, 640, ' ')
        p.drawString(323, 640, ' ')
        p.drawString(380, 640, ' ')
        
    else:
        p.drawString(33, 640, f'{content.subject1}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 640, f'{content.starttime1_1} - {content.endtime1_1}')
        p.drawString(279, 640, f'{content.room1}')
        p.drawString(323, 640, f'{content.day1_1}')
        sig1 = content.signature1
        if sig1 == "1_sig":
            p.drawString(380, 640, 'Unapproved')
        else:
            p.drawString(380, 640, f'{content.signature1}')
            
    p.setFont("Helvetica", 10)
    sub2 = content.subject2
    if len(sub2) == 0:
        p.drawString(33, 625, ' ')
        p.drawString(204, 625,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,625, ' ')
        p.drawString(323, 625, ' ')
        p.drawString(380, 625, ' ')
        
    else:
        p.drawString(33, 625, f'{content.subject2}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 625, f'{content.starttime1_2} - {content.endtime1_2}')
        p.drawString(279, 625, f'{content.room2}')
        p.drawString(323, 625, f'{content.day1_2}')
        sig2 = content.signature2
        if sig2 == "1_sig":
            p.drawString(380, 625, 'Unapproved')
        else:
            p.drawString(380, 625, f'{content.signature2}')
            
    p.setFont("Helvetica", 10)
    sub3 = content.subject3
    if len(sub3) == 0:
        p.drawString(33, 611, ' ')
        p.drawString(204, 611,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,611, ' ')
        p.drawString(323, 611, ' ')
        p.drawString(380, 611, ' ')
        
    else:
        p.drawString(33, 611, f'{content.subject3}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 611, f'{content.starttime1_3} - {content.endtime1_3}')
        p.drawString(279, 611, f'{content.room3}')
        p.drawString(323, 611, f'{content.day1_3}')
        sig3 = content.signature3
        if sig3 == "1_sig":
            p.drawString(380, 611, 'Unapproved')
        else:
            p.drawString(380, 611, f'{content.signature3}')
            
    
    p.setFont("Helvetica", 10)
    sub4 = content.subject4
    if len(sub4) == 0:
        p.drawString(33, 597, ' ')
        p.drawString(204, 597,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,597, ' ')
        p.drawString(323, 597, ' ')
        p.drawString(380, 597, ' ')
        
    else:
        p.drawString(33, 597, f'{content.subject4}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 597, f'{content.starttime1_4} - {content.endtime1_4}')
        p.drawString(279, 597, f'{content.room4}')
        p.drawString(323, 597, f'{content.day1_4}')
        sig4 = content.signature4
        if sig4 == "1_sig":
            p.drawString(380, 597, 'Unapproved')
        else:
            p.drawString(380, 597, f'{content.signature4}')
    
    
    p.setFont("Helvetica", 10)
    sub5 = content.subject5
    if len(sub5) == 0:
        p.drawString(33, 584, ' ')
        p.drawString(204, 584,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,584, ' ')
        p.drawString(323, 584, ' ')
        p.drawString(380, 584, ' ')
        
    else:
        p.drawString(33, 584, f'{content.subject5}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 584, f'{content.starttime1_5} - {content.endtime1_5}')
        p.drawString(279, 584, f'{content.room5}')
        p.drawString(323, 584, f'{content.day1_5}')
        sig5 = content.signature5
        if sig5 == "1_sig":
            p.drawString(380, 584, 'Unapproved')
        else:
            p.drawString(380, 584, f'{content.signature5}')
            
            
    p.setFont("Helvetica", 10)
    sub6 = content.subject6
    if len(sub6) == 0:
        p.drawString(33, 570, ' ')
        p.drawString(204, 570,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,570, ' ')
        p.drawString(323, 570, ' ')
        p.drawString(380, 570, ' ')
        
    else:
        p.drawString(33, 570, f'{content.subject6}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 570, f'{content.starttime1_6} - {content.endtime1_6}')
        p.drawString(279, 570, f'{content.room6}')
        p.drawString(323, 570, f'{content.day1_6}')
        sig6 = content.signature6
        if sig6 == "1_sig":
            p.drawString(380, 570, 'Unapproved')
        else:
            p.drawString(380, 570, f'{content.signature6}')
            
            
    p.setFont("Helvetica", 10)
    sub7 = content.subject7
    if len(sub7) == 0:
        p.drawString(33, 555, ' ')
        p.drawString(204, 555,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,555, ' ')
        p.drawString(323, 555, ' ')
        p.drawString(380, 555, ' ')
        
    else:
        p.drawString(33, 555, f'{content.subject7}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 555, f'{content.starttime1_7} - {content.endtime1_7}')
        p.drawString(279, 555, f'{content.room7}')
        p.drawString(323, 555, f'{content.day1_7}')
        sig7 = content.signature7
        if sig7 == "1_sig":
            p.drawString(380, 555, 'Unapproved')
        else:
            p.drawString(380, 555, f'{content.signature7}')
            

    p.setFont("Helvetica", 10)
    sub8 = content.subject8
    if len(sub8) == 0:
        p.drawString(33, 542, ' ')
        p.drawString(204, 542,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,542, ' ')
        p.drawString(323, 542, ' ')
        p.drawString(380, 542, ' ')
        
    else:
        p.drawString(33, 542, f'{content.subject8}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 542, f'{content.starttime1_8} - {content.endtime1_8}')
        p.drawString(279, 542, f'{content.room8}')
        p.drawString(323, 542, f'{content.day1_8}')
        sig8 = content.signature8
        if sig8 == "1_sig":
            p.drawString(380, 542, 'Unapproved')
        else:
            p.drawString(380, 542, f'{content.signature8}')
            
    p.setFont("Helvetica", 10)
    sub9 = content.subject9
    if len(sub9) == 0:
        p.drawString(33, 529, ' ')
        p.drawString(204, 529,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,529, ' ')
        p.drawString(323, 529, ' ')
        p.drawString(380, 529, ' ')
        
    else:
        p.drawString(33, 529, f'{content.subject9}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 529, f'{content.starttime1_9} - {content.endtime1_9}')
        p.drawString(279, 529, f'{content.room9}')
        p.drawString(323, 529, f'{content.day1_9}')
        sig9 = content.signature9
        if sig9 == "1_sig":
            p.drawString(380, 529, 'Unapproved')
        else:
            p.drawString(380, 529, f'{content.signature9}')
            
    
    
    p.setFont("Helvetica", 10)
    sub10 = content.subject10
    if len(sub10) == 0:
        p.drawString(33, 515, ' ')
        p.drawString(204, 515,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,515, ' ')
        p.drawString(323, 515, ' ')
        p.drawString(380, 515, ' ')
        
    else:
        p.drawString(33, 515, f'{content.subject10}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 515, f'{content.starttime1_10} - {content.endtime1_10}')
        p.drawString(279, 515, f'{content.room10}')
        p.drawString(323, 515, f'{content.day1_10}')
        sig10 = content.signature10
        if sig10 == "1_sig":
            p.drawString(380, 515, 'Unapproved')
        else:
            p.drawString(380, 515, f'{content.signature10}')
    
    #additional subj
    
    p.setFont("Helvetica", 10)
    addsub1 = content.addsubject1
    if len(addsub1) == 0:
        p.drawString(33, 305, ' ')
        p.drawString(204, 305,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,305, ' ')
        p.drawString(323, 305, ' ')
        p.drawString(380, 305, ' ')
        
    else:
        p.drawString(33, 305, f'{content.addsubject1}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 305, f'{content.add_starttime1_1} - {content.add_endtime1_1}')
        p.drawString(279, 305, f'{content.addroom1}')
        p.drawString(323, 305, f'{content.addday1_1}')
        addsig1 = content.addsignature1
        if addsig1 == "1_sig":
            p.drawString(380, 305, 'Unapproved')
        else:
            p.drawString(380, 305, f'{content.addsignature1}')
    
    p.setFont("Helvetica", 10)
    addsub2 = content.addsubject2
    if len(addsub2) == 0:
        p.drawString(33, 290, ' ')
        p.drawString(204, 290,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,290, ' ')
        p.drawString(323, 290, ' ')
        p.drawString(380, 290, ' ')
        
    else:
        p.drawString(33, 290, f'{content.addsubject2}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 290, f'{content.add_starttime1_2} - {content.add_endtime1_2}')
        p.drawString(279, 290, f'{content.addroom2}')
        p.drawString(323, 290, f'{content.addday1_2}')
        addsig2 = content.addsignature2
        if addsig2 == "1_sig":
            p.drawString(380, 290, 'Unapproved')
        else:
            p.drawString(380, 290, f'{content.addsignature2}')
            
    
    p.setFont("Helvetica", 10)
    addsub3 = content.addsubject3
    if len(addsub3) == 0:
        p.drawString(33, 276, ' ')
        p.drawString(204, 276,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,276, ' ')
        p.drawString(323, 276, ' ')
        p.drawString(380, 276, ' ')
        
    else:
        p.drawString(33, 276, f'{content.addsubject3}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 276, f'{content.add_starttime1_3} - {content.add_endtime1_3}')
        p.drawString(279, 276, f'{content.addroom3}')
        p.drawString(323, 276, f'{content.addday1_3}')
        addsig3 = content.addsignature3
        if addsig3 == "1_sig":
            p.drawString(380, 276, 'Unapproved')
        else:
            p.drawString(380, 276, f'{content.addsignature3}')
            
            

    p.setFont("Helvetica", 10)
    addsub4 = content.addsubject4
    if len(addsub4) == 0:
        print ("empty")
        p.drawString(33, 262, ' ')
        p.drawString(204, 262,' ')
        p.setFont("Helvetica", 8)
        p.drawString(279,262, ' ')
        p.drawString(323, 262, ' ')
        p.drawString(380, 262, ' ')
        
    else:
        p.drawString(33, 262, f'{content.addsubject4}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 262, f'{content.add_starttime1_4} - {content.add_endtime1_4}')
        p.drawString(279, 262, f'{content.addroom4}')
        p.drawString(323, 262, f'{content.addday1_4}')
        addsig4 = content.addsignature4
        if addsig4 == "1_sig":
            p.drawString(380, 262, 'Unapproved')
        else:
            p.drawString(380, 262, f'{content.addsignature4}')
            
            
    p.setFont("Helvetica", 10)
    addsub5 = content.addsubject5
    if len(addsub5) == 0:
        p.drawString(33, 249, ' ')
        p.drawString(204, 249,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,249, ' ')
        p.drawString(323, 249, ' ')
        p.drawString(380, 249, ' ')
        
    else:
        p.drawString(33, 249, f'{content.addsubject5}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 249, f'{content.add_starttime1_5} - {content.add_endtime1_5}')
        p.drawString(279, 249, f'{content.addroom5}')
        p.drawString(323, 249, f'{content.addday1_5}')
        addsig5 = content.addsignature5
        if addsig5 == "1_sig":
            p.drawString(380, 249, 'Unapproved')
        else:
            p.drawString(380, 249, f'{content.addsignature5}')
            
            
    p.setFont("Helvetica", 10)
    addsub6 = content.addsubject6
    if len(addsub6) == 0:
        p.drawString(33, 235, ' ')
        p.drawString(204, 235,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,235, ' ')
        p.drawString(323, 235, ' ')
        p.drawString(380, 235, ' ')
        
    else:
        p.drawString(33, 235, f'{content.addsubject6}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 235, f'{content.add_starttime1_6} - {content.add_endtime1_6}')
        p.drawString(279, 235, f'{content.addroom6}')
        p.drawString(323, 235, f'{content.addday1_6}')
        addsig6 = content.addsignature6
        if addsig6 == "1_sig":
            p.drawString(380, 235, 'Unapproved')
        else:
            p.drawString(380, 235, f'{content.addsignature6}')
            
            
    p.setFont("Helvetica", 10)
    addsub7 = content.addsubject7
    if len(addsub7) == 0:
        p.drawString(33, 220, ' ')
        p.drawString(204, 220,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,220, ' ')
        p.drawString(323, 220, ' ')
        p.drawString(380, 220, ' ')
    else:
        p.drawString(33, 220, f'{content.addsubject7}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 220, f'{content.add_starttime1_7} - {content.add_endtime1_7}')
        p.drawString(279, 220, f'{content.addroom7}')
        p.drawString(323, 220, f'{content.addday1_7}')
        addsig7 = content.addsignature7
        if addsig7 == "1_sig":
            p.drawString(380, 220, 'Unapproved')
        else:
            p.drawString(380, 220, f'{content.addsignature7}')
            
            
            
    p.setFont("Helvetica", 10)
    addsub8 = content.addsubject8
    if len(addsub8) == 0:
        p.drawString(33, 207, ' ')
        p.drawString(204, 207,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,207, ' ')
        p.drawString(323, 207, ' ')
        p.drawString(380, 207, ' ')
        
    else:
        p.drawString(33, 207, f'{content.addsubject8}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 207, f'{content.add_starttime1_8} - {content.add_endtime1_8}')
        p.drawString(279, 207, f'{content.addroom8}')
        p.drawString(323, 207, f'{content.addday1_8}')
        addsig8 = content.addsignature8
        if addsig8 == "1_sig":
            p.drawString(380, 207, 'Unapproved')
        else:
            p.drawString(380, 207, f'{content.addsignature8}')
            
            
    p.setFont("Helvetica", 10)
    addsub9 = content.addsubject9
    if len(addsub9) == 0:
        p.drawString(33,193, ' ')
        p.drawString(204,193,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279,193, ' ')
        p.drawString(323,193, ' ')
        p.drawString(380,193, ' ')
        
    else:
        p.drawString(33, 193, f'{content.addsubject9}')
        p.setFont("Helvetica", 8)
        p.drawString(204,193, f'{content.add_starttime1_9} - {content.add_endtime1_9}')
        p.drawString(279,193, f'{content.addroom9}')
        p.drawString(323,193, f'{content.addday1_9}')
        addsig9 = content.addsignature9
        if addsig9 == "1_sig":
            p.drawString(380,193, 'Unapproved')
        else:
            p.drawString(380,193, f'{content.addsignature9}')
            
            
    p.setFont("Helvetica", 10)
    addsub10 = content.addsubject10
    if len(addsub10) == 0:
        p.drawString(33, 180, ' ')
        p.drawString(204, 180,' ')
        
        p.setFont("Helvetica", 8)
        p.drawString(279, 180, ' ')
        p.drawString(323, 180, ' ')
        p.drawString(380, 180, ' ')
        
    else:
        p.drawString(33, 180, f'{content.addsubject10}')
        p.setFont("Helvetica", 8)
        p.drawString(204, 180, f'{content.add_starttime1_10} - {content.add_endtime1_10}')
        p.drawString(279, 180, f'{content.addroom10}')
        p.drawString(323, 180, f'{content.addday1_10}')
        addsig10 = content.addsignature10
        if addsig10 == "1_sig":
            p.drawString(380, 180, 'Unapproved')
        else:
            p.drawString(380, 180, f'{content.addsignature10}')


    p.setFont("Helvetica", 10)
    p.drawString(235, 151, f'{content.unenrolled_application_deadline}')
    p.drawString(195, 73, f'{content.trainP_startdate}')
    p.drawString(390, 73, f'{content.trainP_enddate}')
    p.drawString(258, 58, f'{content.instructor_name}')

    for line in lines:
        textob.textLine(line)

    #p.drawString(300, 755, f'{request.user.middle_name[0:1]}')

    p.drawText(textob)
    p.showPage()
    p.save()

    # Merging 2 Pdfs
    buffer.seek(0)
    infos = PdfFileReader(buffer)
    clearance_pdf = PdfFileReader(open(r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf/Graduation_form.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'C:/Users/Acer/request_credentials_system/gradclear_project/gradclear_app/static/pdf/Graduation_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf/Graduation_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=Graduation Form.pdf'
        return response



def clearance_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = clearance_form_table.objects.get(id=id)
    textob = p.beginText()

    print(content)
    print("hello world")

    lines = []

    p.drawString(80, 755, f'{content.name}')
    p.drawString(400, 755, f'{content.date_filed}')
    p.setFont("Helvetica", 9)
    p.drawString(130, 710, f'{content.present_address}')
    p.setFont("Helvetica", 10)
    p.drawString(150, 681, f'{content.date_admitted_in_tup}')
    p.drawString(120, 655, f'{content.course}')
    # p.drawString(180, 629, f'{content.highschool_graduated}')

    hs_grad = content.highschool_graduated
    num=len(hs_grad.split())
    
    if num > 3:
        p.setFont("Helvetica", 9)
        result =' '.join(hs_grad.split()[:3])
        p.drawString(180, 629, f"""{result}""")
        result1 =' '.join(hs_grad.split()[3:])
        p.drawString(43, 605, f"""{result1}""")
    else: 
        p.setFont("Helvetica", 9)
        p.drawString(180, 629, f'{content.highschool_graduated}')
        
    p.setFont("Helvetica", 10)  
    p.drawString(400, 681, f'{content.amount_paid}')
    p.drawString(217, 530, f'{content.number_of_terms_in_tupc}')
    p.drawString(430, 530, f'{content.date_of_previously_requested_form}')

    # signature
    p.drawString(130, 290, f'{content.accountant_signature}')
    p.drawString(150, 240, f'{content.liberal_arts_signature}')
    p.drawString(169, 215, f'{content.mathsci_dept_signature}')
    p.drawString(120, 190, f'{content.pe_dept_signature}')
    # wala sa liberal arts
    # temporary lang itong sa dept like dit, educ etc. pati na sa shop adviser
    
    p.drawString(100, 115, f'{content.ieduc_dept_signature}')
    p.drawString(435, 290, f'{content.it_dept_signature}')
    

    
    
    p.drawString(425, 265, f'{content.library_signature}')
    p.drawString(435, 240, f'{content.guidance_office_signature}')
    p.drawString(455, 215, f'{content.osa_signature}')
    p.drawString(482, 190, f'{content.academic_affairs_signature}')

    tupc_grad = content.tupc_graduate
    if tupc_grad == "YES":
        p.drawString(208, 580, '/')
        p.drawString(183, 555, f'{content.year_graduated_in_tupc}')
    else:
        p.drawString(270, 580, '/')

    prev_form = content.have_previously_requested_form
    if prev_form == "YES":
        p.drawString(428, 611, '/')
        p.drawString(380, 560, f'{content.date_of_previously_requested_form}')
        p.drawString(430, 505, f'{content.purpose_of_request_reason}')
    else:
        p.drawString(490, 611, '/')

    # purpose
    form_purpose = content.purpose_of_request

    if form_purpose == "Honorable Dismissal":
        p.drawString(45, 434, '/')
    elif form_purpose == "Evaluation":
        p.drawString(298, 434, '/')
    elif form_purpose == "Transcript of Records":
        p.drawString(45, 412, '/')
    elif form_purpose == "Re-Evaluation":
        p.drawString(298, 412, '/')
    elif form_purpose == "Diploma":
        p.drawString(45, 390, '/')
    elif form_purpose == "Application for Graduation":
        p.drawString(298, 390, '/')
    elif form_purpose == "Certification":
        p.drawString(45, 370, '/')
    else:
        p.drawString(400, 370, f'{content.purpose_of_request}')

    for line in lines:
        textob.textLine(line)

    #p.drawString(300, 755, f'{request.user.middle_name[0:1]}')

    p.drawText(textob)
    p.showPage()
    p.save()

    # Merging 2 Pdfs
    buffer.seek(0)
    infos = PdfFileReader(buffer)
    clearance_pdf = PdfFileReader(open(
        r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Clearance_form.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Clearance_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Clearance_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=Clearance Form.pdf'
        return response


def appointment(request, id):
    email_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        username=email_temp[0]).values_list('email', flat=True).distinct()

    rec_email = email[0]

    subject = 'Appointment Request for Clearance Form'

    message1 = 'Greetings,<br><br>'
    message2 = 'Mr./Ms. ' + "<strong>" + request.user.last_name + "</strong>" + \
        ' would like to speak with you regarding with the application form you requested. Contact him/her through this email "' + \
        request.user.email + '".<br>'
    message3 = '<br> <br>Note: This is an automated message, do not reply.'

    message = message1 + message2 + message3
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send()

    messages.success(request, "Email Sent.")
    return redirect('faculty_dashboard_clearance_list')


def appointmentgrad(request, id):
    email_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        username=email_temp[0]).values_list('email', flat=True).distinct()

    rec_email = email[0]

    subject = 'Appointment Request for Graduation Form'

    message1 = 'Greetings,<br><br>'
    message2 = 'Mr./Ms. ' + "<strong>" + request.user.last_name + "</strong>" + \
        ' would like to speak with you regarding with the application form you requested. Contact him/her through this email "' + \
        request.user.email + '".<br>'
    message3 = '<br> <br>Note: This is an automated message, do not reply.'

    message = message1 + message2 + message3
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send()

    messages.success(request, "Email Sent.")
    return redirect('faculty_dashboard_graduation_list')

def reg_appointmentgrad(request, id):
    print('a')

    email_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        username=email_temp[0]).values_list('email', flat=True).distinct()

    rec_email = email[0]

    subject = 'Appointment Request for Graduation Form'

    message1 = 'Greetings,<br><br>'
    message2 = 'Mr./Ms. ' + "<strong>" + request.user.last_name + "</strong>" + \
        ' would like to speak with you regarding with the application form you requested. Contact him/her through this email "' + \
        request.user.email + '".<br>'
    message3 = '<br> <br>Note: This is an automated message, do not reply.'

    message = message1 + message2 + message3
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send()

    messages.success(request, "Email Sent.")
    return redirect('registrar_dashboard')

def reggrad_appointment(request,id):
    if request.method == 'POST':
        email_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            username=email_temp[0]).values_list('email', flat=True).distinct()
        rec_email = email[0]
        recipient_list = [rec_email, ]

        purpose = graduation_form_table.objects.filter(
        id=id).values_list('purpose_of_request', flat=True).distinct()
        purpose_of = graduation_form_table.objects.filter(
            purpose_of_request=purpose[0]).values_list('purpose_of_request', flat=True).distinct()
        purpose_of_req =  purpose_of[0]
        purpose_of_request = [purpose_of_req, ]

        name = graduation_form_table.objects.filter(
        id=id).values_list('name', flat=True).distinct()
        s_name = graduation_form_table.objects.filter(
            name=name[0]).values_list('name', flat=True).distinct()
        st_name =  s_name[0]
        student_name = [st_name, ]

        subject = 'Appointment Request for Graduation Form'
        # message1 = 'Greetings,'+ 'Mr./Ms. ' + "<strong>" + name + "</strong><br><br>"
        message1 = 'Greetings from the  '+"<strong>"+'Registrar,'+"</strong><br><br>"
        message2 = 'Your request for'+\
            ' has been approved. Follow the guidelines below for the claiming of your credentials. Please take note of the date and time of the appointment and bring all the necessary requirements. Thank you! "<br><br>'
        message3 = "<strong>"+'GUIDELINES:'+"</strong><br><br>"
        message4 =  "<strong>"+'Note: '+"</strong>"+'This is an automated message, do not reply.<br><br>'

        message = message1 + message2 + message3 + message4

        purpose_req = request.POST.get('purpose_of_request')
        date_appointment = request.POST.get('date_appointment')
        time_appointment = request.POST.get('time_appointment')
        additionalmessage = request.POST.get('additionalmessage')
        email = request.POST.get('email')
       
        
        
        data = {
                'purpose_of_request': purpose_of_request,
                'student_name': student_name,
                'date_appointment': date_appointment, 
                'time_appointment': time_appointment, 
                'subject': subject, 
                'message': message,
                'additionalmessage': additionalmessage,
        }
        message='''{}
        Purpose:\n\t\t{}\n<br>
        Name:\n\t\t{}\n<br>
        Date:\n\t\t{}\n<br>
        Time:\n\t\t{}\n<br>
        Additonal Message:\n\t\t{}\n<br>
        
        '''''.format(data['message'], data ['purpose_of_request'], data ['student_name'], data ['date_appointment'], data ['time_appointment'], data ['additionalmessage'])
        msg = EmailMessage(subject, message,'', email, recipient_list,)
        msg.content_subtype = "html"
        msg.send()
        messages.success(request, "Appointment Schedule Sent.")
    return render(request, 'html_files/appointment.html', {})

def regclear_appointment(request,id):
    if request.method == 'POST':
        email_temp = clearance_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            username=email_temp[0]).values_list('email', flat=True).distinct()
        rec_email = email[0]
        recipient_list = [rec_email, ]

        purpose = clearance_form_table.objects.filter(
        id=id).values_list('purpose_of_request', flat=True).distinct()
        purpose_of = clearance_form_table.objects.filter(
            purpose_of_request=purpose[0]).values_list('purpose_of_request', flat=True).distinct()
        purpose_of_req =  purpose_of[0]
        purpose_of_request = [purpose_of_req, ]

        name = clearance_form_table.objects.filter(
        id=id).values_list('name', flat=True).distinct()
        s_name = clearance_form_table.objects.filter(
            name=name[0]).values_list('name', flat=True).distinct()
        st_name =  s_name[0]
        student_name = [st_name, ]

        subject = 'Appointment Request for Clearance Form'
        # message1 = 'Greetings,'+ 'Mr./Ms. ' + "<strong>" + request.user.last_name + "</strong><br><br>"
        message1 = 'Greetings from the  '+"<strong>"+'Registrar,'+"</strong><br><br>"
        message2 = 'Your request for'+\
            ' has been approved. Follow the guidelines below for the claiming of your credentials. Please take note of the date and time of the appointment and bring all the necessary requirements. Thank you! "<br><br>'
        message3 = "<strong>"+'GUIDELINES:'+"</strong><br><br>"
        message4 = "<strong>"+'Note: '+"</strong>"+'This is an automated message, do not reply.<br><br>'

        message = message1 + message2 + message3 + message4

        purpose_req = request.POST.get('purpose_of_request')
        date_appointment = request.POST.get('date_appointment')
        time_appointment = request.POST.get('time_appointment')
        additionalmessage = request.POST.get('additionalmessage')
        email = request.POST.get('email')
        
        
        
        data = {
                'purpose_of_request': purpose_of_request,
                'student_name': student_name,
                'date_appointment': date_appointment, 
                'time_appointment': time_appointment, 
                'subject': subject, 
                'message': message,
                'additionalmessage': additionalmessage,
                
               
        }
        message='''{}
        Purpose:\n\t\t{}\n<br>
        Name:\n\t\t{}\n<br>
        Date:\n\t\t{}\n<br>
        Time:\n\t\t{}\n<br>
        Additonal Message:\n\t\t{}\n<br>
        
        '''''.format(data['message'], data ['purpose_of_request'], data ['student_name'] , data ['date_appointment'], data ['time_appointment'], data ['additionalmessage'])
        msg = EmailMessage(subject, message,'', email, recipient_list,)
        msg.content_subtype = "html"
        msg.send()
        messages.success(request, "Appointment Schedule Sent.")
    return render(request, 'html_files/appointment.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('email_box_01')
        password = request.POST.get('password_box_01')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            p = user_table.objects.filter(username=username).values_list(
                'user_type', flat=True).distinct()
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
            else:
                return redirect('/')
        else:
            messages.error(request, ("Incorrect Username or Password"))
            return redirect('/')
    else:
        return render(request, 'html_files/1Cover Page.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def student_registration(request):
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
            form.instance.username = "TUPC-" + id_num
            username = "TUPC-" + id_num
            
            form.instance.full_name = last + ", " + first + " "+ middle
           
            form.instance.user_type = "STUDENT"
            form.save()
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Account Saved. Keep in mind that your username is: ' + username)
            return redirect('/')
        else:
            messages.error(
                request, "There is an error with your form. Try again.")
    img_object = form.instance
    user_identifier = "STUDENT"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)

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
            form.instance.username = "TUPC-" + id_num
            username = "TUPC-" + id_num
            
            form.instance.full_name = last + ", " + first + " "+ middle
           
            form.instance.user_type = "OLD STUDENT"
            form.save()
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Account Saved. Keep in mind that your username is: ' + username)
            return redirect('/')
        else:
            messages.error(
                request, "There is an error with your form. Try again.")
    img_object = form.instance
    user_identifier = "OLD STUDENT"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)


def faculty_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.get("username")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.username = "TUPC-" + id_num
            form.instance.position = "FACULTY"
            username = "TUPC-" + id_num
            form.instance.user_type = "FACULTY"
            form.instance.designation = "---"
            form.instance.full_name = last + ", " + first + " " + middle
            
            agreement = request.POST.get('agreement')
            chosen_SignatureType = request.POST.get('signature_type')
            
            if agreement == "AGREED":
                if chosen_SignatureType =="ESIGN":
                    esign_signature = request.POST.get('image_encoded')
            
                    if esign_signature == "":
                        messages.error(request, "Signature Pad is BLANK. Please create your Signature.")
                    else:
                        image_decode = base64.b64decode(esign_signature.replace('data:image/png;base64,',''))

                        file_name = 'Media/signatures/' + last + ", " + first + " " + middle + '_APPROVED.png'

                        # Create image file from base64 and saved in MEDIA file
                        with open(file_name, 'wb') as img_file:
                            img_file.write(image_decode)
                            #file name saved in the database
                            form.instance.uploaded_signature = 'signatures/' + last + ", " + first + " " + middle + '_APPROVED.png'
                            form.instance.time_savedsignature = datetime.now()
                else:
                    pass
            elif agreement == "DECLINE":
                form.instance.uploaded_signature = "DECLINE"
                form.instance.time_savedsignature = datetime.now()
            else:
                messages.error(request, "Approval Type is not determine")

            form.save()
            messages.success(
                request, 'Account Saved. Keep in mind that your username is: ' + username)

            return redirect('/')
        else:
            messages.error(
                request, "There is an error with your form. Try again.")
    img_object = form.instance
    user_identifier = "FACULTY"
    context = {'form': form,'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)


def alumnus_registration(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST, request.FILES)
        if form.is_valid():
            user_type = form.cleaned_data.get("username")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.username = "TUPC-" + id_num
            username = "TUPC-" + id_num
            form.instance.user_type = "ALUMNUS"
            form.instance.full_name = last + ", " + first + " " + middle
         
        
            form.save()
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Account Saved. Keep in mind that your username is: ' + username)
            return redirect('/')
           
        else:
            messages.error(
                request, "There is an error with your form. Try again.")
    img_object = form.instance
    user_identifier = "ALUMNUS"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)


def cover(request):
    return render(request, 'html_files/1Cover Page.html')


@login_required(login_url='/')
def student_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS" or "OLD STUDENT":
        username = request.user.username
        full_name = request.user.full_name
        first = request.user.first_name
        last = request.user.last_name
        middle = request.user.middle_name
        
        mid = middle[0] + "."
        name2 = last + ", " + first + " " + mid

        print(username)

        st0 = request_form_table.objects.filter(name= full_name)
        st = graduation_form_table.objects.filter(student_id=username)
        st1 = clearance_form_table.objects.filter(student_id=username)
        
        check_form137 = Document_checker_table.objects.filter(Q(name=full_name)|Q(name=name2)).values_list('form_137',flat=True).distinct()
        check_form137_inrequest = request_form_table.objects.filter(Q(name=full_name)|Q(name=name2)).values_list('form_137',flat=True).distinct()
        check_clearance = clearance_form_table.objects.filter(student_id=username).values_list('approval_status',flat=True).distinct()
        check_graduation = graduation_form_table.objects.filter(student_id=username).values_list('approval_status',flat=True).distinct()
        
        # document checker
        display =[]
        # Form137-A
        if check_form137.exists():
            if check_form137[0] == '❌':
                print('Missing FORM 137-A')
                display.append("FORM 137-A")
                
        elif check_form137_inrequest.exists():
            for i in check_form137_inrequest:
                if i == '❌':
                    print(check_form137_inrequest)
                    print('Missing FORM 137-A')
                    display.append("FORM 137-A")  
                else:
                    pass
        else:
            pass
                  
        if not check_clearance:
            display.append("CLEARANCE")
        else:
            if check_clearance[0] == 'ON PROGRESS':
                display.append("CLEARANCE (ON PROGRESS)")
                
        if not check_graduation:
            pass
        else:
            if check_graduation[0] == 'ON PROGRESS':
                print('Clearance Pending')
                display.append("GRADUATION (ON PROGRESS)")
  
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {'st': st, 'st1': st1, 'st0': st0, 'display':display}
    return render(request, 'html_files/4.1Student Dashboard.html', context)



@login_required(login_url='/')
def clearance_form(request):
    a = user_table.objects.filter(user_type="FACULTY").values_list('full_name', flat=True).distinct()
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or 'ALUMNUS' or 'OLD STUDENT':
        user = request.user.user_type
        print(user)
        if request.method == "POST":
            form = clearance_form

            # id_number = request.user.id()
            student_id = request.POST.get('stud_id_420')
            last_name = request.POST.get('ln_box_420')
            first_name = request.POST.get('fn_box_420')
            middle_name = request.POST.get('mn_box_420')
            name = last_name + ", " + first_name + " " + middle_name
            name2 = first_name + " " + last_name
            present_address = request.POST.get('padd_box_420')
            course = request.POST.get('course_420')
            date_filed = request.POST.get('dfiled_box_420')
            date_admitted = request.POST.get('dait_box_420')
            highschool_graduated = request.POST.get('hswg_box_420')
            tupc_graduate = request.POST.get('grad_option_420')
            highschool_graduated_date = request.POST.get('iydfiled_box_420')
            terms = request.POST.get('notit_box_420')
            amount = request.POST.get('amountp_box_420')
            or_number = request.POST.get('receiptnum_box_42')
            last_request = request.POST.get('requested_option_420')
            last_request_date = request.POST.get('dbrtime_box_420')
            last_term = request.POST.get('lasterm_box_420')
            course_adviser = request.POST.get('course_adviser_420')
            course_adviser_signature = request.POST.get('course_adviser_420') + "_UNAPPROVED"
            purpose_reason = request.POST.get('preq_box_420')
            purpose = request.POST.get('purpose_request_420')
            form = clearance_form_table.objects.create(student_id=student_id, name=name, present_address=present_address, course=course,
                                                       date_filed=date_filed, date_admitted_in_tup=date_admitted,
                                                       highschool_graduated=highschool_graduated, tupc_graduate=tupc_graduate, year_graduated_in_tupc=highschool_graduated_date,
                                                       number_of_terms_in_tupc=terms, amount_paid=amount, have_previously_requested_form=last_request,
                                                       date_of_previously_requested_form=last_request_date, last_term_in_tupc=last_term,
                                                       course_adviser=course_adviser, course_adviser_signature=course_adviser_signature, 
                                                       purpose_of_request=purpose, purpose_of_request_reason=purpose_reason,)
            form.save()
            
            return redirect('student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.2Student Clearance Form.html', {'a': a})


@login_required(login_url='/')
def graduation_form(request):
    a = user_table.objects.filter(user_type="FACULTY").values_list('full_name', flat=True).distinct()
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
            name = last_name + ", " + first_name + " " + middle_name
            name2 =first_name + " " + last_name
            course = request.POST.get('course_getter')

            d = request.POST.get('shift_option')
            e = request.POST.get('stdfor_option')
            f = request.POST.get('enrolled_option')
            h = request.POST.get('ersem_box_43')
            i = request.POST.get('deadline_box_43')
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

            u2 = request.POST.get('starttime2')
            v2 = request.POST.get('endtime2')
            q2 = request.POST.get('day2')
            u3 = request.POST.get('starttime3')
            v3 = request.POST.get('endtime3')
            q3 = request.POST.get('day3')

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

            o6 = request.POST.get('addsubject6')
            p6 = request.POST.get('addroom6')
            t6 = request.POST.get('addfaculty6')
            w1_6 = request.POST.get('add_starttime1_6')
            x1_6 = request.POST.get('add_endtime1_6')
            r1_6 = request.POST.get('addday1_6')

            o7 = request.POST.get('addsubject7')
            p7 = request.POST.get('addroom7')
            t7 = request.POST.get('addfaculty7')
            w1_7 = request.POST.get('add_starttime1_7')
            x1_7 = request.POST.get('add_endtime1_7')
            r1_7 = request.POST.get('addday1_7')

            o8 = request.POST.get('addsubject8')
            p8 = request.POST.get('addroom8')
            t8 = request.POST.get('addfaculty8')
            w1_8 = request.POST.get('add_starttime1_8')
            x1_8 = request.POST.get('add_endtime1_8')
            r1_8 = request.POST.get('addday1_8')

            o9 = request.POST.get('addsubject9')
            p9 = request.POST.get('addroom9')
            t9 = request.POST.get('addfaculty9')
            w1_9 = request.POST.get('add_starttime1_9')
            x1_9 = request.POST.get('add_endtime1_9')
            r1_9 = request.POST.get('addday1_9')

            o10 = request.POST.get('addsubject10')
            p10 = request.POST.get('addroom10')
            t10 = request.POST.get('addfaculty10')
            w1_10 = request.POST.get('add_starttime1_10')
            x1_10 = request.POST.get('add_endtime1_10')
            r1_10 = request.POST.get('addday1_10')

            w2 = request.POST.get('add_starttime2')
            x2 = request.POST.get('add_endtime2')
            r2 = request.POST.get('addday2')
            r3 = request.POST.get('addday3')
            w3 = request.POST.get('add_starttime3')
            x3 = request.POST.get('add_endtime3')

            sig_s1  = ""
            sig_s2  = ""
            sig_s3  = ""
            sig_s4  = ""
            sig_s5  = ""
            sig_s6  = ""
            sig_s7  = ""
            sig_s8  = ""
            sig_s9  = ""
            sig_s10  = ""

            sig_t1  = ""
            sig_t2  = ""
            sig_t3  = ""
            sig_t4  = ""
            sig_t5  = ""
            sig_t6  = ""
            sig_t7  = ""
            sig_t8  = ""
            sig_t9  = ""
            sig_t10  = ""       

            if s1 == "1":
                s1 = "NO FACULTY"
                sig_s1 = "NO SIGNATURE"
            else:
                sig_s1 = s1 + "_UNAPPROVED"
                
            if s2 == "1":
                s2 = "NO FACULTY"
                sig_s2 = "NO SIGNATURE"
            else:
                sig_s2 = s2 + "_UNAPPROVED"
            if s3 == "1":
                s3 = "NO FACULTY"
                sig_s3 = "NO SIGNATURE"
            else:
                sig_s3 = s3 + "_UNAPPROVED"
            if s4 == "1":
                s4 = "NO FACULTY"
                sig_s4 = "NO SIGNATURE"
            else:
                sig_s4 = s4 + "_UNAPPROVED"
            if s5 == "1":
                s5 = "NO FACULTY"
                sig_s5 = "NO SIGNATURE"
            else:
                sig_s5 = s5 + "_UNAPPROVED"
            if s6 == "1":
                s6 = "NO FACULTY"
                sig_s6 = "NO SIGNATURE"
            else:
                sig_s6 = s6 + "_UNAPPROVED"
            if s7 == "1":
                s7 = "NO FACULTY"
                sig_s7 = "NO SIGNATURE"
            else:
                sig_s7 = s7 + "_UNAPPROVED"
            if s8 == "1":
                s8 = "NO FACULTY"
                sig_s8 = "NO SIGNATURE"
            else:
                sig_s8 = s8 + "_UNAPPROVED"
            if s9 == "1":
                s9 = "NO FACULTY"
                sig_s9 = "NO SIGNATURE"
            else:
                sig_s9 = s9 + "_UNAPPROVED"
            if s10 == "1":
                s10 = "NO FACULTY"
                sig_s10 = "NO SIGNATURE"
            else:
                sig_s10 = s10 + "_UNAPPROVED"

            if t1 == "1":
                t1 = "NO FACULTY"
                sig_t1 = "NO SIGNATURE"
            else:
                sig_t1 = t1 + "_UNAPPROVED"
            if t2 == "1":
                t2 = "NO FACULTY"
                sig_t2 = "NO SIGNATURE"
            else:
                sig_t2 = t2 + "_UNAPPROVED"
            if t3 == "1":
                t3 = "NO FACULTY"
                sig_t3 = "NO SIGNATURE"
            else:
                sig_t3 = t3 + "_UNAPPROVED"
            if t4 == "1":
                t4 = "NO FACULTY"
                sig_t4 = "NO SIGNATURE"
            else:
                sig_t4 = t4 + "_UNAPPROVED"
            if t5 == "1":
                t5 = "NO FACULTY"
                sig_t5 = "NO SIGNATURE"
            else:
                sig_t5 = t5 + "_UNAPPROVED"
            if t6 == "1":
                t6 = "NO FACULTY"
                sig_t6 = "NO SIGNATURE"
            else:
                sig_t6 = t6 + "_UNAPPROVED"
            if t7 == "1":
                t7 = "NO FACULTY"
                sig_t7 = "NO SIGNATURE"
            else:
                sig_t7 = t7 + "_UNAPPROVED"
            if t8 == "1":
                t8 = "NO FACULTY"
                sig_t8 = "NO SIGNATURE"
            else:
                sig_t8 = t8 + "_UNAPPROVED"
            if t9 == "1":
                t9 = "NO FACULTY"
                sig_t9 = "NO SIGNATURE"
            else:
                sig_t9 = t9 + "_UNAPPROVED"
            if t10 == "1":
                t10 = "NO FACULTY"
                sig_t10 = "NO SIGNATURE"    
            else:
                sig_t10 = t10 + "_UNAPPROVED"

            if l == "1":
                l = "NO FACULTY"
                sig_l = "NO SIGNATURE"
            else:
                sig_l = l + "_UNAPPROVED"

            
            form = graduation_form_table.objects.create(name=name, student_id=student_id, course=course, shift=d,
                                                        study_load=e, status=f, enrolled_term=h, unenrolled_application_deadline=i,
                                                        trainP_startdate=j, trainP_enddate=k, instructor_name=l, day2=q2, day3=q3,
                                                        addday2=r2, addday3=r3, starttime2=u2, endtime2=v2, starttime3=u3, endtime3=v3,
                                                        add_starttime2=w2,  add_endtime2=x2, add_starttime3=w3,  add_endtime3=x3,

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
                                                        addsubject6=o6, addroom6=p6, addfaculty6=t6, add_starttime1_6=w1_6, add_endtime1_6=x1_6, addday1_6=r1_6,
                                                        addsubject7=o7, addroom7=p7, addfaculty7=t7, add_starttime1_7=w1_7, add_endtime1_7=x1_7, addday1_7=r1_7,
                                                        addsubject8=o8, addroom8=p8, addfaculty8=t8, add_starttime1_8=w1_8, add_endtime1_8=x1_8, addday1_8=r1_8,
                                                        addsubject9=o9, addroom9=p9, addfaculty9=t9, add_starttime1_9=w1_9, add_endtime1_9=x1_9, addday1_9=r1_9,
                                                        addsubject10=o10, addroom10=p10, addfaculty10=t10, add_starttime1_10=w1_10, add_endtime1_10=x1_10,
                                                        addday1_10=r1_10,
                                                        
                                                        signature1=sig_s1 , signature2=sig_s2 , signature3=sig_s3 , signature4=sig_s4 , signature5=sig_s5 ,
                                                        signature6=sig_s6 , signature7=sig_s7 , signature8=sig_s8 , signature9=sig_s9 , signature10=sig_s10 ,
                                                        addsignature1=sig_t1 , addsignature2=sig_t2 , addsignature3=sig_t3 , addsignature4=sig_t4 , addsignature5=sig_t5 ,
                                                        addsignature6=sig_t6 , addsignature7=sig_t7 , addsignature8=sig_t8 , addsignature9=sig_t9 , addsignature10=sig_t10 ,
                                                        sitsignature=sig_l )
            form.save()
            print('8')
                
            return redirect('student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    form = Graduation_form_table(request.POST or None)
    return render(request, 'html_files/4.3Student Graduation Form.html', {'form': form, 'a': a})

# alumnus not yet working


@login_required(login_url='/')
def alumnus_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "ALUMNUS":
        username = request.user.username
        print(username)

        st = graduation_form_table.objects.filter(student_id=username)
        st1 = clearance_form_table.objects.filter(student_id=username)
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/4.1Student Dashboard.html', {'st': st, 'st1': st1})


# @login_required(login_url='/')
# def clearance_form(request):
#     context = {}
#     if request.user.is_authenticated and request.user.user_type == "ALUMNUS":
#         if request.method == "POST":
#             form = clearance_form

#             # id_number = request.user.id()
#             student_id = request.POST.get('stud_id_420')
#             last_name = request.POST.get('ln_box_420')
#             first_name = request.POST.get('fn_box_420')
#             middle_name = request.POST.get('mn_box_420')
#             name = last_name + ", " + first_name + " " + middle_name
#             present_address = request.POST.get('padd_box_420')
#             course = request.POST.get('course_420')
#             date_filed = request.POST.get('dfiled_box_420')
#             date_admitted = request.POST.get('dait_box_420')
#             highschool_graduated = request.POST.get('hswg_box_420')
#             tupc_graduate = request.POST.get('grad_option_420')
#             highschool_graduated_date = request.POST.get('iydfiled_box_420')
#             terms = request.POST.get('notit_box_420')
#             amount = request.POST.get('amountp_box_420')
#             or_number = request.POST.get('receiptnum_box_42')
#             last_request = request.POST.get('requested_option_420')
#             last_request_date = request.POST.get('dbrtime_box_420')
#             last_term = request.POST.get('lasterm_box_420')
#             purpose_reason = request.POST.get('preq_box_420')
#             purpose = request.POST.get('purpose_request_420')
#             form = clearance_form_table.objects.create(student_id=student_id, name=name, present_address=present_address, course=course,
#                                                        date_filed=date_filed, date_admitted_in_tup=date_admitted,
#                                                        highschool_graduated=highschool_graduated, tupc_graduate=tupc_graduate, year_graduated_in_tupc=highschool_graduated_date,
#                                                        number_of_terms_in_tupc=terms, amount_paid=amount, have_previously_requested_form=last_request,
#                                                        date_of_previously_requested_form=last_request_date, last_term_in_tupc=last_term,
#                                                        purpose_of_request=purpose, purpose_of_request_reason=purpose_reason,)
#             form.save()

#             return redirect('alumnus_dashboard')
#     else:
#         messages.error(
#             request, "You are trying to access an unauthorized page and is forced to logout.")
#         return redirect('/')

#     return render(request, 'html_files/4.2Student Clearance Form.html', context)


@login_required(login_url='/')
def faculty_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        unapproved = request.user.full_name + "_UNAPPROVED"
        st = graduation_form_table.objects.filter(Q(signature1=unapproved) | Q(signature2=unapproved) | Q(signature3=unapproved) |
                                                  Q(signature4=unapproved) | Q(signature5=unapproved) | Q(signature6=unapproved) |
                                                  Q(signature7=unapproved) | Q(signature8=unapproved) | Q(signature9=unapproved) | Q(signature10=unapproved) |
                                                  Q(addsignature1=unapproved) | Q(addsignature2=unapproved) | Q(addsignature3=unapproved) |
                                                  Q(addsignature4=unapproved) | Q(addsignature5=unapproved) | Q(addsignature6=unapproved) |
                                                  Q(addsignature7=unapproved) | Q(addsignature8=unapproved) | Q(addsignature9=unapproved) |
                                                  Q(addsignature10=unapproved)).order_by('-id')
        print(unapproved)

        if request.user.department == "HOCS" or request.user.department == "HDLA" or request.user.department == "HDMS" or request.user.department == "HDPECS" or request.user.department == "HDIT" or request.user.department == "HDIE" or request.user.department == "HOCL" or request.user.department == "HOGS" or request.user.department == "HOSA" or request.user.department == "HADAA":
            st1 = clearance_form_table.objects.filter(Q(accountant_signature="UNAPPROVED") | Q(mathsci_dept_signature="UNAPPROVED") |
                                                      Q(pe_dept_signature="UNAPPROVED") | Q(ieduc_dept_signature="UNAPPROVED") | Q(it_dept_signature="UNAPPROVED") |
                                                      Q(ieng_dept_signature="UNAPPROVED") | Q(library_signature="UNAPPROVED") |
                                                      Q(guidance_office_signature="UNAPPROVED") | Q(osa_signature="UNAPPROVED") |
                                                      Q(academic_affairs_signature="UNAPPROVED")).order_by('-id')
            return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, 'st1': st1, })

        with_clearance = clearance_form_table.objects.filter(course_adviser=request.user.full_name) 
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, 'with_clearance':with_clearance })


@login_required(login_url='/')
def faculty_dashboard_clearance_list(request):
    # val = request.POST.get('valdeterminer')
    # userdeterminer = request.POST.get('userdeterminer')
    # print(val, userdeterminer)
    userdeterminer = request.user.department
    f_n = request.user.full_name
    f_n_unapproved = request.user.full_name + "_UNAPPROVED"
    f_n_approved = request.user.full_name + "_APPROVED"
    signature = request.user.uploaded_signature
    signature_datetime = request.user.signature_timesaved
    id_Facultynumber = request.user.id
    print(signature)
        
    st = ""

    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if userdeterminer == "HOCS":
            st = clearance_form_table.objects.filter(
                accountant_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                accountant_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HDMS":
            st = clearance_form_table.objects.filter(
                mathsci_dept_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                mathsci_dept_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HDPECS":
            st = clearance_form_table.objects.filter(
                pe_dept_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                pe_dept_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HDED":
            st = clearance_form_table.objects.filter(
                ieduc_dept_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                ieduc_dept_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})
            
        elif userdeterminer == "HDIT":
            st = clearance_form_table.objects.filter(
                it_dept_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                it_dept_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})
            
        elif userdeterminer == "HDIE":
            st = clearance_form_table.objects.filter(
                ieng_dept_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                ieng_dept_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})
            
        elif userdeterminer == "HOCL":
            
            st = clearance_form_table.objects.filter(
                library_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                library_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HOGS":
            st = clearance_form_table.objects.filter(
                guidance_office_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                guidance_office_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HOSA":
            st = clearance_form_table.objects.filter(
                osa_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                osa_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})

        elif userdeterminer == "HADAA":
            st = clearance_form_table.objects.filter(
                academic_affairs_signature="UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                academic_affairs_signature="APPROVED").values()
            
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1})
        
        if clearance_form_table.objects.filter(
                course_adviser=f_n):
            st = clearance_form_table.objects.filter(
                course_adviser_signature__icontains="_UNAPPROVED").values()
            st1 = clearance_form_table.objects.filter(
                course_adviser_signature__icontains="_APPROVED").values()
           
            return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'st1': st1,'saved_signature' : signature, 'signature_datetime' : signature_datetime, 'id' : id_Facultynumber})

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st,'saved_signature' : signature, 'signature_datetime' : signature_datetime, 'id' : id_Facultynumber})


@login_required(login_url='/')
def update(request, id):
    print('here')
    if request.user.is_authenticated and request.user.user_type == "FACULTY":     
        name_temp = clearance_form_table.objects.filter(
            id=id).values_list('name', flat=True).distinct()
        email_temp = clearance_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            username=email_temp[0]).values_list('email', flat=True).distinct()
        rec_email = email[0]
        f_n = request.user.full_name
        f_n_approved = request.user.full_name + "_APPROVED"
        
        print(f_n) 

        print(rec_email)
        if clearance_form_table.objects.filter(course_adviser=f_n, id=id):
            clearance_form_table.objects.filter(id=id).update(
                course_adviser_signature=f_n_approved)
            
        if request.user.department == "HOCS":
            clearance_form_table.objects.filter(
                id=id).update(accountant_signature=f_n_approved)

        if request.user.department == "HDMS":
            clearance_form_table.objects.filter(id=id).update(
                mathsci_dept_signature=f_n_approved)

        if request.user.department == "HDPECS":
            clearance_form_table.objects.filter(
                id=id).update(pe_dept_signature=f_n_approved)

        if request.user.department == "HDED":
            clearance_form_table.objects.filter(
                id=id).update(ieduc_dept_signature=f_n_approved)

        if request.user.department == "HDIT":
            clearance_form_table.objects.filter(
                id=id).update(it_dept_signature=f_n_approved)

        if request.user.department == "HDIE":
            clearance_form_table.objects.filter(
                id=id).update(ieng_dept_signature=f_n_approved)

        if request.user.department == "HOCL":
            clearance_form_table.objects.filter(
                id=id).update(library_signature=f_n_approved)
            
        if request.user.department == "HOGS":
            clearance_form_table.objects.filter(id=id).update(
                guidance_office_signature=f_n_approved)

        if request.user.department == "HOSA":
            clearance_form_table.objects.filter(
                id=id).update(osa_signature=f_n_approved)

        if request.user.department == "HADAA":
            clearance_form_table.objects.filter(id=id).update(
                academic_affairs_signature=f_n_approved)
        
        approved_text = "APPROVED"
        approved_courseadv = "_APPROVED"
        approval_status_checker=clearance_form_table.objects.filter(
            Q(liberal_arts_signature__exact=approved_text) &
            Q(accountant_signature__exact=approved_text) &
            Q(mathsci_dept_signature__exact=approved_text) &
            Q(pe_dept_signature__exact=approved_text) &
            Q(ieduc_dept_signature__exact=approved_text) &
            Q(it_dept_signature__exact=approved_text) &
            Q(ieng_dept_signature__exact=approved_text) &
            Q(library_signature__exact=approved_text) &
            Q(guidance_office_signature__exact=approved_text) &
            Q(osa_signature__exact=approved_text) &
            Q(academic_affairs_signature__exact=approved_text) &
            Q(course_adviser_signature__endswith=approved_courseadv), id=id)
        if approval_status_checker:
            clearance_form_table.objects.filter(
                        id=id).update(approval_status="APPROVED")
            
            name = name_temp[0]
            # Alumnus_table.objects.filter(
            #             Name=name).update(clearance="✔") this section is on hold
            request_form_table.objects.filter(
                        name=name).update(clearance="✔")
    
        subject = 'Clearance Form Approved'
        message = f'Mr./Ms. {request.user.last_name} has approved your form. Check out our site to see your progress.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [rec_email, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False, auth_user=None,
                  auth_password=None, connection=None, html_message=None)

        messages.success(request, "Form Approved.")
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return redirect(faculty_dashboard_clearance_list)


@login_required(login_url='/')
def faculty_dashboard_graduation_list(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        #signature
        signature = request.user.uploaded_signature
        signature_datetime = request.user.signature_timesaved
        id_Facultynumber = request.user.id
        print(signature)
            
        user = str(request.POST.get('namedeterminer2'))    
        global f_n
        f_n = ""
        global field_sig
        field_sig = ""
        temp = request.POST.get('namedeterminer2')
        temp = str(temp) + "_UNAPPROVED"
        f_n = temp
        print('trial')
        print(f_n)
        val = request.POST.get('valdeterminer')
        
        
        
        # USE REQUEST.USER TO AUTO SHOW DATA
        full_name = request.user.full_name +"_UNAPPROVED"
        # st = graduation_form_table.objects.filter(Q(faculty1=full_name) | Q(faculty2=full_name) | Q(faculty3=full_name) |
        #                                           Q(faculty4=full_name) | Q(faculty5=full_name) | Q(faculty6=full_name) |
        #                                           Q(faculty7=full_name) | Q(faculty8=full_name) | Q(faculty9=full_name) | Q(faculty10=full_name) |
        #                                           Q(addfaculty1=full_name) | Q(addfaculty2=full_name) | Q(addfaculty3=full_name) |
        #                                           Q(addfaculty4=full_name) | Q(addfaculty5=full_name) | Q(addfaculty6=full_name) |
        #                                           Q(addfaculty7=full_name) | Q(addfaculty8=full_name) | Q(addfaculty9=full_name) | Q(addfaculty10=full_name))
        st =""
        res= graduation_form_table.objects.filter(
            Q(signature1__contains=full_name) |
            Q(signature2__contains=full_name) |
            Q(signature3__contains=full_name) |
            Q(signature4__contains=full_name) |
            Q(signature5__contains=full_name) |
            Q(signature6__contains=full_name) |
            Q(signature7__contains=full_name) |
            Q(signature8__contains=full_name) |
            Q(signature9__contains=full_name) |
            Q(signature10__contains=full_name) |
            Q(addsignature1__contains=full_name) |
            Q(addsignature2__contains=full_name) |
            Q(addsignature3__contains=full_name) |
            Q(addsignature4__contains=full_name) |
            Q(addsignature5__contains=full_name) |
            Q(addsignature6__contains=full_name) |
            Q(addsignature7__contains=full_name) |
            Q(addsignature8__contains=full_name) |
            Q(addsignature9__contains=full_name) |
            Q(addsignature10__contains=full_name) |
            Q(sitsignature__contains=full_name) 
        ) 
        if res:

        # if val == "UNAPPROVED":
        #     full_name = request.user.full_name + "_UNAPPROVED"
        #     print(full_name)
            st = graduation_form_table.objects.filter(Q(signature1=full_name) | Q(signature2=full_name) | Q(signature3=full_name) |
                                                      Q(signature4=full_name) | Q(signature5=full_name) | Q(signature6=full_name) |
                                                      Q(signature7=full_name) | Q(signature8=full_name) | Q(signature9=full_name) | Q(signature10=full_name) |
                                                      Q(addsignature1=full_name) | Q(addsignature2=full_name) | Q(addsignature3=full_name) |
                                                      Q(addsignature4=full_name) | Q(addsignature5=full_name) | Q(addsignature6=full_name) |
                                                      Q(addsignature7=full_name) | Q(addsignature8=full_name) | Q(addsignature9=full_name) |
                                                      Q(addsignature10=full_name) | Q(sitsignature=full_name))
        # elif val == "APPROVED":
        approval = request.user.full_name + "_APPROVED"
        st1 = graduation_form_table.objects.filter(Q(signature1=approval) | Q(signature2=approval) | Q(signature3=approval) |
                                                    Q(signature4=approval) | Q(signature5=approval) | Q(signature6=approval) |
                                                    Q(signature7=approval) | Q(signature8=approval) | Q(signature9=approval) | Q(signature10=approval) |
                                                    Q(addsignature1=approval) | Q(addsignature2=approval) | Q(addsignature3=approval) |
                                                    Q(addsignature4=approval) | Q(addsignature5=approval) | Q(addsignature6=approval) |
                                                    Q(addsignature7=approval) | Q(addsignature8=approval) | Q(addsignature9=approval) |
                                                    Q(addsignature10=approval) | Q(sitsignature=approval))
    
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.3Faculty Graduation List.html', {'st': st, 'val': val, 'st1': st1, 'saved_signature' : signature, 'signature_datetime' : signature_datetime, 'id' : id_Facultynumber})


@login_required(login_url='/')
def updategrad(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        name_temp = graduation_form_table.objects.filter(
            id=id).values_list('name', flat=True).distinct()
        email_temp = graduation_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            username=email_temp[0]).values_list('email', flat=True).distinct()
 
        rec_email = email[0]
        print(rec_email) 
        f_n1 = request.user.full_name + '_UNAPPROVED'
        print("this is f_n", f_n1)  
        a = graduation_form_table.objects.filter(
            signature1__contains=f_n1, id=id)
        b = graduation_form_table.objects.filter(
            signature2__contains=f_n1, id=id)
        c = graduation_form_table.objects.filter(
            signature3__contains=f_n1, id=id)
        d = graduation_form_table.objects.filter(
            signature4__contains=f_n1, id=id)
        e = graduation_form_table.objects.filter(
            signature5__contains=f_n1, id=id)
        f = graduation_form_table.objects.filter(
            signature6__contains=f_n1, id=id)
        g = graduation_form_table.objects.filter(
            signature7__contains=f_n1, id=id)
        h = graduation_form_table.objects.filter(
            signature8__contains=f_n1, id=id)
        i = graduation_form_table.objects.filter(
            signature9__contains=f_n1, id=id)
        j = graduation_form_table.objects.filter(
            signature10__contains=f_n1, id=id)
        k = graduation_form_table.objects.filter(
            addsignature1__contains=f_n1, id=id)
        l = graduation_form_table.objects.filter(
            addsignature2__contains=f_n1, id=id)
        m = graduation_form_table.objects.filter(
            addsignature3__contains=f_n1, id=id)
        n = graduation_form_table.objects.filter(
            addsignature4__contains=f_n1, id=id)
        o = graduation_form_table.objects.filter(
            addsignature5__contains=f_n1, id=id)
        p = graduation_form_table.objects.filter(
            addsignature6__contains=f_n1, id=id)
        q = graduation_form_table.objects.filter(
            addsignature7__contains=f_n1, id=id)
        r = graduation_form_table.objects.filter(
            addsignature8__contains=f_n1, id=id)
        s = graduation_form_table.objects.filter(
            addsignature9__contains=f_n1, id=id)
        t = graduation_form_table.objects.filter(
            addsignature10__contains=f_n1, id=id)
        u = graduation_form_table.objects.filter(
            sitsignature__contains=f_n1, id=id)
             
        approval =request.user.full_name + "_APPROVED"
        if a.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature1=approval)

        if b.exists(): 
            graduation_form_table.objects.filter(
                id=id).update(signature2=approval)
            
        if c.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature3=approval)
            
        if d.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature4=approval)
            
        if e.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature5=approval)
            
        if f.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature6=approval)
            
        if g.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature7=approval)
            
        if h.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature8=approval)
            
        if i.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature9=approval)
            
        if j.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature10=approval)
            
        if k.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature1=approval)
            
        if l.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature2=approval)
            
        if m.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature3=approval)
            
        if n.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature4=approval)
            
        if o.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature5=approval)
            
        if p.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature6=approval)
            
        if q.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature7=approval)
            
        if r.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature8=approval)
            
        if s.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature9=approval)
            
        if t.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature10=approval)

        if u.exists():
            graduation_form_table.objects.filter(
                id=id).update(sitsignature=approval)

        approved_text = "_APPROVED"

        approval_status_checker_2=graduation_form_table.objects.exclude(
            Q(signature1="NO SIGNATURE") ,
            Q(signature2="NO SIGNATURE") ,
            Q(signature3="NO SIGNATURE") ,
            Q(signature4="NO SIGNATURE") ,
            Q(signature5="NO SIGNATURE") ,
            Q(signature6="NO SIGNATURE") ,
            Q(signature7="NO SIGNATURE") ,
            Q(signature8="NO SIGNATURE") ,
            Q(signature9="NO SIGNATURE") ,
            Q(signature10="NO SIGNATURE") ,
            Q(addsignature1="NO SIGNATURE") ,
            Q(addsignature2="NO SIGNATURE") ,
            Q(addsignature3="NO SIGNATURE") ,
            Q(addsignature4="NO SIGNATURE") ,
            Q(addsignature5="NO SIGNATURE") ,
            Q(addsignature6="NO SIGNATURE") ,
            Q(addsignature7="NO SIGNATURE") ,
            Q(addsignature8="NO SIGNATURE") ,
            Q(addsignature9="NO SIGNATURE") ,
            Q(addsignature10="NO SIGNATURE") ,
            Q(sitsignature="NO SIGNATURE"), id=id).filter(
            Q(signature1__endswith=approved_text) |
            Q(signature2__endswith=approved_text) |
            Q(signature3__endswith=approved_text) |
            Q(signature4__endswith=approved_text) |
            Q(signature5__endswith=approved_text) |
            Q(signature6__endswith=approved_text) |
            Q(signature7__endswith=approved_text) |
            Q(signature8__endswith=approved_text) |
            Q(signature9__endswith=approved_text) |
            Q(signature10__endswith=approved_text) |
            Q(addsignature1__endswith=approved_text) |
            Q(addsignature2__endswith=approved_text) |
            Q(addsignature3__endswith=approved_text) |
            Q(addsignature4__endswith=approved_text) |
            Q(addsignature5__endswith=approved_text) |
            Q(addsignature6__endswith=approved_text) |
            Q(addsignature7__endswith=approved_text) |
            Q(addsignature8__endswith=approved_text) |
            Q(addsignature9__endswith=approved_text) |
            Q(addsignature10__endswith=approved_text) |
            Q(sitsignature__endswith=approved_text), id=id)

        print("this is", approval_status_checker_2)
        if approval_status_checker_2:
            print(approval_status_checker_2)
            graduation_form_table.objects.filter(
                id=id).update(approval_status="APPROVED")
            
        messages.success(request, "Form Approved.")
        subject = 'Graduation Form Approved'
        message = f'Mr./Ms. {request.user.last_name} has approved your form. Check out our site to see your progress.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [rec_email, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False, auth_user=None,
                  auth_password=None, connection=None, html_message=None)

        return redirect(faculty_dashboard_graduation_list)
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/5.3Faculty Graduation List.html')


@login_required(login_url='/')
def registrar_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        # CLEARANCE FORMS
        all = clearance_form_table.objects.all()
        cBSCE = clearance_form_table.objects.filter(
            course="BSCE").values().count()
        cBSEE = clearance_form_table.objects.filter(
            course="BSEE").values().count()
        cBSME = clearance_form_table.objects.filter(
            course="BSME").values().count()
        cBSIE_ICT = clearance_form_table.objects.filter(
            course="BSIE-ICT").values().count()
        cBSIE_HE = clearance_form_table.objects.filter(
            course="BSIE-HE").values().count()
        cBTTE_CP = clearance_form_table.objects.filter(
            course="BTTE-CP").values().count()
        cBTTE_EI = clearance_form_table.objects.filter(
            course="BTTE-EI").values().count()
        cBTTE_AU = clearance_form_table.objects.filter(
            course="BTTE-AU").values().count()
        cBTTE_HVACT = clearance_form_table.objects.filter(
            course="BTTE-HVACT").values().count()
        cBTTE_E = clearance_form_table.objects.filter(
            course="BTTE-E").values().count()
        cBGT_AT = clearance_form_table.objects.filter(
            course="BGT-AT").values().count()
        cBET_CT = clearance_form_table.objects.filter(
            course="BET-CT").values().count()
        cBET_ET = clearance_form_table.objects.filter(
            course="BET-ET").values().count()
        cBET_EsET = clearance_form_table.objects.filter(
            course="BET-EsET").values().count()
        cBET_CoET = clearance_form_table.objects.filter(
            course="BET-CoET").values().count()
        cBET_MT = clearance_form_table.objects.filter(
            course="BET-MT").values().count()
        cBET_PPT = clearance_form_table.objects.filter(
            course="BET-PPT").values().count()
        cBET_AT = clearance_form_table.objects.filter(
            course="BET-AT").values().count()

        # GRADUATION FORMS
        gBSCE = graduation_form_table.objects.filter(
            course="BSCE").values().count()
        gBSEE = graduation_form_table.objects.filter(
            course="BSEE").values().count()
        gBSME = graduation_form_table.objects.filter(
            course="BSME").values().count()
        gBSIE_ICT = graduation_form_table.objects.filter(
            course="BSIE-ICT").values().count()
        gBSIE_HE = graduation_form_table.objects.filter(
            course="BSIE-HE").values().count()
        gBTTE_CP = graduation_form_table.objects.filter(
            course="BTTE-CP").values().count()
        gBTTE_EI = graduation_form_table.objects.filter(
            course="BTTE-EI").values().count()
        gBTTE_AU = graduation_form_table.objects.filter(
            course="BTTE-AU").values().count()
        gBTTE_HVACT = graduation_form_table.objects.filter(
            course="BTTE-HVACT").values().count()
        gBTTE_E = graduation_form_table.objects.filter(
            course="BTTE-E").values().count()
        gBGT_AT = graduation_form_table.objects.filter(
            course="BGT-AT").values().count()
        gBET_CT = graduation_form_table.objects.filter(
            course="BET-CT").values().count()
        gBET_ET = graduation_form_table.objects.filter(
            course="BET-ET").values().count()
        gBET_EsET = graduation_form_table.objects.filter(
            course="BET-EsET").values().count()
        gBET_CoET = graduation_form_table.objects.filter(
            course="BET-CoET").values().count()
        gBET_MT = graduation_form_table.objects.filter(
            course="BET-MT").values().count()
        gBET_PPT = graduation_form_table.objects.filter(
            course="BET-PPT").values().count()
        gBET_AT = graduation_form_table.objects.filter(
            course="BET-AT").values().count()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/7.1Registrar Dashboard.html',
                  {'all': all, 'cBSCE': cBSCE, 'cBSEE': cBSEE, 'cBSME': cBSME, 'cBSIE_ICT': cBSIE_ICT,
                   'cBSIE_HE': cBSIE_HE, 'cBTTE_CP': cBTTE_CP, 'cBTTE_EI': cBTTE_EI, 'cBTTE_AU': cBTTE_AU,
                   'cBTTE_HVACT': cBTTE_HVACT, 'cBTTE_E': cBTTE_E, 'cBGT_AT': cBGT_AT, 'cBET_CT': cBET_CT,
                   'cBET_ET': cBET_ET, 'cBET_EsET': cBET_EsET, 'cBET_CoET': cBET_CoET, 'cBET_MT': cBET_MT,
                   'cBET_PPT': cBET_PPT, 'cBET_AT': cBET_AT,

                   'gBSCE': gBSCE, 'gBSEE': gBSEE, 'gBSME': gBSME, 'gBSIE_ICT': gBSIE_ICT,
                   'gBSIE_HE': gBSIE_HE, 'gBTTE_CP': gBTTE_CP, 'gBTTE_EI': gBTTE_EI, 'gBTTE_AU': gBTTE_AU,
                   'gBTTE_HVACT': gBTTE_HVACT, 'gBTTE_E': gBTTE_E, 'gBGT_AT': gBGT_AT, 'gBET_CT': gBET_CT,
                   'gBET_ET': gBET_ET, 'gBET_EsET': gBET_EsET, 'gBET_CoET': gBET_CoET, 'gBET_MT': gBET_MT,
                   'gBET_PPT': gBET_PPT, 'gBET_AT': gBET_AT,
                   })


@login_required(login_url='/')
def name_list(request):
    enteruser = request.POST.get('validator')
    to_edit = request.POST.get('validator')
    p = user_table.objects.filter(username=enteruser).values_list(
        to_edit, flat=True).distinct()
    va = p[0]


@login_required(login_url='/')
def updateAddress(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        print('here')
        if request.method == "POST":
            saddress = request.POST.get('address_box_041')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(address=saddress)
            return redirect('/student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/4.1Student Dashboard.html')


@login_required(login_url='/')
def updateEmail(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS" or "OLD STUDENT":
        if request.method == "POST":
            semail = request.POST.get('ea_box_041')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(email=semail)
            return redirect('/student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.1Student Dashboard.html')


@login_required(login_url='/')
def updateCourse(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        if request.method == "POST":
            scourse = request.POST.get('course_drp_041')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(course=scourse)
            return redirect('/student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.1Student Dashboard.html')


@login_required(login_url='/')
def updatePassword(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        if request.method == "POST":
            new_password = request.POST.get('new_pass_041')
            confirm_password = request.POST.get('confirm_pass_041')

            if new_password == confirm_password:
                print("same")
                v = request.POST.get('validator2')
                u = user_table.objects.get(username__exact=v)

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


@login_required(login_url='/')
def updateContact(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        print('here')
        if request.method == "POST":
            scontact = request.POST.get('cnum_box_041')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                contact_number=scontact)
            return redirect('/student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/4.1Student Dashboard.html')


@login_required(login_url='/')
def faculty_updateAddress(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print('here')
        if request.method == "POST":
            faddress = request.POST.get('address_box_051')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(address=faddress)
            return redirect('/faculty_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    print('running')
    return render(request, 'html_files/5.1Faculty Dashboard.html')


@login_required(login_url='/')
def faculty_updateEmail(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print('here')
        if request.method == "POST":
            femail = request.POST.get('ea_box_051')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(email=femail)
            return redirect('/faculty_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    print('running')
    return render(request, 'html_files/5.1Faculty Dashboard.html')


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
                u = user_table.objects.get(username__exact=v)

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


@login_required(login_url='/')
def faculty_updateContact(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print('here')
        if request.method == "POST":
            scontact = request.POST.get('cnum_box_051')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                contact_number=scontact)
            return redirect('/faculty_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.1Faculty Dashboard.html')


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
                u = user_table.objects.get(username__exact=v)

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


@login_required(login_url='/')
def display_clearform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS" or "OLD STUDENT" or "FACULTY" or "REGISTRAR":
        clearance = clearance_form_table.objects.filter(id=id).values()
        
        #Signature Display
        #ACCOUNTANT
        check_status = clearance_form_table.objects.filter(id=id,accountant_signature__icontains = 'UNAPPROVED')
        if check_status:
            accountant = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('accountant_signature', flat=True).distinct()
            acc_sig = str(faculty_approved[0])
            fac_name_get = acc_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            account_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            accountant = account_sig[0]
            
        #COURSE ADVISER
        check_status = clearance_form_table.objects.filter(id=id,course_adviser_signature__icontains = 'UNAPPROVED')
        if check_status:
            course_adviser = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('course_adviser_signature', flat=True).distinct()
            adviser_sig = str(faculty_approved[0])
            fac_name_get = adviser_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            ca_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            course_adviser = ca_sig[0]
        
        #LIBERAL ARTS
        check_status = clearance_form_table.objects.filter(id=id,liberal_arts_signature__icontains = 'UNAPPROVED')
        if check_status:
            liberal_arts = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('liberal_arts_signature', flat=True).distinct()
            lib_sig = str(faculty_approved[0])
            fac_name_get = lib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            libart_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            liberal_arts = libart_sig[0]
        
        #CAMPUS LIBRARIAN
        check_status = clearance_form_table.objects.filter(id=id,library_signature__icontains = 'UNAPPROVED')
        if check_status:
            campus_library = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('library_signature_signature', flat=True).distinct()
            camlib_sig = str(faculty_approved[0])
            fac_name_get = camlib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            cam_lib_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            campus_library = cam_lib_sig[0]
        
        #MATH & SCIENCES
        check_status = clearance_form_table.objects.filter(id=id,mathsci_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            math_and_science = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('mathsci_dept_signature', flat=True).distinct()
            mas_sig = str(faculty_approved[0])
            fac_name_get = mas_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            mathsci_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            math_and_science = mathsci_sig[0]
            
        #GUIDANCE COUNCELOR
        check_status = clearance_form_table.objects.filter(id=id,guidance_office_signature__icontains = 'UNAPPROVED')
        if check_status:
            guidance = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('guidance_office_signature', flat=True).distinct()
            guid_sig = str(faculty_approved[0])
            fac_name_get = guid_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            gui_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            guidance = gui_sig[0]
        
        #DPECS
        check_status = clearance_form_table.objects.filter(id=id,pe_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            dpecs = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('pe_dept_signature', flat=True).distinct()
            pe_sig = str(faculty_approved[0])
            fac_name_get = pe_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            pe_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            dpecs = pe_dept_sig[0]
        
        #OSA
        check_status = clearance_form_table.objects.filter(id=id,osa_signature__icontains = 'UNAPPROVED')
        if check_status:
            osa = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('osa_signature', flat=True).distinct()
            student_osa_sig = str(faculty_approved[0])
            fac_name_get = student_osa_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            student_affairs_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            osa = student_affairs_sig[0]
        
        #ADAA
        check_status = clearance_form_table.objects.filter(id=id,academic_affairs_signature__icontains = 'UNAPPROVED')
        if check_status:
            adaa = "UNAPPROVED"
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('academic_affairs_signature', flat=True).distinct()
            asst_dir_acad_sig = str(faculty_approved[0])
            fac_name_get = asst_dir_acad_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            adaa_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            adaa = adaa_sig[0]
        
        #INDUSTRIAL
        check_status = clearance_form_table.objects.filter(id=id,ieduc_dept_signature__icontains = 'UNAPPROVED',it_dept_signature__icontains = 'UNAPPROVED',ieng_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            industrial = "UNAPPROVED"
            it_department = "NONE"
        else:
            if clearance_form_table.objects.filter(id=id,ieduc_dept_signature__icontains = 'UNAPPROVED'):
                pass
            else:
                faculty_approved = clearance_form_table.objects.filter(id=id).values_list('ieduc_dept_signature', flat=True).distinct()
                ieduc = str(faculty_approved[0])
                fac_name_get = ieduc.split('_',1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)
                
                ieduc_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                industrial = ieduc_sig[0]
                it_department = "EDUCATOR"
            
            if clearance_form_table.objects.filter(id=id,it_dept_signature__icontains = 'UNAPPROVED'):
                pass
            else:
                faculty_approved = clearance_form_table.objects.filter(id=id).values_list('it_dept_signature', flat=True).distinct()
                it = str(faculty_approved[0])
                fac_name_get = it.split('_',1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)
                
                it_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                industrial = it_dept_sig[0]
                it_department = "TECHNOLOGIES"
                
            if clearance_form_table.objects.filter(id=id,ieng_dept_signature__icontains = 'UNAPPROVED'):
                pass
            else:
                faculty_approved = clearance_form_table.objects.filter(id=id).values_list('ieng_dept_signature', flat=True).distinct()
                eng = str(faculty_approved[0])
                fac_name_get = eng.split('_',1)[0]
                str_fac_name = str(fac_name_get)
                print(str_fac_name)
                
                eng_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
                industrial = eng_dept_sig[0]
                it_department = "ENGINEERS"
 
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {
        'clearance': clearance, 
        'accountant': accountant,
        'liberal_arts': liberal_arts,
        'math_and_science': math_and_science,
        'dpecs' : dpecs,
        'industrial': industrial,
        'it_department' : it_department,
        'course_adviser' : course_adviser,
        'campus_library' : campus_library,
        'guidance' : guidance,
        'osa' : osa,
        'adaa' : adaa 
    }

    print('running')
    return render(request, 'html_files/clearance_form_display.html', context)


@login_required(login_url='/')
def display_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "OLD STUDENT" or "ALUMNUS" or "FACULTY" or "REGISTRAR":
        graduation = graduation_form_table.objects.filter(id=id).values()
        
        #SUBJECT #1
        check_status = graduation_form_table.objects.filter(id=id,signature1__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature1 = 'NO SIGNATURE')
        if check_status:
            subject_1 = "UNAPPROVED"
        elif check_signature:
            subject_1 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature1', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty1_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_1 = faculty1_sig[0]
            
        #SUBJECT #2
        check_status = graduation_form_table.objects.filter(id=id,signature2__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature2 = 'NO SIGNATURE')
        if check_status:
            subject_2 = "UNAPPROVED"
        elif check_signature:
            subject_2 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature2', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty2_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_2 = faculty2_sig[0]
        
        #SUBJECT #3
        check_status = graduation_form_table.objects.filter(id=id,signature3__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature3 = 'NO SIGNATURE')
        if check_status:
            subject_3 = "UNAPPROVED"
        elif check_signature:
            subject_3 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature3', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty3_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_3 = faculty3_sig[0]
        
        #SUBJECT #4
        check_status = graduation_form_table.objects.filter(id=id,signature4__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature4 = 'NO SIGNATURE')
        if check_status:
            subject_4 = "UNAPPROVED"
        elif check_signature:
            subject_4 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature4', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty4_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_4 = faculty4_sig[0]
            
        #SUBJECT #5
        check_status = graduation_form_table.objects.filter(id=id,signature5__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature5 = 'NO SIGNATURE')
        if check_status:
            subject_5 = "UNAPPROVED"
        elif check_signature:
            subject_5 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature5', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty5_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_5 = faculty5_sig[0]
        
        #SUBJECT #6
        check_status = graduation_form_table.objects.filter(id=id,signature6__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature6 = 'NO SIGNATURE')
        if check_status:
            subject_6 = "UNAPPROVED"
        elif check_signature:
            subject_6 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature6', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty6_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_6 = faculty6_sig[0]
            
        #SUBJECT #7
        check_status = graduation_form_table.objects.filter(id=id,signature7__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature7 = 'NO SIGNATURE')
        if check_status:
            subject_7 = "UNAPPROVED"
        elif check_signature:
            subject_7 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature7', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty7_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_7 = faculty7_sig[0]
            
        #SUBJECT #8
        check_status = graduation_form_table.objects.filter(id=id,signature8__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature8 = 'NO SIGNATURE')
        if check_status:
            subject_8 = "UNAPPROVED"
        elif check_signature:
            subject_8 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature8', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty8_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_8 = faculty8_sig[0]
        
        #SUBJECT #9
        check_status = graduation_form_table.objects.filter(id=id,signature9__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature9 = 'NO SIGNATURE')
        if check_status:
            subject_9 = "UNAPPROVED"
        elif check_signature:
            subject_9 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature9', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty9_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_9 = faculty9_sig[0]
            
        #SUBJECT #10
        check_status = graduation_form_table.objects.filter(id=id,signature10__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature10 = 'NO SIGNATURE')
        if check_status:
            subject_10 = "UNAPPROVED"
        elif check_signature:
            subject_10 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('signature10', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            faculty10_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            subject_10 = faculty10_sig[0]
            
        #ADD SUBJECT #1
        check_status = graduation_form_table.objects.filter(id=id,addsignature1__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature1 = 'NO SIGNATURE')
        if check_status:
            addsubject_1 = "UNAPPROVED"
        elif check_signature:
            addsubject_1 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature1', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty1_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_1 = addfaculty1_sig[0]
            
        #ADD SUBJECT #2
        check_status = graduation_form_table.objects.filter(id=id,addsignature2__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature2 = 'NO SIGNATURE')
        if check_status:
            addsubject_2 = "UNAPPROVED"
        elif check_signature:
            addsubject_2 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature2', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty2_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_2 = addfaculty2_sig[0]
        
        #ADD SUBJECT #3
        check_status = graduation_form_table.objects.filter(id=id,addsignature3__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature3 = 'NO SIGNATURE')
        if check_status:
            addsubject_3 = "UNAPPROVED"
        elif check_signature:
            addsubject_3 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature3', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty3_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_3 = addfaculty3_sig[0]
        
        #ADD SUBJECT #4
        check_status = graduation_form_table.objects.filter(id=id,addsignature4__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature4 = 'NO SIGNATURE')
        if check_status:
            addsubject_4 = "UNAPPROVED"
        elif check_signature:
            addsubject_4 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature4', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty4_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_4 = addfaculty4_sig[0]
            
        #ADD SUBJECT #5
        check_status = graduation_form_table.objects.filter(id=id,addsignature5__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature5 = 'NO SIGNATURE')
        if check_status:
            addsubject_5 = "UNAPPROVED"
        elif check_signature:
            addsubject_5 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature5', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty5_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_5 = addfaculty5_sig[0]
        
        #ADD SUBJECT #6
        check_status = graduation_form_table.objects.filter(id=id,addsignature6__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature6 = 'NO SIGNATURE')
        if check_status:
            addsubject_6 = "UNAPPROVED"
        elif check_signature:
            addsubject_6 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature6', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty6_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_6 = addfaculty6_sig[0]
            
        #ADD SUBJECT #7
        check_status = graduation_form_table.objects.filter(id=id,addsignature7__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature7 = 'NO SIGNATURE')
        if check_status:
            addsubject_7 = "UNAPPROVED"
        elif check_signature:
            addsubject_7 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature7', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty7_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_7 = addfaculty7_sig[0]
            
        #ADD SUBJECT #8
        check_status = graduation_form_table.objects.filter(id=id,addsignature8__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature8 = 'NO SIGNATURE')
        if check_status:
            addsubject_8 = "UNAPPROVED"
        elif check_signature:
            addsubject_8 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature8', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty8_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_8 = addfaculty8_sig[0]
        
        #ADD SUBJECT #9
        check_status = graduation_form_table.objects.filter(id=id,addsignature9__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature9 = 'NO SIGNATURE')
        if check_status:
            addsubject_9 = "UNAPPROVED"
        elif check_signature:
            addsubject_9 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature9', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty9_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_9 = addfaculty9_sig[0]
            
        #ADD SUBJECT #10
        check_status = graduation_form_table.objects.filter(id=id,addsignature10__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,addsignature10 = 'NO SIGNATURE')
        if check_status:
            addsubject_10 = "UNAPPROVED"
        elif check_signature:
            addsubject_10 = ""
        else:
            faculty_approved = graduation_form_table.objects.filter(id=id).values_list('addsignature10', flat=True).distinct()
            sub_sig = str(faculty_approved[0])
            fac_name_get = sub_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            addfaculty10_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            addsubject_10 = addfaculty10_sig[0]
        
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    context = {
        'graduation': graduation,
        'subject_1' : subject_1,
        'subject_2' : subject_2,
        'subject_3' : subject_3,
        'subject_4' : subject_4,
        'subject_5' : subject_5,
        'subject_6' : subject_6,
        'subject_7' : subject_7,
        'subject_8' : subject_8,
        'subject_9' : subject_9,
        'subject_10' : subject_10,
        'addsubject_1' : addsubject_1,
        'addsubject_2' : addsubject_2,
        'addsubject_3' : addsubject_3,
        'addsubject_4' : addsubject_4,
        'addsubject_5' : addsubject_5,
        'addsubject_6' : addsubject_6,
        'addsubject_7' : addsubject_7,
        'addsubject_8' : addsubject_8,
        'addsubject_9' : addsubject_9,
        'addsubject_10' : addsubject_10
    }
    print('running')
    return render(request, 'html_files/graduation_form_display.html', context)


@login_required(login_url='/')
def registrar_dashboard_clearance_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        
        if id == " ":
            all = clearance_form_table.objects.all()
            return render(request,  'html_files/7.2Registrar Clearance List.html', {'all': all})
        all = clearance_form_table.objects.filter(course=id).values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request,  'html_files/7.2Registrar Clearance List.html', {'all': all})


@login_required(login_url='/')
def registrar_dashboard_graduation_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        if id == " ":
            all = graduation_form_table.objects.all()
            return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all})
        all = graduation_form_table.objects.filter(course=id).values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all})


def set_appointment(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        date = ""
        time = ""

        if request.method == "POST":
            print("1")
            date = request.post.get('date_appointment')
            time = request.post.get('time_appointment')
            print("2")
            name_temp = clearance_form_table.objects.filter(
                id=id).values_list('name', flat=True).distinct()
            name = user_table.objects.filter(full_name=name_temp[0]).values_list(
                'first_name', flat=True).distinct()
            email_temp = clearance_form_table.objects.filter(
                id=id).values_list('student_id', flat=True).distinct()
            email = user_table.objects.filter(
                username=email_temp[0]).values_list('email', flat=True).distinct()

            rec_email = email[0]
            print(rec_email)
            print(date)
            subject = 'Appointment Request for Clearance Form'

            message1 = 'Greetings,<br> <br>'
            message2 = 'Mr./Ms. ' + "<strong>" + request.user.first_name + "</strong>" + \
                ' would like to speak with you regarding with the clearance form you requested. An appointment with him/her has been set on the following date and time below.<br>'
            message3 = '<br> <br>Appointment: ' + date + " ," + time + '<br>'
            message4 = '<br> <br>Please be guided accordingly.'
            message = message1 + message2 + message3 + message4
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [rec_email, ]
            msg = EmailMessage(subject, message, email_from, recipient_list,)
            msg.content_subtype = "html"
            msg.send()
            return redirect('faculty_dashboard_clearance_list')
    return render(request, 'html_files/appointment.html')


#FACULTY LIST
@login_required(login_url='/')
def registrar_dashboard_faculty_list(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
    
        all_faculty = user_table.objects.filter(user_type = "FACULTY")
        faculty_data = {
            'all':all_faculty,
        }
        return render(request,  'html_files/7.4Registrar Faculty List.html', faculty_data)

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    # return render(request,  'html_files/7.4Registrar Faculty List.html', {'all': all_faculty})

def faculty_designation_update(request, id):
    form_change = request.POST.get('designationSelect')
    user_table.objects.filter(id=id).update(designation=form_change)
    
    if form_change == "---":
        user_table.objects.filter(id=id).update(position="FACULTY")
    else:
        user_table.objects.filter(id=id).update(position="HEAD")
    return redirect(registrar_dashboard_faculty_list)

#STUDENT LIST
@login_required(login_url='/')
def registrar_dashboard_student_list(request):
    # declaring template
    template = "html_files/Student list.html"
    student_data = user_table.objects.filter(Q(user_type='STUDENT') |Q(user_type='OLD STUDENT'))
        
    context = {'data':student_data}
    return render(request, template, context)

#ALUMNI LIST
@login_required(login_url='/')
def registrar_dashboard_alumni_list(request):
    # declaring template
    template = "html_files/Alumni List.html"
    alumnus_data = user_table.objects.filter(user_type="ALUMNUS")
    
    context = {'data':alumnus_data}
    return render(request, template, context)

#REQUEST LIST AND DOCUMENT CHECKER LIST 
#REQUEST LIST WITH ORGANIZER
@login_required(login_url='/')
def registrar_dashboard_organize_request_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        
        sorter = request.POST.get('request_table_organizer')
        
        if id == "CLAIMED":
            requests = request_form_table.objects.filter(claim = "CLAIMED").order_by('-time_requested').values()
        elif id =="UNCLAIMED":
            requests = request_form_table.objects.filter(claim = "UNCLAIMED").order_by('-time_requested').values()
        elif id =="OLDEST":
            requests = request_form_table.objects.all().order_by('time_requested').values()
        elif id =="LATEST":
            requests = request_form_table.objects.all().order_by('-time_requested').values()
        else:
            requests = request_form_table.objects.all().order_by('-time_requested').values()
            
        doc = Document_checker_table.objects.all().values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    
    return render(request,'html_files/Request List.html', {'data': requests,'data2': doc})

#DEFAULT PAGE
def registrar_dashboard_request_list(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        requests = request_form_table.objects.all().order_by('-time_requested').values()
        doc = Document_checker_table.objects.all().values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    
    return render(request,'html_files/Request List.html', {'data': requests,'data2': doc})

def request_official_update(request, id):
    form_change = request.POST.get('or_select')
    request_form_table.objects.filter(id=id).update(official_receipt=form_change)
    return redirect(registrar_dashboard_request_list)

def request_form137_update(request, id):
    form_change = request.POST.get('form137_select')
    request_form_table.objects.filter(id=id).update(form_137=form_change)
    return redirect(registrar_dashboard_request_list)

def request_TOR_update(request, id):
    form_change = request.POST.get('TOR_select')
    request_form_table.objects.filter(id=id).update(TOR=form_change)
    return redirect(registrar_dashboard_request_list)

def request_claim_update(request, id):
    form_change = request.POST.get('claim_select')
    request_form_table.objects.filter(id=id).update(claim=form_change)
    return redirect(registrar_dashboard_request_list)

#REQUEST FORM
@login_required(login_url='/')
def request_form(request):
    context = {}
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS" or "OLD STUDENT":
        user = request.user.user_type

        print(user)            
        if request.method == "POST":
            form = request_form
            student_id = request.POST.get('stud_id_pre')
            last_name = request.POST.get('ln_box_pre')
            first_name = request.POST.get('fn_box_pre')
            middle_name = request.POST.get('mn_box_pre')
            course = request.POST.get('course_pre')
            date = request.POST.get('date_pre')
            control_num = request.POST.get('control_pre')
            address = request.POST.get('add_box_pre')
            contact_num = request.POST.get('contact_pre')
            current_stat = request.POST.get('check_status_pre')
            purpose = request.POST.get('purpose')
            request = request.POST.get('purpose_request_pre')
            
            full_name = last_name + ", " + first_name + " " + middle_name
            mid = middle_name[0] + "."
            name2 = last_name + ", " + first_name + " " + mid
            
            print(name2)
    
            form = request_form_table.objects.create(student_id=student_id, name=full_name, name2=name2,
                                                     address=address, course=course,date=date, control_number=control_num,
                                                     contact_number=contact_num,current_status=current_stat,purpose_of_request_reason = purpose,
                                                     request=request)
            form.save()
            return redirect('student_dashboard')
            
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request,'html_files/Request form.html', context)

#UPLOAD DOCUMENT CHECKER LIST
@login_required(login_url='/')
def upload_document_checker(request):
      # declaring template
    template = "html_files/Request List.html"
    data = Document_checker_table.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'data': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='"') or my_csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = Document_checker_table.objects.update_or_create(
            name = column[0],
            form_137 = column[1],
            TOR = column[2],
        )
        
    for row in Document_checker_table.objects.all().reverse():
        if Document_checker_table.objects.filter(name=row.name).count() > 1:
            row.delete()
    requests = request_form_table.objects.all().order_by('-id').values()
    
    context = {'data':requests,'data2':data}
    return render(request, template, context)

#UPDATE SIGNATURE
@login_required(login_url='/')
def update_clearance_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        create_signature = request.POST.get('image_encoded')
        uploaded_signature = request.FILES.get('new_upload_signature', False)
        signature_timesaved = datetime.now()
        full_name = request.user.full_name
        
        if create_signature =="":
            if uploaded_signature is None:
                print("NO SIGNATURE SAVED")
            else:
                recent_sig = request.user.uploaded_signature
                print(str(recent_sig))
                if os.path.exists("Media/" + str(recent_sig)):
                    os.remove("Media/" + str(recent_sig))
                
                file_name ="signatures/"+ str(uploaded_signature)
                
                fs = FileSystemStorage()
        
                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                
                user_table.objects.filter(id=id).update(uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
        else:
            #remove recent signature
            recent_sig = request.user.uploaded_signature
            if os.path.exists("Media/" + str(recent_sig)):
                os.remove("Media/" + str(recent_sig))
                    
            #save signature in the storage       
            image_decode = base64.b64decode(create_signature.replace('data:image/png;base64,',''))        
            file_name = 'Media/signatures/' + full_name + '_APPROVED.png'
            # Create image file from base64
            with open(file_name, 'wb') as img_file:
                img_file.write(image_decode)
                print("saved")
                    
                c_signature = 'signatures/' + full_name + '_APPROVED.png'
            
            user_table.objects.filter(id=id).update(uploaded_signature=c_signature)
            user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
            
    return redirect(faculty_dashboard_clearance_list)

#UPDATE SIGNATURE IN GRADUATION
@login_required(login_url='/')
def update_grad_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        create_signature = request.POST.get('image_encoded')
        uploaded_signature = request.FILES.get('new_upload_signature', False)
        signature_timesaved = datetime.now()
        full_name = request.user.full_name
        
        if create_signature =="":
            if uploaded_signature is None:
                print("NO SIGNATURE SAVED")
            else:
                recent_sig = request.user.uploaded_signature
                print(str(recent_sig))
                if os.path.exists("Media/" + str(recent_sig)):
                    os.remove("Media/" + str(recent_sig))
                
                file_name ="signatures/"+ str(uploaded_signature)
                
                fs = FileSystemStorage()
        
                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                
                user_table.objects.filter(id=id).update(uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
        else:
            #remove recent signature
            recent_sig = request.user.uploaded_signature
            if os.path.exists("Media/" + str(recent_sig)):
                os.remove("Media/" + str(recent_sig))
                    
            #save signature in the storage       
            image_decode = base64.b64decode(create_signature.replace('data:image/png;base64,',''))        
            file_name = 'Media/signatures/' + full_name + '_APPROVED.png'
            # Create image file from base64
            with open(file_name, 'wb') as img_file:
                img_file.write(image_decode)
                print("saved")
                    
                c_signature = 'signatures/' + full_name + '_APPROVED.png'
            
            user_table.objects.filter(id=id).update(uploaded_signature=c_signature)
            user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
            
    return redirect(faculty_dashboard_graduation_list)

#DELETE SIGNATURE
@login_required(login_url='/')
def delete_clearance_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        recent_sig = request.user.uploaded_signature
        signature_timesaved = datetime.now()
        signature_saved = "DECLINE"
        print(str(recent_sig))
        if os.path.exists("Media/" + str(recent_sig)):
            os.remove("Media/" + str(recent_sig))

        user_table.objects.filter(id=id).update(uploaded_signature=signature_saved)
        user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
        
    return redirect(faculty_dashboard_clearance_list)

@login_required(login_url='/')
def delete_graduation_signature(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        recent_sig = request.user.uploaded_signature
        signature_timesaved = datetime.now()
        signature_saved = "DECLINE"
        print(str(recent_sig))
        if os.path.exists("Media/" + str(recent_sig)):
            os.remove("Media/" + str(recent_sig))

        user_table.objects.filter(id=id).update(uploaded_signature=signature_saved)
        user_table.objects.filter(id=id).update(signature_timesaved=signature_timesaved)
        
    return redirect(faculty_dashboard_graduation_list)
