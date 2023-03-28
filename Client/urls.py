from django.urls import path
from . import views
from .tool import dummy

urlpatterns = [
    path ('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path('dashboard/',views.dashboard, name='dashboard' ),
    path('savemeter/',views.savemeter, name='savemeter' ),
    path('savefakemeter',dummy.savefakemeter, name='savefakemeter' ),
    path('settings/<int:id>',views.settings, name='settings' ), 
    path('settings/updatesettings/<int:id>',views.updatesettings, name='updatesettings' ), 
  
  #  path('employee/',views.index, name='employee' ),
  # path('create/',views.create, name='create' ),
  # path('create/createData/',views.createData, name='createData' ),
  # path('delete/<int:id>', views.delete, name='delete'),
  # path('update/<int:id>',views.update, name='update' ),
  # path('update/updateData/<int:id>',views.updateData, name='updateData' ),
] 