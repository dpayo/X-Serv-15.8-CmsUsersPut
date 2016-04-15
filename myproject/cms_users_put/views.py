
from django.shortcuts import render
from models import Table
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.


def analyze (request,recurso):

    salida =""
    if request.method == 'GET':
        if request.user.is_authenticated():
            salida += "You're inside " + request.user.username + "!"
            salida += "<a href='/logout/'>Logout</a><br>"
            try:
                record = Table.objects.get(resource=recurso)
                return HttpResponse(record.name)
            except Table.DoesNotExist:

                lista=Table.objects.all()
                for fila in lista:
                    salida += "<ul><li> Recurso: "+str(fila.resource)+"\r"+str(fila.name)+"</li></ul>"
                return HttpResponse('<br>Recursos: '+salida)
        else:
            return HttpResponse("Not logged in"+"<a href=http://"+request.get_host()+"/login/"+"> Log in</a>")
    elif request.method == 'PUT':
        print str(request.user.is_authenticated())
        if request.user.is_authenticated():
            record = Table(resource= recurso,name =request.body)
            record.save()
            return HttpResponse("<h1><p>Logged in as "  + request.user.username+"</p>Actualizando.../h1>"+ str(recurso)+"......"+str(request.body))

        else:
            return HttpResponse("Not logged in"+"<a href=http://"+request.get_host()+"/admin/login/"+"> Log in</a>")
