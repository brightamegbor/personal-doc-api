from django.conf.urls import url
from personal_doc_app import views

urlpatters = [
  url(r'^api/login$', views.login),
  url(r'^api/register$', views.register)
]