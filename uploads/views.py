from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import cloudinary.uploader
import json
from .forms import ImagePostForm, Tributeform
from .models import ImageComment, ImagePost, Tribute, TributeComment


# Create your views here.
transformation=[
    {"width": 200,
      "height": 200, 
      "crop": "auto", 
      "gravity":"auto", 
    #   "effect": "improve:50"
      }
    ]

def index(request):
    images = ImagePost.objects.order_by('?')
    tributes = Tribute.objects.all()
    form = Tributeform()

    context = {
        'images':images,
        'tributes':tributes,
        'form':form
    }

    return render(request, 'index.html', context)

# this saves both url and image to local storage
def picture_post(request):
    form = ImagePostForm()

    if request.method == 'POST':
        form = ImagePostForm(request.POST, files= request.FILES)

        if form.is_valid():
            form_instance =form.save(commit=False)
            image = form.cleaned_data['image']
            
            image_url = cloudinary.uploader.upload(image,transformation=transformation)
            print(f'image url is {image_url} \n type is {type(image_url)}')
            # print(f'form_instance is: {form_instance}')
            form.instance.url = image_url['url']
            form_instance.save()
            
            return render(request, 'upload.html', {'image':image_url})
    else:
        return render(request, 'upload.html', {'form':form})

# this only saves cloudinary image url to db
@csrf_exempt
def picture_post_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(f'data is:{data}')
        image_post = ImagePost(url=data)
        image_post.save()
        return JsonResponse({'message':'text saved successfully'})

def tribute_post(request):
    if request.method == 'POST':
        form = Tributeform(request.POST)
        
        if form.is_valid():
            # print(f'this is post data: {request.POST}')
            writer = request.POST.get('name')
            email = request.POST.get('email')
            tribute_text = request.POST.get('textarea')
            # my_form = form.save(commit=False)
            form.instance.writer = writer
            form.instance.tribute = tribute_text
            form.save()
            print(f'writer:{writer}\nemail:{email}\ntribute:{tribute_text}')
            # tribute = Tribute.objects.create(writer=writer, email=email, tribute=tribute_text)
            return HttpResponsePermanentRedirect(reverse('upload:index_page')+'#tributes')

