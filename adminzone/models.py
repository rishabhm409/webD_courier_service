from django.db import models

# Create your models here.
class Notification(models.Model):
    notificationmsg=models.TextField()
    posteddate=models.CharField(max_length=20)

class City(models.Model):
    cityname=models.CharField(max_length=100)

class Qualification(models.Model):
    qualificatiom=models.CharField(max_length=50)

class Packet(models.Model):
    refno=models.CharField(max_length=20,primary_key=True)
    sendername=models.CharField(max_length=50)
    senderaddress=models.TextField()
    sendermobo=models.CharField(max_length=50)
    receivername=models.CharField(max_length=50)
    receiveraddress=models.TextField()
    receivermobo=models.CharField(max_length=15)
    source=models.CharField(max_length=50)
    mid= models.CharField(max_length=50)
    destination= models.CharField(max_length=50)
    weight= models.CharField(max_length=50)
    charge=models.IntegerField()
    postdate= models.CharField(max_length=50)
    status= models.CharField(max_length=50)