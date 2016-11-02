from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import SolutionCreate

urlpatterns = [
    url(r'^create/$', login_required(SolutionCreate.as_view()), name='question_create'),
]