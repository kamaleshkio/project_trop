from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import DEFAULT_FROM_EMAIL
# Create your views here.
from django.utils.encoding import smart_str

from college.models import college_register1, ctransfer_certificate1, degree_certificate11
from government.models import community_certificate1, birth_certificate1
from school.models import transfer_certificate1, attendance_certificate1, sports_certificate1, school_birth1
from user.models import college_details1
from reportlab.platypus import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import json
import os
from os.path import dirname, join
import hashlib
class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(nonce = 1, previous_hash = '0')

    def create_block(self, nonce, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'nonce': nonce,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            else:
                new_nonce += 1
        return new_nonce

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

def college_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = college_register1.objects.get(collegename=uname, password=pswd)
            request.session['collegeid'] = check.id
            request.session['collegename'] = check.collegename
            request.session['cemail'] = check.email
            return redirect('college_home')
        except:
            pass
        return redirect('college_login')
    return render(request, 'college/college_login.html')

def college_register(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        password = request.POST.get('password')
        college_register1.objects.create(collegename=fullname, email=email, mobile=mobile,  password=password)
        return redirect('college_login')
    return render(request, 'college/college_register.html')

def college_home(request):
    collegename = request.session['collegename']
    cemail = request.session['cemail']

    collegedet = college_details1.objects.filter(college_name=collegename)
    return render(request, 'college/college_home.html',{'collegedet':collegedet})

def cgenerate_tc(request,pk):
    objjs = college_details1.objects.get(id=pk)
    unid = objjs.id
    request.session['unid'] = unid
    uname = objjs.uname
    fullname = objjs.fullname
    dateof_birth = objjs.dateof_birth
    address = objjs.address
    religion = objjs.religion
    caste = objjs.caste
    father_name = objjs.father_name
    mother_name = objjs.mother_name
    cname = objjs.college_name
    dateof_admission = objjs.dateof_admission
    degree = objjs.degree
    joining_year = objjs.joining_year
    if request.method == "POST":
        finishing_year = request.POST.get('finishing_year')
        status = request.POST.get('status')
        college_details1.objects.filter(id=unid).update(degree_finishingyear=finishing_year, status=status)
        return redirect('cgenerate_tc1')
    return render(request, 'college/cgenerate_tc.html',{'uname':uname})

def cgenerate_tc1(request):
    unid = request.session['unid']
    schdet = college_details1.objects.filter(id=unid)
    for t11 in schdet:
        uname = t11.uname
        fullname = t11.fullname
        dateof_birth = t11.dateof_birth
        address = t11.address
        religion = t11.religion
        caste = t11.caste
        father_name = t11.father_name
        mother_name = t11.mother_name
        cname = t11.college_name
        dateof_admission = t11.dateof_admission
        degree = t11.degree
        joining_year = t11.joining_year
        degree_finishingyear = t11.degree_finishingyear
        status = t11.status
        elems = []
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1
        elems.append(Paragraph("Transfer Certificate", title_style))
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)

        output_path = join(ROOT_DIR, 'college_tc')
        print(output_path)
        pdf_filename = output_path + "/" + uname + '_' + "collegetc" + '.pdf'
        print(pdf_filename)
        data = [
            ['Full Name :', fullname],
            ['Date Of Birth :', dateof_birth],
            ['Religion :', religion],
            ['Caste :', caste],
            ['Father Name :', father_name],
            ['Mother Name :', mother_name],
            ['Address:', address],
            ['College Name:', cname],
            ['Date Of Admission:', dateof_admission],
            ['Degree:', degree],
            ['Degree Joining Year:', joining_year],
            ['Degree Finishing Year:', degree_finishingyear],
            ['Course Status:', status]
        ]
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        table_style = TableStyle([('FONTSIZE', (0, 0), (13, 13), 24), ('ALIGN', (0, 0), (13, 13), 'LEFT')])
        table = Table(data, rowHeights=35)
        table.setStyle(table_style)
        elems.append(table)
        pdf.build(elems)
        blockchain = Blockchain()
        previous_block1 = blockchain.get_previous_block()
        previous_nonce1 = previous_block1['nonce']
        print(previous_nonce1)
        nonce1 = blockchain.proof_of_work(previous_nonce1)
        previous_hash1 = blockchain.hash(previous_block1)
        block1 = blockchain.create_block(nonce1, previous_hash1)
        atimestamp = str(datetime.datetime.now())
        apphash = ctransfer_certificate1.objects.all().count()
        print(apphash)

        if request.method == "POST" and request.FILES['college_transfer_certificate']:
            per_name = request.POST.get('uname1')
            college_transfer_certificate = request.FILES['college_transfer_certificate']
            fs = FileSystemStorage()
            filename = fs.save(college_transfer_certificate.name, college_transfer_certificate)
            uploaded_file_url = fs.url(filename)

            if apphash == 0:
                ctransfer_certificate1.objects.create(uname=uname, full_name=fullname,
                                                     dateof_birth=dateof_birth, religion=religion, caste=caste,
                                                     father_name=father_name, mother_name=mother_name, address=address,
                                                     file_path=uploaded_file_url, phash1=apphash,
                                                     newhash1=previous_hash1,
                                                     atimestamp=atimestamp, cname=cname,
                                                     dateof_admission=dateof_admission,
                                                     degree=degree, joining_year=joining_year,
                                                     degree_finishingyear=degree_finishingyear, status=status,
                                                      certificate_file=college_transfer_certificate)
            else:
                ahash22 = ctransfer_certificate1.objects.all().last()
                aphash = ahash22.newhash1
                ctransfer_certificate1.objects.create(uname=uname, full_name=fullname,
                                                     dateof_birth=dateof_birth, religion=religion, caste=caste,
                                                     father_name=father_name, mother_name=mother_name, address=address,
                                                     file_path=uploaded_file_url, phash1=aphash,
                                                     newhash1=previous_hash1,
                                                     atimestamp=atimestamp, cname=cname,
                                                     dateof_admission=dateof_admission,
                                                     degree=degree, joining_year=joining_year,
                                                     degree_finishingyear=degree_finishingyear, status=status,
                                                      certificate_file=college_transfer_certificate)
    return render(request, 'college/cgenerate_tc1.html',{'uname':uname})

def degree_certificate(request):
    collegename = request.session['collegename']
    cemail = request.session['cemail']

    collegedet = college_details1.objects.filter(college_name=collegename)
    return render(request, 'college/degree_certificate.html',{'collegedet':collegedet})

def degree_certificate1(request,pk):
    objjs = college_details1.objects.get(id=pk)
    unid = objjs.id
    request.session['unid'] = unid
    uname = objjs.uname
    fullname = objjs.fullname
    dateof_birth = objjs.dateof_birth
    address = objjs.address
    religion = objjs.religion
    caste = objjs.caste
    father_name = objjs.father_name
    mother_name = objjs.mother_name
    cname = objjs.college_name
    dateof_admission = objjs.dateof_admission
    degree = objjs.degree
    joining_year = objjs.joining_year
    if request.method == "POST":
        university = request.POST.get('university')
        college_details1.objects.filter(id=unid).update(university=university)
        return redirect('degree_certificate2')
    return render(request, 'college/degree_certificate1.html',{'uname':uname})

def degree_certificate2(request):
    unid = request.session['unid']
    schdet = college_details1.objects.filter(id=unid)
    for t11 in schdet:
        uname = t11.uname
        fullname = t11.fullname
        dateof_birth = t11.dateof_birth

        cname = t11.college_name
        university = t11.university
        dateof_admission = t11.dateof_admission
        degree = t11.degree
        joining_year = t11.joining_year
        degree_finishingyear = t11.degree_finishingyear
        status = t11.status
        elems = []
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1
        elems.append(Paragraph("Degree Certificate", title_style))
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)

        output_path = join(ROOT_DIR, 'degree_certificate')
        print(output_path)
        pdf_filename = output_path + "/" + uname + '_' + "degreecertificate" + '.pdf'
        print(pdf_filename)
        data = [
            ['Full Name :', fullname],
            ['Date Of Birth :', dateof_birth],
            ['College Name:', cname],
            ['University:', university],
            ['Date Of Admission:', dateof_admission],
            ['Degree:', degree],
            ['Degree Joining Year:', joining_year],
            ['Degree Finishing Year:', degree_finishingyear],
            ['Course Status:', status]
        ]
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        table_style = TableStyle([('FONTSIZE', (0, 0), (13, 13), 24), ('ALIGN', (0, 0), (13, 13), 'LEFT')])
        table = Table(data, rowHeights=35)
        table.setStyle(table_style)
        elems.append(table)
        pdf.build(elems)
        blockchain = Blockchain()
        previous_block1 = blockchain.get_previous_block()
        previous_nonce1 = previous_block1['nonce']
        print(previous_nonce1)
        nonce1 = blockchain.proof_of_work(previous_nonce1)
        previous_hash1 = blockchain.hash(previous_block1)
        block1 = blockchain.create_block(nonce1, previous_hash1)
        atimestamp = str(datetime.datetime.now())
        apphash = degree_certificate11.objects.all().count()
        print(apphash)
        if request.method == "POST" and request.FILES['degree_certificate']:
            per_name = request.POST.get('uname1')
            degree_certificate = request.FILES['degree_certificate']
            fs = FileSystemStorage()
            filename = fs.save(degree_certificate.name, degree_certificate)
            uploaded_file_url = fs.url(filename)

            if apphash == 0:
                degree_certificate11.objects.create(uname=uname, full_name=fullname,
                                                      dateof_birth=dateof_birth,
                                                      file_path=uploaded_file_url, phash1=apphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp, cname=cname,university=university,
                                                      dateof_admission=dateof_admission,
                                                      degree=degree, joining_year=joining_year,
                                                      degree_finishingyear=degree_finishingyear, status=status,
                                                      certificate_file=degree_certificate)
            else:
                ahash22 = degree_certificate11.objects.all().last()
                aphash = ahash22.newhash1
                degree_certificate11.objects.create(uname=uname, full_name=fullname,
                                                      dateof_birth=dateof_birth,
                                                      file_path=uploaded_file_url, phash1=aphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp, cname=cname,university=university,
                                                      dateof_admission=dateof_admission,
                                                      degree=degree, joining_year=joining_year,
                                                      degree_finishingyear=degree_finishingyear, status=status,
                                                      certificate_file=degree_certificate)
    return render(request, 'college/degree_certificate2.html',{'uname':uname})

