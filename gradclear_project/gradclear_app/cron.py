from gradclear_app.views import send_email_all

# SCHEDULED EMAIL ALL SIGNATORIES FROM MONDAY TO FRIDAY AT 4PM 
def my_scheduled_job():
    send_email_all()
    print("Email notifications has been sent to the signatories.")