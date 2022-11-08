from .models import Wishlist


def wishlist_contents(request):

    counter_wish_products = 0

    if request.user.is_authenticated:
        counter_wish_products = Wishlist.objects.filter(
            user=request.user).count()

    context = {
            'counter_wish_products': counter_wish_products,
        }

    return context
