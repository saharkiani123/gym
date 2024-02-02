from django.contrib import admin
from .models import StudiumSet, Possibilitie, SportField, ClassTime, WeeklyReservation


admin.site.register(StudiumSet)
admin.site.register(ClassTime)
admin.site.register(WeeklyReservation)
admin.site.register(Possibilitie)
admin.site.register(SportField)
