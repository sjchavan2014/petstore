from django.urls import path
from myapp import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('enter/',views.data,name="enter"),
    path('update/<int:id>',views.update,name= "update"),
    path('<int:id>',views.delete,name="delete"),
    path('cart/',views.cart, name="cart"),
    path('addtocart/',views.add_to_cart,name='addtocart'),
    path('viewscart/',views.view_cart, name= 'viewscart'),
    path('removecart/<int:id>',views.remove_cart,name='removecart'),
    path('cartincrease/',views.cart_increase, name='cartincrease'),
    path('cartdecrease/',views.cart_decrease, name='cartdecrease'),
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('logout/',views.LogOut, name='logout'),
    path('orderplace/',views.Order_Place, name='orderplace'),
    path('ordermessage/',views.Order_message, name='ordermessage'),
    path('vieworder/',views.view_order, name='vieworder'),
    path('address/',views.Address1, name='address'),
]
