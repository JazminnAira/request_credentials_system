from django.urls import path, re_path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('cover', cover, name='cover'),
     path('student_signup', student_registration, name='student_signup'),
     path('faculty_signup', faculty_registration, name='faculty_signup'),
     path('alumnus_signup', alumnus_registration, name='alumnus_signup'),
     path('', login_user, name='login'),
     path('logout', logout_user, name='logout'),
     path('student_dashboard', views.student_dashboard, name='student_dashboard'),
     path('clearance_form', views.clearance_form, name='clearance_form'),
     path('graduation_form', views.graduation_form, name='graduation_form'),
     path('alumnus_dashboard', views.alumnus_dashboard, name='alumnus_dashboard'),
     path('faculty_dashboard', views.faculty_dashboard, name='faculty_dashboard'),
     path('faculty_dashboard_clearance_list', views.faculty_dashboard_clearance_list,
          name='faculty_dashboard_clearance_list'),
     path('faculty_dashboard_graduation_list', views.faculty_dashboard_graduation_list,
          name='faculty_dashboard_graduation_list'),
     path('registrar_dashboard', views.registrar_dashboard,
          name='registrar_dashboard'),
     path('registrar_dashboard_clearance_list', views.registrar_dashboard_clearance_list,
          name='registrar_dashboard_clearance_list'),
     path('registrar_dashboard_graduation_list', views.registrar_dashboard_graduation_list,
          name='registrar_dashboard_graduation_list'),
     path('registrar_dashboard_faculty_list', registrar_dashboard_faculty_list, name="registrar_dashboard_faculty_list"),
     path('registrar_dashboard_student_list', registrar_dashboard_student_list, name="registrar_dashboard_student_list"),
     path('faculty_list_update/<int:id>', views.faculty_list_update, name='faculty_list_update'),
     path('update/<int:id>', views.update, name='update'),
     path('updategrad/<int:id>', views.updategrad, name='updategrad'),
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
     path('display_clearform/<int:id>', display_clearform, name='display_clearform'),
     path('display_gradform/<int:id>', display_gradform, name='display_gradform'),
     path('registrar_dashboard_clearance_list/<str:id>', registrar_dashboard_clearance_list,
               name='registrar_dashboard_clearance_list'),
     path('registrar_dashboard_graduation_list/<str:id>', registrar_dashboard_graduation_list,
               name='registrar_dashboard_graduation_list'),  
     path('set_appointment/<int:id>', set_appointment, name='set_appointment'),
     path('appointment/<int:id>', views.appointment, name='appointment'),
     path('appointmentgrad/<int:id>', views.appointmentgrad, name='appointmentgrad'),
     path('clearance_print/<str:id>', clearance_print, name='clearance_print'),
     path('graduation_print/<str:id>', graduation_print, name='graduation_print'),
    ] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)