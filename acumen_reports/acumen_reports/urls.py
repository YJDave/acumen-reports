from django.conf.urls import url, include
from django.contrib import admin
from useraccounts.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^(?P<user_name>\w+)/', include('useraccounts.urls')),

]
