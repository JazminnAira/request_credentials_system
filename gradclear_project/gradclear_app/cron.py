from gradclear_app.views import send_email_all

def my_cron_job():
     send_email_all()
     print("works")