from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClassmateList.as_view(), name='classmate_list'),
    path('view/<int:pk>', views.ClassmateView.as_view(), name='classmate_view'),
    path('new', views.ClassmateCreate.as_view(), name='classmate_new'),
    path('view/<int:pk>', views.ClassmateView.as_view(), name='classmate_view'),
    path('edit/<int:pk>', views.ClassmateUpdate.as_view(), name='classmate_edit'),
    path('delete/<int:pk>', views.ClassmateDelete.as_view(), name='classmate_delete'),
]
