from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from posts.models import Post
from django.utils import timezone


def all_products(request):
    products = Product.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "products.html", {"products": products, 'posts': posts})
    
def all_products2(request):
    products = Product.objects.all()
    return render(request, "allproducts.html", {"products": products})
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.save()
    return render(request, "productdetail.html", {'product': product})
    
def get_posts2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "products.html", {'posts': posts})