from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting_param = request.GET.get('sort')
    if sorting_param == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sorting_param == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sorting_param == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all().order_by('id')
    phones = [phone for phone in phone_objects]
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = [phone for phone in Phone.objects.all() if phone.slug == slug]
    context = {'phone': phone[0]}
    return render(request, template, context)
