from django.urls import path, re_path
from personal_doc_app.views import index

urlpatterns = [
  path('', index),
]
  # url(r'^api/login$', views.login),
  # url(r'^api/register$', views.register)