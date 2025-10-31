from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=9)
    city = models.CharField(max_length=20)

    def __str__(self):
        return "{},{}-{}".format(self.street, self.postal_code,self.city)
    
    class Meta:
        verbose_name_plural = "Address Entries"



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()

class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(16)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_best_seller = models.BooleanField(default= False )
    slug = models.SlugField(default="",null=False, blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse("detail-book", args=[self.slug])
    


    def __str__(self):
        return f"{self.title} ({self.rating})"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)