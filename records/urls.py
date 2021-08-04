from django.urls import path

from . import views

app_name = "records"
urlpatterns = [
    path("", views.records, name="records"),
    path('add-profile/', views.addProfile, name="profile"),
    path('add-plans/<str:user>/', views.addPlans, name='plans'),
    path('plan/<str:user>/', views.seePlans, name="seePlans"),
    path('update-profile/<str:user>/',
         views.updateProfile,
         name="updateProfile"),
    path('update-plans/<str:user>/', views.updatePlans, name="updatePlan"),
    path('login_view/', views.login_view, name='login_view'),
]
