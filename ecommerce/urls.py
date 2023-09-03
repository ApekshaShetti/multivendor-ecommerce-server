"""
http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzNzMzNTc5LCJpYXQiOjE2OTM3MzI2MDMsImp0aSI6IjA0Zjk2N2YxZjJlNzRmNDc4MGIyYmUyY2QzM2RlODYxIiwidXNlcl9pZCI6MX0.KIwEUxxnFBcSLW6H08OrnDQIBwSQZuvnND701l8U0po"


http http://127.0.0.1:8000/api/token/refresh/ refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzgxOTAwMywiaWF0IjoxNjkzNzMyNjAzLCJqdGkiOiJkNjA0OWJlNzhmYTA0ZDM5ODg4NDcwZGFjNTBlOGIzOCIsInVzZXJfaWQiOjF9.pnuqnNOT41F53lhZHBPEvRwUxthBuLwdYvqLaYH95ls"
"""

from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('ecommerce_app.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

