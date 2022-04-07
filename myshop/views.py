from django.shortcuts import render
from .models import Categories, Product, SliderImage


def loginView(request):
    
    return render(request, 'myshop/my-account.html')


def homeView(request):
    categories = Categories.objects.all()
    product = Product.objects.all().first
    slider_images = SliderImage.objects.all()[:3] #slider image
    image1 = Product.objects.filter(category=13) #image1 
    topsell = Product.objects.filter(category=1) #kunning eng yaxshi takliflari
    product = Product.objects.filter(category=2).first() # eng mashhur mahsulotlar birinchsi
    products = Product.objects.filter(category=11)
    all_products = Product.objects.all()[:6]
    recommand_products = Product.objects.filter(category=12) #siz uchun tavfsiya
    
    context = {
        "slider_images": slider_images,
        "categories": categories,
        "product": product,
        "image1": image1,
        "topsell": topsell,
        "product": product,
        "products": products,
        "all_products": all_products,
        "recommand_products": recommand_products 
    }
    
    return render(request, 'myshop/index.html', context)


def aboutView(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }
    
    return render(request, 'myshop/about.html', context)


def shopView(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }
     
    return render(request, 'myshop/shop.html', context)


def myWishlistView(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }
    
    return render(request, 'myshop/wishlist.html', context)


def myCardView(request):
    categories = Categories.objects.all()
    context = {
        "categories": categories
    }

    return render(request, 'myshop/cart.html', context)