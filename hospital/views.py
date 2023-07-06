from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from django.contrib.auth.models import User
from government.models import bkey_request1, gov_login
from hospital.models import birth_details
from user.models import user_reg1




# Create your views here.
def hospital_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        if uname == 'hospital' and password == 'hospital':
            return redirect("hospital_home")

    return render(request, 'hospital/hospital_login.html')


def hospital_home(request):
    obj1=user_reg1.objects.all()
    if request.method == "POST":
        uname = request.POST.get('uname')
        gender = request.POST.get('gender')
        birth_place = request.POST.get('birth_place')
        dateof_birth = request.POST.get('dateof_birth')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        address = request.POST.get('address')
        birth_details.objects.create(uname=uname, gender=gender, birth_place=birth_place, dateof_birth=dateof_birth,
                                     father_name=father_name,mother_name=mother_name,address=address)
    return render(request, 'hospital/hospital_home.html',{'obj1':obj1})

def hview_request(request):
    sts1="pending"
    request11=bkey_request1.objects.filter(status1=sts1)
    return render(request, 'hospital/hview_request.html',{'request11':request11})

def bkey_generate11(request,pk):
        username1="admin"
        sts11="send"
        uname1 = User.objects.make_random_password(length=5, allowed_chars="01234567889")
        print(uname1)
        subject = "Key Details"
        text_content = ""
        objs = bkey_request1.objects.get(id=pk)
        uemail = objs.email
        print(uemail)
        html_content = "<br/><p>Your Key:<strong>" + str(uname1) + "<strong></p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [uemail]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            gov_login.objects.filter(username=username1).update(key1=uname1)
            bkey_request1.objects.filter(id=pk).update(status1=sts11,key1=uname1)
            return redirect("hview_request")
        return render(request, 'hospital/bkey_generate11.html')