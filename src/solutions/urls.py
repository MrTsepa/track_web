from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import SolutionCreate, SolutionDetailView, SolutionRunView, SolutionStatuses

urlpatterns = [
    url(r'^create/$', login_required(SolutionCreate.as_view()), name='solution_create'),
    url(r'^(?P<pk>[0-9]+)/code/$', login_required(SolutionDetailView.as_view()), name='solution_detail'),
    url(r'^(?P<pk>[0-9]+)/run/$', login_required(SolutionRunView.as_view()), name='solution_run'),
    url(r'statuses/$', SolutionStatuses.as_view(), name='solutions_statuses')
]