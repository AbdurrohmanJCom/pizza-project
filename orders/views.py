from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from .models import RegularPizza, SicilianPizza, Toppings, Subs, Pasta, Salads, DinnerPlatters, ShoppingCart
from django.db.models import Sum

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    username = request.user
    context = {
        "username": request.user,
        "shopping_cart": ShoppingCart.objects.filter(username=username).all(),
        "regular_pizzas": RegularPizza.objects.all(),
        "sicilian_pizzas": SicilianPizza.objects.all(),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinner_platters": DinnerPlatters.objects.all(),
    }

    total_price = ShoppingCart.objects.aggregate(Sum('price'))['price__sum']
    if total_price:
        total = '{0:.2f}'.format(total_price)
        context["total"] = total

    return render(request, "orders/index.html", context)


def register(request):
    if request.method == "GET":
        return render(request, "orders/register.html")
    else:
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username =request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, "orders/register.html", {"message": "Username already exists!"})
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "GET":
        return render(request, "orders/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def order(request, order_name, price, toppingsList=''):
    username = request.user
    new_order = ShoppingCart(username=username, order=order_name, price=price, toppingsList=toppingsList)
    new_order.save()
    return HttpResponseRedirect(reverse("index"))


def customer_order(request):
    context = {
        "username": request.user,
        "user_order": ShoppingCart.objects.all(),
        "total": request.POST["total"]
    }
    
    return render(request, "orders/confirm.html", context)


def confirm_order(request):
    orders = ShoppingCart.objects.filter(username=request.user).all()
    for order in orders:
        order.approved = "pending"
        order.save()
    return HttpResponseRedirect(reverse("index"))


def staff(request):
    username = request.user
    context = {
        "username": username,
        "shopping_cart": ShoppingCart.objects.all()
    }
    return render(request, "orders/staff.html", context)


def approve_order(request, order_id):
    order = ShoppingCart.objects.get(pk=order_id)
    order.approved = "approved"
    order.save()
    return HttpResponseRedirect(reverse("staff"))
    
