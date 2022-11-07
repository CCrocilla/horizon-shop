from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle Generic Webhook Event """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_internt_succeded(self, event):
        """ Handle payment_internt_succeded Webhook Event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_internt_failed(self, event):
        """ Handle payment_internt_failed Webhook Event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )