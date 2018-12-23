# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail.content import Content
from sendgrid.helpers.mail.email import Email
from sendgrid.helpers.mail.mail import Mail
from decouple import config


def send_mail(to_email, message):

    sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))
    from_email = Email(config('FROM_EMAIL'))
    to_email = Email(to_email)
    subject = config('SUBJECT')
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)
