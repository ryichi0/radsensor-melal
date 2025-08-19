import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dotenv import load_dotenv

load_dotenv()

urlpatterns = [
    path(os.getenv("ADMIN_URL"), admin.site.urls),
    path('', include('home.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/product/', include('product.urls')),
    path('api/contact/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
