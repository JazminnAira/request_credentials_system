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
from django.core import mail
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import my_csv, csv,  io
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
from datetime import datetime,date,timedelta
import os
import time

def req_print(request,id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = request_form_table.objects.get(id=id)
   
    textob = p.beginText()

    print(content)
    print("hello world")

    lines = []

    p.setFont("Helvetica", 7)
    p.drawString(73, 238, f'{content.address}')
    # List of Payments
    p.setFont("Helvetica", 9)
    p.drawString(88, 833, f'{content.name2}')
    p.drawString(325, 833, f'{content.course}')
    p.drawString(468, 833, f'{content.date}')
    
   
#   Claim Stub
    p.setFont("Helvetica", 9)
    p.drawString(95, 583, f'{content.name2}')
    p.drawString(322, 583, f'{content.course}')
    p.drawString(430, 583, f'{content.date}')
    


# Request Form
    p.setFont("Helvetica", 9)
    p.drawString(80, 252, f'{content.name2}')
    p.drawString(300, 252, f'{content.course}')
    p.drawString(400, 252, f'{content.date}')
    p.drawString(520, 252, f'{content.control_number}')
    p.drawString(450, 238, f'{content.contact_number}')
    
    p.setFont("Helvetica", 11)
    status = content.current_status
    yearget = status.split()
    yeargrad =yearget[-1]
    if status == "STUDENT":
        p.drawString(30, 225, '/')
    elif status =="OLD STUDENT":
        p.drawString(195, 225, '/')
    else:
        p.drawString(327, 225, '/')
        p.drawString(460, 225, f"""{yeargrad}""")
        # PALAGAY NG YEAR GRAD

    # purpose
    form_purpose = content.request
    word_list = form_purpose.split()  # list of words

    cert = word_list[0]
    cert4 = ' '.join(form_purpose.split()[1:])
    
    others = ' '.join(form_purpose.split()[1:])
    

    if form_purpose == "Honorable Dismissal":
        p.drawString(327, 528, '✔')
        p.drawString(257, 171, '✔')
    elif form_purpose == "Verification":
        p.drawString(266, 777, '✔')
    elif form_purpose == "Subject Description":
        p.drawString(266, 803, '✔')
        p.drawString(327, 555, '✔')
        p.drawString(257, 198, '✔')
    elif form_purpose == "CAV":
        p.drawString(47, 762, '✔')
        p.drawString(60, 517, '✔')
        p.drawString(30, 157, '✔')
    elif form_purpose == "Transcript of Records":
        p.drawString(47, 803, '✔')
        p.drawString(60, 555, '✔')
        p.drawString(30, 198, '✔')
    elif form_purpose == "Authentication/Verification":
        p.drawString(264, 790, '✔')
        p.drawString(327, 541, '✔')
        p.drawString(257, 184, '✔')
    elif form_purpose == "Diploma":
        p.drawString(47, 777, '✔')
        p.drawString(60, 528, '✔')
        p.drawString(30, 171, '✔')
    elif  cert == "Certification:":
        p.drawString(47, 790, '✔')
        p.drawString(60, 541, '✔')
        p.drawString(30, 184, '✔')
        p.setFont("Helvetica", 9)
        p.drawString(128, 542, f"""{cert4}""")
        p.drawString(100, 184, f"""{cert4}""")
        # paayos pa 
        # padadagdag additional info
    else:
        p.setFont("Helvetica", 11)
        
        p.drawString(327, 517, '✔')
        p.drawString(257, 157, '✔')
        p.setFont("Helvetica", 9)
        p.drawString(440, 517, f"""{others}""")
        p.drawString(375, 157, f"""{others}""")
        # temporary lang itong purpose_of_request_reason
        
        
    o_r = content.official_receipt
    f137 = content.form_137
    clearance = content.clearance
    
    
    if clearance == "✔":
        p.drawString(230, 130, '✔')
    else:
        p.drawString(230, 130, '')
        
        
    if f137 == "✔":
        p.drawString(147, 130, '✔')
    else:
        p.drawString(147, 130, '')
        
    if o_r == "✔":
        p.drawString(318, 130, '✔')
    else:
        p.drawString(318, 130, '')

    p.setFont("Helvetica", 9)
    p.drawString(115, 143, f'{content.purpose_of_request_reason}')
    
    
    reg = user_table.objects.get(user_type="REGISTRAR")
    p.drawString(425, 450, f'{reg.full_name}')
    p.drawString(285, 115, f'{reg.full_name}')
    
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
        r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Required_Forms.pdf', 'rb'))

    info_page = clearance_pdf.getPage(0)
    info_page.mergePage(infos.getPage(0))

    output = PdfFileWriter()

    output.addPage(info_page)
    to_merge = open(
        r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Request_form_Generated.pdf', 'wb')
    output.write(to_merge)
    to_merge.close()

    with open(r'C:\Users\Acer\request_credentials_system\gradclear_project\gradclear_app\static\pdf\Request_form_Generated.pdf', 'rb', ) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename=Required Form.pdf'
        return response


def graduation_print(request, id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    content = graduation_form_table.objects.get(id=id)
    fac = user_table.objects.all()
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
    p.setFont("Helvetica", 7)
    sub1 = content.subject1
    faculty = content.faculty1
    fac = user_table.objects.get(full_name = faculty)
    stat = fac.uploaded_signature
    
    
    
    print(stat)
    if len(sub1) == 0:
        p.drawString(33, 640, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
    else:
        p.drawString(33, 640, f'{content.subject1}')
        p.setFont("Helvetica", 7)
        p.drawString(204, 640, f'{content.starttime1_1} - {content.endtime1_1}')
        p.drawString(279, 640, f'{content.room1}')
        p.drawString(323, 640, f'{content.day1_1}')
        sig1 = content.signature1
        faculty = content.faculty1
        fac = user_table.objects.get(full_name = faculty)
        stat = fac.uploaded_signature
        if sig1 == "NO_APPROVED":
            p.drawString(380, 640, 'Unapproved')
        elif stat =="DECLINE":  
            p.drawString(380, 638,f'{content.faculty1}')
            
        else:
            sig1trig = content.signature1
            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
            p.drawImage(im,500, 640, height = 15, width = 80 , mask='auto')
            p.drawString(380, 638,f'{content.faculty1}')
               
        p.setFont("Helvetica", 7)
        sub2 = content.subject2

        if len(sub2) == 0:
            p.drawString(33, 625, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
        
        else:
            p.drawString(33, 625, f'{content.subject2}')
            p.setFont("Helvetica", 7)
            p.drawString(204, 625, f'{content.starttime1_2} - {content.endtime1_2}')
            p.drawString(279, 625, f'{content.room2}')
            p.drawString(323, 625, f'{content.day1_2}')
            sig2 = content.signature2
            faculty2 = content.faculty2
            fac2 = user_table.objects.get(full_name = faculty2)
            stat = fac2.uploaded_signature
            if sig2 == "NO_APPROVED":
                p.drawString(380, 625, 'Unapproved')
            elif stat == "DECLINE":
                p.drawString(380, 625,f'{content.faculty2}' )
            else:
                sig1trig = content.signature2
                im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                p.drawString(380, 625,f'{content.faculty2}' )
                p.drawImage(im,500, 625, height = 15, width = 80 , mask='auto')

      
            p.setFont("Helvetica", 7)
            sub3 = content.subject3
            print(sub3)
            if len(sub3) == 0:
                p.drawString(33, 611, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
            else:
                p.drawString(33, 611, f'{content.subject3}')
                p.setFont("Helvetica", 7)
                p.drawString(204, 611, f'{content.starttime1_3} - {content.endtime1_3}')
                p.drawString(279, 611, f'{content.room3}')
                p.drawString(323, 611, f'{content.day1_3}')
                sig3 = content.signature3
                faculty3 = content.faculty3
                fac3 = user_table.objects.get(full_name = faculty3)
                stat = fac3.uploaded_signature
                if sig3 == "NO_APPROVED":
                    p.drawString(380, 611, 'Unapproved')
                elif stat == "DECLINE":
                    p.drawString(380, 611,f'{content.faculty3}' )
                else:
                    sig1trig = content.signature3
                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                    p.drawString(380, 611,f'{content.faculty3}' )
                    p.drawImage(im,500, 609, height = 15, width = 80 , mask='auto')
    
                    p.setFont("Helvetica", 7)
                    sub4 = content.subject4
                    if len(sub4) == 0:
                        p.drawString(33, 597,'----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')

                    else:
                        p.drawString(33, 597, f'{content.subject4}')
                        p.setFont("Helvetica", 7)
                        p.drawString(204, 597, f'{content.starttime1_4} - {content.endtime1_4}')
                        p.drawString(279, 597, f'{content.room4}')
                        p.drawString(323, 597, f'{content.day1_4}')
                        sig4 = content.signature4
                        faculty = content.faculty4
                        fac = user_table.objects.get(full_name = faculty)
                        stat = fac.uploaded_signature
                        if sig4 == "NO_APPROVED":
                            p.drawString(380, 597, 'Unapproved')
                        elif stat == "DECLINE":
                                p.drawString(380, 597,f'{content.faculty4}' )
                        else:
                            sig1trig = content.signature4
                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                            p.drawString(380, 597,f'{content.faculty4}' )
                            p.drawImage(im,500, 597, height = 15, width = 80 , mask='auto')

                            p.setFont("Helvetica", 7)
                            sub5 = content.subject5
                            if len(sub5) == 0:
                                p.drawString(33, 584, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                            else:
                                p.drawString(33, 584, f'{content.subject5}')
                                p.setFont("Helvetica", 7)
                                p.drawString(204, 584, f'{content.starttime1_5} - {content.endtime1_5}')
                                p.drawString(279, 584, f'{content.room5}')
                                p.drawString(323, 584, f'{content.day1_5}')
                                sig5 = content.signature5
                                faculty = content.faculty5
                                fac = user_table.objects.get(full_name = faculty)
                                stat = fac.uploaded_signature
                                if sig5 == "NO_APPROVED":
                                    p.drawString(380, 584, 'Unapproved')
                                elif stat == "DECLINE":
                                    p.drawString(380, 584,f'{content.faculty5}' )
                                else:
                                    sig1trig = content.signature5
                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                    p.drawString(380, 584,f'{content.faculty5}' )
                                    p.drawImage(im,500, 584, height = 15, width = 80 , mask='auto')

                                    p.setFont("Helvetica", 7)
                                    sub6 = content.subject6
                                    print(sub6)
                                    if len(sub6) == 0:
                                        p.drawString(39, 570, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                    else:
                                        p.drawString(33, 570, f'{content.subject6}')
                                        p.setFont("Helvetica", 7)
                                        p.drawString(204, 570, f'{content.starttime1_6} - {content.endtime1_6}')
                                        p.drawString(279, 570, f'{content.room6}')
                                        p.drawString(323, 570, f'{content.day1_6}')
                                        sig6 = content.signature6
                                        faculty = content.faculty6
                                        fac = user_table.objects.get(full_name = faculty)
                                        stat = fac.uploaded_signature
                                        if sig6 == "NO_APPROVED":
                                            p.drawString(380, 570, 'Unapproved')
                                        elif stat == "DECLINE":
                                                p.drawString(380, 570,f'{content.faculty6}' )
                                        else:
                                            sig1trig = content.signature6
                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                            p.drawString(380, 570,f'{content.faculty6}' )
                                            p.drawImage(im,500, 570, height = 15, width = 80 , mask='auto')
            
            
                                            p.setFont("Helvetica", 7)
                                            sub7 = content.subject7
                                            if len(sub7) == 0: 
                                                p.drawString(33, 555, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
        
                                            else:
                                                p.drawString(33, 555, f'{content.subject7}')
                                                p.setFont("Helvetica", 7)
                                                p.drawString(204, 555, f'{content.starttime1_7} - {content.endtime1_7}')
                                                p.drawString(279, 555, f'{content.room7}')
                                                p.drawString(323, 555, f'{content.day1_7}')
                                                sig7 = content.signature7
                                                faculty = content.faculty7
                                                fac = user_table.objects.get(full_name = faculty)
                                                stat = fac.uploaded_signature
                                                if sig7 == "NO_APPROVED":
                                                    p.drawString(380, 555, 'Unapproved')
                                                elif stat == "DECLINE":
                                                        p.drawString(380, 555,f'{content.faculty7}' )    
                                                else:
                                                    sig1trig = content.signature7
                                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                    p.drawString(380, 555,f'{content.faculty7}' )
                                                    p.drawImage(im,500, 555, height = 15, width = 80 , mask='auto')
                

                                                    p.setFont("Helvetica", 7)
                                                    sub8 = content.subject8
                                                    if len(sub8) == 0: 
                                                                                                                      
                                                        p.drawString(33, 542, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                    else:
                                                        p.drawString(33, 542, f'{content.subject8}')
                                                        p.setFont("Helvetica", 7)
                                                        p.drawString(204, 542, f'{content.starttime1_8} - {content.endtime1_8}')
                                                        p.drawString(279, 542, f'{content.room8}')
                                                        p.drawString(323, 542, f'{content.day1_8}')
                                                        sig8 = content.signature8
                                                        faculty = content.faculty8
                                                        fac = user_table.objects.get(full_name = faculty)
                                                        stat = fac.uploaded_signature
                                                        if sig8 == "NO_APPROVED":
                                                            p.drawString(380, 542, 'Unapproved')
                                                        elif stat == "DECLINE":
                                                                p.drawString(380, 542,f'{content.faculty8}' )
                                                        else:
                                                            sig1trig = content.signature8
                                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                            p.drawString(380, 542,f'{content.faculty8}' )
                                                            p.drawImage(im,500, 542, height = 15, width = 80 , mask='auto')
                                                            
                                                            
                                                            p.setFont("Helvetica", 7)
                                                            sub9 = content.subject9
                                                            if len(sub9) == 0:
                                                                p.drawString(33, 529, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                            else:
                                                                p.drawString(33, 529, f'{content.subject9}')
                                                                p.setFont("Helvetica", 7)
                                                                p.drawString(204, 529, f'{content.starttime1_9} - {content.endtime1_9}')
                                                                p.drawString(279, 529, f'{content.room9}')
                                                                p.drawString(323, 529, f'{content.day1_9}')
                                                                sig9 = content.signature9
                                                                faculty = content.faculty9
                                                                fac = user_table.objects.get(full_name = faculty)
                                                                stat = fac.uploaded_signature
                                                                if sig9 == "NO_APPROVED":
                                                                    p.drawString(380, 529, 'Unapproved')
                                                                elif stat == "DECLINE":
                                                                        p.drawString(380, 529,f'{content.faculty9}' )
                                                                else:
                                                                    sig1trig = content.signature9
                                                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                                    p.drawString(380, 529,f'{content.faculty9}' )
                                                                    p.drawImage(im,500, 529, height = 15, width = 80 , mask='auto')                    
            
            
                                                                    p.setFont("Helvetica", 7)
                                                                    sub10 = content.subject10
                                                                    if len(sub10) == 0:
                                                                        p.drawString(33, 515, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                
                                                                    else:
                                                                        p.drawString(33, 515, f'{content.subject10}')
                                                                        p.setFont("Helvetica", 7)
                                                                        p.drawString(204, 515, f'{content.starttime1_10} - {content.endtime1_10}')
                                                                        p.drawString(279, 515, f'{content.room10}')
                                                                        p.drawString(323, 515, f'{content.day1_10}')
                                                                        sig10 = content.signature10
                                                                        faculty = content.faculty10
                                                                        fac = user_table.objects.get(full_name = faculty)
                                                                        stat = fac.uploaded_signature
                                                                        if sig10 == "NO_APPROVED":
                                                                            p.drawString(380, 515, 'Unapproved')
                                                                        elif stat == "DECLINE":
                                                                                p.drawString(380, 515,f'{content.faculty10}' )
                                                                        else:
                                                                            sig1trig = content.signature10
                                                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                                            p.drawString(380, 515,f'{content.faculty10}' )
                                                                            p.drawImage(im,500, 515, height = 15, width = 80 , mask='auto')
    #additional subj
  

    addsub1 = content.addsubject1
    if len(addsub1) == 0:
        p.drawString(33, 305, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
        
    else:
        p.drawString(33, 305, f'{content.addsubject1}')
        p.setFont("Helvetica", 7)
        p.drawString(204, 305, f'{content.add_starttime1_1} - {content.add_endtime1_1}')
        p.drawString(279, 305, f'{content.addroom1}')
        p.drawString(323, 305, f'{content.addday1_1}')
        addsig1 = content.addsignature1
        faculty = content.addfaculty1
        fac = user_table.objects.get(full_name = faculty)
        stat = fac.uploaded_signature
        if addsig1 == "NO_APPROVED":
            p.drawString(380, 305, 'Unapproved')
        elif stat == "DECLINE":
                p.drawString(380, 305,f'{content.addfaculty1}' )
        else:
            sig1trig = content.addsignature1
            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
            p.drawString(380, 305,f'{content.addfaculty1}' )
            p.drawImage(im,500, 305, height = 15, width = 80 , mask='auto')

    
            p.setFont("Helvetica", 7)
            addsub2 = content.addsubject2
            if len(addsub2) == 0:
                p.drawString(33, 290, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
            else:
                p.drawString(33, 290, f'{content.addsubject2}')
                p.setFont("Helvetica", 7)
                p.drawString(204, 290, f'{content.add_starttime1_2} - {content.add_endtime1_2}')
                p.drawString(279, 290, f'{content.addroom2}')
                p.drawString(323, 290, f'{content.addday1_2}')
                addsig2 = content.addsignature2
                faculty = content.addfaculty2
                fac = user_table.objects.get(full_name = faculty)
                stat = fac.uploaded_signature
                if addsig2 == "NO_APPROVED":
                    p.drawString(380, 290, 'Unapproved')
                elif stat == "DECLINE":
                    p.drawString(380, 290,f'{content.addfaculty2}' )
                else:
                    sig1trig = content.addsignature2
                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                    p.drawString(380, 290,f'{content.addfaculty2}' )
                    p.drawImage(im,500, 290, height = 15, width = 80 , mask='auto')
    
                    p.setFont("Helvetica", 7)
                    addsub3 = content.addsubject3
                    if len(addsub3) == 0:
                        p.drawString(33, 276, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                        
                    else:
                        p.drawString(33, 276, f'{content.addsubject3}')
                        p.setFont("Helvetica", 7)
                        p.drawString(204, 276, f'{content.add_starttime1_3} - {content.add_endtime1_3}')
                        p.drawString(279, 276, f'{content.addroom3}')
                        p.drawString(323, 276, f'{content.addday1_3}')
                        addsig3 = content.addsignature3
                        faculty = content.addfaculty3
                        fac = user_table.objects.get(full_name = faculty)
                        stat = fac.uploaded_signature
                        if addsig3 == "NO_APPROVED":
                            p.drawString(380, 276, 'Unapproved')
                        elif stat == "DECLINE":
                            p.drawString(380, 276,f'{content.addfaculty3}' )
                        else:
                            sig1trig = content.addsignature3
                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                            p.drawString(380, 276,f'{content.addfaculty3}' )
                            p.drawImage(im,500, 276, height = 15, width = 80 , mask='auto')
                            
            

                            p.setFont("Helvetica", 7)
                            addsub4 = content.addsubject4
                            if len(addsub4) == 0:
                                print ("empty")
                                p.drawString(33, 262, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                
                            else:
                                p.drawString(33, 262, f'{content.addsubject4}')
                                p.setFont("Helvetica", 7)
                                p.drawString(204, 262, f'{content.add_starttime1_4} - {content.add_endtime1_4}')
                                p.drawString(279, 262, f'{content.addroom4}')
                                p.drawString(323, 262, f'{content.addday1_4}')
                                addsig4 = content.addsignature4
                                faculty = content.addfaculty4
                                fac = user_table.objects.get(full_name = faculty)
                                stat = fac.uploaded_signature
                                if addsig4 == "NO_APPROVED":
                                    p.drawString(380, 262, 'Unapproved')
                                elif stat == "DECLINE":
                                    p.drawString(380, 262,f'{content.addfaculty4}' )
                                else:
                                    sig1trig = content.addsignature4
                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                    p.drawString(380, 262,f'{content.addfaculty4}' )
                                    p.drawImage(im,500, 262, height = 15, width = 80 , mask='auto')
            
            
                                    p.setFont("Helvetica", 7)
                                    addsub5 = content.addsubject5
                                    if len(addsub5) == 0:
                                        p.drawString(33, 249, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                    else:
                                        p.drawString(33, 249, f'{content.addsubject5}')
                                        p.setFont("Helvetica", 7)
                                        p.drawString(204, 249, f'{content.add_starttime1_5} - {content.add_endtime1_5}')
                                        p.drawString(279, 249, f'{content.addroom5}')
                                        p.drawString(323, 249, f'{content.addday1_5}')
                                        addsig5 = content.addsignature5
                                        faculty = content.addfaculty5
                                        fac = user_table.objects.get(full_name = faculty)
                                        stat = fac.uploaded_signature
                                        if addsig5 == "NO_APPROVED":
                                            p.drawString(380, 249, 'Unapproved')
                                        elif stat == "DECLINE":
                                            p.drawString(380, 249,f'{content.addfaculty5}' )
                                        else:
                                            sig1trig = content.addsignature5
                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                            p.drawString(380, 249,f'{content.addfaculty5}' )
                                            p.drawImage(im,500, 249, height = 15, width = 80 , mask='auto')
            
                                            p.setFont("Helvetica", 7)
                                            addsub6 = content.addsubject6
                                            if len(addsub6) == 0:
                                                p.drawString(33, 235, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                            else:
                                                p.drawString(33, 235, f'{content.addsubject6}')
                                                p.setFont("Helvetica", 7)
                                                p.drawString(204, 235, f'{content.add_starttime1_6} - {content.add_endtime1_6}')
                                                p.drawString(279, 235, f'{content.addroom6}')
                                                p.drawString(323, 235, f'{content.addday1_6}')
                                                addsig6 = content.addsignature6
                                                faculty = content.addfaculty6
                                                fac = user_table.objects.get(full_name = faculty)
                                                stat = fac.uploaded_signature
                                                if addsig6 == "NO_APPROVED":
                                                    p.drawString(380, 235, 'Unapproved')
                                                elif stat == "DECLINE":
                                                    p.drawString(380, 235,f'{content.addfaculty6}' )
                                                else:
                                                    sig1trig = content.addsignature6
                                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                    p.drawString(380, 235,f'{content.addfaculty6}' )
                                                    p.drawImage(im,500, 235, height = 15, width = 80 , mask='auto')
                                                    
            
            
                                                    p.setFont("Helvetica", 7)
                                                    addsub7 = content.addsubject7
                                                    if len(addsub7) == 0:
                                                        p.drawString(33, 220, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                    else:
                                                        p.drawString(33, 220, f'{content.addsubject7}')
                                                        p.setFont("Helvetica", 7)
                                                        p.drawString(204, 220, f'{content.add_starttime1_7} - {content.add_endtime1_7}')
                                                        p.drawString(279, 220, f'{content.addroom7}')
                                                        p.drawString(323, 220, f'{content.addday1_7}')
                                                        addsig7 = content.addsignature7
                                                        faculty = content.addfaculty7
                                                        fac = user_table.objects.get(full_name = faculty)
                                                        stat = fac.uploaded_signature
                                                        if addsig7 == "NO_APPROVED":
                                                            p.drawString(380, 220, 'Unapproved')
                                                        elif stat == "DECLINE":
                                                            p.drawString(380, 220,f'{content.addfaculty7}' )
                                                        else:
                                                            sig1trig = content.addsignature7
                                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                            p.drawString(380, 220,f'{content.addfaculty7}' )
                                                            p.drawImage(im,500, 220, height = 15, width = 80 , mask='auto')
            
            
                                                            p.setFont("Helvetica", 7)
                                                            addsub8 = content.addsubject8
                                                            if len(addsub8) == 0:
                                                                p.drawString(33, 207, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                                
                                                            else:
                                                                p.drawString(33, 207, f'{content.addsubject8}')
                                                                p.setFont("Helvetica", 7)
                                                                p.drawString(204, 207, f'{content.add_starttime1_8} - {content.add_endtime1_8}')
                                                                p.drawString(279, 207, f'{content.addroom8}')
                                                                p.drawString(323, 207, f'{content.addday1_8}')
                                                                addsig8 = content.addsignature8
                                                                faculty = content.addfaculty8
                                                                fac = user_table.objects.get(full_name = faculty)
                                                                stat = fac.uploaded_signature
                                                                if addsig8 == "NO_APPROVED":
                                                                    p.drawString(380, 207, 'Unapproved')
                                                                elif stat == "DECLINE":
                                                                    p.drawString(380, 207,f'{content.addfaculty8}' )
                                                                else:
                                                                    sig1trig = content.addsignature8
                                                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                                    p.drawString(380, 207,f'{content.addfaculty8}' )
                                                                    p.drawImage(im,500, 207, height = 15, width = 80 , mask='auto')
                                                                    
            
                                                                    p.setFont("Helvetica", 7)
                                                                    addsub9 = content.addsubject9
                                                                    if len(addsub9) == 0:
                                                                        p.drawString(33,193, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                                        
                                                                    else:
                                                                        p.drawString(33, 193, f'{content.addsubject9}')
                                                                        p.setFont("Helvetica", 7)
                                                                        p.drawString(204,193, f'{content.add_starttime1_9} - {content.add_endtime1_9}')
                                                                        p.drawString(279,193, f'{content.addroom9}')
                                                                        p.drawString(323,193, f'{content.addday1_9}')
                                                                        addsig9 = content.addsignature9
                                                                        faculty = content.addfaculty9
                                                                        fac = user_table.objects.get(full_name = faculty)
                                                                        stat = fac.uploaded_signature
                                                                        if addsig9 == "NO_APPROVED":
                                                                            p.drawString(380,193, 'Unapproved')
                                                                        elif stat == "DECLINE":
                                                                            p.drawString(380, 193,f'{content.addfaculty9}' )
                                                                        else:
                                                                            sig1trig = content.addsignature9
                                                                            im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                                            p.drawString(380, 193,f'{content.addfaculty9}' )
                                                                            p.drawImage(im,500, 193, height = 15, width = 80 , mask='auto')
            
            
                                                                            p.setFont("Helvetica", 7)
                                                                            addsub10 = content.addsubject10
                                                                            if len(addsub10) == 0:
                                                                                p.drawString(33, 180, '----------------------------------------------------------------------------------------------------------Nothing Follows----------------------------------------------------------------------------------------------------------')
                                                                                
                                                                            else:
                                                                                p.drawString(33, 180, f'{content.addsubject10}')
                                                                                p.setFont("Helvetica", 7)
                                                                                p.drawString(204, 180, f'{content.add_starttime1_10} - {content.add_endtime1_10}')
                                                                                p.drawString(279, 180, f'{content.addroom10}')
                                                                                p.drawString(323, 180, f'{content.addday1_10}')
                                                                                addsig10 = content.addsignature10
                                                                                faculty = content.addfaculty10
                                                                                fac = user_table.objects.get(full_name = faculty)
                                                                                stat = fac.uploaded_signature
                                                                                if addsig10 == "NO_APPROVED":
                                                                                    p.drawString(380, 180, 'Unapproved')
                                                                                elif stat == "DECLINE":
                                                                                    p.drawString(380, 180,f'{content.addfaculty10}' )
                                                                                else:
                                                                                    sig1trig = content.addsignature10
                                                                                    im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
                                                                                    p.drawString(380, 180,f'{content.addfaculty10}' )
                                                                                    p.drawImage(im,500, 180, height = 15, width = 80 , mask='auto')

    p.setFont("Helvetica", 7)
    p.drawString(235, 151, f'{content.unenrolled_application_deadline}')
    p.drawString(195, 73, f'{content.trainP_startdate}')
    p.drawString(390, 73, f'{content.trainP_enddate}')
    
    sitsig = content.sitsignature
    ins = content.instructor_name
    fac = user_table.objects.get(full_name = ins)
    stat = fac.uploaded_signature
    if sitsig == "NO_APPROVED":
        p.drawString(258, 58, 'Unapproved')
    elif stat == "DECLINE":
        p.drawString(258, 58,f'{content.instructor_name}' )
    else:
        sig1trig = content.sitsignature
        im = "C:\\Users\\Acer\\request_credentials_system\\gradclear_project\\Media\\signatures\\"+sig1trig+".png"
        p.drawString(258, 58,f'{content.instructor_name}' )
        p.drawImage(im,258, 58, height = 15, width = 80 , mask='auto')
    

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


def appointment(request, id, form):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        gform = form
        if request.method == 'POST':
            email_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
            email = user_table.objects.filter(
                student_id=email_temp[0]).values_list('email', flat=True).distinct()
            rec_email = email[0]
            recipient_list = [rec_email, ]

            purpose = request_form_table.objects.filter(
            id=id).values_list('request', flat=True).distinct()
            purpose_of = request_form_table.objects.filter(
                request=purpose[0]).values_list('request', flat=True).distinct()
            purpose_of_req =  purpose_of[0]
            purpose_of_request = purpose_of_req, 

            name_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
            name = user_table.objects.filter(
                student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
            last_name = name[0]

            gender_temp = user_table.objects.filter(
            id=id).values_list('gender', flat=True).distinct()
            gender = user_table.objects.filter(
                gender=gender_temp[0]).values_list('gender', flat=True).distinct()
            gender_choice = gender[0]
            gender_final=""
            if gender_choice == "FEMALE":
                gender_final = "Ms."
            else:
                gender_final= "Mr."
            
            faculty_gender = request.user.gender
            gender_fac=""
            if faculty_gender == "FEMALE":
                gender_fac = "Ms."
            else:
                gender_fac= "Mr."

            subject = 'Application for Clearance Form '
            message1 = 'Good day, '+ "<strong>" + gender_final +  name[0] + ",</strong><br><br>"
            # message1 = 'Greetings from the  '+"<strong>"+'Registrar,'+"</strong><br><br>"
            message2 = 'Your Application for Clearance Form has pending concerns with  '+"<strong>"+ gender_fac + request.user.last_name +".</strong><br><br>"
            message3 = '  An appointment for discussing the said concerns was scheduled. Please arrive at the set date and time of appointment. <br><br>'
            message4 =  "<i>"+' Failure to comply may result to declined application.'"</i>"
            message5 =  'For other concerns, please contact the official email of TUPC Registrar:   '+ 'tupc_registrar@tup.edu.ph'
            message6 =  "<strong>"+'Technological University of the Philippines-Cavite Campus'+"</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br>'
            message7 =  "<i>"+'***This is an automated message, do not reply.'+"</i>"


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
            message='''{}
            <strong>Date:</strong>\n\t\t{}\n<br>
            <strong>Time:</strong>\n\t\t{}\n<br><br>
            <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br>
            \n\t\t{}\n<br><br><br><br>
            \n\t\t{}\n<br><br><br>
            \n\t\t{}\n<br>
            \n\t\t{}\n<br>
            
            '''''.format(data['message'],data ['date_appointment'], data ['time_appointment'], data ['additionalmessage'], data ['message4'], data ['message5'], data ['message6'], data ['message7'])
            msg = EmailMessage(subject, message,'', email, recipient_list,)
            msg.content_subtype = "html"
            msg.send()
            messages.success(request, "Appointment Schedule Sent.")
    
            return redirect(faculty_dashboard_clearance_list) 
        
        else:
            return render(request, 'html_files/appointment.html', {'gform' : gform})
        
        

def appointmentgrad(request, id, form):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        gform = form
        if request.method == 'POST':
            email_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
            email = user_table.objects.filter(
                student_id=email_temp[0]).values_list('email', flat=True).distinct()
            rec_email = email[0]
            recipient_list = [rec_email, ]

            purpose = request_form_table.objects.filter(
            id=id).values_list('request', flat=True).distinct()
            purpose_of = request_form_table.objects.filter(
                request=purpose[0]).values_list('request', flat=True).distinct()
            purpose_of_req =  purpose_of[0]
            purpose_of_request = purpose_of_req, 

            name_temp = request_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
            name = user_table.objects.filter(
                student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
            last_name = name[0]

            gender_temp = user_table.objects.filter(
            id=id).values_list('gender', flat=True).distinct()
            gender = user_table.objects.filter(
                gender=gender_temp[0]).values_list('gender', flat=True).distinct()
            gender_choice = gender[0]
            gender_final=""
            if gender_choice == "FEMALE":
                gender_final = "Ms."
            else:
                gender_final= "Mr."
            
            faculty_gender = request.user.gender
            gender_fac=""
            if faculty_gender == "FEMALE":
                gender_fac = "Ms."
            else:
                gender_fac= "Mr."

            subject = 'Application for Graduation Form '
            message1 = 'Good day, '+ "<strong>" + gender_final +  name[0] + ",</strong><br><br>"
            message2 = 'Your Application for Clearance Form has pending concerns with  '+  "<strong>"+ gender_fac+   request.user.last_name +".</strong><br><br>"
            message3 =  '  An appointment for discussing the said concerns was scheduled. Please arrive at the set date and time of appointment. <br><br>'
            message4 =  "<i>"+' Failure to comply may result to declined application.'+"</i>"
            message5 =  'For other concerns, please contact the official email of TUPC Registrar:   '+ 'tupc_registrar@tup.edu.ph'
            message6 =  "<strong>"+'Technological University of the Philippines-Cavite Campus'+"</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br>'
            message7 =  "<i>"+'***This is an automated message, do not reply.'+"</i>"


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
            message='''{}
            <strong>Date of Appointment:</strong>\n\t\t{}\n<br>
            <strong>Time of Appointment:</strong>\n\t\t{}\n<br><br>
            <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br>
            \n\t\t{}\n<br><br><br><br>
            \n\t\t{}\n<br><br><br>
            \n\t\t{}\n<br>
            \n\t\t{}\n<br>
            
            '''''.format(data['message'],data ['date_appointment'], data ['time_appointment'], data ['additionalmessage'], data ['message4'], data ['message5'], data ['message6'], data ['message7'])
            msg = EmailMessage(subject, message,'', email, recipient_list,)
            msg.content_subtype = "html"
            msg.send()
            messages.success(request, "Appointment Schedule Sent.")
            return redirect('faculty_dashboard_graduation_list')
        else:
            return render(request, 'html_files/appointment.html', {'gform' : gform})

def reggrad_appointment(request, id):
    email_temp = graduation_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
    email = user_table.objects.filter(
        student_id=email_temp[0]).values_list('email', flat=True).distinct()

    rec_email = email[0]
    name_temp = graduation_form_table.objects.filter(
    id=id).values_list('student_id', flat=True).distinct()
    print("name_temp",name_temp) 
    name = user_table.objects.filter(
        student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
    last_name = name[0]

    gender_temp = user_table.objects.filter(
    id=id).values_list('gender', flat=True).distinct()
    gender = user_table.objects.filter(
        gender=gender_temp[0]).values_list('gender', flat=True).distinct()
    gender_choice = gender[0]
    gender_final=""
    if gender_choice == "FEMALE":
        gender_final = "Ms."
    else:
        gender_final= "Mr."
    

    subject = 'Application for Graduation Form'
    message1 = 'Good day,   '+ gender_final + "<strong>" + name[0] + ",</strong><br><br>"
    message2 = 'Your Application for Graduation Form has been approved and is now available for printing. Kindly visit this '+ '(link)'+' and follow the guidelines below.<br><br>'
    message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to this site' + '(link)'+'.<br>'+'2. On your dashboard, view your request form from the table.<br>'+'3. Click the "Print" button to print the form. Please take note that the form should be printed in Legal Size Paper (8.5 x 14 inches).<br>'+'4. Arrive at the appointed date and time for claiming your request.<br>'+'5. Proceed to the Office of the University Registrar for the procedures.<br><br><br>'
    message4 =  'For other concerns, please contact the official email of TUPC Registrar:   '+ 'tupc_registrar@tup.edu.ph<br><br><br><br>'
    message5 =  "<strong>"+'Technological University of the Philippines-Cavite Campus'+"</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br><br>'
    message6 =  "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"

    message = message1 + message2 + message3 +message4 + message5 + message6 

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send()

    messages.success(request, "Email Sent.")
    return redirect('/registrar_dashboard_graduation_list/%20')

def regclear_appointment(request,id):
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

    gender_temp = user_table.objects.filter(
    id=id).values_list('gender', flat=True).distinct()
    gender = user_table.objects.filter(
        gender=gender_temp[0]).values_list('gender', flat=True).distinct()
    gender_choice = gender[0]
    gender_final=""
    if gender_choice == "FEMALE":
        gender_final = "Ms."
    else:
        gender_final= "Mr."
    

    subject = 'Application for Clearance Form'
    message1 = 'Good day,   '+ gender_final + "<strong>" + name[0] + ",</strong><br><br>"
    message2 = 'Your Application for Clearance Form has been approved and is now available for printing. Kindly visit this' + '(link)' +' and follow the guidelines below.<br><br>'
    message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to this site'+ '(link)'+'.<br>'+'2. On your dashboard, view your request form from the table.<br>'+'3. Click the "Print" button to print the form. Please take note that the form should be printed in Legal Size Paper (8.5 x 14 inches).<br>'+'4. Arrive at the appointed date and time for claiming your request.<br>'+'5. Proceed to the Office of the University Registrar for the procedures.<br><br><br>'
    message4 =  'For other concerns, please contact the official email of TUPC Registrar:   '+ 'tupc_registrar@tup.edu.ph<br><br><br><br>'
    message5 =  "<strong>"+'Technological University of the Philippines-Cavite Campus'+"</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite<br><br><br>'
    message6 =  "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"

    message = message1 + message2 + message3 +message4 + message5 + message6 

    email_from = settings.EMAIL_HOST_USER
    recipient_list = [rec_email, ]
    msg = EmailMessage(subject, message, email_from, recipient_list,)
    msg.content_subtype = "html"
    msg.send()

    messages.success(request, "Email Sent.")
    return redirect('/registrar_dashboard_clearance_list/%20')

def request_appointment(request,id):
    if request.method == 'POST':
        email_temp = request_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            student_id=email_temp[0]).values_list('email', flat=True).distinct()
        rec_email = email[0]
        recipient_list = [rec_email, ]

        gender_temp = user_table.objects.filter(
        id=id).values_list('gender', flat=True).distinct()
        gender = user_table.objects.filter(
            gender=gender_temp[0]).values_list('gender', flat=True).distinct()
        gender_choice = gender[0]
        gender_final=""
        if gender_choice == "FEMALE":
            gender_final = "Ms."
        else:
            gender_final= "Mr."
        

        purpose = request_form_table.objects.filter(
        id=id).values_list('request', flat=True).distinct()
        purpose_of = request_form_table.objects.filter(
            request=purpose[0]).values_list('request', flat=True).distinct()
        purpose_of_req =  purpose_of[0]
        purpose_of_request = purpose_of_req, 

        name_temp = request_form_table.objects.filter(
        id=id).values_list('student_id', flat=True).distinct()
        name = user_table.objects.filter(
            student_id=name_temp[0]).values_list('last_name', flat=True).distinct()
        last_name = name[0]

        subject = 'Claiming of '+ purpose_of_request[0] 
        message1 = "Good day, "+ gender_final + "<strong>" + name[0] + ",</strong><br><br>"
        message2 = 'Your request for  '+ "<strong>"+ purpose_of_request[0] +"</strong>"+  \
            '   has been approved. Kindly visit the'+ '(link)' +' and follow the guidelines below for claiming your requested credentials.<br><br>'
        message3 = "<strong>"+'GUIDELINES:'+"</strong><br>"+'1. Login to this site '+ '(link)' +'.<br>'+'2. On your dashboard, view your request form from the table.<br>'+'3. Click the "Print" button to print the form. Please take note that the form should be printed in Legal Size Paper (8.5 x 14 inches).<br>'+ '4. For credentials with payment required, please prepare the amount to pay.'+'5. Arrive at the appointed date and time for claiming your request.<br>'+'6. Proceed to the Office of the University Registrar for the procedures.<br><br>'
        message4 =  'For other concerns, please contact the official email of TUPC Registrar:   '+ 'tupc_registrar@tup.edu.ph'
        message5 =  "<strong>"+'Technological University of the Philippines-Cavite Campus'+"</strong><br>"+'CQT Avenue, Salawag, Dasmarinas, Cavite'
        message6 =  "<i>"+'***This is an automated message, do not reply.<br><br>'+"</i>"


        message = message1 + message2 + message3 

        purpose_req = request.POST.get('purpose_of_request')
        amount = request.POST.get('amount')
        date_appointment = request.POST.get('date_appointment')
        request_form_table.objects.filter(
        id=id).update(appointment =date_appointment)

        time_appointment = request.POST.get('time_appointment')
        additionalmessage = request.POST.get('additionalmessage')
        email = request.POST.get('email')
       
        
        
        data = {
                'amount': amount,
                'date_appointment': date_appointment, 
                'time_appointment': time_appointment, 
                'subject': subject, 
                'message': message,
                'message4': message4,
                'message5': message5,
                'message6': message6,
                'additionalmessage': additionalmessage,
        }
        message='''{}
        <strong>Amount to  Pay:</strong>\n\t\t{}\n<br>
        <strong>Date of  Appointment:</strong>\n\t\t{}\n<br>
        <strong>Time of  Appointment:</strong>\n\t\t{}\n<br><br>
        <strong>Note from the TUPC Registrar:</strong>\n\t\t{}\n<br><br>
        \n\t\t{}\n<br><br><br><br>
        \n\t\t{}\n<br><br><br>
        \n\t\t{}\n<br>
        
        '''''.format(data['message'],data ['amount'],data ['date_appointment'], data ['time_appointment'], data ['additionalmessage'], data ['message4'], data ['message5'], data ['message6'])
        msg = EmailMessage(subject, message,'', email, recipient_list,)
        msg.content_subtype = "html"
        msg.send()
        messages.success(request, "Appointment Schedule Sent.")
        return redirect('registrar_dashboard_request_list')
    else:
        return render(request, 'html_files/appointment.html', {})

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
            print("P:",p)
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
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            last = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            temp= form.cleaned_data.get("profile_picture")
            
            # middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = email
            
            form.instance.full_name = first + " " + middle + " "+ last
           
            form.instance.user_type = "STUDENT"
            
            form.save()
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Account Saved. Keep in mind that your username is: ' + email)
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
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = email
            
            form.instance.full_name =   first + " "+ middle + " " + last 
           
            form.instance.user_type = "OLD STUDENT"
            form.save()
            # subject = 'SIGNUP SUCCESS'
            # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email, ]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Account Saved. Keep in mind that your username is: ' + email)
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
            username=form.cleaned_data.get("email")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.position = "FACULTY"
            form.instance.username = username
            form.instance.user_type = "FACULTY"
            form.instance.designation = "---"
            form.instance.full_name = last + ", " + first + " " + middle

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
            username = form.cleaned_data.get("email")
            id_num = form.cleaned_data.get("id_number")
            last = form.cleaned_data.get("last_name")
            first = form.cleaned_data.get("first_name")
            middle = form.cleaned_data.get("middle_name")
            form.instance.student_id = "TUPC-" + id_num
            form.instance.username = username
            form.instance.user_type = "ALUMNUS"
            form.instance.full_name = first + " " + middle + " "+ last
        
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
        
        # TO DETERMINE IF STUDENT IS 4TH YEAR OR NOT
        todays_date = date.today()
        id_num = request.user.id_number
        sliced_id = int(str(id_num)[:2]) 
        current_year ='"'+str(todays_date.year) +'"'
        temp =int(current_year[2:5])  
        graduating = temp - sliced_id 
 
        student_id = request.user.student_id
        full_name = request.user.full_name
        first = request.user.first_name
        last = request.user.last_name
        middle = request.user.middle_name
        
        mid = middle[0] + "."
        name2 = last + ", " + first + " " + mid

        print(student_id)

        st0 = request_form_table.objects.filter(student_id= student_id)
        st = graduation_form_table.objects.filter(student_id=student_id)
        st1 = clearance_form_table.objects.filter(student_id=student_id)
        
        check_form137 = Document_checker_table.objects.filter(Q(name=full_name)|Q(name=name2)).values_list('form_137',flat=True).distinct()
        check_form137_inrequest = request_form_table.objects.filter(Q(name=full_name)|Q(name=name2)).values_list('form_137',flat=True).distinct()
        check_clearance = clearance_form_table.objects.filter(student_id=student_id).values_list('approval_status',flat=True).distinct()
        check_graduation = graduation_form_table.objects.filter(student_id=student_id).values_list('approval_status',flat=True).distinct()
        check_apply_graduation = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request="Application for Graduation")).values_list('approval_status', flat=True).distinct()
        
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
        
        if request.user.user_type == "ALUMNUS":
            pass
        elif request.user.user_type == "OLD STUDENT":
            pass
        else: 
            if not check_clearance:
                display.append("CLEARANCE")
            else:
                for i in check_clearance:
                    if i == "APPROVED":
                        pass
                    else:
                        display.append("CLEARANCE (ON PROCESS)")
            
            if check_apply_graduation:
                if check_apply_graduation[0] != "APPROVED":
                    display.append("CLEARANCE OF APPLICATION FOR GRADUATION (ON PROCESS)")
                else:
                    pass
            else:
                pass
                
        if not check_graduation:
            pass
        else:
            if check_graduation[0] != 'APPROVED':
               
                display.append("GRADUATION (ON PROGRESS)")
  
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {'st': st, 'st1': st1, 'st0': st0, 'display':display, 'graduating': graduating }
    return render(request, 'html_files/4.1Student Dashboard.html', context)



@login_required(login_url='/')
def clearance_form(request):
    a = user_table.objects.filter(user_type="FACULTY").values_list('full_name', flat=True).distinct()
    
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        # TO DETERMINE IF STUDENT HAS GRADUATION OR NONE
        todays_date = date.today() 
        id_num = request.user.id_number
        sliced_id = int(str(id_num)[:2]) 
        current_year ='"'+str(todays_date.year) +'"'
        temp =int(current_year[2:5])  
        with_graduation = temp - sliced_id
        fullname = request.user.full_name
        print(with_graduation)
        
        user = request.user.user_type
        if request.method == "POST":
            form = clearance_form

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
            request_clearance = clearance_form_table.objects.filter(name=fullname).order_by('-time_requested').values_list('approval_status', flat=True).distinct()
            application_graduation = clearance_form_table.objects.filter(name=fullname).order_by('-time_requested').values_list('purpose_of_request', flat=True).distinct()
            check_apply_graduation = clearance_form_table.objects.filter(Q(name=fullname), Q(purpose_of_request="Application for Graduation")).values_list('approval_status', flat=True).distinct()
            
            if request_clearance:
                if application_graduation[0] !="Application for Graduation":
                    if request_clearance[0] =="APPROVED":
                        allow_request = request_clearance[0]
                        if check_apply_graduation:
                            graduation_allow = check_apply_graduation[0]
                        else:
                            graduation_allow = ""
                    else:
                        allow_request = "UNAPPROVED"
                        if check_apply_graduation:
                            if check_apply_graduation[0] == "APPROVED":
                                graduation_allow = check_apply_graduation[0]
    
                            else:
                                graduation_allow = check_apply_graduation[0]
                        else:
                            graduation_allow = ""
                else:
                    allow_request =""
                    if check_apply_graduation[0] == "APPROVED":
                        graduation_allow = check_apply_graduation[0]

                    else:
                        graduation_allow = check_apply_graduation[0]
            else:
                allow_request = ""
                graduation_allow = ""

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.2Student Clearance Form.html', {'a': a, 'with_graduation':with_graduation, 'allow' : allow_request, 'graduation_allow': graduation_allow})

def clearance_view(request):
    fullname = request.user.full_name
    check_apply_graduation = clearance_form_table.objects.filter(Q(name=fullname), Q(purpose_of_request="Application for Graduation")).values_list('approval_status', flat=True).distinct()
    id_application_for_grad = clearance_form_table.objects.filter(Q(name=fullname), Q(purpose_of_request="Application for Graduation")).values_list('id', flat=True).distinct()
    clearance_for_graduation = clearance_form_table.objects.filter(Q(name=fullname), Q(purpose_of_request="Application for Graduation")).values()
    
    if id_application_for_grad:
        id = id_application_for_grad[0]
    else:
        pass
    
    if check_apply_graduation:
        #Signature Display
        #ACCOUNTANT
        check_status = clearance_form_table.objects.filter(id=id,accountant_signature__icontains = 'UNAPPROVED')
        if check_status:
            accountant = "UNAPPROVED"
            accountant_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('accountant_signature', flat=True).distinct()
            acc_sig = str(faculty_approved[0])
            fac_name_get = acc_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            account_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            accountant = account_sig[0]
            accountant_name = str_fac_name
            
        #COURSE ADVISER
        check_status = clearance_form_table.objects.filter(id=id,course_adviser_signature__icontains = 'UNAPPROVED')
        if check_status:
            course_adviser = "UNAPPROVED"
            adviser_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('course_adviser_signature', flat=True).distinct()
            adviser_sig = str(faculty_approved[0])
            fac_name_get = adviser_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            ca_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            course_adviser = ca_sig[0]
            adviser_name = str_fac_name
        
        #LIBERAL ARTS
        check_status = clearance_form_table.objects.filter(id=id,liberal_arts_signature__icontains = 'UNAPPROVED')
        if check_status:
            liberal_arts = "UNAPPROVED"
            liberal_artsName = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('liberal_arts_signature', flat=True).distinct()
            lib_sig = str(faculty_approved[0])
            fac_name_get = lib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            libart_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            liberal_arts = libart_sig[0]
            liberal_artsName = str_fac_name
        
        #CAMPUS LIBRARIAN
        check_status = clearance_form_table.objects.filter(id=id,library_signature__icontains = 'UNAPPROVED')
        if check_status:
            campus_library = "UNAPPROVED"
            librarian_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('library_signature_signature', flat=True).distinct()
            camlib_sig = str(faculty_approved[0])
            fac_name_get = camlib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            cam_lib_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            campus_library = cam_lib_sig[0]
            librarian_name = str_fac_name
        
        #MATH & SCIENCES
        check_status = clearance_form_table.objects.filter(id=id,mathsci_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            math_and_science = "UNAPPROVED"
            math_and_science_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('mathsci_dept_signature', flat=True).distinct()
            mas_sig = str(faculty_approved[0])
            fac_name_get = mas_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            mathsci_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            math_and_science = mathsci_sig[0]
            math_and_science_name = str_fac_name
            
        #GUIDANCE COUNCELOR
        check_status = clearance_form_table.objects.filter(id=id,guidance_office_signature__icontains = 'UNAPPROVED')
        if check_status:
            guidance = "UNAPPROVED"
            guidance_councelor = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('guidance_office_signature', flat=True).distinct()
            guid_sig = str(faculty_approved[0])
            fac_name_get = guid_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            gui_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            guidance = gui_sig[0]
            guidance_councelor = str_fac_name
        
        #DPECS
        check_status = clearance_form_table.objects.filter(id=id,pe_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            dpecs = "UNAPPROVED"
            dpecs_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('pe_dept_signature', flat=True).distinct()
            pe_sig = str(faculty_approved[0])
            fac_name_get = pe_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            pe_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            dpecs = pe_dept_sig[0]
            dpecs_name = str_fac_name
        
        #OSA
        check_status = clearance_form_table.objects.filter(id=id,osa_signature__icontains = 'UNAPPROVED')
        if check_status:
            osa = "UNAPPROVED"
            osa_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('osa_signature', flat=True).distinct()
            student_osa_sig = str(faculty_approved[0])
            fac_name_get = student_osa_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            student_affairs_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            osa = student_affairs_sig[0]
            osa_name = str_fac_name
        
        #ADAA
        check_status = clearance_form_table.objects.filter(id=id,academic_affairs_signature__icontains = 'UNAPPROVED')
        if check_status:
            adaa = "UNAPPROVED"
            adaa_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('academic_affairs_signature', flat=True).distinct()
            asst_dir_acad_sig = str(faculty_approved[0])
            fac_name_get = asst_dir_acad_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            adaa_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            adaa = adaa_sig[0]
            adaa_name = str_fac_name
        
        #INDUSTRIAL
        check_status = clearance_form_table.objects.filter(id=id,ieduc_dept_signature__icontains = 'UNAPPROVED',it_dept_signature__icontains = 'UNAPPROVED',ieng_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            industrial = "UNAPPROVED"
            it_department = "NONE"
            it_name = " "
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
                it_name = str_fac_name
            
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
                it_name = str_fac_name
                
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
                it_name = str_fac_name
        
        context ={
            'clearance' : clearance_for_graduation,
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
            'adaa' : adaa,
            'accountant_name' : accountant_name,
            'adviser_name' : adviser_name,
            'liberal_artsName' : liberal_artsName,
            'librarian_name' : librarian_name,
            'math_and_science_name' : math_and_science_name,
            'guidance_councelor' : guidance_councelor,
            'dpecs_name' : dpecs_name,
            'osa_name' : osa_name,
            'adaa_name' : adaa_name,
            'it_name' : it_name,
                
            }
        return render(request, 'html_files/clearance_form_display.html',context)
    else:
        return redirect(clearance_form)

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

            # u2 = request.POST.get('starttime2')
            # v2 = request.POST.get('endtime2')
            # q2 = request.POST.get('day2')
            # u3 = request.POST.get('starttime3')
            # v3 = request.POST.get('endtime3')
            # q3 = request.POST.get('day3')

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

            # w2 = request.POST.get('add_starttime2')
            # x2 = request.POST.get('add_endtime2')
            # r2 = request.POST.get('addday2')
            # r3 = request.POST.get('addday3')
            # w3 = request.POST.get('add_starttime3')
            # x3 = request.POST.get('add_endtime3')

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
            if t6 == "1":
                t6 = "NO FACULTY"
                sig_t6 = "NO_APPROVED"
            else:
                sig_t6 = t6 + "_UNAPPROVED"
            if t7 == "1":
                t7 = "NO FACULTY"
                sig_t7 = "NO_APPROVED"
            else:
                sig_t7 = t7 + "_UNAPPROVED"
            if t8 == "1":
                t8 = "NO FACULTY"
                sig_t8 = "NO_APPROVED"
            else:
                sig_t8 = t8 + "_UNAPPROVED"
            if t9 == "1":
                t9 = "NO FACULTY"
                sig_t9 = "NO_APPROVED"
            else:
                sig_t9 = t9 + "_UNAPPROVED"
            if t10 == "1":
                t10 = "NO FACULTY"
                sig_t10 = "NO_APPROVED"    
            else:
                sig_t10 = t10 + "_UNAPPROVED"

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
        student_id = request.user.student_id
        print(student_id)

        st = graduation_form_table.objects.filter(student_id=student_id)
        st1 = clearance_form_table.objects.filter(student_id=student_id)
    
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
        st1=""
        st = graduation_form_table.objects.filter(Q(signature1=unapproved) | Q(signature2=unapproved) | Q(signature3=unapproved) |
                                                  Q(signature4=unapproved) | Q(signature5=unapproved) | Q(signature6=unapproved) |
                                                  Q(signature7=unapproved) | Q(signature8=unapproved) | Q(signature9=unapproved) | Q(signature10=unapproved) |
                                                  Q(addsignature1=unapproved) | Q(addsignature2=unapproved) | Q(addsignature3=unapproved) |
                                                  Q(addsignature4=unapproved) | Q(addsignature5=unapproved) | Q(addsignature6=unapproved) |
                                                  Q(addsignature7=unapproved) | Q(addsignature8=unapproved) | Q(addsignature9=unapproved) |
                                                  Q(addsignature10=unapproved)).order_by('-time_requested')
        print(unapproved)

        if request.user.department == "HOCS":
            st1 = clearance_form_table.objects.filter(accountant_signature="UNAPPROVED").order_by('-time_requested') 
        elif request.user.department == "HDLA":
            st1 = clearance_form_table.objects.filter(liberal_arts_signature = "UNAPPROVED").order_by('-time_requested') 
        elif request.user.department == "HDMS":
            st1 = clearance_form_table.objects.filter(mathsci_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDPECS":
            st1 = clearance_form_table.objects.filter(pe_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDIT":
            st1 = clearance_form_table.objects.filter(it_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HDIE":
            st1 = clearance_form_table.objects.filter(ieduc_dept_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HOCL":
            st1 = clearance_form_table.objects.filter(library_signature="UNAPPROVED").order_by('-time_requested')
        elif request.user.department == "HOGS":
            st1 = clearance_form_table.objects.filter(guidance_office_signature="UNAPPROVED").order_by('-time_requested') 
        elif request.user.department == "HOSA":
            st1 = clearance_form_table.objects.filter(osa_signature="UNAPPROVED").order_by('-time_requested') 
        elif request.user.department == "HADAA":
            st1 = clearance_form_table.objects.filter(academic_affairs_signature="UNAPPROVED").order_by('-time_requested')
               
        if clearance_form_table.objects.filter(course_adviser_signature = unapproved):
            st1= clearance_form_table.objects.filter(course_adviser_signature = unapproved).order_by('-time_requested')    

        with_clearance = clearance_form_table.objects.filter(course_adviser=request.user.full_name)  
        return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, 'st1':st1, 'with_clearance':with_clearance })


         
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

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
    dep= request.user.department 
    course_adv= clearance_form_table.objects.filter(course_adviser=request.user.full_name )
    
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if request.user.department == "HOCS":
            st = clearance_form_table.objects.filter(accountant_signature="UNAPPROVED").order_by('-time_requested') 
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(accountant_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HDLA":
            st = clearance_form_table.objects.filter(liberal_arts_signature = "UNAPPROVED").order_by('-time_requested') 
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(liberal_arts_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HDMS":
            st = clearance_form_table.objects.filter(mathsci_dept_signature="UNAPPROVED").order_by('-time_requested')
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(mathsci_dept_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HDPECS":
            st = clearance_form_table.objects.filter(pe_dept_signature="UNAPPROVED").order_by('-time_requested')
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(pe_dept_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HDIT":
            st = clearance_form_table.objects.filter(it_dept_signature="UNAPPROVED").order_by('-time_requested')
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(it_dept_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HDIE":
            st = clearance_form_table.objects.filter(ieduc_dept_signature="UNAPPROVED").order_by('-time_requested')
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(ieduc_dept_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HOCL":
            st = clearance_form_table.objects.filter(library_signature="UNAPPROVED").order_by('-time_requested')
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(library_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HOGS":
            st = clearance_form_table.objects.filter(guidance_office_signature="UNAPPROVED").order_by('-time_requested') 
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(guidance_office_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HOSA":
            st = clearance_form_table.objects.filter(osa_signature="UNAPPROVED").order_by('-time_requested') 
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(osa_signature="UNAPPROVED")).order_by('-time_requested')    
    
        elif request.user.department == "HADAA":
            st = clearance_form_table.objects.filter(academic_affairs_signature="UNAPPROVED").order_by('-time_requested')
               
            if clearance_form_table.objects.filter(course_adviser_signature = f_n_unapproved):
                st= clearance_form_table.objects.filter(Q(course_adviser_signature = f_n_unapproved) & Q(academic_affairs_signature="UNAPPROVED")).order_by('-time_requested')    
        else:
            st = clearance_form_table.objects.filter(course_adviser_signature=f_n_unapproved).order_by('-time_requested')


        # st= clearance_form_table.objects.all().order_by('-time_requested')
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            print("list:", id_list) 
            for i in id_list:
                if clearance_form_table.objects.filter(course_adviser_signature=f_n +"_UNAPPROVED", id=int(i)):
                 clearance_form_table.objects.filter(id=int(i)).update(
                course_adviser_signature=f_n_approved)
    
                if request.user.department == "HOCS":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(accountant_signature=f_n_approved)

                if request.user.department == "HDMS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        mathsci_dept_signature=f_n_approved)

                if request.user.department == "HDPECS":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(pe_dept_signature=f_n_approved)

                if request.user.department == "HDED":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(ieduc_dept_signature=f_n_approved)

                if request.user.department == "HDIT":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(it_dept_signature=f_n_approved)

                if request.user.department == "HDIE":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(ieng_dept_signature=f_n_approved)

                if request.user.department == "HOCL":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(library_signature=f_n_approved)

                if request.user.department == "HOGS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        guidance_office_signature=f_n_approved)

                if request.user.department == "HOSA":
                    clearance_form_table.objects.filter(
                        id=int(i)).update(osa_signature=f_n_approved)

                if request.user.department == "HADAA":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        academic_affairs_signature=f_n_approved)
            
                name_temp = clearance_form_table.objects.filter(
                id=int(i)).values_list('name', flat=True).distinct()
                email_temp = clearance_form_table.objects.filter(
                    id=int(i)).values_list('student_id', flat=True).distinct()
                email = user_table.objects.filter(
                    student_id=email_temp[0]).values_list('email', flat=True).distinct()
                rec_email = email[0]
                f_n = request.user.full_name
                cursor = connection.cursor()
                query= "SELECT approval_status from `gradclear_app_clearance_form_table` where id=%s"
                val=(int(i),)
                cursor.execute(query, val)

                row = cursor.fetchone()
                rownum=row[0]
                print('rownum', rownum)
                if len(rownum) <5:
                    temp=rownum[0]
                    print(temp,"this 1")
                else:
                    rownum1=rownum[0]
                    rownum2=rownum[1]
                    full_num= rownum1[0],rownum2[0]
                    temp = full_num[0] + full_num[1]
                    print("this 2",temp)

                app_status = int(temp)
                print(app_status)
                numerator =app_status +1
                adder = str(numerator) + "/12"
                dep = request.user.department
                
                if dep == "HDLA":
                    clearance_form_table.objects.filter(id=int(i)).update(
                    liberal_arts_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                    approval_status=adder)               
                if dep == "HOCS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        accountant_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                if dep == "HDMS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        mathsci_dept_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)               
                if dep == "HDPECS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        pe_dept_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                if dep == "HDED":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        ieduc_dept_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                if dep == "HDIT":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        it_dept_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)               
                if dep == "HDIE":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        ieng_dept_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                if dep == "HOCL":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        library_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)               
                if dep == "HOGS":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        guidance_office_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                if dep == "HOSA":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        osa_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)               
                if dep == "HADAA":
                    clearance_form_table.objects.filter(id=int(i)).update(
                        academic_affairs_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)  
                if clearance_form_table.objects.filter(course_adviser=f_n):
                    clearance_form_table.objects.filter(id=int(i)).update(
                        course_adviser_signature=f_n_approved)
                    clearance_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                approved_text = "_APPROVED"
                approval_status_checker=clearance_form_table.objects.filter(
                    Q(liberal_arts_signature__endswith=approved_text) &
                    Q(accountant_signature__endswith=approved_text) &
                    Q(mathsci_dept_signature__endswith=approved_text) &
                    Q(pe_dept_signature__endswith=approved_text) &
                    Q(ieduc_dept_signature__endswith=approved_text) &
                    Q(it_dept_signature__endswith=approved_text) &
                    Q(ieng_dept_signature__endswith=approved_text) &
                    Q(library_signature__endswith=approved_text) &
                    Q(guidance_office_signature__endswith=approved_text) &
                    Q(osa_signature__endswith=approved_text) &
                    Q(academic_affairs_signature__endswith=approved_text) &
                    Q(course_adviser_signature__endswith=approved_text), id=int(i))
                if approval_status_checker:
                    clearance_form_table.objects.filter(
                                id=int(i)).update(approval_status="APPROVED")
                    
                    name = name_temp[0]
                    request_form_table.objects.filter(
                                name=name).update(clearance="✔")
                    

                messages.success(request, "Form Approved.")

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/') 
    return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'dep':dep, 'f_n_unapproved':f_n_unapproved, 'f_n_approved':f_n_approved, 'course_adv':course_adv, 'e_signature' : esignature, 'esignature_datetime' : esignature_datetime, 'uploaded_signature': uploaded_signature, 'uploaded_datetime' : uploaded_signature_datetime,  'id' : id_Facultynumber})

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

    cursor = connection.cursor()
    query= "SELECT approval_status from `gradclear_app_clearance_form_table` where id=%s"
    val=(id,)
    cursor.execute(query, val)

    row = cursor.fetchone()
    rownum=row[0]
    print('rownum', rownum)
    if len(rownum) <5:
        temp=rownum[0]
        print(temp,"this 1")
    else:
        rownum1=rownum[0]
        rownum2=rownum[1]
        full_num= rownum1[0],rownum2[0]
        temp = full_num[0] + full_num[1]
        print("this 2",temp)

    app_status = int(temp)
    print(app_status)
    numerator =app_status +1
    adder = str(numerator) + "/12"


    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if dep == "liberal_arts_signature":
            clearance_form_table.objects.filter(id=id).update(
                liberal_arts_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)               
        if dep == "accountant_signature":
            clearance_form_table.objects.filter(id=id).update(
                accountant_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "mathsci_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                mathsci_dept_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)               
        if dep == "pe_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                pe_dept_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "ieduc_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                ieduc_dept_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "it_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                it_dept_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)               
        if dep == "ieng_dept_signature":
            clearance_form_table.objects.filter(id=id).update(
                ieng_dept_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "library_signature":
            clearance_form_table.objects.filter(id=id).update(
                library_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)               
        if dep == "guidance_office_signature":
            clearance_form_table.objects.filter(id=id).update(
                guidance_office_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if dep == "osa_signature":
            clearance_form_table.objects.filter(id=id).update(
                osa_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)               
        if dep == "academic_affairs_signature":
            clearance_form_table.objects.filter(id=id).update(
                academic_affairs_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)  
        if dep == "course_adviser_signature":
            clearance_form_table.objects.filter(id=id).update(
                course_adviser_signature=f_n_approved)
            clearance_form_table.objects.filter(id=id).update(
                approval_status=adder)
        
        approved_text = "_APPROVED"
        approval_status_checker=clearance_form_table.objects.filter(
            Q(liberal_arts_signature__endswith=approved_text) &
            Q(accountant_signature__endswith=approved_text) &
            Q(mathsci_dept_signature__endswith=approved_text) &
            Q(pe_dept_signature__endswith=approved_text) &
            Q(ieduc_dept_signature__endswith=approved_text) &
            Q(it_dept_signature__endswith=approved_text) &
            Q(ieng_dept_signature__endswith=approved_text) &
            Q(library_signature__endswith=approved_text) &
            Q(guidance_office_signature__endswith=approved_text) &
            Q(osa_signature__endswith=approved_text) &
            Q(academic_affairs_signature__endswith=approved_text) &
            Q(course_adviser_signature__endswith=approved_text), id=id)
        if approval_status_checker:
            clearance_form_table.objects.filter(
                        id=id).update(approval_status="APPROVED")
            
            name = name_temp[0]
            request_form_table.objects.filter(
                        name=name).update(clearance="✔")
            
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
        esignature = request.user.e_signature
        esignature_datetime = request.user.e_signature_timesaved
        uploaded_signature = request.user.uploaded_signature
        uploaded_signature_datetime = request.user.uploaded_signature_timesaved
        id_Facultynumber = request.user.id

        full_name=request.user.full_name
        f_n_unapproved= request.user.full_name + "_UNAPPROVED"
        f_n_approved= request.user.full_name + "_APPROVED"

        st= graduation_form_table.objects.filter(Q(faculty1=full_name)| Q(faculty2=full_name) |
        Q(faculty3=full_name)| Q(faculty4=full_name) |Q(faculty5=full_name)| Q(faculty6=full_name) |
        Q(faculty7=full_name)| Q(faculty8=full_name) |Q(faculty9=full_name)| Q(faculty10=full_name) |
        Q(addfaculty1=full_name)| Q(addfaculty2=full_name) |Q(addfaculty3=full_name)| Q(addfaculty4=full_name) |
        Q(addfaculty5=full_name)| Q(addfaculty6=full_name) |Q(addfaculty7=full_name)| Q(addfaculty8=full_name) |
        Q(addfaculty9=full_name)| Q(addfaculty10=full_name)|Q(instructor_name=full_name) ).order_by('-time_requested')
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            print("list:", id_list) 
            for i in id_list:
                name_temp = graduation_form_table.objects.filter(
                id=int(i)).values_list('name', flat=True).distinct()
                email_temp = graduation_form_table.objects.filter(
                    id=int(i)).values_list('student_id', flat=True).distinct()
                email = user_table.objects.filter(
                    student_id=email_temp[0]).values_list('email', flat=True).distinct()
        
                rec_email = email[0]
                print(rec_email) 
                f_n1 = request.user.full_name + '_UNAPPROVED'
                    
                approval =request.user.full_name + "_APPROVED"
                c1= graduation_form_table.objects.filter(id=int(i), signature1__contains = "NO_APPROVED").count()
                c2= graduation_form_table.objects.filter(id=int(i), signature2__contains = "NO_APPROVED").count()
                c3= graduation_form_table.objects.filter(id=int(i), signature3__contains = "NO_APPROVED").count()
                c4= graduation_form_table.objects.filter(id=int(i), signature4__contains = "NO_APPROVED").count()
                c5= graduation_form_table.objects.filter(id=int(i), signature5__contains = "NO_APPROVED").count()
                c6= graduation_form_table.objects.filter(id=int(i), signature6__contains = "NO_APPROVED").count()
                c7= graduation_form_table.objects.filter(id=int(i), signature7__contains = "NO_APPROVED").count()
                c8= graduation_form_table.objects.filter(id=int(i), signature8__contains = "NO_APPROVED").count()
                c9= graduation_form_table.objects.filter(id=int(i), signature9__contains = "NO_APPROVED").count()
                c10= graduation_form_table.objects.filter(id=int(i), signature10__contains = "NO_APPROVED").count()
                ac1= graduation_form_table.objects.filter(id=int(i), addsignature1__contains = "NO_APPROVED").count()
                ac2= graduation_form_table.objects.filter(id=int(i), addsignature2__contains = "NO_APPROVED").count()
                ac3= graduation_form_table.objects.filter(id=int(i), addsignature3__contains = "NO_APPROVED").count()
                ac4= graduation_form_table.objects.filter(id=int(i), addsignature4__contains = "NO_APPROVED").count()
                ac5= graduation_form_table.objects.filter(id=int(i), addsignature5__contains = "NO_APPROVED").count()
                ac6= graduation_form_table.objects.filter(id=int(i), addsignature6__contains = "NO_APPROVED").count()
                ac7= graduation_form_table.objects.filter(id=int(i), addsignature7__contains = "NO_APPROVED").count()
                ac8= graduation_form_table.objects.filter(id=int(i), addsignature8__contains = "NO_APPROVED").count()
                ac9= graduation_form_table.objects.filter(id=int(i), addsignature9__contains = "NO_APPROVED").count()
                ac10= graduation_form_table.objects.filter(id=int(i), addsignature10__contains = "NO_APPROVED").count()
                sc1= graduation_form_table.objects.filter(id=int(i), sitsignature__contains = "NO_APPROVED").count()
                
                 
                f_n = request.user.full_name
                if graduation_form_table.objects.filter(
                    sitsignature__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(sitsignature=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                            approval_status=adder)

                if graduation_form_table.objects.filter(
                    signature1__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature1=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)

                if graduation_form_table.objects.filter(
                    signature2__contains=f_n1, id=int(i)): 
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature2=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature3__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature3=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature4__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature4=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature5__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature5=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature6__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature6=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature7__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature7=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature8__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature8=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature9__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature9=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    signature10__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(signature10=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature1__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature1=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature2__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature2=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature3__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature3=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature4__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature4=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature5__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature5=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature6__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature6=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature7__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature7=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature8__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature8=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature9__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature9=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
                    adder = str(numerator) + "/" + str(denominator)

                    graduation_form_table.objects.filter(id=int(i)).update(
                        approval_status=adder)
                
                if graduation_form_table.objects.filter(
                    addsignature10__contains=f_n1, id=int(i)):
                    graduation_form_table.objects.filter(
                        id=int(i)).update(addsignature10=approval)
                    
                    total= 0
                    final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,
                                    ac6,ac7,ac8,ac9,ac10,sc1]
                    for a in final_count:
                        total+= a
                    denominator = 21 - int(total) 
                    cursor = connection.cursor()
                    query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
                    val=(int(i),)
                    cursor.execute(query, val)

                    row = cursor.fetchone()
                    rownum=row[0]
                    print('rownum', rownum)
                    if len(rownum) <5:
                        temp=rownum[0]
                        print(temp,"this 1")
                    else:
                        rownum1=rownum[0]
                        rownum2=rownum[1]
                        full_num= rownum1[0],rownum2[0]
                        temp = full_num[0] + full_num[1]
                        print("this 2",temp)

                    app_status = int(temp)
                    numerator =app_status +1
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
                f_n_approved =request.user.full_name + "_APPROVED"
        
                messages.success(request, "Subject Approved.") 

                approval_status_checker_2=graduation_form_table.objects.filter(id=int(i),
                    signature1__endswith = '_APPROVED' ,
                    signature2__endswith = '_APPROVED' , 
                    signature3__endswith = '_APPROVED' , 
                    signature4__endswith = '_APPROVED' , 
                    signature5__endswith = '_APPROVED' , 
                    signature6__endswith = '_APPROVED' , 
                    signature7__endswith = '_APPROVED' , 
                    signature8__endswith = '_APPROVED' , 
                    signature9__endswith = '_APPROVED' , 
                    signature10__endswith = '_APPROVED' , 
                    addsignature1__endswith = '_APPROVED' , 
                    addsignature2__endswith = '_APPROVED' , 
                    addsignature3__endswith = '_APPROVED' , 
                    addsignature4__endswith = '_APPROVED' , 
                    addsignature5__endswith = '_APPROVED' , 
                    addsignature6__endswith = '_APPROVED' , 
                    addsignature7__endswith = '_APPROVED' , 
                    addsignature8__endswith = '_APPROVED' , 
                    addsignature9__endswith = '_APPROVED' , 
                    addsignature10__endswith = '_APPROVED',
                    sitsignature__endswith = '_APPROVED')

                if approval_status_checker_2:
                    print(approval_status_checker_2)
                    graduation_form_table.objects.filter(
                        id=int(i)).update(approval_status="APPROVED")
                    
                    
            return redirect(faculty_dashboard_graduation_list)

                
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.3Faculty Graduation List.html', {'st': st, 'f_n_unapproved': f_n_unapproved,'f_n_approved': f_n_approved, 'e_signature' : esignature, 'esignature_datetime' : esignature_datetime, 'uploaded_signature': uploaded_signature, 'uploaded_datetime' : uploaded_signature_datetime, 'id' : id_Facultynumber})

@login_required(login_url='/')
def update_graduation(request, id, sig, type):
    print("starts here")
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print(type)
        name_temp = graduation_form_table.objects.filter(
            id=id).values_list('name', flat=True).distinct()
        email_temp = graduation_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            student_id=email_temp[0]).values_list('email', flat=True).distinct()
 
        rec_email = email[0]
        print(rec_email) 
        f_n_unapproved = request.user.full_name + '_UNAPPROVED'
        f_n_approved =request.user.full_name + "_APPROVED"

        c1= graduation_form_table.objects.filter(id=id, signature1__contains = "NO_APPROVED").count()
        c2= graduation_form_table.objects.filter(id=id, signature2__contains = "NO_APPROVED").count()
        c3= graduation_form_table.objects.filter(id=id, signature3__contains = "NO_APPROVED").count()
        c4= graduation_form_table.objects.filter(id=id, signature4__contains = "NO_APPROVED").count()
        c5= graduation_form_table.objects.filter(id=id, signature5__contains = "NO_APPROVED").count()
        c6= graduation_form_table.objects.filter(id=id, signature6__contains = "NO_APPROVED").count()
        c7= graduation_form_table.objects.filter(id=id, signature7__contains = "NO_APPROVED").count()
        c8= graduation_form_table.objects.filter(id=id, signature8__contains = "NO_APPROVED").count()
        c9= graduation_form_table.objects.filter(id=id, signature9__contains = "NO_APPROVED").count()
        c10= graduation_form_table.objects.filter(id=id, signature10__contains = "NO_APPROVED").count()
        ac1= graduation_form_table.objects.filter(id=id, addsignature1__contains = "NO_APPROVED").count()
        ac2= graduation_form_table.objects.filter(id=id, addsignature2__contains = "NO_APPROVED").count()
        ac3= graduation_form_table.objects.filter(id=id, addsignature3__contains = "NO_APPROVED").count()
        ac4= graduation_form_table.objects.filter(id=id, addsignature4__contains = "NO_APPROVED").count()
        ac5= graduation_form_table.objects.filter(id=id, addsignature5__contains = "NO_APPROVED").count()
        ac6= graduation_form_table.objects.filter(id=id, addsignature6__contains = "NO_APPROVED").count()
        ac7= graduation_form_table.objects.filter(id=id, addsignature7__contains = "NO_APPROVED").count()
        ac8= graduation_form_table.objects.filter(id=id, addsignature8__contains = "NO_APPROVED").count()
        ac9= graduation_form_table.objects.filter(id=id, addsignature9__contains = "NO_APPROVED").count()
        ac10= graduation_form_table.objects.filter(id=id, addsignature10__contains = "NO_APPROVED").count()
        sc1= graduation_form_table.objects.filter(id=id, sitsignature__contains = "NO_APPROVED").count()
        
        final_count = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8,ac9,ac10,sc1]
        total= 0
        for i in final_count:
            total+= i
        denominator = 21 - int(total) 
        cursor = connection.cursor()
        query= "SELECT approval_status from `gradclear_app_graduation_form_table` where id=%s"
        val=(id,)
        cursor.execute(query, val)

        row = cursor.fetchone()
        rownum=row[0]
        print('rownum', rownum)
        if len(rownum) <5:
            temp=rownum[0]
            print(temp,"this 1")
        else:
            rownum1=rownum[0]
            rownum2=rownum[1]
            full_num= rownum1[0],rownum2[0]
            temp = full_num[0] + full_num[1]
            print("this 2",temp)

        app_status = int(temp)
        numerator =app_status +1
        adder = str(numerator) + "/" + str(denominator)

        if sig == "signature1":
            graduation_form_table.objects.filter(id=id).update(
                signature1=f_n_approved) 
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
              
        if sig == "signature2":
            graduation_form_table.objects.filter(id=id).update(
                signature2=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature3":
            graduation_form_table.objects.filter(id=id).update(
                signature3=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature4":
            graduation_form_table.objects.filter(id=id).update(
                signature4=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature5":
            graduation_form_table.objects.filter(id=id).update(
                signature5=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature6":
            graduation_form_table.objects.filter(id=id).update(
                signature6=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature7":
            graduation_form_table.objects.filter(id=id).update(
                signature7=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature8":
            graduation_form_table.objects.filter(id=id).update(
                signature8=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature9":
            graduation_form_table.objects.filter(id=id).update(
                signature9=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "signature10":
            graduation_form_table.objects.filter(id=id).update(
                signature10=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature1":
            graduation_form_table.objects.filter(id=id).update(
                addsignature1=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature2":
            graduation_form_table.objects.filter(id=id).update(
                addsignature2=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature3":
            graduation_form_table.objects.filter(id=id).update(
                addsignature3=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature4":
            graduation_form_table.objects.filter(id=id).update(
                addsignature4=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature5":
            graduation_form_table.objects.filter(id=id).update(
                addsignature5=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature6":
            graduation_form_table.objects.filter(id=id).update(
                addsignature6=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature7":
            graduation_form_table.objects.filter(id=id).update(
                addsignature7=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature8":
            graduation_form_table.objects.filter(id=id).update(
                addsignature8=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature9":
            graduation_form_table.objects.filter(id=id).update(
                addsignature9=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "addsignature10":
            graduation_form_table.objects.filter(id=id).update(
                addsignature10=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
        if sig == "sitsignature":
            graduation_form_table.objects.filter(id=id).update(
                sitsignature=f_n_approved)
            graduation_form_table.objects.filter(id=id).update(
                approval_status=adder)
                 
        messages.success(request, "Subject Approved.") 

        approval_status_checker_2=graduation_form_table.objects.filter(id=id,
            signature1__endswith = '_APPROVED' ,
            signature2__endswith = '_APPROVED' , 
            signature3__endswith = '_APPROVED' , 
            signature4__endswith = '_APPROVED' , 
            signature5__endswith = '_APPROVED' , 
            signature6__endswith = '_APPROVED' , 
            signature7__endswith = '_APPROVED' , 
            signature8__endswith = '_APPROVED' , 
            signature9__endswith = '_APPROVED' , 
            signature10__endswith = '_APPROVED' , 
            addsignature1__endswith = '_APPROVED' , 
            addsignature2__endswith = '_APPROVED' , 
            addsignature3__endswith = '_APPROVED' , 
            addsignature4__endswith = '_APPROVED' , 
            addsignature5__endswith = '_APPROVED' , 
            addsignature6__endswith = '_APPROVED' , 
            addsignature7__endswith = '_APPROVED' , 
            addsignature8__endswith = '_APPROVED' , 
            addsignature9__endswith = '_APPROVED' , 
            addsignature10__endswith = '_APPROVED',
            sitsignature__endswith = '_APPROVED')

        if approval_status_checker_2:
            print(approval_status_checker_2)
            graduation_form_table.objects.filter(
                id=id).update(approval_status="APPROVED")
             
        return redirect(faculty_dashboard_graduation_list)
        
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    


@login_required(login_url='/')
def registrar_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
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
      
       
        
        unapproved_forms_count = clearance_form_table.objects.filter(approval_status="APPROVED").count()
        clearance_count = all.count() - unapproved_forms_count
        if clearance_count == 0:
            clearance_badge =""
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
       

       
        unapproved_forms_count2 = graduation_form_table.objects.filter(approval_status="APPROVED").count()
        graduation_count = graduation_form_table.objects.all().count() - unapproved_forms_count2
        if graduation_count == 0:
            graduation_badge =""
        else:
            graduation_badge = graduation_count
        
        unapproved_forms_count3 = request_form_table.objects.filter(claim="CLAIMED").count()
        request_count = request_form_table.objects.all().count() - unapproved_forms_count3
        if request_count == 0:
            request_badge =""
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
                   'c_PPET': c_PPET, 'cBSIE_AET': cBSIE_AET,'cBSIE_MPET': cBSIE_MPET, 'cBTTE_ART': cBTTE_ART, 
                   'cBTTE_AET': cBTTE_AET, 'cBTTE_CET': cBTTE_CET,'cBTTE_CoET': cBTTE_CoET, 'cBBTTE_EET': cBTTE_EET, 
                   'cBTTE_EsET': cBTTE_EsET, 'cBTTE_MPET': cBTTE_MPET,'cBTTE_PPET': cBTTE_PPET,'cBT_AET':cBT_AET,

                   'gBSIE_ICT': gBSIE_ICT, 'gBSIE_IA': gBSIE_IA, 'gBGT_ART': gBGT_ART, 'gBET_CT': gBET_CT,
                   'gBET_ET': gBET_ET, 'gBET_EsET': gBET_EsET, 'gBET_CoET': gBET_CoET, 'gBET_MT': gBET_MT,
                   'gBET_PPT': gBET_PPT, 'gBT_CET': gBT_CET, 'gBT_CoET': gBT_CoET, 'gBT_EET': gBT_EET,
                   'gBT_EsET': gBT_EsET, 'gBT_MPET': gBT_MPET, 'gBT_PPET': gBT_PPET, 'g_MPET': g_MPET,
                   'g_PPET': g_PPET, 'gBSIE_AET': gBSIE_AET,'gBSIE_MPET': gBSIE_MPET, 'gBTTE_ART': gBTTE_ART, 
                   'gBTTE_AET': gBTTE_AET, 'gBTTE_CET': gBTTE_CET,'gBTTE_CoET': gBTTE_CoET, 'gBBTTE_EET': gBTTE_EET, 
                   'gBTTE_EsET': gBTTE_EsET, 'gBTTE_MPET': gBTTE_MPET,'gBTTE_PPET': gBTTE_PPET,'gBT_AET':gBT_AET,'clearance_badge' : clearance_badge, 'graduation_badge':graduation_badge, 'request_badge': request_badge,
                   })

@login_required(login_url='/')
def name_list(request):
    enteruser = request.POST.get('validator')
    to_edit = request.POST.get('validator')
    p = user_table.objects.filter(student_id=enteruser).values_list(
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
            accountant_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('accountant_signature', flat=True).distinct()
            acc_sig = str(faculty_approved[0])
            fac_name_get = acc_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            account_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            accountant = account_sig[0]
            accountant_name = str_fac_name
            
        #COURSE ADVISER
        check_status = clearance_form_table.objects.filter(id=id,course_adviser_signature__icontains = 'UNAPPROVED')
        if check_status:
            course_adviser = "UNAPPROVED"
            adviser_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('course_adviser_signature', flat=True).distinct()
            adviser_sig = str(faculty_approved[0])
            fac_name_get = adviser_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            ca_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            course_adviser = ca_sig[0]
            adviser_name = str_fac_name
        
        #LIBERAL ARTS
        check_status = clearance_form_table.objects.filter(id=id,liberal_arts_signature__icontains = 'UNAPPROVED')
        if check_status:
            liberal_arts = "UNAPPROVED"
            liberal_artsName = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('liberal_arts_signature', flat=True).distinct()
            lib_sig = str(faculty_approved[0])
            fac_name_get = lib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            libart_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            liberal_arts = libart_sig[0]
            liberal_artsName = str_fac_name
        
        #CAMPUS LIBRARIAN
        check_status = clearance_form_table.objects.filter(id=id,library_signature__icontains = 'UNAPPROVED')
        if check_status:
            campus_library = "UNAPPROVED"
            librarian_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('library_signature_signature', flat=True).distinct()
            camlib_sig = str(faculty_approved[0])
            fac_name_get = camlib_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            cam_lib_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            campus_library = cam_lib_sig[0]
            librarian_name = str_fac_name
        
        #MATH & SCIENCES
        check_status = clearance_form_table.objects.filter(id=id,mathsci_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            math_and_science = "UNAPPROVED"
            math_and_science_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('mathsci_dept_signature', flat=True).distinct()
            mas_sig = str(faculty_approved[0])
            fac_name_get = mas_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            mathsci_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            math_and_science = mathsci_sig[0]
            math_and_science_name = str_fac_name
            
        #GUIDANCE COUNCELOR
        check_status = clearance_form_table.objects.filter(id=id,guidance_office_signature__icontains = 'UNAPPROVED')
        if check_status:
            guidance = "UNAPPROVED"
            guidance_councelor = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('guidance_office_signature', flat=True).distinct()
            guid_sig = str(faculty_approved[0])
            fac_name_get = guid_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            gui_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            guidance = gui_sig[0]
            guidance_councelor = str_fac_name
        
        #DPECS
        check_status = clearance_form_table.objects.filter(id=id,pe_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            dpecs = "UNAPPROVED"
            dpecs_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('pe_dept_signature', flat=True).distinct()
            pe_sig = str(faculty_approved[0])
            fac_name_get = pe_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            pe_dept_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            dpecs = pe_dept_sig[0]
            dpecs_name = str_fac_name
        
        #OSA
        check_status = clearance_form_table.objects.filter(id=id,osa_signature__icontains = 'UNAPPROVED')
        if check_status:
            osa = "UNAPPROVED"
            osa_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('osa_signature', flat=True).distinct()
            student_osa_sig = str(faculty_approved[0])
            fac_name_get = student_osa_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            student_affairs_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            osa = student_affairs_sig[0]
            osa_name = str_fac_name
        
        #ADAA
        check_status = clearance_form_table.objects.filter(id=id,academic_affairs_signature__icontains = 'UNAPPROVED')
        if check_status:
            adaa = "UNAPPROVED"
            adaa_name = " "
        else:
            faculty_approved = clearance_form_table.objects.filter(id=id).values_list('academic_affairs_signature', flat=True).distinct()
            asst_dir_acad_sig = str(faculty_approved[0])
            fac_name_get = asst_dir_acad_sig.split('_',1)[0]
            str_fac_name = str(fac_name_get)
            print(str_fac_name)
            
            adaa_sig = user_table.objects.filter(full_name=str_fac_name).values_list('uploaded_signature', flat=True).distinct()
            adaa = adaa_sig[0]
            adaa_name = str_fac_name
        
        #INDUSTRIAL
        check_status = clearance_form_table.objects.filter(id=id,ieduc_dept_signature__icontains = 'UNAPPROVED',it_dept_signature__icontains = 'UNAPPROVED',ieng_dept_signature__icontains = 'UNAPPROVED')
        if check_status:
            industrial = "UNAPPROVED"
            it_department = "NONE"
            it_name = " "
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
                it_name = str_fac_name
            
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
                it_name = str_fac_name
                
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
                it_name = str_fac_name
 
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
        'adaa' : adaa,
        'accountant_name' : accountant_name,
        'adviser_name' : adviser_name,
        'liberal_artsName' : liberal_artsName,
        'librarian_name' : librarian_name,
        'math_and_science_name' : math_and_science_name,
        'guidance_councelor' : guidance_councelor,
        'dpecs_name' : dpecs_name,
        'osa_name' : osa_name,
        'adaa_name' : adaa_name,
        'it_name' : it_name,
    }

    print('running')
    return render(request, 'html_files/clearance_form_display.html', context)


@login_required(login_url='/')
def display_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "OLD STUDENT" or "ALUMNUS" or "FACULTY" or "REGISTRAR":
        graduation = graduation_form_table.objects.filter(id=id).values()
        
        #SUBJECT #1
        check_status = graduation_form_table.objects.filter(id=id,signature1__icontains = 'UNAPPROVED')
        check_signature = graduation_form_table.objects.filter(id=id,signature1 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature2 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature3 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature4 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature5 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature6 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature7 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature8 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature9 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,signature10 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature1 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature2 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature3 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature4 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature5 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature6 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature7 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature8 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature9 = 'NO_APPROVED')
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
        check_signature = graduation_form_table.objects.filter(id=id,addsignature10 = 'NO_APPROVED')
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
            all_list = graduation_form_table.objects.filter(approval_status="APPROVED")
            return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all, 'all_list':all_list})
        else:
            all =graduation_form_table.objects.filter(course=id)
            all_list = graduation_form_table.objects.filter(course=id, approval_status="APPROVED")
            return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all, 'all_list':all_list})
            
        return render(request,  'html_files/7.3Registrar Graduation List.html', {'all': all})
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
                student_id=email_temp[0]).values_list('email', flat=True).distinct()

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
    
#DELETE FACULTY  
def faculty_list_remove(request, id):
    print("hey")
    delete_faculty = user_table.objects.get(id=id)
    delete_faculty.delete()
    
    return redirect (registrar_dashboard_faculty_list)

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
    student_data = user_table.objects.filter(Q(user_type='STUDENT') |Q(user_type='OLD STUDENT') |Q(user_type='ALUMNUS'))
        
    context = {'data':student_data}
    return render(request, template, context)

#DELETE STUDENT/REQUESTER
def student_list_remove(request, id):
    print("hey")
    delete_student = user_table.objects.get(id=id)
    delete_student.delete()
    
    return redirect (registrar_dashboard_student_list)

#REQUEST LIST AND DOCUMENT CHECKER LIST 
#REQUEST LIST WITH ORGANIZER
@login_required(login_url='/')
def registrar_dashboard_organize_request_list(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        
        sorter = id
        
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
    
    return render(request,'html_files/Request List.html', {'data': requests,'data2': doc, 'sorter_type' : sorter})

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
        student_name = request.user.full_name
        
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

            if user == "STUDENT":
                if request == 'Honorable Dismissal':
                    check_clearance = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        return redirect('student_dashboard')
                    else:
                        return redirect('clearance_form')
                        
                elif request == 'Transcript of Records':
                    check_clearance = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        return redirect('student_dashboard')
                    else:
                        return redirect('clearance_form')
                elif request == 'Diploma':
                    check_clearance = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request))
                    if check_clearance:
                        return redirect('student_dashboard')
                    else:
                        return redirect('clearance_form')
                elif request.__contains__('Certification'):
                    check_clearance = clearance_form_table.objects.filter(Q(name=full_name), Q(purpose_of_request=request.__contains__('Certification')))
                    if check_clearance:
                        return redirect('student_dashboard')
                    else:
                        return redirect('clearance_form')
                elif request.__contains__('Others'):
                    check_clearance = clearance_form_table.objects.filter(Q(name=full_name),Q(purpose_of_request=request))
                    if check_clearance:
                        return redirect('student_dashboard')
                    else:
                        return redirect('clearance_form')
                else: 
                    return redirect('student_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            unapproved_request = request_form_table.objects.filter(name = student_name).order_by('-time_requested').values_list('approval_status', flat=True).distinct()
            if unapproved_request:
                allow_request = unapproved_request[0]
            else:
                allow_request =""
            context ={'allow' : allow_request}

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
            if bool(uploaded_signature) == False:
                messages.error(request, "No New Signature Saved. Please Try Again.")
            else:
                recent_sig = request.user.uploaded_signature
                if recent_sig:
                    print(str(recent_sig))
                    if os.path.exists("Media/" + str(recent_sig)):
                        os.remove("Media/" + str(recent_sig))
                else:
                    pass
                        
                file_name ="uploaded signatures/"+ str(uploaded_signature)
                        
                fs = FileSystemStorage()
                        
                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                        
                user_table.objects.filter(id=id).update(uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(uploaded_signature_timesaved=signature_timesaved)
                
                messages.success(request, "Your Signature had been updated. It may take a few minutes to update accross the site.")
        else:
            #remove recent signature
            recent_sig = request.user.e_signature
            if recent_sig:
                    print(str(recent_sig))
                    if os.path.exists("Media/" + str(recent_sig)):
                        os.remove("Media/" + str(recent_sig))
                    else:
                        pass
                    
            #save signature in the storage       
            image_decode = ContentFile(base64.b64decode(create_signature.replace('data:image/png;base64,','')))        
            file_name = 'esignatures/' + full_name + '_APPROVED.png'

            fs = FileSystemStorage()
            filename = fs.save(file_name, image_decode)
            
            user_table.objects.filter(id=id).update(e_signature=file_name)
            user_table.objects.filter(id=id).update(e_signature_timesaved=signature_timesaved)
            messages.success(request, "Your Signature had been updated. It may take a few minutes to update accross the site.")
            
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
            if bool(uploaded_signature) == False:
                messages.error(request, "No New Signature Saved. Please Try Again.")
            else:
                recent_sig = request.user.uploaded_signature
                if recent_sig:
                    print(str(recent_sig))
                    if os.path.exists("Media/" + str(recent_sig)):
                        os.remove("Media/" + str(recent_sig))
                else:
                    pass
                    
                file_name ="uploaded signatures/"+ str(uploaded_signature)
                        
                fs = FileSystemStorage()
                        
                filename = fs.save(file_name, uploaded_signature)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)
                        
                user_table.objects.filter(id=id).update(uploaded_signature=file_name)
                user_table.objects.filter(id=id).update(uploaded_signature_timesaved=signature_timesaved)
                messages.success(request, "Your Signature had been updated. It may take a few minutes to update accross the site.")
        else:
            #remove recent signature
            recent_sig = request.user.e_signature
            if recent_sig:
                print(str(recent_sig))
                if os.path.exists("Media/" + str(recent_sig)):
                    os.remove("Media/" + str(recent_sig))
                else:
                    pass
                    
            #save signature in the storage       
            image_decode = ContentFile(base64.b64decode(create_signature.replace('data:image/png;base64,','')))        
            file_name = 'esignatures/' + full_name + '_APPROVED.png'

            fs = FileSystemStorage()
            filename = fs.save(file_name, image_decode)
            
            user_table.objects.filter(id=id).update(e_signature=file_name)
            user_table.objects.filter(id=id).update(e_signature_timesaved=signature_timesaved)
            messages.success(request, "Your Signature had been updated. It may take a few minutes to update accross the site.")
            
            
    return redirect(faculty_dashboard_graduation_list)

@login_required(login_url='/')
def display_reqform(request,id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS" or "OLD STUDENT" or "REGISTRAR":
        reqs = request_form_table.objects.filter(id=id).values()

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    context = {
        "reqs": reqs
    }

    print('running')
    return render(request, 'html_files/Request_form_display.html', context)

@login_required(login_url='/')
def delete_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        delete_grad = graduation_form_table.objects.get(id=id)
        delete_grad.delete()
        return redirect('/registrar_dashboard_graduation_list/%20')

@login_required(login_url='/')
def delete_clearform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        delete_clear = clearance_form_table.objects.get(id=id)
        delete_clear.delete()
        return redirect('/registrar_dashboard_clearance_list/%20')

@login_required(login_url='/')
def delete_reqform(request, id):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        delete_req = request_form_table.objects.get(id=id)
        delete_req.delete()
        return redirect('registrar_dashboard_request_list')