from django.urls import path
from . import views
from chat.api_views import UploadFile
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
app_name = "chat"
urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('messages/', views.messages, name='messages'),
    path('upload/', views.upload, name='views.upload'),
    path('swagger/', schema_view),
    path('api/', UploadFile.as_view(), name='api_upload'),
]

