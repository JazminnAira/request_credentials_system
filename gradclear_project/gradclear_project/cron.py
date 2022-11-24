from gradclear_app.views import *

def my_cron_job():
     send_email_all()
     print("works")