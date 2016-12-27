from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import resolve_url, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from .models import Solution


class SolutionStatuses(View):
    def get(self, request):
        ids = request.GET.get('ids')
        if ids is None:
            return HttpResponse()
        ids = ids.split(',')
        solutions = dict(Solution.objects.filter(id__in=ids).values_list('id', 'status'))
        return JsonResponse(solutions)


class SolutionCreate(CreateView):
    model = Solution
    fields = ['code', 'task']

    def get_success_url(self):
        self.object.run_tests()
        return resolve_url('tasks:task_detail', pk=self.object.task.id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SolutionCreate, self).form_valid(form)


class SolutionRunView(View):
    def dispatch(self, request, pk=None, *args, **kwargs):
        self.solution = get_object_or_404(Solution, pk=pk)
        return super(SolutionRunView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        self.solution.run_tests()
        return HttpResponse(self.solution.status)


class SolutionDetailView(DetailView):
    model = Solution
    template_name = "solutions/solution_detail.html"
