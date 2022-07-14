from pyexpat.errors import messages
from urllib import request
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from Kojo.Carrito import Carrito
from .models import Coments, Producto, Venta, VentaProducto, Planta,FundacionMiembro
import datetime
import random
from .serializer import PlantaSerializer, miembrosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def planta_lista(request, format=None):
    """"
    Lista de todas las plantas
    """
    if request.method == 'GET':
        plantas = Planta.objects.all()
        serializer = PlantaSerializer(plantas, many=True)
        return Response({'Plantitas': serializer.data})
    if request.method == 'POST':
        serializer = PlantaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def planta_detalle(request, id, format=None):
    try:
        planta = Planta.objects.get(pk=id)
    except Planta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlantaSerializer(planta)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlantaSerializer(planta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        planta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def home(request):
    return render(request, 'Kojo/index.html')


def plantaData(request):
    return render(request, 'Kojo/plantaData.html')


def contactanos(request):
    comentario = Coments.objects.all()
    return render(request, 'Kojo/contactanos.html', {"comentarios": comentario})


def api(request):
    return render(request, 'Kojo/api.html')


def crea(request):
    return render(request, 'Kojo/crearCuenta.html')


def carrito(request):
    return render(request, 'Kojo/carrito.html')


def compras(request):
    ventas = Venta.objects.filter(idUser = request.user).all()
    ctx={}
    if Venta.objects.filter(idUser=request.user).exists():
        ctx['compras'] = ventas 
    else:
        messages.success(request, 'No a realizado compras')
    return render(request, 'Kojo/compras.html',ctx)


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'Kojo/productos.html', {'productos': productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    messages.success(request, 'Agregado al Carrito')
    return redirect("productos")


def btn_agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("home")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("carrito")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


def quienes(request):
    return render(request, 'Kojo/quienesSomos.html')


def logear(request):
    return render(request, 'registration/login.html')


def envioComentario(request):
    if (request.method == 'POST'):
        nombre = request.POST['nombre']
        apellidos = request.POST['apellido']
        email = request.POST['email']
        comuna = request.POST['comuna']
        comentario = request.POST['comentario']

        comentario = Coments.objects.create(
            nombre=nombre, apellidos=apellidos, email=email, comuna=comuna, comentario=comentario
        )
    else:
        comentario = comentario
    return redirect('contactanos')



def pagar(request):
    if(request.method == 'POST'):
        carro = request.session["carrito"]
        if (len(carro) <= 0):
            return redirect('carrito')
        numeroOrden = random.uniform(100, 999)
        descuento = 0
        total = 0
        for produ in carro:
            total += int(carro[produ]["acumulado"])
        if carro[produ]["cantidad"] >= 15:
            descuento = 3000
            total = total-descuento

        idUsuario = request.session["_auth_user_id"]
        #print(request.session.keys())
        fechaCompra = datetime.datetime.now()
        usuario=User.objects.get(pk=idUsuario)
        #print(idUsuario)
        fechaEntrga = fechaCompra+datetime.timedelta(days=3)
        venta = Venta.objects.create(
            nmr_orden=numeroOrden,
            total=total,
            fch_compra=fechaCompra,
            fch_entrega=fechaEntrga,
            idUser=usuario,
        )
        venta.save()
        for produ in carro:
            print(carro[produ]["producto_id"])
            productoEnCarro = Producto.objects.get(
                pk=carro[produ]["producto_id"])
            detalle = VentaProducto.objects.create(
                cantidad=carro[produ]["cantidad"],
                orden=venta,
                producto=productoEnCarro,
            )
            detalle.save()
            productoEnCarro.stock -= carro[produ]["cantidad"]
            productoEnCarro.save()
        carrito = Carrito(request)
        carrito.limpiar()
        messages.success(request, 'Pagado Correctamente')
        request.session['nmr_orden'] = int(venta.nmr_orden)
    return redirect('carrito')


def registroUsuario(request):
    if (request.method == 'POST'):
        usuario = request.POST['usuario']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        contrasena = request.POST['password']
        email = request.POST['correo']

        user = User.objects.create(
            username=usuario,
            first_name=nombre,
            last_name=apellido,
            password=contrasena,
            email=email,

        )
    user.set_password(contrasena)
    user.save()
    try:
        fundaok=request.POST['fundacion']
        if fundaok == 'on':
            FundacionMiembro.objects.create(
              ID_Usuario=user,
              userName=user,
            )
    except:
        print("No se unio")
    print(request.POST)
    return redirect('crearCuenta')


def cambiar(request):
    if (request.method == 'POST'):
        
        user = User.objects.get(username=request.user)
        
        #miembro=FundacionMiembro.objects.get(ID_Usuario=request.user.id)
            #request.user.fundaEs=True
        #else:
            #request.user.fundaEs=False
        #request.miembro.ID_usuario=request.POST['user']
        #miembro.ID_usuario=request.post['user']
        
        request.user.username = request.POST['usuario']
        request.user.first_name = request.POST['nombre']
        request.user.last_name = request.POST['apellido']
        request.user.password = request.POST['password']
        request.user.email = request.POST['email']
        user.username = request.POST['usuario']
        user.first_name = request.POST['nombre']
        user.last_name = request.POST['apellido']
        user.email = request.POST['email']
        if (request.POST['password']):
            user.set_password(request.POST['password'])
        user.save()
    return render(request, 'Kojo/cambiarDatos.html')


def check_user(request):
    if request.method == "GET":
        user = request.GET["username"]
        check = User.objects.filter(username=user)
        if len(check) == 1:
            return HttpResponse("Existe")
        else:
            return HttpResponse("no existe")


def seguimiento(request):
    ctx = {}
    if request.method == 'GET':
        if 'num_pedido' in request.GET:
            num = request.GET['num_pedido']
            if Venta.objects.filter(nmr_orden=num).exists():
                orden = Venta.objects.get(nmr_orden=num)
                ctx['orden'] = orden.__dict__
    return render(request, 'kojo/seguimiento.html', ctx)


@csrf_exempt
@api_view(['GET', 'POST'])
def miembro_lista(request, format=None):
    """"
    Lista de Miembros
    """
    if request.method == 'GET':
        miembro = FundacionMiembro.objects.all()
        serializer = miembrosSerializer(miembro, many=True)
        return Response({'Miembros': serializer.data})
    if request.method == 'POST':
        serializer = miembrosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def miembro_detalle(request, id, format=None):
    try:
        miembro= FundacionMiembro.objects.get(pk=id)
    except miembro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = miembrosSerializer(miembro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlantaSerializer(miembro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        miembro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)