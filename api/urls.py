from django.urls import path, include

from .router import router


urlpatterns = [
    path('auth/', include(('rest_framework.urls', 'api'), namespace='rest_framework')),
    path('', include((router.urls, 'api'))),
]
