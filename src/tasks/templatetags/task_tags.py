from django import template

register = template.Library()


@register.simple_tag
def is_solved_by(task, user):
    for solution in task.solutions.all():
        if solution.user == user and solution.status == "OK":
            return True
    return False
