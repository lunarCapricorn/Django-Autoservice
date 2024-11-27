from django.contrib import admin

# Register your models here.

from .models import Automobilio_modelis, Uzsakymas, Automobilis, Uzsakymo_eilute, Paslauga

admin.site.register(Automobilio_modelis)
admin.site.register(Uzsakymas)
admin.site.register(Automobilis)
admin.site.register(Uzsakymo_eilute)
admin.site.register(Paslauga)