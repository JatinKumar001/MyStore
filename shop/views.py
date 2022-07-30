from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Product, Contact, Orders
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from math import ceil

n = []
name1 = ""
address1 = ""
email1 = ""
def search_item(request):
    if request.method == "POST":
        searched = request.POST['searched']
        if searched == 'fashion':                # use or function to make it more specific and change its category.
            allprod = []
            catprod = Product.objects.values('category', 'id')
            cats = {i['category'] for i in catprod}
            for cat in cats:
                if (cat == searched):
                    prod = Product.objects.filter(category=cat)
                    allprod.append(prod)
            return render(request, "store/men-fashion.html", {'searched':searched, 'allprod':allprod})
        else:
            allprod = []
            catprod = Product.objects.values('category', 'id')
            cats = {i['category'] for i in catprod}
            for cat in cats:
                if (cat == searched):
                    prod = Product.objects.filter(category=cat)
                    allprod.append(prod)
            return render(request, "store/phone.html", {'searched':searched, 'allprod':allprod})

    else:
        return render(request, "store/index.html")


def index(request):
    allprod = []
    phprod = []
    catprod = Product.objects.values('category', 'id')
    cats = {i['category'] for i in catprod}
    for cat in cats:
        if (cat == 'fashion'):
            prod = Product.objects.filter(category=cat)
            allprod.append(prod)
        if(cat == 'phone'):
            pprod = Product.objects.filter(category=cat)
            phprod.append(pprod)
    params = {'allprod': allprod, 'phprod': phprod, 'fname':n}
    return render(request, "store/index.html", params)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'store/contact.html')

# def fashion(request):
#     allprod = []
#     catprod = Product.objects.values('category', 'id')
#     cats = {i['category'] for i in catprod}
#     for cat in cats:
#         if (cat == 'fashion'):
#             prod = Product.objects.filter(category=cat)
#             allprod.append(prod)
#     params = {'allprod': allprod}
#     return render(request, "store/men-fashion.html", params)

# def phone(request):
#     allprod = []
#     catprod = Product.objects.values('category', 'id')
#     cats = {i['category'] for i in catprod}
#     for cat in cats:
#         if (cat == 'phone'):
#             prod = Product.objects.filter(category=cat)
#             allprod.append(prod)
#     params = {'allprod': allprod}
#     return render(request, "store/phone.html", params)

def individual(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "store/individual-page.html", {'product':product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST['itemsJson']
        name = name1
        email = email1
        order = Orders(items_json=items_json, name=1)
        order.save()
        thank = True
        id = order.order_id
        return render(request, "store/checkout.html",{'thank':thank, 'id': id})
    return render(request, "store/checkout.html")

def sign(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['emailid']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        # name1 += username
        # email1 += email
        messages.success(request, "Your Account has been successfully created.")

        # return render(request, "store/sign.html")
        redirect("/signin")
        # return redirect('contact')

    return render(request, "store/sign.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            n.append(user.first_name)
            # return render(request, "store/index.html", {"fname":fname})
            return redirect("/")
        else:
            messages.error(request, "Check your detail once again!")
            return redirect("/")

    return render(request, "store/sign.html")
    # return redirect("/")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("/")