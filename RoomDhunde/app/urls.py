from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('<int:customer_id>/',views.detail,name='detail'),
    path('submit',views.submit,name='submit'),
]