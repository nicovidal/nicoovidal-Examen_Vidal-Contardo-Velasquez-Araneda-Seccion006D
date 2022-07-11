from django.contrib import admin
from .models import Coments,Producto,Venta,VentaProducto,Planta,FundacionMiembro
# Register your models here.

admin.site.register(Coments)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(VentaProducto)
admin.site.register(Planta)
admin.site.register(FundacionMiembro)
