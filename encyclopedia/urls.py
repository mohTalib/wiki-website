from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entries, name="entries"),
    path('search/', views.search, name="search"),
    path('new/', views.new_page, name="new_page"),
    path('edit/', views.edit, name="edit"),
    path('save_edit/', views.save_newpage, name="save_newpage"),
    path('rande/',views.rande, name="rande"),
]
