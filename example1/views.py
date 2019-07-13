from django.http import HttpResponse


def helloview(request):
    return HttpResponse("Hello Mahesh")