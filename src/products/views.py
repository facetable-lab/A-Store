from django.shortcuts import render


def home(_request):
    _context = {
        'title': 'A-Store',
    }

    return render(request=_request, template_name='products/home.html', context=_context)


def products(_request):
    return render(request=_request, template_name='products/products.html')
