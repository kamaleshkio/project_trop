import os
from pathlib import PureWindowsPath
from wsgiref.util import FileWrapper

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.encoding import smart_str

from college.models import degree_certificate11, ctransfer_certificate1
from government.models import birth_certificate1, community_certificate1, genration_card
from office.models import salary_slip, exp_certificate
from school.models import attendance_certificate1, transfer_certificate1, sports_certificate1
from user.models import user_reg1, community_details, school_details1, college_details1, office_details,  \
    ration_carddetails


def user_index(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = user_reg1.objects.get(uname=uname, password=pswd)
            request.session['userid'] = check.id
            request.session['username'] = check.uname
            return redirect('user_home')
        except:
            pass
        return redirect('user_index')
    return render(request, 'user/user_index.html')

def user_register(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        user_reg1.objects.create(fullname=fullname, email=email, mobile=mobile, uname=uname, password=password)
        return redirect('user_index')
    return render(request, 'user/user_register.html')

def user_home(request):
    userid = request.session['userid']
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        dateof_birth = request.POST.get('dateof_birth')
        address = request.POST.get('address')
        religion = request.POST.get('religion')
        caste = request.POST.get('caste')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        community_details.objects.create(fullname=fullname, uname=uname, dateof_birth=dateof_birth, address=address, religion=religion,
                                 caste=caste,father_name=father_name,mother_name=mother_name)
    return render(request, 'user/user_home.html',{'username1':username1})

def ration_card(request):
    userid = request.session['userid']
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        dateof_birth = request.POST.get('dateof_birth')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        member_count = request.POST.get('member_count')
        ration_carddetails.objects.create(fullname=fullname, uname=uname, dateof_birth=dateof_birth, address=address, age=age,
                                 gender=gender,member_count=member_count)
    return render(request, 'user/ration_card.html',{'username1':username1})

def school_details(request):
    userid = request.session['userid']
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        dateof_birth = request.POST.get('dateof_birth')
        address = request.POST.get('address')
        religion = request.POST.get('religion')
        caste = request.POST.get('caste')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        dateof_admission = request.POST.get('dateof_admission')
        last_studiedclass = request.POST.get('last_studiedclass')
        reason_leaving = request.POST.get('reason_leaving')
        school_name = request.POST.get('school_name')
        school_details1.objects.create(fullname=fullname, uname=uname, dateof_birth=dateof_birth, address=address, religion=religion,
                                 caste=caste,father_name=father_name,mother_name=mother_name,dateof_admission=dateof_admission,
                                         last_studiedclass=last_studiedclass,reason_leaving=reason_leaving,school_name=school_name)
    return render(request, 'user/school_details.html',{'username1':username1})

def college_details(request):
    userid = request.session['userid']
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        dateof_birth = request.POST.get('dateof_birth')
        address = request.POST.get('address')
        religion = request.POST.get('religion')
        caste = request.POST.get('caste')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        dateof_admission = request.POST.get('dateof_admission')
        degree = request.POST.get('degree')
        joining_year = request.POST.get('joining_year')
        college_name = request.POST.get('college_name')
        college_details1.objects.create(fullname=fullname, uname=uname, dateof_birth=dateof_birth, address=address, religion=religion,
                                 caste=caste,father_name=father_name,mother_name=mother_name,dateof_admission=dateof_admission,
                                         degree=degree,joining_year=joining_year,college_name=college_name)
    return render(request, 'user/college_details.html',{'username1':username1})

def working_details(request):
    userid = request.session['userid']
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        company_name = request.POST.get('company_name')
        designation = request.POST.get('designation')
        office_details.objects.create(fullname=fullname, uname=uname, company_name=company_name,designation=designation)
    return render(request, 'user/working_details.html',{'username1':username1})

def user_allcertificates(request):
    certificate1=''
    file_path1=''
    username1 = request.session['username']
    if request.method == "POST":
        fullname = request.POST.get('name')
        certificate_name = request.POST.get('certificate_name')
        if certificate_name == "birth_certificate":
            return redirect('view_birthcertificate')
        elif certificate_name == "community_certificate":
            return redirect('viewcommunity_certificate')
        elif certificate_name == "ration_card":
            return redirect('view_rationcard')
        elif certificate_name == "school_attendance":
            return redirect('view_schoolattendace')
        elif certificate_name == "school_tc":
            return redirect('view_schooltc')
        elif certificate_name == "school_sports":
            return redirect('view_schoolsports')
        elif certificate_name == "degree_certificate":
            return redirect('viewdegree_certificate')
        elif certificate_name == "college_tc":
            return redirect('view_collegetc')
        elif certificate_name == "salary_slip":
            return redirect('view_salaryslip')
        elif certificate_name == "experience_certificate":
            return redirect('viewexperience_certificate')


    return render(request, 'user/user_allcertificates.html',{'username1':username1})

def view_birthcertificate(request):
    username1 = request.session['username']
    certificate1=birth_certificate1.objects.filter(uname=username1)
    return render(request, 'user/view_birthcertificate.html',{'certificate1':certificate1})

def download_birthcertificate(request,pk):
    username1 = request.session['username']
    objspath = birth_certificate1.objects.get(id=pk)
    fpath1 = objspath.file_path


    fs = FileSystemStorage()
    filename=os.path.basename(fpath1)
    print(filename)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/view_birthcertificate.html')

def viewcommunity_certificate(request):
    username1 = request.session['username']
    certificate1=community_certificate1.objects.filter(uname=username1)
    return render(request, 'user/viewcommunity_certificate.html',{'certificate1':certificate1})

def download_communitycertificate(request,pk):
    username1 = request.session['username']
    objspath1 = community_certificate1.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/viewcommunity_certificate.html')

def view_rationcard(request):
    username1 = request.session['username']
    certificate1=genration_card.objects.filter(uname=username1)
    return render(request, 'user/view_rationcard.html',{'certificate1':certificate1})

def download_rationcard(request,pk):
    username1 = request.session['username']
    objspath1 = genration_card.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/view_rationcard.html')

def view_schoolattendace(request):
    username1 = request.session['username']
    certificate1=attendance_certificate1.objects.filter(uname=username1)
    return render(request, 'user/view_schoolattendace.html',{'certificate1':certificate1})

def download_schoolattendance(request,pk):
    username1 = request.session['username']
    objspath1 = attendance_certificate1.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_schoolattendance.html')

def view_schooltc(request):
    username1 = request.session['username']
    certificate1=transfer_certificate1.objects.filter(uname=username1)
    return render(request, 'user/view_schooltc.html',{'certificate1':certificate1})

def download_schooltc(request,pk):
    username1 = request.session['username']
    objspath1 = transfer_certificate1.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_schooltc.html')

def view_schoolsports(request):
    username1 = request.session['username']
    certificate1=sports_certificate1.objects.filter(uname=username1)
    return render(request, 'user/view_schoolsports.html',{'certificate1':certificate1})

def download_schoolsports(request,pk):
    username1 = request.session['username']
    objspath1 = sports_certificate1.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_schoolsports.html')

def viewdegree_certificate(request):
    username1 = request.session['username']
    certificate1=degree_certificate11.objects.filter(uname=username1)
    return render(request, 'user/viewdegree_certificate.html',{'certificate1':certificate1})

def download_degreecertificate(request,pk):
    username1 = request.session['username']
    objspath1 = degree_certificate11.objects.get(id=pk)
    fpath11 = objspath1.file_path

    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_degreecertificate.html')

def view_collegetc(request):
    username1 = request.session['username']
    certificate1=ctransfer_certificate1.objects.filter(uname=username1)
    return render(request, 'user/view_collegetc.html',{'certificate1':certificate1})

def download_collegetc(request,pk):
    username1 = request.session['username']
    objspath1 = ctransfer_certificate1.objects.get(id=pk)
    fpath11 = objspath1.file_path
    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_collegetc.html')

def view_salaryslip(request):
    username1 = request.session['username']
    certificate1=salary_slip.objects.filter(uname=username1)
    return render(request, 'user/view_salaryslip.html',{'certificate1':certificate1})

def download_salaryslip(request,pk):
    username1 = request.session['username']
    objspath1 = salary_slip.objects.get(id=pk)
    fpath11 = objspath1.file_path
    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/download_salaryslip.html')

def viewexperience_certificate(request):
    username1 = request.session['username']
    certificate1 = exp_certificate.objects.filter(uname=username1)
    return render(request, 'user/viewexperience_certificate.html',{'certificate1':certificate1})


def downloadexperience_certificate(request,pk):
    username1 = request.session['username']
    objspath1 = exp_certificate.objects.get(id=pk)
    fpath11 = objspath1.file_path
    fs1 = FileSystemStorage()
    filename1 = os.path.basename(fpath11)
    print(filename1)
    if fs1.exists(filename1):
        with fs1.open(filename1) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename1)
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')

    return render(request, 'user/downloadexperience_certificate.html')
