from django.contrib import admin

from turns import models

class InlineReservation(admin.StackedInline):
    model = models.Reservation


@admin.register(models.ReservationDay)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [InlineReservation]