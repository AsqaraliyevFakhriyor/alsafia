from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect

from myshop.models.likes import Likes
from myshop.models.products import Products
from myshop.models.categories import Categories

from myshop.utils import send_message

def loginView(request) -> None:
    return render(request, 'myshop/my-account.html')


def homeView(request) -> object:
    categories = Categories.objects.all()
    day_recommends = Products.objects.filter(
        category=Categories.KUN_TAKLIFLARI)  # kunning eng yaxhi takliflari
    best_seller = Products.objects.filter(
        category=Categories.ENG_KOP_SOTILADIGAN)  # eng ko'p sotiladigan
    the_most_popular = Products.objects.filter(
        category=Categories.ENG_MASHHUR_MAHSULOTLAR)[:4]  # eng mashhur mahsulotlar
    _all_products = Products.objects.all() # all products
    
    context = {
        "best_seller": best_seller,
        "day_recommends": day_recommends,
        "the_most_popular": the_most_popular,
        "categories": categories,
        "all_products": _all_products
    }

    return render(request, 'myshop/index.html', context)


def aboutView(request):
    return render(request, 'myshop/about.html')


def shopView(request):
    return render(request, 'myshop/shop.html')


def shopDetailView(request, id):
    return render(request, 'myshop/shop-detail.html')


def myWishlistView(request):
    return render(request, 'myshop/wishlist.html')


def myCardView(request):
    return render(request, 'myshop/cart.html')


def contactView(request):
    return render(request, 'myshop/contact.html')


def faqView(request):
    return render(request, 'myshop/faq.html')


def categoryView(request, id: int) -> object:    
    if id == 0:
        products = Products.objects.all()
        
    if id > 0:
        products = Products.objects.filter(category_id=id)

    context: dict = {
        "products": products
    }

    return render(request, 'myshop/by_category.html', context)


def sendMessageView(request) -> None:
    if request.method == 'POST':
        mydict: dict = {}
        product_id = request.META['HTTP_REFERER'][29:-1]
        mydict.update({
            "name": request.POST.get('name'),
            "phone": request.POST.get('phone'),
            "product_id": product_id
        })
        send_message(mydict)
        return redirect('shop-detail', product_id)


def likeView(request, id: int) -> None:
    item, _ = Likes.objects.get_or_create(products_id=id, user=request.user)
    if item.liked:
        item.isFalse()
    
    if not item.liked:
        item.isTrue()
    
    return redirect('category', request.META['HTTP_REFERER'][34:-1])