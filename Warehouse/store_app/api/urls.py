from django.urls import path
from store_app.api.views import StoreView, ProductView

urlpatterns = [
    path('store/', StoreView.as_view(), name='store'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:product_id>/', ProductView.as_view(), name='read_product'),
    path('products/<int:product_id>/inventory/', ProductView.as_view(), name='update_product')
]
