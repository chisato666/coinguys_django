from django.urls import path, include
from . import views

urlpatterns = [
     path('submit_backtest', views.submit_backtest),
     path('check_alert', views.check_alert),

     path('show_alert', views.show_alert),
     path('', views.say_hello),
     path('getProfiles',views.getProfiles, name='getProfiles'),
     path('get_btcusdt_price', views.get_btcusdt_price, name='get_btcusdt_price'),

     path('ajax/',views.ajax)


]

