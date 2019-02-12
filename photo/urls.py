from django.conf.urls import url
from . import views

app_name="photo"

urlpatterns = [
    url(r'^$', views.photo_homepage),
    url(r'^gallery/', views.photo_list, name='list'),
    url(r'^upload/', views.photo_upload, name='upload'),
    url(r'^upload-error/',  views.photo_upload_error, name='upload_error'),
    url(r'^(?P<slug>[\w-]+)/$', views.photo_detail, name="detail"),
]
