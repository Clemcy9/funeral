from django.urls import path
from .views import index, tribute_post, picture_post_api,tributes, gallery

app_name = 'upload'

urlpatterns = [
    path('', index, name='index_page'),
    path('gallery/', gallery, name='gallery'),
    path('tributes/', tributes, name='tributes'),
    path('tribute-upload/', tribute_post, name='tribute_upload'),
    path('pic-upload-api/', picture_post_api, name='pic_upload_api')
]