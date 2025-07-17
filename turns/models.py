from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class ReservationDay(models.Model):
    date = models.DateField(_("Date"))


    class Meta:
        verbose_name = _("Reservation Day")
        verbose_name_plural = _("Reservation Days")
        ordering = ('-date',)

    def __str__(self):
        return str(self.date)


class Reservation(models.Model):
    day = models.ForeignKey(ReservationDay, on_delete=models.PROTECT, related_name='reservations', verbose_name=_("Day"))
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("User"), blank=True, null=True)
    time = models.TimeField(_("Time"))

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
        ordering = ('-time',)

    def __str__(self):
        return f"{self.user} - {self.day} - {self.time}"
