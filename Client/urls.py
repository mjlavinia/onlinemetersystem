from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path('dashboard/',views.dashboard, name='dashboard' ),
    path('savemeter/',views.savemeter, name='savemeter' ),
  #  path('employee/',views.index, name='employee' ),
  # path('create/',views.create, name='create' ),
  # path('create/createData/',views.createData, name='createData' ),
  # path('delete/<int:id>', views.delete, name='delete'),
  # path('update/<int:id>',views.update, name='update' ),
  # path('update/updateData/<int:id>',views.updateData, name='updateData' ),
] 