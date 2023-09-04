from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola este es un sesponse")

