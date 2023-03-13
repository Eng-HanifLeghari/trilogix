from django.shortcuts import render


def trilogix_website(request):
    return render(request, 'trilogix/index.html')
