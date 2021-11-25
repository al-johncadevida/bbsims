from django.contrib import admin
from .models import User, Resident, Official, Profile


admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Resident)
admin.site.register(Official)