import email
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
import my_csv, io
from textwrap import wrap

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
        # response['Content-Disposition'] = 'attachment;filename=Graduation Form.pdf'
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
    # p.drawString(130, 710, f'{content.present_address}')
    
    address = content.present_address
    
    p.drawString(150, 681, f'{content.date_admitted_in_tup}')
    p.drawString(120, 655, f'{content.course}')
    p.drawString(180, 629, f'{content.highschool_graduated}')
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
        # response['Content-Disposition'] = 'attachment;filename=Clearance Form.pdf'
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
            email = form.cleaned_data.get("email")
            # middle = form.cleaned_data.get("middle_name")
            form.instance.username = "TUPC-" + id_num
            username = "TUPC-" + id_num
            form.instance.user_type = "STUDENT"
            form.instance.full_name = last + ", " + first

            SearchUser = first + " " + last
            e = Enrolled.objects.filter(Name=SearchUser).values_list('Name', flat=True).distinct()
            if e:
                va= e[0]
                if va == SearchUser:
                    form.save()
                    # subject = 'SIGNUP SUCCESS'
                    # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
                    # email_from = settings.EMAIL_HOST_USER
                    # recipient_list = [email, ]
                    # send_mail( subject, message, email_from, recipient_list )
                    messages.success(request, 'Account Saved. Keep in mind that your username is: ' + username)
                    return redirect('/')
                else:
                    messages.error(request, "Unregistered Alumni")
            else:
                    messages.error(request, "Unregistered Alumni")
        else:
            messages.error(
                request, "There is an error with your form. Try again.")
    img_object = form.instance
    user_identifier = "STUDENT"
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
    return render(request, 'html_files/1Sign_Up.html', context)


def faculty_registration(request):
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
            form.instance.user_type = "FACULTY"
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
    context = {'form': form, 'img_object': img_object, 'user': user_identifier}
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

            SearchUser = first + " " + last
            a = Enrolled.objects.filter(Name=SearchUser).values_list('Name', flat=True).distinct()
            if a:
                va= a[0]
                if va == SearchUser:
                    form.save()
                    # subject = 'SIGNUP SUCCESS'
                    # message = f'Hi {first}, thank you for registering in TUPC Application for Clearance and Graduation Form.'
                    # email_from = settings.EMAIL_HOST_USER
                    # recipient_list = [email, ]
                    # send_mail( subject, message, email_from, recipient_list )
                    messages.success(request, 'Account Saved. Keep in mind that your username is: ' + username)
                    return redirect('/')
                else:
                    messages.error(request, "Unenrolled Student")
            else:
                    messages.error(request, "Unenrolled Student")
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
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "ALUMNUS":
        username = request.user.username
        print(username)

        st = graduation_form_table.objects.filter(student_id=username)
        st1 = clearance_form_table.objects.filter(student_id=username)
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')
    return render(request, 'html_files/4.1Student Dashboard.html', {'st': st, 'st1': st1})


@login_required(login_url='/')
def clearance_form(request):
    context = {}
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or 'ALUMNUS':
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
            purpose_reason = request.POST.get('preq_box_420')
            purpose = request.POST.get('purpose_request_420')
            form = clearance_form_table.objects.create(student_id=student_id, name=name, present_address=present_address, course=course,
                                                       date_filed=date_filed, date_admitted_in_tup=date_admitted,
                                                       highschool_graduated=highschool_graduated, tupc_graduate=tupc_graduate, year_graduated_in_tupc=highschool_graduated_date,
                                                       number_of_terms_in_tupc=terms, amount_paid=amount, have_previously_requested_form=last_request,
                                                       date_of_previously_requested_form=last_request_date, last_term_in_tupc=last_term,
                                                       purpose_of_request=purpose, purpose_of_request_reason=purpose_reason,)
            form.save()

            return redirect('student_dashboard')
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.2Student Clearance Form.html', context)


