from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from catalog.views import PresentationListView, modify
from catalog.resources import PresentationResource

presentation_resource = PresentationResource()

urlpatterns = [
    url('login/', auth_views.login, name='login'),
    url('logout/', auth_views.logout, name='logout'),
    url(r'^catalog/$', PresentationListView.as_view(), name='catalog'),
    url(r'^catalog/modify/(?P<p_id>[\w{}.-]{36})/$', modify, name='modify'),
    url(r'^api/', include(presentation_resource.urls)),
    path('admin/', admin.site.urls),
]
