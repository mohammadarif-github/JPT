from django.contrib import admin

# Register your models here.


from .models import Recipe,Review,Comment


admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Comment)
