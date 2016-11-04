from django.conf.urls import url
from views import TaskList,      TaskDetailAndCreate

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', TaskDetailAndCreate.as_view(), name='task_detail_and_create'),
    url(r'$', TaskList.as_view(), name='task_list'),
]
