from django.contrib import admin
from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDelete,
    EmployeeTemplateView,
    EmployeeView,
    )

app_name='createcrud'
urlpatterns = [
    path('create/',EmployeeCreateView.as_view(),name="index" ),
    path('detail/<int:pk>',EmployeeDetailView.as_view(),name="detail" ),
    path('update/<int:pk>/',EmployeeUpdateView.as_view(),name="update" ),
    path('delete/<int:pk>/',EmployeeDelete.as_view(),name="delete" ),
    path('template',EmployeeTemplateView.as_view(),name="template"),
    path('temview',EmployeeView.as_view(),name="template"),
    path('list/',EmployeeListView.as_view(),name="list" ),
]