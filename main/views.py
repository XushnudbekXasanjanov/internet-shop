from django.shortcuts import render,redirect
from .models import *

def Index(request):
    user = request.user
    context = {
        'home':Home.objects.last(),
        'homeabout':HomeAbout.objects.last(),
        'homeservice':HomeAboutService.objects.all()[:6],
        'products': Product.objects.all().order_by('-id'),
        'member': AboutMembers.objects.last(),
        'expert': AboutExperts.objects.all(),
        'blog':Blog.objects.all()
    }
    return render(request,'index.html',context)

def AboutView(request):
    context = {
        'about':About.objects.last(),
        'member':AboutMembers.objects.last(),
        'expert':AboutExperts.objects.all()[:4]
    }
    return render(request,'about.html',context)

def BlogView(request):
    context = {
        'blog':Blog.objects.all().order_by('-date'),
        'products':Product.objects.all(),
        'categorys': ProductCategories.objects.all()
    }
    return render(request,'blog.html',context)

def BlogSingle(request,pk):
    context = {
        'blog':Blog.objects.get(id=pk),
        'blogs':Blog.objects.all().order_by('-date'),
        'categorys': ProductCategories.objects.all()
    }
    return render(request,'blog-single.html',context)

def CartView(request):
    user = request.user
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
    context = {
        "total": total,
        "card": card,

    }
    return render(request, 'cart.html', context)

def CheckoutView(request):
    user = request.user
    total = 0
    if user.is_anonymous:
        pass
    else:
        card = Card.objects.filter(user=user)
        for i in card:
            if i.product.bonus > 0:
                total += i.product.bonus
            else:
                total += i.product.price
        context = {
            "total": total,
            'card': card
            }
        return render(request,'checkout.html',context)

def ContactView(request):
    return render(request,'contact.html')

def AddContact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return redirect('contact')

def ProductSingle(request,pk):
    context = {
        'product':Product.objects.get(id=pk),
        'products':Product.objects.all()
    }
    return render(request,'product-single.html',context)

def ProfileView(request):
    user = request.user
    context = {
    'profile':Profile.objects.last()
    }
    return render(request,'profile.html',context)

def ServiceView(request):
    context = {
        'service':Services.objects.last(),
        'miniservice':MiniServices.objects.all()[:4],
        'plan':ServicePlan.objects.last()
    }
    return render(request,'service.html',context)

def ShopView(request):
    context = {
        'products':Product.objects.all().order_by('-id'),
        'categorys': ProductCategories.objects.all()
    }
    return render(request,'shop.html',context)

from django.contrib.auth import login, logout, authenticate

def Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('index')
    return render(request,'index.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                    login(request,usr)
                    return redirect('index')
            else:
                return redirect('registration')
        else:
            return redirect('registration')
    return redirect('index')

def Logout(request):
    logout(request)
    return redirect('index')

def AddCard(request,pk):
    user = request.user
    product = Product.objects.get(id=pk)
    Card.objects.create(user=user,product=product)
    return redirect('index')

def DeleteCard(request,pk):
    Card.objects.get(id=pk).delete()
    return redirect('cart')

def AddOrder(request):
    if request.method == "POST":
        user_id = request.POST.get('user')
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        mobile = request.POST.get('mobile')
        state =request.POST.get('state')
        city =request.POST.get('city')
        user = User.objects.get(id=user_id)
        order = Order.objects.create(
            user=user,
            name=name,
            adress=adress,
            mobile=mobile,
            state=state,
            city=city,
            price=0
        )
        total_price = 0
        for i in Card.objects.filter(user=user):
            OrderItem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price
            )
            total_price += i.product.price
            order.price = total_price
            order.save()
            for i in Card.objects.filter(user=user):
                i.delete()
            return redirect('index')
    return redirect('checkout')

def AddWishlist(request,pk):
    user = request.user
    product = Product.objects.get(id=pk)
    Wishlist.objects.create(user=user,product=product)
    return redirect('index')

def WishlistView(request):
    user = request.user
    if user.is_anonymous:
        pass
    else:
        wishlist = Wishlist.objects.filter(user=user)
    context = {
        'wishlist':wishlist
    }
    return render(request,'wishlist.html',context)

def DeleteWishlist(request,pk):
    Wishlist.objects.get(id=pk).delete()
    return redirect('wishlist')

def SearchView(request):
    return render(request,'search.html')

def SearchProduct(request):
    if request.method == 'POST':
              name = request.POST.get('name')
              context = {
                'search': Product.objects.filter(title__icontains=name)
                }
              return render(request, 'search.html', context)
    return redirect('shop')

def SearchBlog(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            context = {
                'search':Blog.objects.filter(title__icontains=name)
            }
            return render(request,'search.html',context)
    return redirect('blog')

def CategoryView(request,pk):
    context = {
        'categorys': ProductCategories.objects.all(),
        'product':Product.objects.filter(category_id=pk),
        'products': Product.objects.all().order_by('-id'),
    }
    return render(request,'category.html',context)

def ChangeProfile(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get('mobile')
        adress = request.POST.get('adress')
        shipping = request.POST.get('shipping')
        text = request.POST.get('text')
        user.username = name
        user.email = email
        user.save()
        Profile.objects.create(mobile=mobile, adress=adress, shipping=shipping, text=text)
        context = {
            "user": user,
        }
        return render(request, "profile.html",context)
    return redirect("index")

def FuncSubscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Subscribe.objects.create(name=name)
    return redirect('index')