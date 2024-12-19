# from django.contrib import admin
# from .models import Watches

# from .models import WatchesUploads


# # Register your models here.
# admin.site.register(Watches)

# class WatchesUploadsAdmin(admin.ModelAdmin):
#     list_display=('name','price','description','image')
#     fields=['name','price','description','image']
        
# admin.site.register(WatchesUploads,WatchesUploadsAdmin)

# from django.contrib import admin
# from .models import Watches, WatchesUploads
# from .models import Wishlist,Cart

# # Register your models here.
# admin.site.register(Watches)

# class WatchesUploadsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'description', 'image')
#     list_filter=('name','price')
#     search_fields=('name', 'price', 'description')
#     fields = ['name', 'price', 'description', 'image']
        
# admin.site.register(WatchesUploads, WatchesUploadsAdmin)

# admin.site.register(Wishlist)
# admin.site.register(Cart)

from django.contrib import admin
from .models import Watches
from . models import WatchesUploads, Wishlist, Cart,WatchReview,CartItem

# Register your models here.
admin.site.register(Watches)

class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ('name', 'price', 'description')
    fields = ['name', 'price', 'description', 'image','count']
        
admin.site.register(WatchesUploads, WatchesUploadsAdmin)

class wishlistAdmin(admin.ModelAdmin):  
    list_display=('user','product')
    list_filter=('user','product')
# admin.site.register(Wishlist,wishlistAdmin)
admin.site.register(Wishlist)



# admin.site.register(Wishlist)
admin.site.register(Cart)

class watchReviewAdmin(admin.ModelAdmin):  
    list_display=('user','product','rating','review_text')
    list_filter=('user','product','rating')

admin.site.register(WatchReview,watchReviewAdmin)

admin.site.register(CartItem)
