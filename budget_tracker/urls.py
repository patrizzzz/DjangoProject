"""
URL configuration for budget_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionsViewSet
from category.views import CategoryViewSet
from user.views import UserViewSet
from recurringtransac.views import RecurringConfigViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionsViewSet)
router.register(r'categories', CategoryViewSet)
router.register('users', UserViewSet)
router.register('recurringtransacconfig', RecurringConfigViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]
