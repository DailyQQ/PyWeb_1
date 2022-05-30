from django.views import View
from django.http import HttpResponse

from random import random


class RandomNumberView(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)