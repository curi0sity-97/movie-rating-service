from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.review_form),
    path('list/', views.review_list),

    path('', views.review_form,name='review_insert'), # get and post req. for insert operation
    path('<int:id>/', views.review_form,name='review_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.review_delete,name='review_delete'),
    path('list/',views.review_list,name='review_list') # get req. to retrieve and display all records
]