from django.http import HttpResponse

from turns.utils.turn_maker import create_reservation


def home(request):
    create_reservation()
    return HttpResponse('success')
