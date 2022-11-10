import stripe
import json

from django.conf import settings
from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# from checkout.webhook_handler import StripeWH_Handler

from horizon_shop.settings import STRIPE_PUBLIC_KEY
from horizon_shop.settings import STRIPE_SECRET_KEY
from horizon_shop.settings import STRIPE_WH_SECRET


@csrf_exempt
def webhook(request):
    payload = request.body

    print(payload)

    return HttpResponse(status=200)