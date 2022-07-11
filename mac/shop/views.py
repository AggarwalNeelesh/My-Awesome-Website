from math import ceil

from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Contacts, Orders, OrderUpdate
import json

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # if items on 1 slide is 4
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # When we were displaying only one list
    # params = {'no_of_slides': nSlides, 'range': range(1,nSlides), 'product': products}

    # Now we000 will display list category wise
    # allProds = [[products, range(1, nSlides), nSlides],
    #            [products, range(1, nSlides), nSlides]]
    # params = {'allProds': allProds}

    allProds = []
    # Category of products
    catprods = Product.objects.values('category')
    # Category's of products stored using Set Comprehension
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    # path is shop/templates/shop/index.html
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    # If Submit contact button was pressed in contacts.html
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = Contacts(name=name, email=email, phone=phone, desc=desc)
        cont.save()
        request.method = "GET"
        return render(request, 'shop/contact.html', {"submitted": True})
    # If nav bars Contact us button was pressed
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid')
        email = request.POST.get('email')
        order = Orders.objects.filter(order_id=orderid, email=email)
        print(orderid, email)
        # If list was empty i.e, order_id doesn't exist or email id didn't match
        if len(order) == 0:
            return HttpResponse('{}')

        order_update = OrderUpdate.objects.filter(order_id=orderid)
        updates = []
        for item in order_update:
            updates.append({'text': item.update_desc, 'time': item.timestamp})
        # dumps converts python object in JSON String
        response = json.dumps(updates, default=str)
        return HttpResponse(response)

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request, pr_id):
    # Fetch the product using the id
    dict1 = {}
    try:
        product = Product.objects.get(id=pr_id)
    except Product.DoesNotExist:
        pass
    else:
        dict1["product"] = product
    return render(request, 'shop/productView.html', dict1)


def checkout(request):
    # If place order button was pressed in checkout.html page
    if request.method == "POST":
        # here itemsJson is name of the input tag inside form in checkout.html
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', 'Lord')
        email = request.POST.get('email', '')
        address = request.POST.get('Address', '') + ", " + request.POST.get('Address2', '')
        city = request.POST.get('City', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('inputZip', '')
        phone = request.POST.get('inputPhone', '')
        orders = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        orders.save()
        order_id = orders.order_id

        # Creating Object for order tracking
        update = OrderUpdate(order_id=orders.order_id, update_desc="The Order has been placed Successfully")
        update.save()

        return render(request, 'shop/checkout.html', {"thanks": True, "orderid": order_id})
    # If checkout button was pressed in cart
    return render(request, 'shop/checkout.html')

