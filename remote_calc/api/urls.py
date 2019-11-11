"""
api/urls.py
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
urlpatterns = [
   path('api', views.VersionAPIView.as_view()),
   path('api/add', views.AddAPIView.as_view()),
   path('api/results', views.ResultsAPIView.as_view()),
   path('api/clear', views.ClearAPIView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
