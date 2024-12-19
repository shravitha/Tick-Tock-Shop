# from django.shortcuts import render, redirect, get_object_or_404

# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from .models import Watches, WatchesUploads, Wishlist, Cart,WatchReview
# from .forms import UploadForm
# from .models import CartItem
# from django.http import JsonResponse

# def home(request):
#     watches = WatchesUploads.objects.all()
#     context = {'watches_t': watches}
#     return render(request, "home.html", context)

# def about(request):
#     return render(request, "about.html")

# # @login_required(login_url="login")
# # def upload(request):
# #     if request.method == 'POST':
# #         form = UploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('home')
# #     else:
# #         form = UploadForm()
# #     return render(request, "WatchUpload.html", {'form': form})

# @login_required(login_url="login")
# def upload(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Ensure 'home' is a valid URL name
#     else:
#         form = UploadForm()

#     return render(request, "WatchUpload.html", {'form': form})

# from django.views import View
# from django.utils.decorators import method_decorator
# class uploadClass(View):
#     def get(request):
#         form=UploadForm()
#         return render(request,"WatchUpload.html",{'form':form})
    
#     @method_decorator(login_required)
#     def post(request):
#         form=UploadForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         return render(request,"WatchUpload.html",{'form':form})
# def login_page(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return render(request,"login.html",{'form':form})
              
#     else:
#         form = AuthenticationForm()
#     return render(request, "login.html", {'form': form})

# def signup_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, "signup.html", {'form': form})

# def logout_user(request):
#     logout(request)
#     return redirect('home')

# def show_product(request, id):
#     product = get_object_or_404(WatchesUploads, id=id)
#     reviews_obj=WatchReview.objects.filter(product=product)
#     return render(request, "product.html", {"product": product,"review":reviews_obj})

# # @login_required(login_url="login")
# def addtowish(request, id):
#     user = request.user
#     product = WatchesUploads.objects.get(id=id)
#     obj1, created = Wishlist.objects.get_or_create(user=user)
#     obj1.products.add(product)
#     obj1.save()
#     return redirect('home')

# # @login_required(login_url="login")
# def addtocart(request, id):
    
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     product = WatchesUploads.objects.get(id=id)
#     cart_item,created=CartItem.objects.get_or_create(user=user_cart,product=product)
#     cart_item.product=product

    
#     return redirect('home')

# # @login_required(login_url="login")
# def show_wishlist(request):
#     user = request.user
#     wish_object = Wishlist.objects.get(user=user)
#     return render(request, "wishcart.html", {"user_products": wish_object.products.all()})

# @login_required(login_url="login")
# def removewish(request,id):
#     product_rm = WatchesUploads.objects.get(id=id)
#     wish_obj = Wishlist.objects.get(user=request.user)
#     wish_obj.products.remove(product_rm)
#     return render(request, "wishcart.html", {"user_products": wish_obj.products.all(), "isCart": False})

# # @login_required(login_url="login")
# # def show_cartlist(request):
# #     user_cart=Cart.objects.get_or_create(user=request.user)
# #     cart_objects=user_cart.cartitem_set.all()
# #     # cart_obj = Cart.objects.get(user=request.user)
# #     return render(request, "cart.html", {"user_products": cart_objects})


# # @login_required(login_url="login")
# # def show_cartlist(request):
# #     user_cart, created = Cart.objects.get_or_create(user=request.user)
# #     cart_objects = user_cart.cartitem_set.all()  


# @login_required(login_url="login")
# def show_cartlist(request):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_objects = user_cart.cartitem_set.all()  # Assuming `CartItem` has a foreign key to `Cart`
    
#     # Ensure the response always returns an HttpResponse
#     if cart_objects:
#         return render(request, "cart.html", {"user_products": cart_objects})
#     else:
#         # If no items in the cart, return an empty response or a message
#         return render(request, "cart.html", {"user_products": cart_objects, "message": "Your cart is empty."})

# # @login_required(login_url="login")
# # def removeCart(request, id):
# #     product_rm = WatchesUploads.objects.get(id=id)
# #     cart_obj = Cart.objects.get(user=request.user)
# #     cart_obj.products.remove(product_rm)
# #     return render(request, "wishcart.html", {"user_products": cart_obj.products.all(), "isCart": True})


