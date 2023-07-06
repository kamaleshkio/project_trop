from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.utils.encoding import smart_str

from college.models import degree_certificate11, ctransfer_certificate1
from office.models import office_register1, emppay_slip, salary_slip, experience1, exp_certificate
from school.models import school_birth1
from user.models import office_details
from reportlab.platypus import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import json
from os.path import dirname, join
import hashlib
import os
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
def office_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pswd = request.POST.get('password')
        try:
            check = office_register1.objects.get(officename=uname, password=pswd)
            request.session['officeid'] = check.id
            request.session['officename'] = check.officename
            request.session['officeemail'] = check.email
            return redirect('office_home')
        except:
            pass
        return redirect('office_login')
    return render(request, 'office/office_login.html')

def office_register(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        password = request.POST.get('password')
        office_register1.objects.create(officename=fullname, email=email, mobile=mobile,  password=password)
    return render(request, 'office/office_register.html')

def office_home(request):
    officename = request.session['officename']
    officeemail = request.session['officeemail']

    officedet = office_details.objects.filter(company_name=officename)
    return render(request, 'office/office_home.html',{'officedet':officedet})

def generate_payslip(request,pk):
    objjs = office_details.objects.get(id=pk)
    unid = objjs.id
    request.session['unid'] = unid
    uname = objjs.uname
    fullname = objjs.fullname
    company_name = objjs.company_name
    designation = objjs.designation
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        uname = request.POST.get('uname')
        designation = request.POST.get('designation')
        month = request.POST.get('month')
        year = request.POST.get('year')
        basic_da = request.POST.get('basic_da')
        hra = request.POST.get('hra')
        conveyance = request.POST.get('conveyance')
        pf = request.POST.get('pf')
        esi = request.POST.get('esi')
        net_salary = request.POST.get('net_salary')
        emppay_slip.objects.create(company_name=company_name, uname=uname, designation=designation, month=month,
                                    year=year,basic_da=basic_da,hra=hra,conveyance=conveyance,pf=pf,esi=esi,net_salary=net_salary)
        return redirect('generate_payslip1')
    return render(request, 'office/generate_payslip.html',{'uname':uname,'company_name':company_name,'designation':designation})

def generate_payslip1(request):
    ename=''
    unid = request.session['unid']
    t11 = emppay_slip.objects.all().last()
    company_name = t11.company_name
    ename = t11.uname
    designation = t11.designation
    month = t11.month
    year = t11.year
    basic_da = t11.basic_da
    hra = t11.hra
    conveyance = t11.conveyance
    pf = t11.pf
    esi = t11.esi
    net_salary = t11.net_salary
    elems = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1
    elems.append(Paragraph("Salary Slip", title_style))
    ROOT_DIR = dirname(dirname(__file__))
    print(ROOT_DIR)
    output_path = join(ROOT_DIR, 'salary_slip')
    print(output_path)
    pdf_filename = output_path + "/" + ename + '_' + "salaryslip" + '.pdf'
    print(pdf_filename)
    data = [
            ['Company Name :', company_name],
            ['Employee Name :', ename],
            ['Designation :', designation],
            ['Month :', month],
            ['Year :', year],
            ['Basic & DA :', basic_da],
            ['HRA:', hra],
            ['Conveyance:', conveyance],
            ['PF:', pf],
            ['E.S.I:', esi],
            ['Net Salary:', net_salary],

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
    apphash = salary_slip.objects.all().count()
    print(apphash)
    if request.method == "POST" and request.FILES['salary_slip1']:
        per_name = request.POST.get('uname1')
        salary_slip1 = request.FILES['salary_slip1']
        fs = FileSystemStorage()
        filename = fs.save(salary_slip1.name, salary_slip1)
        uploaded_file_url = fs.url(filename)

        if apphash == 0:
            salary_slip.objects.create(company_name=company_name, uname=ename, designation=designation, month=month,
                                            year=year,basic_da=basic_da,hra=hra,conveyance=conveyance,pf=pf,esi=esi,net_salary=net_salary,
                                                      file_path=uploaded_file_url, phash1=apphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,certificate_file=salary_slip1)
        else:
            ahash22 = salary_slip.objects.all().last()
            aphash = ahash22.newhash1
            salary_slip.objects.create(company_name=company_name, uname=ename, designation=designation, month=month,
                                            year=year,basic_da=basic_da,hra=hra,conveyance=conveyance,pf=pf,esi=esi,net_salary=net_salary,
                                                      file_path=uploaded_file_url, phash1=aphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,certificate_file=salary_slip1)

    return render(request, 'office/generate_payslip1.html',{'uname':ename})

def experience_certificate(request):
    officename = request.session['officename']
    officeemail = request.session['officeemail']

    officedet1 = office_details.objects.filter(company_name=officename)
    return render(request, 'office/experience_certificate.html',{'officedet1':officedet1})

def generate_experience(request,pk):
    objjs = office_details.objects.get(id=pk)
    unid = objjs.id
    request.session['unid'] = unid
    uname = objjs.uname
    fullname = objjs.fullname
    company_name = objjs.company_name
    designation = objjs.designation
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        uname = request.POST.get('uname')
        designation = request.POST.get('designation')
        exp_year = request.POST.get('exp_year')
        starting_year = request.POST.get('starting_year')
        finishing_year = request.POST.get('finishing_year')

        experience1.objects.create(company_name=company_name, uname=uname, designation=designation, exp_year=exp_year,
                                    starting_year=starting_year,finishing_year=finishing_year)
        return redirect('generate_experience1')
    return render(request, 'office/generate_experience.html',{'uname':uname,'company_name':company_name,'designation':designation})

def generate_experience1(request):
    ename=''
    unid = request.session['unid']
    t11 = experience1.objects.all().last()
    company_name = t11.company_name
    ename = t11.uname
    designation = t11.designation
    exp_year = t11.exp_year
    starting_year = t11.starting_year
    finishing_year = t11.finishing_year
    elems = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1
    elems.append(Paragraph("Experience Certificate", title_style))
    ROOT_DIR = dirname(dirname(__file__))
    print(ROOT_DIR)
    output_path = join(ROOT_DIR, 'experience_certificate')
    print(output_path)
    pdf_filename = output_path + "/" + ename + '_' + "experiencecertificate" + '.pdf'
    print(pdf_filename)
    data = [
            ['Company Name :', company_name],
            ['Employee Name :', ename],
            ['Designation :', designation],
            ['Experience :', exp_year],
            ['Starting Year :', starting_year],
            ['Finishing Year :', finishing_year],


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
    apphash = exp_certificate.objects.all().count()
    print(apphash)

    if request.method == "POST" and request.FILES['experience_certificate']:
        per_name = request.POST.get('uname1')
        experience_certificate = request.FILES['experience_certificate']
        fs = FileSystemStorage()
        filename = fs.save(experience_certificate.name, experience_certificate)
        uploaded_file_url = fs.url(filename)

        if apphash == 0:
            exp_certificate.objects.create(company_name=company_name, uname=ename, designation=designation, exp_year=exp_year,
                                            starting_year=starting_year,finishing_year=finishing_year,
                                                      file_path=uploaded_file_url, phash1=apphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,certificate_file=experience_certificate)
        else:
            ahash22 = exp_certificate.objects.all().last()
            aphash = ahash22.newhash1
            exp_certificate.objects.create(company_name=company_name, uname=ename, designation=designation,exp_year=exp_year,
                                            starting_year=starting_year,finishing_year=finishing_year,
                                                      file_path=uploaded_file_url, phash1=aphash,
                                                      newhash1=previous_hash1,
                                                      atimestamp=atimestamp,certificate_file=experience_certificate)

    return render(request, 'office/generate_experience1.html',{'uname':ename})

def office_accesscertificate(request):
    certificate1 = ''
    officename = request.session['officename']
    print(officename)
    officedet = office_details.objects.filter(company_name=officename)
    if request.method == "POST":
        uname = request.POST.get('uname')
        certificate_name = request.POST.get('certificate_name')
        if certificate_name == "degree_certificate":
            certificate1 = degree_certificate11.objects.filter(uname=uname)
            cname = "degree_certificate"
            request.session['cname'] = cname
        else:
            certificate1 = ctransfer_certificate1.objects.filter(uname=uname)
            cname = "college_tc"
            request.session['cname'] = cname
    return render(request, 'office/office_accesscertificate.html',{'schooldet':officedet,'certificate1':certificate1})

def office_request1(request,pk):
    keyresult2 = ''
    sts11 = "send"
    sts22 = "deactivate"
    cname = request.session['cname']
    if cname == "degree_certificate":
        request1 = degree_certificate11.objects.get(id=pk)
        person_id = request1.id
        request.session['person_id1'] = person_id
        person_name = request1.uname
        request.session['student_name'] = person_name
    else:
        request1 = ctransfer_certificate1.objects.get(id=pk)
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
            if certificate_name1 == "degree_certificate":
                keyresult2 = degree_certificate11.objects.filter(uname=person_name11)
            else:
                keyresult2 = ctransfer_certificate1.objects.filter(uname=person_name11)

            school_birth1.objects.filter(studnet_name=person_name, key1=unkey, status1=sts11).update(status1=sts22)
    return render(request, 'office/office_request1.html',{'person_name':person_name,'keyresult2':keyresult2})

def officekey_request(request):
    officename = request.session['officename']
    print(officename)
    officeemail = request.session['officeemail']
    person_id1 = request.session['person_id1']
    student_name = request.session['student_name']
    cname = request.session['cname']
    sts1 = "pending"
    key1 = "pending"
    school_birth1.objects.create(requestor=officename, studnet_name=student_name, email=officeemail,certificate_name=cname, status1=sts1)
    return render(request, 'office/officekey_request.html')

def download_ccertificate(request,pk):
    objspath1=''
    username1 = request.session['username']
    cname = request.session['cname']
    if cname == "degree_certificate":
        objspath1 = degree_certificate11.objects.get(id=pk)
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
    else:
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


    return render(request, 'office/download_ccertificate.html')