from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about',views.about,name='about'),
    url(r'^carrer',views.carrer,name='carrer'),
    url(r'^login',views.login,name='login'),
    url(r'^complain',views.complain,name='complain'),
    url(r'^newcomplain',views.newcomplain,name='newcomplain'),
    url(r'^login',views.login,name='login'),
    url(r'^adminzone/validateuser',views.validateuser,name='validateuser'),
    url(r'^consign',views.consign,name='consign'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
