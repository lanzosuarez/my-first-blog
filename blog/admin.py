from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)		 # To make our model visible on the admin page.
								 # we need to register the model with admin.site.register(Post).
									
								 # to create superuser. python manage.py createsuperuser
								 #https://docs.djangoproject.com/en/1.9/ref/contrib/admin/