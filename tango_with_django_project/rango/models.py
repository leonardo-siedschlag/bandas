from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)#chave primaria
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

    def save(self, *args, **kwargs):
        #como this self = this do java
        self.slug = slugify(self.name)#argumento
        super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.ImageField(default=0)



    def __unicode__(self):
        return self.title
