from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hi', content_type='text/plain')
