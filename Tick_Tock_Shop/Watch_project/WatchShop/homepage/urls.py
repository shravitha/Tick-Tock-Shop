# from django.contrib import admin
# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('upload/', views.upload, name='upload_images'),
#     path('login/', views.login_page, name='login'),
#     path('signup/', views.signup_user, name='signup'),
#     path('logout/', views.logout_user, name='logout'),
#     path('product/<int:id>/', views.show_product, name='product'),
#     path('addtowish/<int:id>', views.addtowish, name='addtowish'),
#     path('addtoCart/', views.addtocart, name='addto_cart'),
#     path('wishlist/', views.show_wishlist, name='show_wishlist'),
#     path('removewish/<int:id>', views.removewish, name='reomovewish'),
#     path('removCart/<int:id>', views.removeCart, name='reomoveCart'),
#     path('show_cartlist/', views.show_cartlist, name='show_cartlist'),
    

# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






# from django.contrib import admin
# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('upload/', views.upload, name='upload_images'),
#     path('login/', views.login_page, name='login'),
#     path('signup/', views.signup_user, name='signup'),
#     path('logout/', views.logout_user, name='logout'),
#     path('product/<int:id>/', views.show_product, name='product'),
#     path('addtowish/<int:id>', views.addtowish, name='addtowish'),
#     path('addtocart/', views.addtocart, name='addtocart'),
#     path('wishlist/', views.show_wishlist, name='show_wishlist'),
#     path('removewish/<int:id>', views.removewish, name='removewish'),  # Ensure the name is correct
#     path('removCart/<int:id>', views.removeCart, name='removecart'),  # Ensure the name is correct
#     path('show_cartlist/', views.show_cartlist, name='show_cartlist'),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload, name='upload_images'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/'
         , views.logout_user, name='logout'),
    path('product/<int:id>/', views.show_product, name='product'),
    path('addtowish/<int:id>/', views.addtowish, name='addtowish'),  # Added trailing slash
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('cart/',views.Cart,name='Cart'),
     # Ensured consistent naming
    path('wishlist/', views.show_wishlist, name='show_wishlist'),
    path('removewish/<int:id>/', views.removewish, name='removewish'),  # Corrected the name and added trailing slash
    path('removCart/<int:id>/', views.removeCart, name='removecart'),  # Corrected the name and added trailing slash
    path('show_cartlist/', views.show_cartlist, name='show_cartlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
