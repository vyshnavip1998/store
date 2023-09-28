from . import views
from django.urls import path

urlpatterns = [

    path('register/', views.register, name='register'),
    path('s', views.s, name='s'),
    # path('register/', views.sign_up, name='register'),
    # path('login/', views.sign_in, name='login'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('explore', views.explore, name='explore'),
    path('view/', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-cities/', views.load_courses, name='ajax_load_cities'),
    path('ack', views.ack, name='ack'),

]
