from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    # url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
    url(r'^searchchannel/$', views.searchchannel_view, name='searchchannel'),
    url(r'^home/$', views.home_view, name='home')
]