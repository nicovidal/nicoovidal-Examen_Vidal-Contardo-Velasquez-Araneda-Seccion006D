def total_carrito(request):
    total=0
    descuento=0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key,value in request.session["carrito"].items():
                total +=int(value["acumulado"])
            if total>10000:
                descuento+=5000
                total=total-descuento
            if total>20000:
                descuento+=10000
                total=total-descuento
    return{"total_carrito":total,"descuentos":descuento}