from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("home", views.index, name="index"),
  path("signup", views.signup, name="signup"),
  path("signin", views.signin, name="signin"),
  path("logout", views.logout_view, name="logout"),
  path("profile/<str:pk>", views.profile, name="profile"),
  path("delivery/<str:pk>", views.delivery, name="delivery"),
  path("description/<str:pk>", views.product_description, name="product-description"),
  path("new-order/<str:pk>", views.new_order, name="new-order"),
  path("order-details/<str:pk>", views.order_details, name="order-details"),
  path("remove-item/<str:pk>", views.remove_item, name="remove-item"),
  path("increase-quantity/<str:pk>", views.increase_quantity, name="increase-quantity"),
  path("decrease-quantity/<str:pk>", views.decrease_quantity, name="decrease-quantity"),
  path("order-summary/<str:pk>", views.order_summary, name="order-summary"),
  path("confirm-order/<str:pk>", views.confirm_order, name="confirm-order"),
]
