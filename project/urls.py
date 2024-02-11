from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path('accounts/', include('accounts.urls')),
   path('accounts/', include('django.contrib.auth.urls')),
   path('admin/', admin.site.urls),
   path('products/', include('products.urls')),
   path('orders/', include('orders.urls')),
   path('', include('settings.urls')),
   path('api-auth/', include('dj_rest_auth.urls')),
   path('api-auth/registration/', include('dj_rest_auth.registration.urls')),
   # path('accounts/', include('allauth.urls')),
   path("__debug__/", include("debug_toolbar.urls")),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
