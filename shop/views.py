from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


def index(request):
    products = Product.objects.all()
    
    # search code
    item_name = request.GET.get('item_name')  # item_name is the name attribute of <input> tag in index.html 
    if item_name != "" and item_name is not None:
        products = products.filter(title__icontains=item_name) 

    # paginator code
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    

    return render(request, 'shop/index.html', {'products': products})