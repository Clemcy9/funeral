from django.urls import path
from .views import picture_post, index, tribute_post, picture_post_api

app_name = 'upload'

urlpatterns = [
    path('', index, name='index_page'),
    path('picture-upload/', picture_post, name='picture_upload'),
    path('tribute-upload/', tribute_post, name='tribute_upload'),
    path('pic-upload-api', picture_post_api, name='pic_upload_api')
]