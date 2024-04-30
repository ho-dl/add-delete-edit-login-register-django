from django.urls import path
from app_home.views import *

from .views import product_add, product_view


urlpatterns = [
    # render html
    path('', index,name='index'),
    path('upload/',addperson,name='addperson'),
    


 

    path('content/<int:person_id>/detail_view/',person_view,name='person_view'),

    path('content/<int:person_id>/delete/',person_delete,name='person_delete'),

    path('content/<int:person_id>/edit/',person_edit,name='person_edit'),

    # path('product/add', product_add, name='product_add'),
    # path('product/view', product_view, name='product_view'),


    path('product/add/', product_add, name='product_add'),
    path('product/view/', product_view, name='product_view'),


    # view products by id 
     path('product/<int:pk>/',product_detail, name='product_detail'),

    #  product eddit by id

    path('product/<int:product_id>/edit',product_edit,name='product_edit')

  


]
