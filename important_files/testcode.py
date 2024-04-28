'''
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
'''