from django.contrib import admin
from .models import *

# LIST DISPLAY ARE COLUMNS DISPLAYED ON ADMIN PAGE
class user_table_admin(admin.ModelAdmin):
     list_display = ('username', 'full_name', 'id_number', 'user_type',
                     'e_signature_timesaved', 'uploaded_signature_timesaved')

class user_deleted_table_admin(admin.ModelAdmin):
     list_display = ('username', 'full_name', 'id_number', 'user_type', 'asigned_position_timestamp',
                     'remove_position_timestamp', 'change_password_timestamp', 'convert_status_timestamp',
                     'deleted_status', 'deleted_timestamp')

class clearance_form_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','purpose_of_request','approval_status')
class clearance_form_deleted_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','purpose_of_request','approval_status',
                     'liberal_timestamp', 'accountant_timestamp', 'mathsci_timestamp', 'pe_timestamp',
                     'ieduc_timestamp', 'it_timestamp', 'eng_timestamp', 'library_timestamp', 'guidance_timestamp',
                     'osa_timestamp', 'academic_timestamp', 'course_adviser_timestamp', 'approved_timestamp',
                     'deleted_status', 'deleted_timestamp')

class graduation_form_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','approval_status')
class graduation_form_deleted_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','approval_status',
                     'subject1_timestamp', 'subject2_timestamp', 'subject3_timestamp', 'subject4_timestamp',
                     'subject5_timestamp', 'subject6_timestamp', 'subject7_timestamp', 'subject8_timestamp',
                     'subject9_timestamp', 'subject10_timestamp', 'addsubject1_timestamp', 'addsubject2_timestamp',
                     'addsubject3_timestamp', 'addsubject4_timestamp', 'addsubject5_timestamp', 'sit_timestamp',
                     'approved_timestamp', 'deleted_status', 'deleted_timestamp')
     
class request_form_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','date','current_status', 'form_137','clearance','request','official_receipt','claim')
class request_form_deleted_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','date','current_status', 'form_137','clearance','request','official_receipt',
                     'or_num', 'or_date','appointment','claim', 'form_137_timestamp', 'clearance_timestamp', 
                     'or_timestamp', 'claim_timestamp', 'approval_timestamp', 'deleted_status', 'deleted_timestamp')

# REGISTER TABLES FOR ADMIN PAGE
admin.site.register(user_table, user_table_admin)
admin.site.register(clearance_form_table, clearance_form_table_admin)
admin.site.register(graduation_form_table, graduation_form_table_admin)
admin.site.register(request_form_table, request_form_table_admin)

admin.site.register(user_deleted_table, user_deleted_table_admin)
admin.site.register(clearance_form_deleted_table, clearance_form_deleted_table_admin)
admin.site.register(graduation_form_deleted_table, graduation_form_deleted_table_admin)
admin.site.register(request_form_deleted_table, request_form_deleted_table_admin)
