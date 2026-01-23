from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("about/", TemplateView.as_view(template_name="shop/product/about.html"), name="about"),
    path("product/<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
    
    path("category/<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    
]
