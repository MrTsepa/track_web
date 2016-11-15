from django.conf.urls import url
from views import TaskList, TaskDetailView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', TaskDetailView.as_view(), name='task_detail_ace_editor'),
    url(r'$', TaskList.as_view(), name='task_list'),
]
