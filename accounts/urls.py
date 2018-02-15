from django.conf.urls import url
from .views import LoginView, RegView, signOut


app_name = 'accounts'
urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^register$', RegView.as_view(), name='register'),
    url(r'^logout$', signOut, name='logout')
]
