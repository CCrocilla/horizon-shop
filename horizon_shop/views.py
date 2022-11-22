from django.shortcuts import render


def ErrorPage404(request, exception):
    """ Function to display the Error Page 404 - Page Not Found """
    return render(request, "404.html", status=404)
