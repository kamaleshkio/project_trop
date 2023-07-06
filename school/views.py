from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.conf.global_settings import DEFAULT_FROM_EMAIL

# Create your views here.
from django.utils.encoding import smart_str

from government.models import community_certificate1, birth_certificate1
from school.models import school_register1, transfer_certificate1, attendance_details, attendance_certificate1, \
    sports_details, sports_certificate1, school_birth1
from user.models import school_details1
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from reportlab.platypus import *
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os
import sys
import datetime
import json
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

def school_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = school_register1.objects.get(schoolname=uname, password=pswd)
            request.session['schoolid'] = check.id
            request.session['schoolname'] = check.schoolname
            request.session['semail'] = check.email
            return redirect('school_home')
        except:
            pass
        return redirect('school_login')
    return render(request, 'school/school_login.html')

def school_register(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        password = request.POST.get('password')

        school_register1.objects.create(schoolname=fullname, email=email, mobile=mobile,  password=password)
        return redirect('school_login')
    return render(request, 'school/school_register.html')

def school_home(request):

    schoolname = request.session['schoolname']
    semail = request.session['semail']

    schooldet = school_details1.objects.filter(school_name=schoolname)
    return render(request, 'school/school_home.html',{'schooldet':schooldet})

def generate_tc(request,pk):
    objjs = school_details1.objects.get(id=pk)
    unid=objjs.id
    request.session['unid'] = unid
    uname = objjs.uname
    fullname = objjs.fullname
    dateof_birth = objjs.dateof_birth
    address = objjs.address
    religion = objjs.religion
    caste = objjs.caste
    father_name = objjs.father_name
    mother_name = objjs.mother_name
    sname = objjs.school_name
    dateof_admission = objjs.dateof_admission
    last_studiedclass = objjs.last_studiedclass
    reason_leaving = objjs.reason_leaving
    if request.method == "POST":
        issue_date = request.POST.get('issue_date')
        general_conduct = request.POST.get('general_conduct')
        school_details1.objects.filter(id=unid).update(issue_date=issue_date, general_conduct=general_conduct)
        return redirect('generate_tc1')
    return render(request, 'school/generate_tc.html',{'uname':uname})

def generate_tc1(request):
    unid = request.session['unid']
    schdet=school_details1.objects.filter(id=unid)
    for t11 in schdet:
        uname = t11.uname
        fullname = t11.fullname
        dateof_birth = t11.dateof_birth
        address = t11.address
        religion = t11.religion
        caste = t11.caste
        father_name = t11.father_name
        mother_name = t11.mother_name
        sname = t11.school_name
        dateof_admission = t11.dateof_admission
        last_studiedclass = t11.last_studiedclass
        reason_leaving = t11.reason_leaving
        issue_date = t11.issue_date
        general_conduct = t11.general_conduct
        elems = []
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1
        elems.append(Paragraph("Transfer Certificate", title_style))
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)

        output_path = join(ROOT_DIR, 'transfer_certificate')
        print(output_path)
        pdf_filename = output_path + "/" + uname + '_' + "transfercertificate" + '.pdf'
        print(pdf_filename)
        data = [
            ['Full Name :', fullname],
            ['Date Of Birth :', dateof_birth],
            ['Religion :', religion],
            ['Caste :', caste],
            ['Father Name :', father_name],
            ['Mother Name :', mother_name],
            ['Address:', address],
            ['School Name:', sname],
            ['Date Of Admission:', dateof_admission],
            ['Last Studied Class:', last_studiedclass],
            ['Reason For Leaving School:', reason_leaving],
            ['Date Of Certificate Issue:', issue_date],
            ['General Conduct:', general_conduct]
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
        apphash = transfer_certificate1.objects.all().count()
        print(apphash)

        if request.method == "POST" and request.FILES['transfer_certificate']:
            per_name = request.POST.get('uname1')
            transfer_certificate = request.FILES['transfer_certificate']
            fs = FileSystemStorage()
            filename = fs.save(transfer_certificate.name, transfer_certificate)
            uploaded_file_url = fs.url(filename)

            if apphash == 0:
                transfer_certificate1.objects.create(uname=uname, full_name=fullname,
                                                      dateof_birth=dateof_birth, religion=religion, caste=caste,
                                                      father_name=father_name, mother_name=mother_name, address=address,
                                                      file_path=uploaded_file_url, phash1=apphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,sname=sname,dateof_admission=dateof_admission,
                                                    last_studiedclass=last_studiedclass,reason_leaving=reason_leaving,
                                                    issue_date=issue_date,general_conduct=general_conduct,certificate_file=transfer_certificate)
            else:
                ahash22 = transfer_certificate1.objects.all().last()
                aphash = ahash22.newhash1
                transfer_certificate1.objects.create(uname=uname, full_name=fullname,
                                                      dateof_birth=dateof_birth, religion=religion, caste=caste,
                                                      father_name=father_name, mother_name=mother_name, address=address,
                                                      file_path=uploaded_file_url, phash1=aphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,sname=sname,dateof_admission=dateof_admission,
                                                    last_studiedclass=last_studiedclass,reason_leaving=reason_leaving,
                                                    issue_date=issue_date,general_conduct=general_conduct,certificate_file=transfer_certificate)
    return render(request, 'school/generate_tc1.html',{'uname':uname})

def generate_attendance(request):
    schoolname = request.session['schoolname']
    objectlist12 = school_details1.objects.all().filter(school_name=schoolname)
    if request.method == "POST":
        uname = request.POST.get('uname')
        sch_name = request.POST.get('sch_name')
        grade = request.POST.get('grade')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        attendance_details.objects.create(uname=uname, sch_name=sch_name, grade=grade, day=day,month=month,year=year)
        attdet = attendance_details.objects.all().last()
        att_unid = attdet.id
        att_uname = attdet.uname
        sch_name1 = attdet.sch_name
        grade1 = attdet.grade
        day1 = attdet.day
        month1 = attdet.month
        year1 = attdet.year
        elems = []
        styles = getSampleStyleSheet()
        styles1 = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1
        title_style1 = styles1['Heading1']
        title_style1.alignment = 1
        elems.append(Paragraph("Attendance Certificate", title_style))
        a1 = Paragraph(
            "This award is presented to" + " " + att_uname + " " + "a student in the" + " " + grade1 + " " + "grade at" + " " +
            sch_name1 + " " + "in recognition of perfect attendace awarded on this" + " " + day1 + " " +
            "day of" + " " + month1 + " " + year1,
            title_style1)
        elems.append(a1)
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)

        output_path = join(ROOT_DIR, 'school_attendance')
        print(output_path)
        pdf_filename = output_path + "/" + att_uname + '_' + "attendancecertificate" + '.pdf'
        print(pdf_filename)

        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        pdf.build(elems)
        return redirect('generate_attendance1')
    return render(request, 'school/generate_attendance.html',{'objectlist12':objectlist12,'schoolname':schoolname})

