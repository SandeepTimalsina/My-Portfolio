from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request,'index.html')


# for sending email to the admin

def send_email(request):
    error_message = None
    success_message = None
    
    if request.method == 'POST':
        subject = request.POST.get("subject", "Undefined_subject")
        message = request.POST.get("message", "Undefined_message")
        from_email = request.POST.get("from_email", "Undifined_sender")
        
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ["sandeeptimalsina100@gmail.com"])
                success_message = "Your message has been sent successfully."
            except BadHeaderError:
                error_message = "Invalid header found."
        else:
            error_message = "Make sure all fields are entered and valid."

    return render(request, 'index.html', {'error_message': error_message, 'success_message': success_message})
