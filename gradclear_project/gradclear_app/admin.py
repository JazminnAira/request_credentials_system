from django.contrib import admin
from .models import *

class user_table_admin(admin.ModelAdmin):
     list_display = ('username', 'full_name', 'user_type')

class clearance_form_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','purpose_of_request','approval_status')

class graduation_form_table_admin(admin.ModelAdmin):
     list_display = ('student_id','name','course','approval_status')
     
class student_table_list(admin.ModelAdmin):
     list_display = ('id','Name','TOR','form_137','clearance','graduation','Status')
     
class alumni_table_list(admin.ModelAdmin):
     list_display = ('id','Name','TOR','form_137','Status')


admin.site.register(user_table, user_table_admin)
admin.site.register(clearance_form_table, clearance_form_table_admin)
admin.site.register(graduation_form_table, graduation_form_table_admin)
admin.site.register(Enrolled,student_table_list)
admin.site.register(Alumnus,alumni_table_list)
