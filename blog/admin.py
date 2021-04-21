from django.contrib import admin

from .models import Post


# Para hacer nuestro modelo visible en la página del administrador
admin.site.register(Post)