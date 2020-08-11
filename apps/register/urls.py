from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    # url(r'^upload_pic$', views.upload_pic),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^profile$', views.profile),
    url(r'^fb$', views.fb),
    url(r'^twitter$', views.twitter),
    url(r'^linkdien$', views.linkdien),
    url(r'^insta$', views.insta),
    url(r'^aboutus$', views.aboutus),
    url(r'^saveprofile1$', views.saveprofile1),
    url(r'^saveprofile2$', views.saveprofile2),
    url(r'^about_me$', views.about_me),
    url(r'^newprofile$', views.newprofile),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)