@login_required(login_url='/')
def graduation_form(request):
    a = user_table.objects.filter(Q(department="DLA") | Q(department="DMS") | Q(department="DPECS") |
                                  Q(department="DIT") | Q(department="DIE") | Q(department="DED") | Q(department="DOE"), user_type="FACULTY").values_list('full_name', flat=True).distinct()
    print(a)
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
                                                        addsubject10=o10, addroom10=p10, addfaculty10=t10, add_starttime1_10=w1_10, add_endtime1_10=x1_10, addday1_10=r1_10,

                                                        signature1=s1 + "_sig", signature2=s2 + "_sig", signature3=s3 + "_sig", signature4=s4 + "_sig", signature5=s5 + "_sig",
                                                        signature6=s6 + "_sig", signature7=s7 + "_sig", signature8=s8 + "_sig", signature9=s9 + "_sig", signature10=s10 + "_sig",
                                                        addsignature1=t1 + "_sig", addsignature2=t2 + "_sig", addsignature3=t3 + "_sig", addsignature4=t4 + "_sig", addsignature5=t5 + "_sig",
                                                        addsignature6=t6 + "_sig", addsignature7=t7 + "_sig", addsignature8=t8 + "_sig", addsignature9=t9 + "_sig", addsignature10=t10 + "_sig")
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
        unapproved = request.user.full_name + "_sig"
        st = graduation_form_table.objects.filter(Q(signature1=unapproved) | Q(signature2=unapproved) | Q(signature3=unapproved) |
                                                  Q(signature4=unapproved) | Q(signature5=unapproved) | Q(signature6=unapproved) |
                                                  Q(signature7=unapproved) | Q(signature8=unapproved) | Q(signature9=unapproved) | Q(signature10=unapproved) |
                                                  Q(addsignature1=unapproved) | Q(addsignature2=unapproved) | Q(addsignature3=unapproved) |
                                                  Q(addsignature4=unapproved) | Q(addsignature5=unapproved) | Q(addsignature6=unapproved) |
                                                  Q(addsignature7=unapproved) | Q(addsignature8=unapproved) | Q(addsignature9=unapproved) |
                                                  Q(addsignature10=unapproved)).order_by('-id')
        print(unapproved)

        if request.user.department == "OCS" or request.user.department == "DLA" or request.user.department == "DMS" or request.user.department == "DPECS" or request.user.department == "DIT" or request.user.department == "DIE" or request.user.department == "OCL" or request.user.department == "OGS" or request.user.department == "OSA" or request.user.department == "ADAA":
            st1 = clearance_form_table.objects.filter(Q(accountant_signature="UNAPPROVED") | Q(mathsci_dept_signature="UNAPPROVED") |
                                                      Q(pe_dept_signature="UNAPPROVED") | Q(ieduc_dept_signature="UNAPPROVED") | Q(it_dept_signature="UNAPPROVED") |
                                                      Q(ieng_dept_signature="UNAPPROVED") | Q(library_signature="UNAPPROVED") |
                                                      Q(guidance_office_signature="UNAPPROVED") | Q(osa_signature="UNAPPROVED") |
                                                      Q(academic_affairs_signature="UNAPPROVED")).order_by('-id')
            return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, 'st1': st1, })

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.1Faculty Dashboard.html', {'st': st, })


