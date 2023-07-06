"""transaction_throughput_provisioning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from transaction_throughput_provisioning import settings
from user import views as userviews
from hospital import views as hospitalviews
from government import views as governmentviews
from college import views as collegeviews
from office import views as officeviews
from school import views as schoolviews



urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',userviews.user_index, name="user_index"),
    url(r'^user_register/$',userviews.user_register, name="user_register"),
    url(r'^user_home/$',userviews.user_home, name="user_home"),
    url(r'^ration_card/$',userviews.ration_card, name="ration_card"),
    url(r'^school_details/$',userviews.school_details, name="school_details"),
    url(r'^college_details/$',userviews.college_details, name="college_details"),
    url(r'^working_details/$',userviews.working_details, name="working_details"),
    url(r'^user_allcertificates/$',userviews.user_allcertificates, name="user_allcertificates"),
    url(r'^view_birthcertificate/$',userviews.view_birthcertificate, name="view_birthcertificate"),
    url(r'^download_birthcertificate/(?P<pk>\d+)/$',userviews.download_birthcertificate, name="download_birthcertificate"),
    url(r'^viewcommunity_certificate/$',userviews.viewcommunity_certificate, name="viewcommunity_certificate"),
    url(r'^download_communitycertificate/(?P<pk>\d+)/$',userviews.download_communitycertificate, name="download_communitycertificate"),
    url(r'^view_rationcard/$', userviews.view_rationcard,name="view_rationcard"),
    url(r'^download_rationcard/(?P<pk>\d+)/$',userviews.download_rationcard, name="download_rationcard"),
    url(r'^view_schoolattendace/$', userviews.view_schoolattendace,name="view_schoolattendace"),
    url(r'^download_schoolattendance/(?P<pk>\d+)/$', userviews.download_schoolattendance, name="download_schoolattendance"),
    url(r'^view_schooltc/$', userviews.view_schooltc,name="view_schooltc"),
    url(r'^download_schooltc/(?P<pk>\d+)/$', userviews.download_schooltc,name="download_schooltc"),
    url(r'^view_schoolsports/$', userviews.view_schoolsports,name="view_schoolsports"),
    url(r'^download_schoolsports/(?P<pk>\d+)/$', userviews.download_schoolsports,name="download_schoolsports"),
    url(r'^viewdegree_certificate/$', userviews.viewdegree_certificate,name="viewdegree_certificate"),
    url(r'^download_degreecertificate/(?P<pk>\d+)/$', userviews.download_degreecertificate,name="download_degreecertificate"),
    url(r'^view_collegetc/$', userviews.view_collegetc,name="view_collegetc"),
    url(r'^download_collegetc/(?P<pk>\d+)/$', userviews.download_collegetc,name="download_collegetc"),
    url(r'^view_salaryslip/$', userviews.view_salaryslip,name="view_salaryslip"),
    url(r'^download_salaryslip/(?P<pk>\d+)/$', userviews.download_salaryslip,name="download_salaryslip"),
    url(r'^viewexperience_certificate/$', userviews.viewexperience_certificate,name="viewexperience_certificate"),
    url(r'^downloadexperience_certificate/(?P<pk>\d+)/$', userviews.downloadexperience_certificate,name="downloadexperience_certificate"),


    url(r'^hospital_login/$',hospitalviews.hospital_login, name="hospital_login"),
    url(r'^hospital_home/$',hospitalviews.hospital_home, name="hospital_home"),
    url(r'^hview_request/$',hospitalviews.hview_request, name="hview_request"),
    url(r'^bkey_generate11/(?P<pk>\d+)/$', hospitalviews.bkey_generate11, name="bkey_generate11"),


    url(r'^government_login/$',governmentviews.government_login, name="government_login"),
    url(r'^government_home/$',governmentviews.government_home, name="government_home"),
    url(r'^generate_birthcertificate/(?P<pk>\d+)/$',governmentviews.generate_birthcertificate, name="generate_birthcertificate"),
    url(r'^bkey_request/$',governmentviews.bkey_request, name="bkey_request"),
    url(r'^birth_certificate/(?P<pk>\d+)/$',governmentviews.birth_certificate, name="birth_certificate"),
    url(r'^comm_certificate/$',governmentviews.comm_certificate, name="comm_certificate"),
    url(r'^generate_communitycertificate/(?P<pk>\d+)/$',governmentviews.generate_communitycertificate, name="generate_communitycertificate"),
    url(r'^rcard_details/$',governmentviews.rcard_details, name="rcard_details"),
    url(r'^generate_rationcard/(?P<pk>\d+)/$',governmentviews.generate_rationcard, name="generate_rationcard"),
    url(r'^gaccess_certificate/$',governmentviews.gaccess_certificate, name="gaccess_certificate"),
    url(r'^gaccess_key1/(?P<pk>\d+)/$', governmentviews.gaccess_key1, name="gaccess_key1"),

    url(r'^office_login/$',officeviews.office_login, name="office_login"),
    url(r'^office_register/$',officeviews.office_register, name="office_register"),
    url(r'^office_home/$',officeviews.office_home, name="office_home"),
    url(r'^generate_payslip/(?P<pk>\d+)/$',officeviews.generate_payslip, name="generate_payslip"),
    url(r'^generate_payslip1/$',officeviews.generate_payslip1, name="generate_payslip1"),
    url(r'^experience_certificate/$',officeviews.experience_certificate, name="experience_certificate"),
    url(r'^generate_experience/(?P<pk>\d+)/$',officeviews.generate_experience, name="generate_experience"),
    url(r'^generate_experience1/$',officeviews.generate_experience1, name="generate_experience1"),
    url(r'^office_accesscertificate/$',officeviews.office_accesscertificate, name="office_accesscertificate"),
    url(r'^office_request1/(?P<pk>\d+)/$',officeviews.office_request1, name="office_request1"),
    url(r'^officekey_request/$',officeviews.officekey_request, name="officekey_request"),
    url(r'^download_ccertificate/(?P<pk>\d+)/$', officeviews.download_ccertificate,name="download_ccertificate"),

    url(r'^school_login/$',schoolviews.school_login, name="school_login"),
    url(r'^school_register/$',schoolviews.school_register, name="school_register"),
    url(r'^school_home/$',schoolviews.school_home, name="school_home"),
    url(r'^generate_tc/(?P<pk>\d+)/$',schoolviews.generate_tc, name="generate_tc"),
    url(r'^generate_tc1/$',schoolviews.generate_tc1, name="generate_tc1"),
    url(r'^generate_attendance/$',schoolviews.generate_attendance, name="generate_attendance"),
    url(r'^generate_attendance1/$',schoolviews.generate_attendance1, name="generate_attendance1"),
    url(r'^generate_sports/$',schoolviews.generate_sports, name="generate_sports"),
    url(r'^generate_sports1/$',schoolviews.generate_sports1, name="generate_sports1"),
    url(r'^school_accesscertificate/$',schoolviews.school_accesscertificate, name="school_accesscertificate"),
    url(r'^school_request1/(?P<pk>\d+)/$',schoolviews.school_request1, name="school_request1"),
    url(r'^schoolkey_request/$',schoolviews.schoolkey_request, name="schoolkey_request"),
    url(r'^download_birthcertificate11/(?P<pk>\d+)/$', schoolviews.download_birthcertificate11,name="download_birthcertificate11"),
    url(r'^school_accessrequest/$',schoolviews.school_accessrequest, name="school_accessrequest"),
    url(r'^schoolaccess_key1/(?P<pk>\d+)/$', schoolviews.schoolaccess_key1, name="schoolaccess_key1"),


    url(r'^college_login/$',collegeviews.college_login, name="college_login"),
    url(r'^college_register/$',collegeviews.college_register, name="college_register"),
    url(r'^college_home/$',collegeviews.college_home, name="college_home"),
    url(r'^cgenerate_tc/(?P<pk>\d+)/$',collegeviews.cgenerate_tc, name="cgenerate_tc"),
    url(r'^cgenerate_tc1/$', collegeviews.cgenerate_tc1, name="cgenerate_tc1"),
    url(r'^degree_certificate/$', collegeviews.degree_certificate, name="degree_certificate"),
    url(r'^degree_certificate1/(?P<pk>\d+)/$', collegeviews.degree_certificate1, name="degree_certificate1"),
    url(r'^degree_certificate2/$', collegeviews.degree_certificate2, name="degree_certificate2"),
    url(r'^college_accesscertificate/$',collegeviews.college_accesscertificate, name="college_accesscertificate"),
    url(r'^college_request1/(?P<pk>\d+)/$',collegeviews.college_request1, name="college_request1"),
    url(r'^collegekey_request/$',collegeviews.collegekey_request, name="collegekey_request"),
    url(r'^download_certificates11/(?P<pk>\d+)/$', collegeviews.download_certificates11,name="download_certificates11"),
    url(r'^college_accessrequest/$',collegeviews.college_accessrequest, name="college_accessrequest"),
    url(r'^collegeaccess_key1/(?P<pk>\d+)/$', collegeviews.collegeaccess_key1, name="collegeaccess_key1"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
