from django.contrib import admin
from .models import Book,Author

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}
    list_filter = ("author",)
    list_display = ("title", "rating", "author")

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)