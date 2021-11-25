from django.contrib import admin
from .models import People, Blotter, BPermit, TermOfficial, TermNow, Vaccination, Household, BPTransaction, \
    Resolution, CovidVac, CovidCase, SVaccination, PVaccination, Pregnant

admin.site.register(People)
admin.site.register(Blotter)
admin.site.register(BPermit)
admin.site.register(TermOfficial)
admin.site.register(TermNow)
admin.site.register(Vaccination)
admin.site.register(Household)
admin.site.register(BPTransaction)
admin.site.register(Resolution)
admin.site.register(CovidVac)
admin.site.register(CovidCase)
admin.site.register(SVaccination)
admin.site.register(PVaccination)
admin.site.register(Pregnant)
#