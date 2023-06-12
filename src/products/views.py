from django.shortcuts import render


def home(request):
    _context = {
        'title': 'A-Store',
        'username': 'Dmitry'
    }

    return render(request, 'products/home.html', _context)


def products(request):
    return render(request, 'products/products.html')
