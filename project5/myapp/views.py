from django.shortcuts import render,HttpResponseRedirect
from.models import Django_sagar,Cart,Order,Address
from.forms import django_form,Signup_Form,AddressForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def home(request):
    a = Django_sagar.objects.all()

    return render(request,'index.html',{'data':a})

def data(request):
    if request.method == "POST":
        fm =django_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/main/home/')

    else:
        fm = django_form()
    return render(request,'Data_enter.html',{'form':fm})


def update(request,id):
    if request.method == "POST":
        pi = Django_sagar.objects.get(pk=id)
        fm = django_form(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/main/home')

    else:
        pi = Django_sagar.objects.get(pk=id)
        fm = django_form(instance=pi)
    return render(request,'update.html',{'form':fm})


def delete(request,id):
    if request.method == "POST":
        pi = Django_sagar.objects.get(pk=id)
        pi.delete() 
        return HttpResponseRedirect('/main/home')


def cart(request):
    if request.user.is_authenticated:
        print(request.user)
        a = Django_sagar.objects.all()
       
       
        cart1 = Cart.objects.filter(user=request.user)
        count = cart1.count()
        uname = request.user
        b = Address.objects.filter(user=request.user).values_list('id',flat=True)
        print(b)
    
        return render(request,'cart.html',{'data':a, 'cartcount':count,'uname':uname,'add_id':b})
    else:
        return HttpResponseRedirect('/main/login')


def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('Cid')
            print(cid)
            item,store = Cart.objects.get_or_create(Django_sagar_id=cid,user=request.user)
            print(item,store)
            if not store:
                item.quantity += 1
                item.save()
            return HttpResponseRedirect('/main/cart')
    
def cart_increase(request):
     if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            print(cid)
            item,store = Cart.objects.get_or_create(Django_sagar_id=cid)
            print(item,store)
            if not store:
                item.quantity += 1
                item.save()
            return HttpResponseRedirect('/main/viewscart/')

    
def cart_decrease(request):
     if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
        
            item,store = Cart.objects.get_or_create(Django_sagar_id=cid)
            print(item,store)
            if not store:
                item.quantity -= 1
                item.save()
                if item.quantity <1:
                    item.delete()


                    return HttpResponseRedirect('/main/viewscart/')


def view_cart(request):
    if request.user.is_authenticated:

        # cart1 = Cart.objects.all().values_list('Django_sagar_id',flat=True)
        # cartdata = Django_sagar.objects.filter(id__in=cart1)    s
        # print(cart1)

        cart1 = Cart.objects.filter(user=request.user).values_list('Django_sagar_id',flat=True)
        cartdata = Django_sagar.objects.filter(id__in=cart1)
        print(cart1)
        print(request.user)
        quantity = Cart.objects.all


        quantity = Cart.objects.all()
        return render(request,'showscart.html',{ 'data':cartdata, 'quantity':quantity})

def remove_cart(request,id):
        if request.method =='GET' :
            os = Cart.objects.filter(Django_sagar_id=id)
            os.delete()
            return HttpResponseRedirect('/main/viewscart/')
        
def SignUp(request):
    if request.method == "POST":
        fm = Signup_Form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Signup_Form()
    return render(request,'signup.html',{'form':fm})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/main/cart/')

    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/main/login')

def Order_Place(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get('pid')
            cart_id = request.POST.get('cid')
            address_id = request.POST.get('aid')
            print(product_id)
            Order.objects.create(user=request.user,Django_sagar_id=product_id,Cart_id=cart_id,address_id=address_id)
            return HttpResponseRedirect('/main/ordermessage/')
        
def view_order(request):
    order = Order.objects.all().values_list('Django_sagar_id',flat=True)
    data = Django_sagar.objects.filter(id__in=order)
    return render(request,'view_order.html',{'data':data})
        
def Order_message(request):
    return render(request,'order_message.html')


#imprting address Form

def Address1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            state = request.POST.get('state')
            Address.objects.create(city=city,pincode=pincode,state=state,user=request.user)
            
        os = Address.objects.filter(user_id=request.user)
        return render(request,'address.html',{'data':os})
    else:
        return HttpResponseRedirect('main/login')
