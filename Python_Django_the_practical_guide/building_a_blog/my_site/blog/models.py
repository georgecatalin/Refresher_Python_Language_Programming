from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index= True)
    content = models.TextField(validators=[MinLengthValidator(10)])