def college_accesscertificate(request):
    certificate1=''
    collegename = request.session['collegename']
    collegedet = college_details1.objects.filter(college_name=collegename)
    if request.method == "POST":
        uname = request.POST.get('uname')
        certificate_name = request.POST.get('certificate_name')
        if certificate_name == "birth_certificate":
            certificate1 = birth_certificate1.objects.filter(uname=uname)
            cname="birth_certificate"
            request.session['cname'] = cname
        elif certificate_name == "community_certificate":
            certificate1 = community_certificate1.objects.filter(uname=uname)
            cname = "community_certificate"
            request.session['cname'] = cname
        elif certificate_name == "school_attendance":
            certificate1 = attendance_certificate1.objects.filter(uname=uname)
            cname = "school_attendance"
            request.session['cname'] = cname
        elif certificate_name == "school_tc":
            certificate1 = transfer_certificate1.objects.filter(uname=uname)
            cname = "school_tc"
            request.session['cname'] = cname
        else:
            certificate1 = sports_certificate1.objects.filter(uname=uname)
            cname = "school_sports"
            request.session['cname'] = cname
    return render(request, 'college/college_accesscertificate.html',{'schooldet':collegedet,'certificate1':certificate1})

def college_request1(request,pk):
    keyresult2 = ''
    sts11 = "send"
    sts22 = "deactivate"
    cname = request.session['cname']
    if cname == "birth_certificate":
        request1 = birth_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    elif cname == "community_certificate":
        request1 = community_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    elif cname == "school_attendance":
        request1 = attendance_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    elif cname == "school_tc":
        request1 = transfer_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    else:
        request1 = sports_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    if request.method == "POST":
        person_name = request.POST.get("person_name")
        unkey = request.POST.get("unkey")
        keyresult = school_birth1.objects.filter(studnet_name=person_name, key1=unkey, status1=sts11)
        for t11 in keyresult:
            person_name11 = t11.studnet_name
            print(person_name11)
            certificate_name1 = t11.certificate_name
            if certificate_name1 == "birth_certificate":
                keyresult2 = birth_certificate1.objects.filter(uname=person_name11)
            elif certificate_name1 == "community_certificate":
                keyresult2 = community_certificate1.objects.filter(uname=person_name11)
            elif certificate_name1 == "school_attendance":
                keyresult2 = attendance_certificate1.objects.filter(uname=person_name11)
            elif certificate_name1 == "school_tc":
                keyresult2 = transfer_certificate1.objects.filter(uname=person_name11)
            else:
                keyresult2 = sports_certificate1.objects.filter(uname=person_name11)
            school_birth1.objects.filter(studnet_name=person_name, key1=unkey, status1=sts11).update(status1=sts22)
    return render(request, 'college/college_request1.html',{'person_name':person_name,'keyresult2':keyresult2})

