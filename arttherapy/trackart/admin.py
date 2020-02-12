from django.contrib import admin

# Register your models here.

from django.contrib import admin

## core
from .models import art_client, art_appointment, art_painting
## lookups
from .models import paintcolor, clientmood
## many x many-s

admin.site.register(art_client)
admin.site.register(art_appointment)
admin.site.register(art_painting)

admin.site.register(paintcolor)
admin.site.register(clientmood)

