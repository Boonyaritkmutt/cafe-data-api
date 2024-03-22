from django.urls import path
from .views import StoreDetailUpdateDelete, StoreList, ProductDetailUpdateDelete, ProductList

urlpatterns = [
    # path('stores/', StoreList.as_view(), name='store_list'),
    # path('stores/<int:store_id>/',
    #      StoreDetailUpdateDelete.as_view(), name='store_detail'),

    path('Product/', ProductList.as_view(), name='Product_list'),
    path('Product/<int:Product_id>/',
         ProductDetailUpdateDelete.as_view(), name='Product_location'),
]

