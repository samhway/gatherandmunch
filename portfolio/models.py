from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here. 

class category(models.Model) :
    category = models.CharField(max_length=50, blank=True, verbose_name='Category', primary_key=True)

    def __str__ (self) :
        return self.category

class post(models.Model) :
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.CharField(max_length=1000, blank=True, verbose_name='Description')
    postContent = models.CharField(max_length=10000, blank=True, verbose_name='Content')
    category = models.ForeignKey(category, default=None, on_delete=CASCADE)
    
    def __str__ (self) :
        return self.title
 
class postImage(models.Model) :
    myPost = models.ForeignKey(post, default=None, on_delete=CASCADE)
    imageName = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='photos', verbose_name='Image')

    def __str__ (self) :
        return str(self.imageName)   

    def pathName (self) :
        return str(self.image.path)[46:]  