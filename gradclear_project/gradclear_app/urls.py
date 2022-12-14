from django.urls import path, re_path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     # LOGIN AND LOGOUT
     path('', login_user, name='login'),
     path('logout', logout_user, name='logout'),

     # COVER
     path('cover', cover, name='cover'),
     path('privacy_policy', privacy_policy, name='privacy_policy'),

     # USER SIGNUP
     path('alumnus_signup', alumnus_registration, name='alumnus_signup'),
     path('faculty_signup', faculty_registration, name='faculty_signup'),
     path('oldstudent_signup', oldstudent_registration, name='oldstudent_signup'),
     path('student_signup', student_registration, name='student_signup'),
     path('staff_signup', staff_registration, name='staff_signup'),

     # DETERMINER OF FILLING UP FORMS IN SIDEBAR
     path('graduation_view', graduation_view, name='graduation_view'),

      # FORMS BACK FOR REGISTRAR
     path('reggrad_back/<int:id>', reggrad_back, name='reggrad_back'),
     path('regclear_back/<int:id>', regclear_back, name='regclear_back'),

     # FORMS
     path('clearance_form/<str:req>', clearance_form, name='clearance_form'),
     path('graduation_form', graduation_form, name='graduation_form'),
     path('request_form', request_form, name="request_form"),

     # FORM DISPLAY
     path('display_reqform/<int:id>', display_reqform, name='display_reqform'),
     path('display_clearform/<int:id>', display_clearform, name='display_clearform'),
     path('registrar_dashboard_organize_clearance_list/display_clearform/<int:id>', display_clearform, name='display_clearform'),
     path('display_gradform/<int:id>', display_gradform, name='display_gradform'),
     path('registrar_dashboard_graduation_list/display_gradform/<str:id>', display_gradform,), 
     path('registrar_dashboard_clearance_list/display_clearform/<str:id>', display_clearform,), 
     
     #APPROVE BY REGISTRAR
     path('approve_clearform/<int:id>', approve_clearform, name='approve_clearform'),

     # DELETE FORMS
     path('delete_gradform/<int:id>', delete_gradform, name='delete_gradform'),
     path('delete_clearform/<int:id>', delete_clearform, name='delete_clearform'),
     path('delete_reqform/<int:id>', delete_reqform, name='delete_reqform'),

     # USER DASHBOARDS
     path('faculty_dashboard', faculty_dashboard, name='faculty_dashboard'),
     path('registrar_dashboard', registrar_dashboard,name='registrar_dashboard'),
     path('student_dashboard', student_dashboard, name='student_dashboard'),

     # FORM LISTS
     path('faculty_dashboard_clearance_list/<int:id>', faculty_dashboard_clearance_list,
          name='faculty_dashboard_clearance_list'),
     path('faculty_dashboard_graduation_list/<int:id>', faculty_dashboard_graduation_list,
          name='faculty_dashboard_graduation_list'),
     path('registrar_dashboard_request_list', registrar_dashboard_request_list, 
          name="registrar_dashboard_request_list"),
     path('registrar_dashboard_clearance_list/<str:id>', registrar_dashboard_clearance_list,
          name='registrar_dashboard_clearance_list'),
     path('registrar_dashboard_graduation_list/<str:id>', registrar_dashboard_graduation_list,
          name='registrar_dashboard_graduation_list'),
     
     # USER LISTS
     path('registrar_dashboard_faculty_list', registrar_dashboard_faculty_list,
          name="registrar_dashboard_faculty_list"),
     path('registrar_dashboard_student_list/<str:id>', registrar_dashboard_student_list,
          name="registrar_dashboard_student_list"),
     path('registrar_dashboard_staff_list/<str:id>', registrar_dashboard_staff_list,
          name="registrar_dashboard_staff_list"),

     # FORM LISTS (WITH FUNCTION OF APPROVING ALL)
     path('faculty_dashboard_clearance_list_all', faculty_dashboard_clearance_list_all, 
          name='faculty_dashboard_clearance_list_all'),
     path('faculty_dashboard_clearance_list/faculty_dashboard_clearance_list_all', faculty_dashboard_clearance_list_all, 
          name='faculty_dashboard_clearance_list_all'),
     path('faculty_dashboard_graduation_list_all', faculty_dashboard_graduation_list_all, 
          name='faculty_dashboard_graduation_list_all'),
     path('faculty_dashboard_graduation_list/faculty_dashboard_graduation_list_all', faculty_dashboard_graduation_list_all, 
          name='faculty_dashboard_graduation_list_all'),

     # UPDATE SIGNATURE
     path('update_clearance_signature/<int:id>', update_clearance_signature , 
          name='update_clearance_signature'),
     path('faculty_dashboard_clearance_list/update_clearance_signature/<int:id>', update_clearance_signature , 
          name='update_clearance_signature'),
     path('update_grad_signature/<int:id>', update_grad_signature ,name='update_grad_signature'),
     path('faculty_dashboard_graduation_list/update_grad_signature/<int:id>', update_grad_signature ,name='update_grad_signature'),
     
     # UPDATE STATUS
     path('faculty_designation_update/<int:id>', faculty_designation_update, 
          name="faculty_designation_update"),
     path('student_status_update/<int:id>', student_status_update, name='student_status_update'),
     path('school_year_update', school_year_update, name='school_year_update'),
     path('registrar_dashboard_student_list/student_status_update/<int:id>', student_status_update, name='student_status_update'),
     
     # REMOVE USER
     path('faculty_list_remove/<int:id>', faculty_list_remove, name="faculty_list_remove"),
     path('registrar_dashboard_student_list/student_list_remove/<int:id>', student_list_remove, name="student_list_remove"),
     path('student_list_remove/<int:id>', student_list_remove, name="student_list_remove"),
     path('staff_list_remove/<int:id>', staff_list_remove, name="staff_list_remove"),
     path('registrar_dashboard_staff_list/staff_list_remove/<int:id>', staff_list_remove, name="staff_list_remove"),
     path('registrar_dashboard_organize_faculty_list/faculty_list_remove/<int:id>', faculty_list_remove, name="faculty_list_remove"),

     # LIST ORGANIZER
     path('registrar_dashboard_organize_request_list/<str:id>', registrar_dashboard_organize_request_list,
          name="registrar_dashboard_organize_request_list"),
     path('registrar_dashboard_organize_clearance_list/<str:id>', registrar_dashboard_organize_clearance_list,
          name="registrar_dashboard_organize_clearance_list"),
     path('registrar_dashboard_organize_faculty_list/<str:id>', registrar_dashboard_organize_faculty_list,
          name="registrar_dashboard_organize_faculty_list"),
     path('registrar_dashboard_organize_request_list/request_official_update/<int:id>',
          request_official_update, name='request_official_update'),
     path('registrar_dashboard_organize_request_list/request_form137_update/<int:id>', 
          request_form137_update, name='request_form137_update'),
     path('registrar_dashboard_organize_request_list/request_claim_update/<int:id>', 
          request_claim_update, name='request_claim_update'),
     
     #  DOCUMENT CHECKER
     path('request_official_update/<int:id>', request_official_update, name='request_official_update'),
     path('request_form137_update/<int:id>', request_form137_update, name='request_form137_update'),
     path('request_claim_update/<int:id>', request_claim_update, name='request_claim_update'),

     # FORM APPROVAL
     path('update_clearance/<int:id>/<str:dep>/<str:sign>', update_clearance, name='update_clearance'),
     path('faculty_dashboard_clearance_list/update_clearance/<int:id>/<str:dep>/<str:sign>', update_clearance, name='update_clearance'),
     path('update_graduation/<int:id>/<str:sub>/<str:sig>', update_graduation, name='update_graduation'),
     path('faculty_dashboard_graduation_list/update_graduation/<int:id>/<str:sub>/<str:sig>', update_graduation, name='update_graduation'),

     # UPDATE STUDENT SETTINGS
     path('updatePassword', updatePassword, name='updatePassword'),
     
     # UPDATE FACULTY SETTINGS
    path('faculty_updatePassword', faculty_updatePassword, name='faculty_updatePassword'),
    
     # UPDATE REGISTRAR SETTINGS
     path('reg_updateName', reg_updateName, name='reg_updateName'),
     path('reg_updateAddress', reg_updateAddress, name='reg_updateAddress'),
     path('reg_updateEmail', reg_updateEmail, name='reg_updateEmail'),
     path('reg_updatePassword', reg_updatePassword, name='reg_updatePassword'),
     path('reg_updateContact', reg_updateContact, name='reg_updateContact'),

      # UPDATE STAFF SETTINGS
     path('staff_updatePassword', staff_updatePassword, name='staff_updatePassword'),


     # PRINT FORMS  
     path('clearance_print/<str:id>', clearance_print, name='clearance_print'),
     path('graduation_print/<str:id>', graduation_print, name='graduation_print'), 
     path('req_print/<int:id>', req_print, name='req_print'),
     
     # SET APPOINTMENTS
     path('appointment/<int:id>/<str:form>', appointment, name='appointment'),
     path('faculty_dashboard_clearance_list/appointment/<int:id>/<str:form>', appointment, name= 'appointment'),
     path('appointmentgrad/<int:id>/<str:form>', appointmentgrad, name='appointmentgrad'),
     path('faculty_dashboard_graduation_list/appointmentgrad/<int:id>/<str:form>', appointmentgrad, name= 'appointmentgrad'),
     path('reggrad_appointment/<int:id>', reggrad_appointment, name='reggrad_appointment'),
     path('regclear_appointment/<int:id>', regclear_appointment, name='regclear_appointment'),
     path('request_appointment/<int:id>', request_appointment, name='request_appointment'),

     # SEND EMAIL TO ALL SIGNATORIES
     path('send_email_all', send_email_all, name='send_email_all'),
     
    ] 
 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)