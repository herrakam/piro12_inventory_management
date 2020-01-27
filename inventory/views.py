from django.forms import forms
from django.shortcuts import render, redirect
from .forms import productform
def stock_list(request):
    return render(request, 'inventory/stock_list.html',)

def create_product(request):
    if request.method == 'POST':
        form = productform(request.POST,request.FILES)
        if form.is_valid():
            Product = forms.save()
            return redirect(Product)
        else:
            pass
    else:
        form = productform()
    return render(request, 'inventory/create_product.html',{'form':form})


def create_client(request):
    return render(request, 'inventory/create_client.html')