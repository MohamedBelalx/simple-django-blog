from django.urls import path

from . import views
app_name = 'articles'

urlpatterns = [
    path('',views.index),
    path('<int:pk>',views.with_id,name='details')
]
