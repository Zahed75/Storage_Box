from django.urls import path
from Upload_App import views

app_name='Upload_App'

urlpatterns = [
    path('', views.file_list, name='index'),
    path('upload/',views.CreateFile.as_view(),name='create_file'),
    path('my-files/',views.MyFiles.as_view(),name='my_files'),
    path('edit/<int:pk>/', views.edit_files, name='edit_files'),
 
  
]
