from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('about/',AboutView,name='about'),
    path('blog/',BlogView,name='blog'),
    path('blog-single/<int:pk>/',BlogSingle,name='blog-single'),
    path('cart/',CartView,name='cart'),
    path('checkout/',CheckoutView,name='checkout'),
    path('contact/',ContactView,name='contact'),
    path('product-single/<int:pk>/',ProductSingle,name='product-single'),
    path('profile/',ProfileView,name='profile'),
    path('service/',ServiceView,name='service'),
    path('shop/',ShopView,name='shop'),
    path('add-contact',AddContact,name='add-contact'),
    path('registration/',Registration,name='registration'),
    path('login/',LoginPage,name='login'),
    path('logout/',Logout,name='logout'),
    path('add-card/<int:pk>/',AddCard,name='add-card'),
    path('delete-card/<int:pk>/',DeleteCard,name='delete-card'),
    path('add-order/',AddOrder,name='add-order'),
    path('add-wishlist/<int:pk>/',AddWishlist,name='add-wishlist'),
    path('wishlist/',WishlistView,name='wishlist'),
    path('delete-wishlist/<int:pk>/', DeleteWishlist, name='delete-wishlist'),
    path('search/',SearchProduct,name='search-product'),
    path('searchpage/', SearchView, name='search'),
    path('category/<int:pk>/',CategoryView,name='category'),
    path('change-profile/',ChangeProfile,name='change-profile'),
    path('add-subscribe/',FuncSubscribe,name='add-subscribe'),
    path('search-blog/',SearchBlog,name='search-blog')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






