from django.http import HttpResponse


def index(request):
    return HttpResponse('Main Page')

def group_posts(request, slug):
    return HttpResponse('Grouped Posts')