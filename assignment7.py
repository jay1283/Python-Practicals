from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'jaypatel',
    ['jay12082003@gmail.com'],
    fail_silently=False,
)