from django.conf.urls import url
from views import TaskList, TaskDetail

urlpatterns = [
        url(r'^(?P<pk>[0-9]+)$', TaskDetail.as_view(), name='task_detail'),
        url(r'$', TaskList.as_view(), name='task_list'),
]
