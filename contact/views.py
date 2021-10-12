from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        #check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id



        contact = Contact(name=name,email=email,subject=subject,message=message,phone=phone,user_id=user_id)

        contact.save()

        # send email
        '''
        send_mail(
        'Sparkle food product',
        'You have an Inquiry,please Login to admin for more information',
        'marduk420@gmail.com',
        ['dixonkijazi@gmail.com'], 
        fail_silently=False
        )

        '''
        messages.success(request,'Your request has been!, We will get back to you soon.')


    return render(request,'account/contact.html')
