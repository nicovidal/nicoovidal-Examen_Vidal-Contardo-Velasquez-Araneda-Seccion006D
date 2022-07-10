from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home,name="index"),

    path('contactanos/', contactanos,name="contactanos"),

    path('planta/<int:id>',views.planta_detalle),
    
    path('api/', api,name="api"),

    path('crearCuenta/', crea,name="crearCuenta"),

    path('productos/', productos,name="productos"),

    path('quienesSomos/', quienes,name="quienesSomos"),

    path('envioComentario/',views.envioComentario),
    
    path('crearUsuario/',views.registroUsuario),

    path('cambiarDatos/',cambiar,name="cambiarDatos"),

    path('check_user/',views.check_user,name="check_user"),

    path('login/',logear,name="Login"),

    path('carrito/',carrito,name="carrito"),
    
    path('seguimiento/',seguimiento,name="seguimiento"),

    path('pagar/',pagar,name="pagar"),

    path('planta/',views.planta_lista),

    path('plantaData/',plantaData,name="plantaData"),

    path('compras/',compras,name="compras")

]
urlpatterns=format_suffix_patterns(urlpatterns,allowed=['json','html'])


