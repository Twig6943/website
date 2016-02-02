# pylint: disable=C0103, C0301
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import forms

urlpatterns = patterns(
    'accounts.views',
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.html',
         'authentication_form': forms.LoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logout.html'},
        name='logout'),
    url(r'^password/change/$', auth_views.password_change,
        kwargs={'template_name': "accounts/password_change.html"},
        name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done,
        kwargs={'template_name': "accounts/password_change_done.html"},
        name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset,
        kwargs={'template_name': "accounts/password_reset.html"},
        name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',  # noqa
        auth_views.password_reset_confirm,
        kwargs={'template_name': "accounts/password_reset_confirm.html"},
        name='password_reset_confirm'),
    url(r'^password/reset/done/$', auth_views.password_reset_done,
        kwargs={'template_name': "accounts/password_reset_done.html"},
        name='password_reset_done'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
        kwargs={'template_name': "accounts/password_reset_complete.html"},
        name='password_reset_complete'),
    url(r'^register/$', 'register', name="register"),
    url(r'^auth/$', 'client_auth', name="client_auth"),
    url(r'^verify/$', 'client_verify'),
    url(r'^associate-steam/', 'associate_steam', name="associate_steam"),
    url(r'^(?P<username>.*)/library/$', 'library_show',
        name="library_show"),
    url(r'^library/add/(?P<slug>[\w-]+)/$', 'library_add',
        name="add_to_library"),
    url(r'^library/remove/(?P<slug>[\w-]+)/$', 'library_remove',
        name="remove_from_library"),
    url(r'^library/steam-sync/', 'library_steam_sync',
        name="library_steam_sync"),
    url(r'profile/$', 'profile', name="profile"),
    url(r'(.*)/edit/$', 'profile_edit', name='profile_edit'),
    url(r'(.*)/$', 'user_account', name="user_account"),
    url(r'send-confirmation$', 'user_send_confirmation', name='user_send_confirmation'),
    url(r'confirm$', 'user_email_confirm', name='user_email_confirm'),
    url(r'discourse-sso$', 'discourse_sso', name='discourse_sso')
)
