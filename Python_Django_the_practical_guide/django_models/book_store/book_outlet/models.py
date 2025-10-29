from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(16)])
    author = models.CharField(null = True, max_length=50)
    is_best_seller = models.BooleanField(default= False )


    def get_absolute_url(self):
        return reverse("detail-book", args=[self.id])
    


    def __str__(self):
        return f"{self.title} ({self.rating})"