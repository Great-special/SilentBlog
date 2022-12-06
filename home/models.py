from django.db import models
# from django.utils.text import slugify
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .utils import generate_slug



# Create your models here.


class BlogModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = FroalaField()
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=True)
    image = models.ImageField(upload_to='blogPost/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        
        super(BlogModel, self).save(*args, **kwargs)
    
    # @property
    def get_image_url(self):
        image_url = self.image.url
        print("Image URL", image_url)
        return image_url
