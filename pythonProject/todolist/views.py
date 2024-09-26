from django.http import HttpResponse

def index(request):
    return HttpResponse("Am i working?")
