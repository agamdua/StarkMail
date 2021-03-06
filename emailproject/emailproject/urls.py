from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emailproject.views.home', name='home'),
    url(r'^$', 'emailproject.views.home', name='home'),
    # url(r'^emailproject/', include('emailproject.foo.urls')),
    url(r'^compose/', 'compose_app.views.compose', name='compose'),
    url(r'^register/', 'register_app.views.post', name='register'),
    url(r'^login/', 'login_app.views.login_view', name='login'),
    url(r'^logout/', 'login_app.views.logout_view', name='logout'),
    url(r'^inbox/', 'inbox_app.views.inbox_view', name='inbox')


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
