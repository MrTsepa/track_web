from django.conf.urls import url
from views import TaskList, TaskDetailAndCreate, TaskDetailAceEditorView

urlpatterns = [
    # url(r'^(?P<pk>[0-9]+)$', TaskDetailAndCreate.as_view(), name='task_detail_and_create'),
    url(r'^(?P<pk>[0-9]+)$', TaskDetailAceEditorView.as_view(), name='task_detail_ace_editor'),
    url(r'$', TaskList.as_view(), name='task_list'),
]
