from django.conf.urls import url
from . import views
from . models import Notification,Qualification,City
urlpatterns=[
    url(r'^$',views.adminhome,name='adminhome'),
    url(r'^addnotification',views.addnotification,name='addnotification'),
    url(r'^delete/(?P<id>\d+)$',views.delete,name='delete'),
    url(r'^city',views.city,name='city'),
    url(r'^cities',views.cities,name='cities'),
    url(r'^qualification',views.qualification,name='qualification'),
    url(r'^quali',views.quali,name='quali'),
    url(r'^delete1/(?P<id>\d+)$',views.delete1,name='delete1'),
    url(r'^delete2/(?P<id>\w+)$',views.delete2,name='delete2'),
    url(r'^packet',views.packet,name='packet'),
   # url(r'^packetget',views.packetget,name='packetget'),
    url(r'^calling',views.calling,name='calling'),
    url(r'^managecomplain',views.managecomplain,name='managecomplain'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^carrermanagement',views.carrermanagement,name='carrermanagement'),
    url(r'^delete3/(?P<id>\d+)$', views.delete3, name='delete3'),
    url(r'^delete4/(?P<refno>\w+)$',views.delete4, name='delete4'),
    url(r'^parcel',views.parcel,name='parcel'),
    url(r'^update', views.update, name='update'),
    url(r'^pupdate/(?P<refno>\w+)$',views.pupdate,name='pupdate'),
    url(r'^logout',views.logout,name='logout'),
]
