from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.db.models.signals import post_save,post_delete
from superpet.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.dispatch import receiver
from products.models import Product
from django.template.loader import render_to_string

import datetime

@user_logged_in.connect
def login_signal(sender,request,user,**kwargs):
    print("****************(login signals:start)******************************")
    print("sender",sender)
    print("request",request)
    print("user",user)
    print("kwargs",kwargs)
    
    send_mail(f"[{user} placed]",
                  "Someone logged in.",
                  EMAIL_HOST_USER,
                  ["artilachure@gmail.com","shankkarpal46@gmail.com","tgorivale2@gmailcom","priyanka.vibhute@itvedant.com"],fail_silently=False)
    
    print("****************(login signals:end)******************************")


@user_logged_out.connect
def login_signal(sender,request,user,**kwargs):
    print("****************(login signals:start)******************************")
    print("sender",sender)
    print("request",request)
    print("user",user)
    print("kwargs",kwargs)
    now = datetime.datetime.now()

    send_mail(f"[{user} placed]",
                  f"Someone logged out.{now}",
                  EMAIL_HOST_USER,
                  ["artilachure@gmail.com","shankkarpal46@gmail.com","tgorivale2@gmailcom","priyanka.vibhute@itvedant.com"],fail_silently=False)
    
    
    
    print("****************(login signals:end)******************************")

@receiver(post_save,sender=Product)
def add_product_signal(sender,instance,created,**kwargs):
    now = datetime.datetime.now()
    if created == True:
        send_mail(f"[placed]",
                  f"Product created.{now}",
                  EMAIL_HOST_USER,
                  ["artilachure@gmail.com","shankkarpal46@gmail.com","tgorivale2@gmailcom","priyanka.vibhute@itvedant.com"],
                  html_message=render_to_string("email.html",{"product":instance}),
                  fail_silently=False)
        
    if created == False:
        send_mail(f"[placed]",
                  f"Product updated.{now},{instance.id},{instance.product_name},{instance.product_description},{instance.product_price},{instance.product_brand}",
                  EMAIL_HOST_USER,
                  ["artilachure@gmail.com","shankkarpal46@gmail.com","tgorivale2@gmailcom","priyanka.vibhute@itvedant.com"],fail_silently=False)
    print("==============================(Product Add Signal:Start)==================================================")

    print("sender",sender)
    print("instance",instance)
    print("created",created)
    print("**kwargs",kwargs)
    print("==============================(Product Sigals Signal:Stop)==================================================")

