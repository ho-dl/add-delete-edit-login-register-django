from django.shortcuts import render,redirect ,get_object_or_404

from .models import *
from app_home.forms import PersonForm
from .models import Product
from django.contrib import messages


# Create your views here.


def index(request):
    people = Person.objects.all()
    return render(request,'index.html',{'people':people})



def addperson(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    return render(request,'addperson.html',{'form':form})




def person_view(request,person_id):
    person =Person.objects.get(id=person_id)
    return render(request,'person_view.html',{'person':person})



def person_delete(request,person_id):
    person =Person.objects.get(id=person_id)
    person.delete()
    return redirect('index')


def person_edit(request,person_id):
    person= Person.objects.get(id=person_id)
    form = PersonForm(instance=person)

    if request.method =='POST':
        form = PersonForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'person_edit.html',{'form':form})


def product_add(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        address =request.POST.get('address')

        product = Product(

            name = name,
            address = address,
            phone = phone,
            email = email,
        )
        product.save()
        messages.success(request,f"{product.name} added successfully")

        return redirect('index')
    
    return render(request,'product_add.html',)




def product_view(request):
    products = Product.objects.filter(name='muhsy')
    return render(request, 'product_view.html', {'products': products})




# view product by id

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

# product eddit by id


def product_edit(request,product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        product.name=name
        product.email=email
        product.phone=phone
        product.address=address
        product.save()
        
        return redirect('product_view')
    return render(request,'product_edit.html',{'product':product})
