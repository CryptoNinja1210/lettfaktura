from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse,HttpResponse

# Create Employee

def insert_pro(request):
    if request.method == "POST":
        Name    = request.POST['name']
        InPrice = request.POST['inPrice']
        Price   = request.POST['price']
        Stock   = request.POST['stock']
        Desc    = request.POST['desc']
        data    = Product(name=Name, inPrice=InPrice, price=Price, stock=Stock, desc=Desc)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')
    
def show_pro(request):
    products    = Product.objects.all()
    data = serialize("json", products, fields=('name', 'inPrice', 'price', 'stock', 'desc'))
    return HttpResponse(data, content_type="application/json")
    # return JsonResponse(products, safe=False)
    # return render(request,'show.html',{'products':products} )

def edit_pro(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST)
        product.name    = request.POST['name']
        product.inPrice = request.POST['inPrice']
        product.price   = request.POST['price']
        product.stock   = request.POST['stock']
        product.desc    = request.POST['desc']
        product.save()   
        return redirect('/show')
    context = {
        'product': product,
    }

    return render(request,'edit.html',context)

def remove_pro(request, pk):
    products = Product.objects.get(id=pk)

    if request.method == 'POST':
        products.delete()
        return redirect('/show')

    context = {
        'products': products,
    }

    return render(request, 'delete.html', context)
