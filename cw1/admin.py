from django.contrib import admin

# Register your models here.
from .models import User,Module,Rate,Professor
admin. site.register(User)
admin. site.register(Module)
admin. site.register(Rate)
admin. site.register(Professor)