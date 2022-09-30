from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("home", views.index, name="index"),
  path("signup", views.signup, name="signup"),
  path("signin", views.signin, name="signin"),
  path("logout", views.logout_view, name="logout"),
  path("profile/<str:pk>", views.profile, name="profile"),
  path("description/<str:pk>", views.product_description, name="product-description"),
  path("new-order/<str:pk>", views.new_order, name="new-order"),
  path("order-details/<str:pk>", views.order_details, name="order-details"),
]
