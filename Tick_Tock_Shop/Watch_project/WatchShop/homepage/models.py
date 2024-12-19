# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User
# # Create your models here.
# class Watches(models.Model):
#     name=models.CharField(max_length=100)
#     description =models.TextField()
#     price=models.FloatField()

#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)

# class WatchesUploads(models.Model):
#     name=models.CharField(max_length=100)
#     description =models.TextField()
#     price=models.FloatField()
#     image=models.ImageField(upload_to="watch_images/")

#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)



# class Wishlist(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     products=models.ForeignKey(WatchesUploads,on_delete=models.CASCADE)
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)

# class Cart(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     products=models.ManyToManyField(WatchesUploads,on_delete=models.CASCADE)
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)


# from django.db import models
# from django.contrib.auth.models import User

# class Watches(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.FloatField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class WatchesUploads(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.FloatField()
#     image = models.ImageField(upload_to="watch_images/")
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class Wishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(WatchesUploads)  # No need for on_delete here
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User

class Watches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class WatchesUploads(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="watch_images/")
    count=models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # products = models.ManyToManyField(WatchesUploads)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class CartItem(models.Model):
#     user = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
#     product = models.ForeignKey(WatchesUploads,on_delete=models.CASCADE)
#     cart_count=models.IntegerField(default=1)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

# class WatchReview(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product=models.ForeignKey(WatchesUploads,on_delete=models.CASCADE)
#     review_text=models.TextField()
#     rating=models.PositiveSmallIntegerField(choices=[(i.str(i) for i in range(1,6))])
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)  # Changed `user` to `cart`
#     product = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
#     cart_count = models.IntegerField(default=1)





class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Ensure there's a quantity field


class WatchReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    