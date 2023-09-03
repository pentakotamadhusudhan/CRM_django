from django.urls import path
from . views import *  

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Django CRM",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pentakotamadhu74@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('register',RegisterView.as_view(),),
    path("reg",reg.as_view()),
    path('register/<int:id>', UserUpdate.as_view(), name='api-register'),
    path('super', SuperUser.as_view(), name='Super-admin'),
    # path('super/<int:id>', RegisterView.as_view(), name='Super-admin'),   
]
