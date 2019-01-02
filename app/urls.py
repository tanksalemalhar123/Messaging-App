from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

app_name='app'
urlpatterns= [
    url(r'^$',views.index, name='index'),
    url(r'^chat/(?P<app_user2>[0-9]+)/$',views.chat, name='chat'),
    url(r'^chat_post/(?P<app_user2>[0-9]+)/$',views.chat_post, name='chat_post'),
    url(r'^chat_poll/(?P<app_user2>[0-9]+)/(?P<msg_id>[0-9]+)/$',views.chat_poll, name='chat_poll'),
    url(r'^app_users/$', views.app_users, name='app_users'),
    url(r'^login_form/$', views.login_form, name='login_form'),
    url(r'^login_action/$', views.login_action, name='login_action'),
    url(r'^logout_action/$', views.logout_action, name='logout_action'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_action/$', views.register_action, name='register_action'),
    url(r'^add_to_contacts/(?P<app_user_id>[0-9]+)/$',views.add_to_contacts, name='add_to_contacts'),
    url(r'^remove_contact/(?P<app_user_id>[0-9]+)/$',views.remove_contact, name='remove_contact'),
    url(r'^my_contacts/$',views.my_contacts, name='my_contacts'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^edit_profile/$',views.edit_profile, name='edit_profile'),
    url(r'^edit_profile_action/$',views.edit_profile_action, name='edit_profile_action'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