@login_required(login_url='/')
def faculty_dashboard_clearance_list(request):
    val = request.POST.get('valdeterminer')
    userdeterminer = request.POST.get('userdeterminer')
    print(val, userdeterminer)
    st = clearance_form_table.objects.all()

    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        if userdeterminer == "OCS":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    accountant_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    accountant_signature=val).values()

        elif userdeterminer == "DMS":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    mathsci_dept_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    mathsci_dept_signature=val).values()

        elif userdeterminer == "DPECS":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    pe_dept_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    pe_dept_signature=val).values()

        elif userdeterminer == "DED":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    ieduc_dept_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    ieduc_dept_signature=val).values()

        elif userdeterminer == "DIT":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    it_dept_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    it_dept_signature=val).values()

        elif userdeterminer == "DIE":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    ieng_dept_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    ieng_dept_signature=val).values()

        elif userdeterminer == "OCL":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    library_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    library_signature=val).values()

        elif userdeterminer == "OGS":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    guidance_office_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    guidance_office_signature=val).values()

        elif userdeterminer == "OSA":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    osa_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    osa_signature=val).values()

        elif userdeterminer == "ADAA":
            if val == "UNAPPROVED":
                st = clearance_form_table.objects.filter(
                    academic_affairs_signature=val).values()
                return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})

            elif val == "APPROVED":
                st = clearance_form_table.objects.filter(
                    academic_affairs_signature=val).values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.2Faculty Clearance List.html', {'st': st, 'val': val})


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
        print(rec_email)
        if request.user.department == "OCS":
            clearance_form_table.objects.filter(
                id=id).update(accountant_signature="APPROVED")

        elif request.user.department == "DMS":
            clearance_form_table.objects.filter(id=id).update(
                mathsci_dept_signature="APPROVED")

        elif request.user.department == "DPECS":
            clearance_form_table.objects.filter(
                id=id).update(pe_dept_signature="APPROVED")

        elif request.user.department == "DED":
            clearance_form_table.objects.filter(
                id=id).update(ieduc_dept_signature="APPROVED")

        elif request.user.department == "DIT":
            clearance_form_table.objects.filter(
                id=id).update(it_dept_signature="APPROVED")

        elif request.user.department == "DIE":
            clearance_form_table.objects.filter(
                id=id).update(ieng_dept_signature="APPROVED")

        elif request.user.department == "OCL":
            clearance_form_table.objects.filter(
                id=id).update(library_signature="APPROVED")

        elif request.user.department == "OGS":
            clearance_form_table.objects.filter(id=id).update(
                guidance_office_signature="APPROVED")

        elif request.user.department == "OSA":
            clearance_form_table.objects.filter(
                id=id).update(osa_signature="APPROVED")

        elif request.user.department == "ADAA":
            clearance_form_table.objects.filter(id=id).update(
                academic_affairs_signature="APPROVED")

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
        user = str(request.POST.get('namedeterminer2'))

        global f_n
        f_n = ""
        global field_sig
        field_sig = ""
        temp = request.POST.get('namedeterminer2')
        temp = str(temp) + "_sig"
        f_n = temp
        val = request.POST.get('valdeterminer')

        # USE REQUEST.USER TO AUTO SHOW DATA
        full_name = request.user.full_name
        st = graduation_form_table.objects.filter(Q(faculty1=full_name) | Q(faculty2=full_name) | Q(faculty3=full_name) |
                                                  Q(faculty4=full_name) | Q(faculty5=full_name) | Q(faculty6=full_name) |
                                                  Q(faculty7=full_name) | Q(faculty8=full_name) | Q(faculty9=full_name) | Q(faculty10=full_name) |
                                                  Q(addfaculty1=full_name) | Q(addfaculty2=full_name) | Q(addfaculty3=full_name) |
                                                  Q(addfaculty4=full_name) | Q(addfaculty5=full_name) | Q(addfaculty6=full_name) |
                                                  Q(addfaculty7=full_name) | Q(addfaculty8=full_name) | Q(addfaculty9=full_name) | Q(addfaculty10=full_name))

        if val == "UNAPPROVED":
            full_name = request.user.full_name + "_sig"
            print(full_name)
            st = graduation_form_table.objects.filter(Q(signature1=full_name) | Q(signature2=full_name) | Q(signature3=full_name) |
                                                      Q(signature4=full_name) | Q(signature5=full_name) | Q(signature6=full_name) |
                                                      Q(signature7=full_name) | Q(signature8=full_name) | Q(signature9=full_name) | Q(signature10=full_name) |
                                                      Q(addsignature1=full_name) | Q(addsignature2=full_name) | Q(addsignature3=full_name) |
                                                      Q(addsignature4=full_name) | Q(addsignature5=full_name) | Q(addsignature6=full_name) |
                                                      Q(addsignature7=full_name) | Q(addsignature8=full_name) | Q(addsignature9=full_name) | Q(addsignature10=full_name))
        elif val == "APPROVED":
            approval = request.user.full_name + "_APPROVED"
            st = graduation_form_table.objects.filter(Q(signature1=approval) | Q(signature2=approval) | Q(signature3=approval) |
                                                      Q(signature4=approval) | Q(signature5=approval) | Q(signature6=approval) |
                                                      Q(signature7=approval) | Q(signature8=approval) | Q(signature9=approval) | Q(signature10=approval) |
                                                      Q(addsignature1=approval) | Q(addsignature2=approval) | Q(addsignature3=approval) |
                                                      Q(addsignature4=approval) | Q(addsignature5=approval) | Q(addsignature6=approval) |
                                                      Q(addsignature7=approval) | Q(addsignature8=approval) | Q(addsignature9=approval) | Q(addsignature10=approval))

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/5.3Faculty Graduation List.html', {'st': st, 'val': val})


