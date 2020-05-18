from django.shortcuts import render,redirect
from . models import Complain,Carrer,LoginInfo
from . import smssender
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification
from adminzone .models import Packet

# Create your views here.
def index(request):
    notification=Notification.objects.all()

    return render(request,'index.html',{'notification':notification})
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request, 'login.html')
def carrer(request):
    if request.method=='POST' and request.FILES['cv']:
        name=request.POST['name']
        gender=request.POST['gender']
        qualification=request.POST['qualification']
        experience=request.POST['experience']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']

        myfile=request.FILES['cv']
        cv=myfile.name
        cr=Carrer(name=name,gender=gender,qualification=qualification,experience=experience,address=address,contactno=contactno,emailaddress=emailaddress,cv=cv)
        cr.save()
        fs=FileSystemStorage()
        fs.save(myfile.name,myfile)

        return render(request, 'carrer.html',{'message':'You are sucessfully applied for jobs'})
    return render(request,'carrer.html')

def complain(request):
    return render(request, 'complain.html')
def newcomplain(request):
    username=request.POST['username']
    gender=request.POST['gender']
    subject=request.POST['subject']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    compalintext=request.POST['compalintext']
    c=Complain(username=username,gender=gender,subject=subject,contactno=contactno,emailaddress=emailaddress,compalintext=compalintext)
    c.save()
    smssender.sentsms(contactno, "Thanks for feedback. we will contact you soon. -Team HR")
    return redirect('index')
def login(request):
    return render(request,'login.html')
def validateuser(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        user=LoginInfo.objects.get(username=username,password=password)
        if user is not None:
            return render(request,'adminhome.html')
    except ObjectDoesNotExist:
        return redirect('login')
    return render(request,'index.html')


def consign(request):
    try:
        reno=request.POST['refno']#taking reference no from index page
        r=Packet.objects.get(refno=reno)
        if r is not None:
           return render(request,'index.html',{'r':r})
    except ObjectDoesNotExist:
        return render(request,'index.html',{'msg':'reference no is not valid'})