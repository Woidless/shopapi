from django.core.mail import send_mail

def send_confirmation_email(user, code):
    send_mail(
        'Hello, activate your account!',
        f'You need to follow the link for activation',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False,
    )

