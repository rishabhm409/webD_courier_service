from django.shortcuts import render,redirect
from datetime import date
from . models import Notification,City,Qualification,Packet
from .refgen import getref
from generalzone.models import Complain,Carrer
# Create your views here.
def adminhome(request):
    ob = Notification.objects.all()
    return render(request,'adminhome.html',{'ob':ob})
def delete(request,id):
    en=Notification.objects.get(id=id)
    en.delete()
    return redirect('adminhome')

def addnotification(request):
    notificationmsg=request.POST['notificationmsg']
    today=date.today()
    posteddate=today.strftime("%d/%m/%y")
    n=Notification(notificationmsg=notificationmsg,posteddate=posteddate)
    n.save()
    return redirect('adminhome')

def city(request):
    ob=City.objects.all()
    return render(request,'city.html',{'ob':ob})
def cities(request):
    cityname=request.POST['cityname']
    o=City(cityname=cityname)
    o.save()
    return redirect('city')
def qualification(request):
    ob=Qualification.objects.all()
    return render(request,'qualification.html',{'ob':ob})

def quali(request):
    qualification=request.POST['qualification']
    o=Qualification(qualificatiom=qualification)
    o.save()
    return redirect('city')

def delete1(request,id):
    en=City.objects.get(id=id)
    en.delete()
    return redirect('city')

def delete2(request,id):
    en=Qualification.objects.get(id=id)
    en.delete()
    return redirect('qualification')


def calling(request):
    refno=request.POST['refno']
    sendername=request.POST['sendername']
    senderaddress=request.POST['senderaddress']
    sendermobo=request.POST['sendermobo']
    receivername=request.POST['receivername']
    receiveraddress= request.POST['receiveraddress']
    receivermobo = request.POST['receivermobno']
    source=request.POST['source']
    mid=request.POST['mid']
    destination=request.POST['destination']
    weight=request.POST['weight']
    charge=request.POST['charge']
    today=date.today()
    postdate=today.strftime('%d/%m/%y')
    status=request.POST['status']
    n=Packet(refno=refno,sendername=sendername,senderaddress=senderaddress,sendermobo=sendermobo,receivername=receivername,receiveraddress=receiveraddress,receivermobo=receivermobo,source=source,mid=mid,destination=destination,weight=weight,charge=charge,postdate=postdate,status=status)
    n.save()
    return redirect('packet')

#def packetget(request):
 #   return render(request,'packet.html')

def packet(request):
    cities=City.objects.all()
    refno=getref()

    return render(request,'packet.html', {'cities': cities, 'refno': refno})

def managecomplain(request):
    complain= Complain.objects.all()
    return render(request, 'managecomplain.html', {'complain': complain})


def delete(request,id):
    d=Complain.objects.get(id=id)
    d.delete()
    return redirect('managecomplain')


def carrermanagement(request):
    ob=Carrer.objects.all()
    return render(request,'carrermanagement.html',{'ob':ob})


def delete3(request,id):
    d=Carrer.objects.get(id=id)
    d.delete()
    return redirect('carrermanagement')

def delete4(request,refno):
    d=Packet.objects.get(refno=refno)
    d.delete()
    return redirect('parcel')

def parcel(request):
    ob=Packet.objects.all()
    return render(request,'parcel.html',{'ob':ob})

def pupdate(request,refno):
    ob=Packet.objects.get(refno=refno)
    cities = City.objects.all()
    return render(request,'pupdate.html',{'ob':ob,'cities':cities})

def update(request):
    refno = request.POST['refno']
    sendername = request.POST['sendername']
    senderaddress = request.POST['senderaddress']
    sendermobo = request.POST['sendermobo']
    receivername = request.POST['receivername']
    receiveraddress = request.POST['receiveraddress']
    receivermobo = request.POST['receivermobno']
    source = request.POST['source']
    mid = request.POST['mid']
    destination = request.POST['destination']
    weight = request.POST['weight']
    charge = request.POST['charge']
    today = date.today()
    postdate = today.strftime('%d/%m/%y')
    status = request.POST['status']
    n = Packet(refno=refno, sendername=sendername, senderaddress=senderaddress, sendermobo=sendermobo,
               receivername=receivername, receiveraddress=receiveraddress, receivermobo=receivermobo, source=source,
               mid=mid, destination=destination, weight=weight, charge=charge, postdate=postdate, status=status)
    n.save()
    return redirect('parcel')

def logout(request):
    return render(request,'login.html')