@login_required(login_url='/')
def updategrad(request, id):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        email_temp = graduation_form_table.objects.filter(
            id=id).values_list('student_id', flat=True).distinct()
        email = user_table.objects.filter(
            username=email_temp[0]).values_list('email', flat=True).distinct()

        rec_email = email[0]
        print(rec_email)
        print("this is f_n", f_n)
        a = graduation_form_table.objects.filter(
            signature1__contains=f_n, id=id)
        b = graduation_form_table.objects.filter(
            signature2__contains=f_n, id=id)
        c = graduation_form_table.objects.filter(
            signature3__contains=f_n, id=id)
        d = graduation_form_table.objects.filter(
            signature4__contains=f_n, id=id)
        e = graduation_form_table.objects.filter(
            signature5__contains=f_n, id=id)
        f = graduation_form_table.objects.filter(
            signature6__contains=f_n, id=id)
        g = graduation_form_table.objects.filter(
            signature7__contains=f_n, id=id)
        h = graduation_form_table.objects.filter(
            signature8__contains=f_n, id=id)
        i = graduation_form_table.objects.filter(
            signature9__contains=f_n, id=id)
        j = graduation_form_table.objects.filter(
            signature10__contains=f_n, id=id)
        k = graduation_form_table.objects.filter(
            addsignature1__contains=f_n, id=id)
        l = graduation_form_table.objects.filter(
            addsignature2__contains=f_n, id=id)
        m = graduation_form_table.objects.filter(
            addsignature3__contains=f_n, id=id)
        n = graduation_form_table.objects.filter(
            addsignature4__contains=f_n, id=id)
        o = graduation_form_table.objects.filter(
            addsignature5__contains=f_n, id=id)
        p = graduation_form_table.objects.filter(
            addsignature6__contains=f_n, id=id)
        q = graduation_form_table.objects.filter(
            addsignature7__contains=f_n, id=id)
        r = graduation_form_table.objects.filter(
            addsignature8__contains=f_n, id=id)
        s = graduation_form_table.objects.filter(
            addsignature9__contains=f_n, id=id)
        t = graduation_form_table.objects.filter(
            addsignature10__contains=f_n, id=id)
        approval = request.user.full_name + "_APPROVED"
        if a.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature1=approval)
            messages.success(request, "Form Approved.")
        if b.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature2=approval)
            messages.success(request, "Form Approved.")
        if c.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature3=approval)
            messages.success(request, "Form Approved.")
        if d.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature4=approval)
            messages.success(request, "Form Approved.")
        if e.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature5=approval)
            messages.success(request, "Form Approved.")
        if f.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature6=approval)
            messages.success(request, "Form Approved.")
        if g.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature7=approval)
            messages.success(request, "Form Approved.")
        if h.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature8=approval)
            messages.success(request, "Form Approved.")
        if i.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature9=approval)
            messages.success(request, "Form Approved.")
        if j.exists():
            graduation_form_table.objects.filter(
                id=id).update(signature10=approval)
            messages.success(request, "Form Approved.")
        if k.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature1=approval)
            messages.success(request, "Form Approved.")
        if l.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature2=approval)
            messages.success(request, "Form Approved.")
        if m.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature3=approval)
            messages.success(request, "Form Approved.")
        if n.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature4=approval)
            messages.success(request, "Form Approved.")
        if o.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature5=approval)
            messages.success(request, "Form Approved.")
        if p.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature6=approval)
            messages.success(request, "Form Approved.")
        if q.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature7=approval)
            messages.success(request, "Form Approved.")
        if r.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature8=approval)
            messages.success(request, "Form Approved.")
        if s.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature9=approval)
            messages.success(request, "Form Approved.")
        if t.exists():
            graduation_form_table.objects.filter(
                id=id).update(addsignature10=approval)
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
def updateName(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
        if request.method == "POST":
            slast_name = request.POST.get('ln_box_041')
            sfirst_name = request.POST.get('fn_box_041')
            smiddle_name = request.POST.get('mn_box_041')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                last_name=slast_name, first_name=sfirst_name, middle_name=smiddle_name, )
            return redirect('/student_dashboard')

    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    return render(request, 'html_files/4.1Student Dashboard.html')


