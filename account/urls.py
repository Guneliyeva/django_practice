from django.urls import path
from .views import *

app_name="accounts"

urlpatterns = [
    path('', account, name="account"),
    path('login/', login_page, name="login"),
    path('register/', register , name="signup"),
    path('logout/', logout_page, name="logout"),
   
]