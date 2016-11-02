from django.shortcuts import resolve_url
from django.views.generic.edit import CreateView
from .models import Solution


class SolutionCreate(CreateView):
    model = Solution
    fields = [ 'code' ]

    def get_success_url(self):
        pass
