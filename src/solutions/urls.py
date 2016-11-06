from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import SolutionCreate, CodeDetailView

urlpatterns = [
    url(r'^create/$', login_required(SolutionCreate.as_view()), name='solution_create'),
    url(r'^(?P<pk>[0-9]+)/code/$', login_required(CodeDetailView.as_view()), name='code_detail_view')
]