@login_required(login_url='/')
def updateEmail(request):
    if request.user.is_authenticated and request.user.user_type == "STUDENT":
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
def faculty_updateName(request):
    if request.user.is_authenticated and request.user.user_type == "FACULTY":
        print('here')
        if request.method == "POST":
            flast_name = request.POST.get('ln_box_051')
            ffirst_name = request.POST.get('fn_box_051')
            fmiddle_name = request.POST.get('mn_box_051')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                last_name=flast_name, first_name=ffirst_name, middle_name=fmiddle_name, )
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
def reg_updateName(request):
    if request.user.is_authenticated and request.user.user_type == "REGISTRAR":
        print('here')
        if request.method == "POST":
            relast_name = request.POST.get('ln_box_071')
            refirst_name = request.POST.get('fn_box_071')
            remiddle_name = request.POST.get('mn_box_071')
            a = request.POST.get('validator')

            user_table.objects.filter(id_number=a).update(
                last_name=relast_name, first_name=refirst_name, middle_name=remiddle_name, )
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
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "FACULTY" or "REGISTRAR":
        clearance = clearance_form_table.objects.filter(id=id).values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    print('running')
    return render(request, 'html_files/clearance_form_display.html', {'clearance': clearance})


@login_required(login_url='/')
def display_gradform(request, id):
    if request.user.is_authenticated and request.user.user_type == "STUDENT" or "FACULTY" or "REGISTRAR":
        graduation = graduation_form_table.objects.filter(id=id).values()
    else:
        messages.error(
            request, "You are trying to access an unauthorized page and is forced to logout.")
        return redirect('/')

    print('running')
    return render(request, 'html_files/graduation_form_display.html', {'graduation': graduation})


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

@login_required(login_url='/')
def registrar_dashboard_student_list(request):
    # declaring template
    template = "html_files/Student list.html"
    enrolled_data = Enrolled.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'data': enrolled_data
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
    for column in my_csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Enrolled.objects.update_or_create(
            Name = column[0],
            Id_number = column[1],
            Status = column[2],
        )
    
    context = {'data':enrolled_data}
    return render(request, template, context)

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
    return render(request,  'html_files/7.4Registrar Faculty List.html', {'all': all_faculty})

def faculty_list_update(request, id):
    pos_change = request.POST.get('positionSelect')
    print(pos_change)
    
    user_table.objects.filter(id=id).update(position=pos_change)
    print('done')
    return redirect(registrar_dashboard_faculty_list)

