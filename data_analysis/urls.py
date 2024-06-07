from django.urls import path
from . import views

app_name = 'data_analysis'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('analyze/<path:file_path>/', views.analyze_file, name='analyze_file'),
]
