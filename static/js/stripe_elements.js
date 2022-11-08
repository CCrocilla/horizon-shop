/* 
Core logic/payment comes from Code Institute(Boutique Ado Project) and Stripe Docs: 
htts:// stripe.com/docs/payments/accept-a-payment
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

const stripe = Stripe(stripePublicKey)

var elements = stripe.elements();
var card = elements.create('card');
var form = document.getElementById('payment-form');

card.mount('#card-element');

$('#submit-button').attr('disabled', true);

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.complete) {
        $('#submit-button').attr('disabled', false);
        return;
    }
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
    $('#submit-button').attr('disabled', true);
});

form.addEventListener('submit', handlerSubmit);

// Handle form submit
function handlerSubmit(event) {
    console.log('Submit Fired!!!')
    event.preventDefault();
    card.update({
        'disabled': true
    });
    activateLoading(true);
    $('#submit').attr('disabled', true);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        },

    }).then(function (result) {
        console.log('Inside Then Function: ', result)
        const urlRedirect = "https://" + window.location.hostname + "/checkout/payment/success"

        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);

            card.update({
                'disabled': false
            });
            $('#submit').attr('disabled', false);
            activateLoading(false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                var form = document.getElementById('payment-form');
                console.log('SUCCEDED')
                form.removeEventListener('submit', handlerSubmit);
                form.submit();
            }
        }
    });
}

// Show a spinner on payment submission
function activateLoading(isLoading) {
    if (isLoading) {
        // Hide the button and show a spinner
        document.getElementById("spinner").classList.remove("hidden");
        document.getElementById("button-text").classList.add("hidden");
    } else {
        document.getElementById("spinner").classList.add("hidden");
        document.getElementById("button-text").classList.remove("hidden");
    }
}