from django import forms
from . import models


class CreateMedia(forms.ModelForm) :
    class Meta:
        model = models.Media
        fields = [
            'title',
            'photo',
            'slug',
            'Left',
            'Top',
            'Right',
            'Bottom',
            'Resize_Width',
            'Resize_Height',
            'Rotate_Degree',
            'Black_White',
            'Share'
        ]