def generate_attendance1(request):
    schoolname = request.session['schoolname']
    attdet = attendance_details.objects.all().last()
    att_unid = attdet.id
    att_uname=attdet.uname
    sch_name1 = attdet.sch_name
    grade1 = attdet.grade
    day1 = attdet.day
    month1 = attdet.month
    year1 = attdet.year

    blockchain = Blockchain()
    previous_block1 = blockchain.get_previous_block()
    previous_nonce1 = previous_block1['nonce']
    print(previous_nonce1)
    nonce1 = blockchain.proof_of_work(previous_nonce1)
    previous_hash1 = blockchain.hash(previous_block1)
    block1 = blockchain.create_block(nonce1, previous_hash1)
    atimestamp = str(datetime.datetime.now())
    apphash = attendance_certificate1.objects.all().count()
    print(apphash)

    if request.method == "POST" and request.FILES['attendance_certificate']:
        att_uname1 = request.POST.get('att_uname1')
        attendance_certificate = request.FILES['attendance_certificate']
        fs = FileSystemStorage()
        filename = fs.save(attendance_certificate.name, attendance_certificate)
        uploaded_file_url = fs.url(filename)

        if apphash == 0:
            attendance_certificate1.objects.create(uname=att_uname1, sch_name=sch_name1,
                                                 grade=grade1, day=day1,month=month1,year=year1,
                                                 file_path=uploaded_file_url, phash1=apphash,
                                                 newhash1=previous_hash1,
                                                 atimestamp=atimestamp,certificate_file=attendance_certificate)
        else:
            ahash22 = attendance_certificate1.objects.all().last()
            aphash = ahash22.newhash1
            attendance_certificate1.objects.create(uname=att_uname1, sch_name=sch_name1,
                                                 grade=grade1, day=day1,month=month1,year=year1,
                                                 file_path=uploaded_file_url, phash1=aphash,
                                                 newhash1=previous_hash1,
                                                 atimestamp=atimestamp,certificate_file=attendance_certificate)
    return render(request, 'school/generate_attendance1.html',{'att_uname':att_uname})

