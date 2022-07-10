from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Coments(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    comentario = models.CharField(max_length=999)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True, verbose_name="ID producto")
    nombreProducto=models.CharField(max_length=255,verbose_name="Nombre Producto")
    stock=models.IntegerField(verbose_name="Stock")
    imagen=models.ImageField(upload_to='productoImagen',null=True,blank=True)
    precio=models.IntegerField()

    def __str__(self):
        return self.nombreProducto



class Venta(models.Model):
    nmr_orden = models.BigIntegerField()
    total = models.IntegerField()
    fch_compra = models.CharField(max_length=40)
    fch_entrega = models.CharField(max_length=40,blank=True, null=True)
    idUser=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nmr_orden)


class VentaProducto(models.Model):
    cantidad=models.IntegerField()
    orden=models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cantidad)

class Planta (models.Model):
    
    nombrePlanta=models.CharField(max_length=255,verbose_name="Nombre planta")
    imagenPlanta=models.ImageField(upload_to='productoImagen',null=True,blank=True)
    nombreCientifico=models.CharField(max_length=255,verbose_name="Nombre cientifico")
    ubicacion=models.CharField(max_length=255,verbose_name="Ubicacion de la plata")
    descripcion=models.CharField(max_length=255,verbose_name="Descripcion")
    

    def __str__(self):
        return self.nombrePlanta