def collegekey_request(request):
    collegename = request.session['collegename']
    semail = request.session['cemail']
    person_id1 = request.session['person_id1']
    student_name = request.session['student_name']
    cname = request.session['cname']
    sts1 = "pending"
    key1 = "pending"
    school_birth1.objects.create(requestor=collegename, studnet_name=student_name, email=semail,certificate_name=cname, status1=sts1)
    return render(request, 'college/collegekey_request.html')

def download_certificates11(request,pk):
    objspath1=''
    username1 = request.session['username']
    cname = request.session['cname']
    if cname == "birth_certificate":
        objspath1 = birth_certificate1.objects.get(id=pk)
        fpath11 = objspath1.file_path
        fs1 = FileSystemStorage()
        filename11 = os.path.basename(fpath11)
        print(filename11)
        if fs1.exists(filename11):
            with fs1.open(filename11) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename11)
                return response
        else:
            return HttpResponseNotFound('The requested pdf was not found in our server.')
    elif cname == "community_certificate":
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
    elif cname == "school_attendance":
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
    elif cname == "school_tc":
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
    else:
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

    return render(request, 'college/download_certificates11.html')


def college_accessrequest(request):
    sts1 = "pending"
    certificates1=''
    if request.method == "POST":
        certificate_name = request.POST.get('certificate_name')
        certificates1 = school_birth1.objects.filter(status1=sts1,certificate_name=certificate_name)
    return render(request, 'college/college_accessrequest.html',{'certificates1':certificates1})

def collegeaccess_key1(request,pk):
    username1="admin"
    sts11="send"
    uname1 = User.objects.make_random_password(length=5, allowed_chars="01234567889")
    print(uname1)
    subject = "Key Details"
    text_content = ""
    objs = school_birth1.objects.get(id=pk)
    uemail = objs.email
    print(uemail)
    html_content = "<br/><p>Your Key:<strong>" + str(uname1) + "<strong></p>"

    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [uemail]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():

        school_birth1.objects.filter(id=pk).update(status1=sts11,key1=uname1)
        return redirect("college_accessrequest")
    return render(request, 'college/collegeaccess_key1.html')