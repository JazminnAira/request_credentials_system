from django.urls import path, re_path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('cover', cover, name='cover'),
     path('student_signup', student_registration, name='student_signup'),
     path('oldstudent_signup', oldstudent_registration, name='oldstudent_signup'),
     path('faculty_signup', faculty_registration, name='faculty_signup'),
     path('alumnus_signup', alumnus_registration, name='alumnus_signup'),
     path('', login_user, name='login'),
     path('logout', logout_user, name='logout'),
     path('student_dashboard', views.student_dashboard, name='student_dashboard'),
     path('clearance_view', views.clearance_view, name='clearance_view'),
     path('clearance_form', views.clearance_form, name='clearance_form'),
     path('graduation_form', views.graduation_form, name='graduation_form'),
     path('request_form', views.request_form, name="request_form"),
     # path('alumnus_dashboard', views.alumnus_dashboard, name='alumnus_dashboard'),
     path('faculty_dashboard', views.faculty_dashboard, name='faculty_dashboard'),
     path('faculty_dashboard_clearance_list', views.faculty_dashboard_clearance_list,
          name='faculty_dashboard_clearance_list'),
     path('update_clearance_signature/<int:id>', update_clearance_signature ,name='update_clearance_signature'),
     path('update_grad_signature/<int:id>', update_grad_signature ,name='update_grad_signature'),
     path('faculty_dashboard_graduation_list', views.faculty_dashboard_graduation_list,
          name='faculty_dashboard_graduation_list'),
     path('registrar_dashboard', views.registrar_dashboard,
          name='registrar_dashboard'),
     path('registrar_dashboard_faculty_list', registrar_dashboard_faculty_list, name="registrar_dashboard_faculty_list"),
     path('faculty_designation_update/<int:id>', views.faculty_designation_update, name="faculty_designation_update"),
     path('faculty_list_remove/<int:id>', views.faculty_list_remove, name="faculty_list_remove"),
     path('registrar_dashboard_student_list', registrar_dashboard_student_list, name="registrar_dashboard_student_list"),
     path('student_list_remove/<int:id>', views.student_list_remove, name="student_list_remove"),
     path('registrar_dashboard_request_list', registrar_dashboard_request_list, name="registrar_dashboard_request_list"),
     path('registrar_dashboard_organize_request_list/<str:id>', registrar_dashboard_organize_request_list, name="registrar_dashboard_organize_request_list"),
     path('upload_document_checker', upload_document_checker, name="upload_document_checker"),
     path('registrar_dashboard_organize_request_list/request_official_update/<int:id>', views.request_official_update, name='request_official_update'),
     path('registrar_dashboard_organize_request_list/request_form137_update/<int:id>', views.request_form137_update, name='request_form137_update'),
     path('registrar_dashboard_organize_request_list/request_TOR_update/<int:id>', views.request_TOR_update, name='request_TOR_update'),
     path('registrar_dashboard_organize_request_list/request_claim_update/<int:id>', views.request_claim_update, name='request_claim_update'),
     path('request_official_update/<int:id>', views.request_official_update, name='request_official_update'),
     path('request_form137_update/<int:id>', views.request_form137_update, name='request_form137_update'),
     path('request_TOR_update/<int:id>', views.request_TOR_update, name='request_TOR_update'),
     path('request_claim_update/<int:id>', views.request_claim_update, name='request_claim_update'),
     path('update_clearance/<int:id>/<str:dep>/<str:sign>', views.update_clearance, name='update_clearance'),
     path('update_graduation/<int:id>/<str:sig>', views.update_graduation, name='update_graduation'),
     path('updateAddress', updateAddress, name='updateAddress'),
     path('updateEmail', updateEmail, name='updateEmail'),
     path('updatePassword', updatePassword, name='updatePassword'),
     path('updateContact', updateContact, name='updateContact'),
     path('faculty_updateAddress', faculty_updateAddress, name='faculty_updateAddress'),
     path('faculty_updateEmail', faculty_updateEmail, name='faculty_updateEmail'),
     path('faculty_updatePassword', faculty_updatePassword, name='faculty_updatePassword'),
     path('faculty_updateContact', faculty_updateContact, name='faculty_updateContact'),
     path('reg_updateAddress', reg_updateAddress, name='reg_updateAddress'),
     path('reg_updateEmail', reg_updateEmail, name='reg_updateEmail'),
     path('reg_updatePassword', reg_updatePassword, name='reg_updatePassword'),
     path('reg_updateContact', reg_updateContact, name='reg_updateContact'),
     path('req_print/<int:id>', req_print, name='req_print'),
     path('display_reqform/<int:id>', display_reqform, name='display_reqform'),
     path('display_clearform/<int:id>', display_clearform, name='display_clearform'),
     path('display_gradform/<int:id>', display_gradform, name='display_gradform'),
     path('registrar_dashboard_clearance_list/<str:id>', registrar_dashboard_clearance_list,
               name='registrar_dashboard_clearance_list'),
     path('registrar_dashboard_graduation_list/<str:id>', registrar_dashboard_graduation_list,
               name='registrar_dashboard_graduation_list'),
     path('registrar_dashboard_graduation_list/display_gradform/<str:id>', display_gradform,), 
     path('registrar_dashboard_clearance_list/display_clearform/<str:id>', display_clearform,),   
     path('set_appointment/<int:id>', set_appointment, name='set_appointment'),
     path('appointment/<int:id>/<str:form>', views.appointment, name='appointment'),
     path('appointmentgrad/<int:id>/<str:form>', views.appointmentgrad, name='appointmentgrad'),
     path('clearance_print/<str:id>', clearance_print, name='clearance_print'),
     path('graduation_print/<str:id>', graduation_print, name='graduation_print'),   
     path('reggrad_appointment/<int:id>', reggrad_appointment, name='reggrad_appointment'),
     path('regclear_appointment/<int:id>', regclear_appointment, name='regclear_appointment'),
     path('request_appointment/<int:id>', request_appointment, name='request_appointment'),
     path('delete_gradform/<int:id>', delete_gradform, name='delete_gradform'),
     path('delete_clearform/<int:id>', delete_clearform, name='delete_clearform'),
     path('delete_reqform/<int:id>', delete_reqform, name='delete_reqform'),
    ] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)