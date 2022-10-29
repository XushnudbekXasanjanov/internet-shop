from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='home/')


class HomeAboutService(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class HomeAbout(models.Model):
    title = models.CharField(max_length=255)
    minititle = models.CharField(max_length=255)
    text = models.TextField()

class ProductCategories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class IndexBlog(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Product(models.Model):
    img = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    price = models.IntegerField()
    bonus = models.IntegerField(default=0)
    rating = models.IntegerField()
    category = models.ForeignKey(ProductCategories,on_delete=models.CASCADE)
    productservice = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class About(models.Model):
    img = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255)
    text = models.TextField()

class AboutMembers(models.Model):
    years = models.IntegerField()
    happycustomers = models.IntegerField()
    products  = models.IntegerField()
    purity = models.IntegerField()

class AboutExperts(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='experts/')
    job = models.CharField(max_length=255)
    about = models.TextField()

class Services(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='services/')

class MiniServices(models.Model):
    miniservicetitle = models.CharField(max_length=255)
    miniservicetext = models.TextField()

class ServicePlan(models.Model):
    basicprice = models.IntegerField()
    standardprice = models.IntegerField()
    premiumprice = models.IntegerField()
    basictext = models.CharField(max_length=255)
    standardtext = models.CharField(max_length=255)
    premiumtext = models.CharField(max_length=255)

class Blog(models.Model):
    firstname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    img = models.ImageField(upload_to='blog/')

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    adress = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    price = models.IntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()


class Profile(models.Model):
    mobile = models.IntegerField()
    adress = models.CharField(max_length=255)
    shipping = models.CharField(max_length=255)
    text = models.TextField()

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Subscribe(models.Model):
    name = models.CharField(max_length=255)

