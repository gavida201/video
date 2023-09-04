from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola este es un sesponse")

def dia_de_hoy(request):
    import datetime
    
    dia = datetime.datetime.now()
    documentoDeTexto = f'hoy es el día {dia}'
    
    return HttpResponse(documentoDeTexto)

def mi_nombre_es(request,nombre):
    documentoDeTexto=f"hola mi nombre es {nombre}"
    return HttpResponse(documentoDeTexto)

def probando_template(request):
    nombre = "luis"
    apellido = "juez"
    
    diccionario = {"nombre": nombre, "apellido": apellido}
    
    mi_html = open("C:/Users/Usuario/Desktop/video/repaso/repaso/template1.html", "r")
    
    plantilla = Template(mi_html.read())
    
    mi_html.close()
    
    mi_contexto = Context(diccionario)
    
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)
    
    