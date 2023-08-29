from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    re_path(r'^order/(?P<order_name>.*)/(?P<price>.*)/(?P<toppingsList>.*)/$', views.order, name="order"),
    path("customer_order", views.customer_order, name="customer_order"),
    path("confirm_order", views.confirm_order, name="confirm_order"),
    path("staff", views.staff, name="staff"), 
    path("<int:order_id>/approve_order", views.approve_order, name="approve_order")
]
