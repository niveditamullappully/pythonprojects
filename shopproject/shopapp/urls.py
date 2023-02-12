from django.urls import path
from . import views
app_name='shopapp'
urlpatterns=[
    path('',views.allProductCategory,name='allproducts'),
    path('<slug:c_slug>/',views.allProductCategory,name='product-by-category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.productDetails,name='productdetail')
]