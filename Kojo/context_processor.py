from Kojo.models import FundacionMiembro


def total_carrito(request):
    total = 0
    descuento = 0
    descuentoMiembro=0
    totalMiembro=0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            try:
                miembro = FundacionMiembro.objects.get(ID_Usuario=request.user.id)
                descuentoMiembro=0.05
            except:
                print("usuario no es miembro")
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
            if total > 10000:
                descuento += 5000
                total = total-descuento
            if total > 20000:
                descuento += 10000
                total = total-descuento
            totalMiembro=total*descuentoMiembro
            total -= totalMiembro
    return{"total_carrito": total, "descuentos": descuento ,"descuentoMiembro":totalMiembro}
