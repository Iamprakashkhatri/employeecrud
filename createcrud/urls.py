from django.contrib import admin
from django.urls import path
from .views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDelete,
    )

app_name='createcrud'
urlpatterns = [
    path('create/',EmployeeCreateView.as_view(),name="index" ),
    path('detail/<int:id>',EmployeeDetailView.as_view(),name="detail" ),
    path('<int:id>/update',EmployeeUpdateView.as_view(),name="update" ),
    path('<int:pk>/delete',EmployeeDelete.as_view(),name="delete" ),
    path('',EmployeeListView.as_view(),name="list" ),
]