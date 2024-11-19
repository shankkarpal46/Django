from .models import Cart
def cart_context_processor(request):
    cartid = request.session.get("cart_id")
    count = 0
    if cartid is not None:
        cart = Cart.objects.get(id = cartid)
        cart.cartitem_set.all()
        count = cart.cartitem_set.all().count()
    return {"count":count}