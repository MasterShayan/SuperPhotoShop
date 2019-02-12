from django.db import models

# Create your models here.
class Media(models.Model):
    title         = models.CharField(max_length=250)
    photo         = models.ImageField()
    slug          = models.SlugField()
    date          = models.DateTimeField(auto_now_add=True)
    Left          = models.IntegerField(default=0)
    Top           = models.IntegerField(default=0)
    Right         = models.IntegerField(default=0)
    Bottom        = models.IntegerField(default=0)
    Resize_Width  = models.IntegerField(default=0)
    Resize_Height = models.IntegerField(default=0)
    Rotate_Degree = models.IntegerField(default=0)
    Black_White   = models.BooleanField(default=False)
    Share         = models.BooleanField(default=False)


    def __str__(self):
        return self.title