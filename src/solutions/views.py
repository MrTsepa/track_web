from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Solution


class SolutionCreate(CreateView):
    model = Solution
    fields = ['code', 'task']

    def get_success_url(self):
        return resolve_url('tasks:task_detail', pk=self.object.task.id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SolutionCreate, self).form_valid(form)


class CodeDetailView(DetailView):
    model = Solution
    template_name = "solutions/code_detail.html"

    def dispatch(self, request, pk=None, *args, **kwargs):
        get_object_or_404(Solution, id=pk).run_tests()
        return super(CodeDetailView, self).dispatch(request, *args, **kwargs)