def generate_sports(request):
    schoolname1 = request.session['schoolname']
    objectlist1 = school_details1.objects.all().filter(school_name=schoolname1)
    if request.method == "POST":
        uname = request.POST.get('uname')
        sch_name = request.POST.get('sch_name')
        sports_name = request.POST.get('sports_name')
        winning_place = request.POST.get('winning_place')
        date = request.POST.get('date')

        sports_details.objects.create(uname=uname, sch_name=sch_name, sports_name=sports_name, winning_place=winning_place, date=date, )
        sportsdet = sports_details.objects.all().last()
        att_unid = sportsdet.id
        att_uname = sportsdet.uname
        sch_name11 = sportsdet.sch_name
        sports_name1 = sportsdet.sports_name
        winning_place1 = sportsdet.winning_place
        date1 = sportsdet.date
        elems = []
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = 1
        elems.append(Paragraph("Sports Certificate", title_style))
        ROOT_DIR = dirname(dirname(__file__))
        print(ROOT_DIR)

        output_path = join(ROOT_DIR, 'sports_certificate')
        print(output_path)
        pdf_filename = output_path + "/" + uname + '_' + "sportscertificate" + '.pdf'
        print(pdf_filename)
        data = [
            ['Full Name :', att_uname],
            ['School Name:', sch_name11],
            ['Sports Name:', sports_name1],
            ['Winning Place:', winning_place1],
            ['Date:', date1],
        ]
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        table_style = TableStyle([('FONTSIZE', (0, 0), (4, 4), 24), ('ALIGN', (0, 0), (4, 4), 'LEFT')])
        table = Table(data, rowHeights=35)
        table.setStyle(table_style)
        elems.append(table)
        pdf.build(elems)
        return redirect('generate_sports1')
    return render(request, 'school/generate_sports.html',{'objectlist1':objectlist1,'schoolname1':schoolname1})

