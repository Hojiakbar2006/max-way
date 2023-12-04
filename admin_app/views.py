# from . import services
# from . import forms
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def login_required_decorator(func):
    return login_required(func, login_url='login_page')

def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, 'admin/login.html')


@login_required_decorator
def home_page(request):
    return render(request, 'admin/main/index.html')


@login_required_decorator
def main_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    user = User.objects.all()
    orders = Order.objects.all()

    ctx = {
        "counts": {
            "products": len(products),
            "users": len(user),
            "categories": len(categories),
            "orders": len(orders),

        },

    }
    return render(request, 'admin/main/index.html', ctx)


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def product_list(request):
    products = Product.objects.all()
    
    ctx = {
        'products': products
    }
    return render(request, "admin/product/index.html", ctx)


@login_required_decorator
def order_list(request):
    orders = Order.objects.all()

    ctx = {
        'orders': orders
    }
    return render(request, "admin/order/index.html", ctx)


@login_required_decorator
def users_list(request):
    users = User.objects.all()

    ctx = {
        'users': users
    }
    return render(request, "admin/user/index.html", ctx)


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()

    ctx = {
        'categories': categories
    }
    return render(request, "admin/category/index.html", ctx)


# @login_required_decarator
# def user_list(request):
#     users = Customer.objects.all()
#     ctx = {
#         'users': users
#     }
#     return render(request, "dashboard/user/list.html", ctx)\



# @login_required_decarator
# def order_list(request):
#     orders = Order.objects.all()
#     ctx = {
#         'orders': orders
#     }
#     return render(request, "dashboard/order/list.html", ctx)


# @login_required_decarator
# def user_create(request):
#     model = Customer()
#     form = forms.UserForm(request.POST or None, instance=model)

#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('user_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/user/form.html', ctx)


# @login_required_decarator
# def user_edit(request, pk):
#     model = Customer.objects.get(pk=pk)
#     form = forms.UserForm(request.POST or None, instance=model)

#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('user_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/user/form.html', ctx)


# @login_required_decarator
# def user_delete(request, pk):
#     model = Customer.objects.get(pk=pk)
#     model.delete()
#     return redirect("category_list")


# @login_required_decarator
# def category_create(request):
#     """This is the metod for creating product categories: Pizzas, Burgers..."""
#     model = Category()
#     form = forms.CategoryForm(request.POST or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()  # form is saved
#         return redirect('category_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/category/form.html', ctx)


# @login_required_decarator
# def category_edit(request, pk):
#     model = Category.objects.get(pk=pk)
#     form = forms.CategoryForm(request.POST or None, instance=model)

#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('category_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/category/form.html', ctx)


# @login_required_decarator
# def category_delete(request, pk):
#     model = Category.objects.get(pk=pk)
#     model.delete()
#     return redirect("category_list")
# ############# product#########################################


# @login_required_decarator
# def product_list(request):
#     products = Product.objects.all()
#     ctx = {
#         'products': products
#     }
#     return render(request, "dashboard/product/list.html", ctx)


# @login_required_decarator
# def product_create(request):
#     model = Product()
#     form = forms.ProductForm(request.POST or None,
#                              request.FILES or None, instance=model)

#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('product_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/product/form.html', ctx)


# @login_required_decarator
# def product_edit(request, pk):
#     model = Product.objects.get(pk=pk)
#     form = forms.ProductForm(request.POST or None,
#                              request.FILES or None, instance=model)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('product_list')
#     ctx = {
#         'model': model,
#         'form': form
#     }
#     return render(request, 'dashboard/product/form.html', ctx)


# @login_required_decarator
# def product_delete(request, pk):
#     model = Product.objects.get(pk=pk)
#     model.delete()
#     return redirect("product_list")


# @login_required_decarator
# def customer_order_list(request, id):
#     customer_orders = services.get_order_by_user(id=id)
#     ctx = {
#         'customer_orders': customer_orders
#     }
#     return render(request, "dashboard/customer_order/list.html", ctx)


# @login_required_decarator
# def orderproduct_list(request, id):
#     productorders = services.get_product_by_order(id=id)
#     ctx = {
#         'productorders': productorders
#     }
#     return render(request, "dashboard/productorder/list.html", ctx)
