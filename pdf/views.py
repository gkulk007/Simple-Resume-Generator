from urllib import response
from ckeditor import *
from django.shortcuts import render
from .models import Profile
# Create your views here.
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from .forms import CKForm
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template 
from xhtml2pdf import pisa  

def accept(request):
    form = CKForm()
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        previous_work = request.POST.get('previous_work','')
        skills = request.POST.get('skills','')
        projects = request.POST.get('projects','')

        profile = Profile(name=name,email=email,phone=phone,summary=summary,school=school,degree=degree,skills=skills,university=university,previous_work=previous_work,projects=projects)
        profile.save()

    return render(request, "pdf/accept.html", {'form':form})

def resume(request,id):
    userprofile = Profile.objects.get(pk=id)
    template = get_template('pdf/resume.html')
    html  = template.render({'userprofile':userprofile})
    result = BytesIO()
 
     #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(userprofile.name)
        return response

    return pdf


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html',{'profiles':profiles})