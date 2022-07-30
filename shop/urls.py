from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="store"),
    # path("fashion/", views.fashion, name="fashion"),
    # path("phone/", views.phone, name="phone"),
    path("contact/", views.contact, name="contact"),
    path("individual-page/<int:myid>", views.individual, name="individual-page"),
    path("checkout/", views.checkout, name="checkout"),
    path("search_item/", views.search_item, name="search-item"),
    path("sign/", views.sign, name="sign"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]