# @login_required(login_url="login")
# def removeCart(request, id):
#     product_rm = get_object_or_404(WatchesUploads, id=id)
#     cart_obj = get_object_or_404(Cart, user=request.user)
#     cart_item = get_object_or_404(CartItem, user=cart_obj, product=product_rm)
#     cart_item.delete()  # Removes the item from the cart
#     return redirect('show_cartlist')  # Redirect to the cart list after removal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Watches, WatchesUploads, Wishlist, Cart, WatchReview, CartItem
from .forms import UploadForm
from django.views import View
from django.utils.decorators import method_decorator

def home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t': watches}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

@login_required(login_url="login")
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, "WatchUpload.html", {'form': form})

class UploadClass(View):
    def get(self, request):
        form = UploadForm()
        return render(request, "WatchUpload.html", {'form': form})
    
    @method_decorator(login_required(login_url="login"))
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "WatchUpload.html", {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, "login.html", {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def show_product(request, id):
    product = get_object_or_404(WatchesUploads, id=id)
    reviews_obj = WatchReview.objects.filter(product=product)
    return render(request, "product.html", {"product": product, "review": reviews_obj})

@login_required(login_url="login")
def addtowish(request, id):
    user = request.user
    product = get_object_or_404(WatchesUploads, id=id)
    obj1, created = Wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

# def addtocart(request, id):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     product = get_object_or_404(WatchesUploads, id=id)
    
#     # Check if the item is already in the cart
#     cart_item, created = CartItem.objects.get_or_create(user=user_cart, product=product)
    
#     # If it's already in the cart, you might want to increase quantity or do nothing
#     # For simplicity, assume you add one item
#     cart_item.quantity += 1  # Ensure CartItem model has a quantity field, or remove this line if you don't have it
#     cart_item.save()

@login_required(login_url="login")
def addtocart(request, id):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(WatchesUploads, id=id)
    
    # Check if the item is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
    
    if not created:  # If the item was not newly created, increment the quantity
        cart_item.quantity += 1
    
    cart_item.save()
    return redirect('show_cartlist')



# def addtocart(request, id):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     product = get_object_or_404(WatchesUploads, id=id)
#     cart_item, created = CartItem.objects.get_or_create(user=user_cart, product=product)
#     cart_item.product = product
#     cart_item.save()
#     return redirect('show_cartlist')

# @login_required(login_url="login")
# def addtocart(request, id):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     product = get_object_or_404(WatchesUploads, id=id)
#     cart_item, created = CartItem.objects.get_or_create(user=user_cart, product=product)
#     cart_item.product = product
#     return redirect('home')

@login_required(login_url="login")
def show_wishlist(request):
    wish_object = get_object_or_404(Wishlist, user=request.user)
    return render(request, "wishcart.html", {"user_products": wish_object.products.all()})

@login_required(login_url="login")
def removewish(request, id):
    product_rm = get_object_or_404(WatchesUploads, id=id)
    wish_obj = get_object_or_404(Wishlist, user=request.user)
    wish_obj.products.remove(product_rm)
    return render(request, "wishcart.html", {"user_products": wish_obj.products.all(), "isCart": False})

# @login_required(login_url="login")
# def show_cartlist(request):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_objects = user_cart.cartitem_set.all()  # Assuming CartItem has a foreign key to Cart
#     return render(request, "cart.html", {"user_products": cart_objects})
@login_required(login_url="login")
def show_cartlist(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()  # Fetch all cart items related to the user
    return render(request, "cart.html", {"user_products": cart_items})
# @login_required(login_url="login")
# def show_cartlist(request):
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_objects = user_cart.cartitem_set.all()  # Retrieve all cart items for the user
    
#     return render(request, "cart.html", {"user_products": cart_objects})


# @login_required(login_url="login")
# def removeCart(request, id):
#     product_rm = get_object_or_404(WatchesUploads, id=id)
#     cart_obj = get_object_or_404(Cart, user=request.user)
#     cart_item = get_object_or_404(CartItem, user=cart_obj, product=product_rm)
#     cart_item.delete()
#     return redirect('show_cartlist')

@login_required(login_url="login")
def removeCart(request, id):
    cart_obj = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart_obj, product_id=id)
    cart_item.delete()
    return redirect('show_cartlist')
