from django.shortcuts import render, redirect
from Phone.models import Phone


def index(request):
    return redirect('show_catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'min_price':
        phones = phones.order_by('price')
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')

    context = {'phones': phones}
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
