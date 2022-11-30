from gradclear_app.views import send_email_all

def my_scheduled_job():
    send_email_all()
    print("Email notifications has been sent to the signatories.")