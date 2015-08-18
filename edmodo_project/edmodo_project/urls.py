from django.conf.urls import patterns, include, url
from django.contrib import admin
from spotlight import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edmodo_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^spotlight/',views.search_form ),

    (r'^search/$', views.search),
    (r'^flag/$', views.flag),
    (r'^flagged/$', views.print_flag),

)

#  url(r'^admin/', include(admin.site.urls)),
#     url(r'^spotlight/', include('spotlight.urls')),
#     (r'^search-form/$', views.search_form),
#     (r'^search/$', views.search),
# )