def generate_sports1(request):
    schoolname11 = request.session['schoolname']
    sportsdet1 = sports_details.objects.all().last()
    sp_unid = sportsdet1.id
    sp_uname=sportsdet1.uname
    sp_sch_name = sportsdet1.sch_name
    sp_sports_name = sportsdet1.sports_name
    sp_winning_place = sportsdet1.winning_place
    sp_date = sportsdet1.date


    blockchain = Blockchain()
    previous_block1 = blockchain.get_previous_block()
    previous_nonce1 = previous_block1['nonce']
    print(previous_nonce1)
    nonce1 = blockchain.proof_of_work(previous_nonce1)
    previous_hash1 = blockchain.hash(previous_block1)
    block1 = blockchain.create_block(nonce1, previous_hash1)
    atimestamp = str(datetime.datetime.now())
    apphash = sports_certificate1.objects.all().count()
    print(apphash)

    if request.method == "POST" and request.FILES['sports_certificate']:
        sp_uname1 = request.POST.get('sp_uname1')
        sports_certificate = request.FILES['sports_certificate']
        fs = FileSystemStorage()
        filename = fs.save(sports_certificate.name, sports_certificate)
        uploaded_file_url = fs.url(filename)

        if apphash == 0:
            sports_certificate1.objects.create(uname=sp_uname1, sch_name=sp_sch_name,sports_name=sp_sports_name,
                                                 winning_place=sp_winning_place, date=sp_date,
                                                 file_path=uploaded_file_url, phash1=apphash,
                                                 newhash1=previous_hash1,
                                                 atimestamp=atimestamp,certificate_file=sports_certificate)
        else:
            ahash22 = sports_certificate1.objects.all().last()
            aphash = ahash22.newhash1
            sports_certificate1.objects.create(uname=sp_uname1, sch_name=sp_sch_name,sports_name=sp_sports_name,
                                                 winning_place=sp_winning_place, date=sp_date,
                                                 file_path=uploaded_file_url, phash1=aphash,
                                                 newhash1=previous_hash1,
                                                 atimestamp=atimestamp,certificate_file=sports_certificate)
    return render(request, 'school/generate_sports1.html',{'sp_uname':sp_uname})

def school_accesscertificate(request):
    certificate1=''
    schoolname = request.session['schoolname']
    schooldet = school_details1.objects.filter(school_name=schoolname)
    if request.method == "POST":
        uname = request.POST.get('uname')
        certificate_name = request.POST.get('certificate_name')
        if certificate_name == "birth_certificate":
            certificate1 = birth_certificate1.objects.filter(uname=uname)
            cname="birth_certificate"
            request.session['cname'] = cname
        else:
            certificate1 = community_certificate1.objects.filter(uname=uname)
            cname = "community_certificate"
            request.session['cname'] = cname
    return render(request, 'school/school_accesscertificate.html',{'schooldet':schooldet,'certificate1':certificate1})

def school_request1(request,pk):
    keyresult2 = ''
    sts11 = "send"
    sts22 = "deactivate"
    cname = request.session['cname']
    if cname=="birth_certificate":
        request1 = birth_certificate1.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    else:
        request1 = community_certificate1.objects.get(id=pk)
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
            certificate_name1=t11.certificate_name
            if certificate_name1=="birth_certificate":
                keyresult2 = birth_certificate1.objects.filter(uname=person_name11)
            else:
                keyresult2 = community_certificate1.objects.filter(uname=person_name11)
            school_birth1.objects.filter(studnet_name=person_name, key1=unkey, status1=sts11).update(status1=sts22)
    return render(request, 'school/school_request1.html',{'person_name':person_name,'keyresult2':keyresult2})

def schoolkey_request(request):
    schoolname = request.session['schoolname']
    semail = request.session['semail']
    person_id1 = request.session['person_id1']
    student_name = request.session['student_name']
    cname = request.session['cname']
    sts1 = "pending"
    key1 = "pending"
    school_birth1.objects.create(requestor=schoolname, studnet_name=student_name, email=semail,certificate_name=cname, status1=sts1)
    return render(request, 'school/schoolkey_request.html')

def download_birthcertificate11(request,pk):
    objspath1=''
    username1 = request.session['username']
    cname = request.session['cname']
    if cname == "birth_certificate":
        objspath1 = birth_certificate1.objects.get(id=pk)
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

    return render(request, 'school/download_birthcertificate11.html')


def school_accessrequest(request):
    sts1 = "pending"
    certificates1=''
    if request.method == "POST":
        certificate_name = request.POST.get('certificate_name')
        certificates1 = school_birth1.objects.filter(status1=sts1,certificate_name=certificate_name)
    return render(request, 'school/school_accessrequest.html',{'certificates1':certificates1})

def schoolaccess_key1(request,pk):
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
        return redirect("school_accessrequest")
    return render(request, 'school/schoolaccess_key1.html')