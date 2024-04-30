from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import cloudinary.uploader
import json
from .forms import ImagePostForm, Tributeform
from .models import ImageComment, ImagePost, Tribute, TributeComment



def index(request):
    images = ImagePost.objects.filter(caption__isnull=False).order_by('?')[:6]
    tributes = Tribute.objects.order_by('?')[:5]
    context = {
        'images':images,
        'tributes':tributes,
    }
    return render(request, 'main.html', context)


def tributes(request):
    tributes = Tribute.objects.order_by('-id')
    return render(request, 'tributeList.html', {'tributes':tributes})

def gallery(request):
    images = ImagePost.objects.order_by('?')
    return render(request, 'gallery.html', {'images':images})

def tribute_post(request):
    form = Tributeform()
    context = {
        'form':form
    }
    if request.method == 'POST':
        form = Tributeform(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('upload:tributes'))
        else:
            return render(request, 'tribute.html', {'form':form})
    return render(request, 'tribute.html', context)


# this only saves cloudinary image url to db
@csrf_exempt
def picture_post_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f'data is:{data}')
        image_post = ImagePost(url=data)
        image_post.save()
        return JsonResponse({'message':'text saved successfully'})
