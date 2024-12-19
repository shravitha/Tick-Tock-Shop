# """
# URL configuration for WatchShop project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# # from django.urls import path, include



# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('',include('homepage.urls'))
 

# # # ]
# # from django.contrib import admin
# # from django.urls import path, include
# # from django.urls import path,include
# # from django.conf.urls.static import static



# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('',include('homepage.urls'))
 

# # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# # from django.conf import settings
# # from django.conf.urls.static import static

# # urlpatterns = [
# #     # Your URL patterns here
# # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings  # Make sure this import is present
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # your other url patterns
#     path('admin/', admin.site.urls),
#     path('',include('homepage.urls'))
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



from django.conf import settings  # Add this import
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls'))
    # Add your URL patterns here
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
