from django.shortcuts import render, redirect
from . import forms
from .models import Media
from PIL import Image 
from django.conf import settings


# Create your views here.
def photo_homepage(request):
    return render(request, 'photo/photo_homepage.html')

def photo_list(request) :
    photos = Media.objects.all().order_by('date')

    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, slug) :
    photo = Media.objects.get(slug=slug)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_upload_error(request):
    if request.method == 'POST':    
        form = forms.CreateMedia(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save()
            img = Image.open(pic.photo)
            img = img.rotate(int(pic.Rotate_Degree))
            if pic.Black_White :
                img = img.convert('L')
            if pic.Top < pic.Bottom and pic.Right > pic.Left :
                img = img.crop((pic.Left, pic.Top, pic.Right, pic.Bottom))
            elif pic.Top == 0 and pic.Bottom == 0 and pic.Right == 0 and pic.Left == 0 :
                pass
            else:
                return redirect('photo:upload_error')
            if pic.Resize_Width > 0 and pic.Resize_Height :
                img = img.resize((pic.Resize_Width, pic.Resize_Height))
            elif pic.Resize_Width == 0 and pic.Resize_Height == 0 : 
                pass
            else :
                return redirect('photo:upload_error')
            img.save(pic.photo.path)
            return redirect('photo:list')
    else :
        form = forms.CreateMedia()
    return render(request, 'photo/rec_edit.html', {'form': form})


def photo_upload(request) :
    if request.method == 'POST':    
        form = forms.CreateMedia(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save()
            img = Image.open(pic.photo)
            img = img.rotate(int(pic.Rotate_Degree))
            if pic.Black_White :
                img = img.convert('L')
            if pic.Top < pic.Bottom and pic.Right > pic.Left :
                img = img.crop((pic.Left, pic.Top, pic.Right, pic.Bottom))
            elif pic.Top == 0 and pic.Bottom == 0 and pic.Right == 0 and pic.Left == 0 :
                pass
            else :
                return redirect('photo:upload_error')
            if pic.Resize_Width > 0 and pic.Resize_Height :
                img = img.resize((pic.Resize_Width, pic.Resize_Height))
            elif pic.Resize_Width == 0 and pic.Resize_Height == 0 : 
                pass
            else :
                return redirect('photo:upload_error')
            img.save(pic.photo.path)
            return redirect('photo:list')
    else :
        form = forms.CreateMedia()
    return render(request, 'photo/rec_edit.html', {'form': form})

