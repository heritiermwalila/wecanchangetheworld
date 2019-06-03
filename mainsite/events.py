from django.core.mail import send_mass_mail

def send_event_email(model, **kwargs):

    subscriber_emails = []
    subscribers = model.objects.all()

    for sub in subscribers:
        subscriber_emails.append(sub.email)


    print(subscriber_emails)
