from django.conf.urls import patterns, include, url



import cros.views
import article.views
import tests.views

urlpatterns = patterns('',
    url(r'^lista_poluproizvoda$', tests.views.ListContactView.as_view(),
    name='tests-list',),
    url(r'^Poluproizvodi$', tests.views.CreateContactView.as_view(),
    name='tests-new',),
    url(r'^delete/(?P<pk>\d+)/$', tests.views.DeleteContactView.as_view(),
    name='tests-delete',),
    url(r'^edit/(?P<pk>\d+)/$', tests.views.UpdateContactView.as_view(),
    name='tests-edit',),
    url(r'^lista_hemikalija$', cros.views.ListContactView.as_view(),
    name='cros-list',),
    url(r'^Hemikalije$', cros.views.CreateContactView.as_view(),
    name='cros-novo',),
    url(r'^delete/(?P<pk>\d+)/$', cros.views.DeleteContactView.as_view(),
    name='cros-delete',),
    url(r'^edit/(?P<pk>\d+)/$', cros.views.UpdateContactView.as_view(),
    name='cros-edit',),
    url(r'^lista_ambalaze$', article.views.ListContactView.as_view(),
    name='article-list',),
    url(r'^Ambalaza$', article.views.CreateContactView.as_view(),
    name='article-novo',),
    url(r'^delete/(?P<pk>\d+)/$', article.views.DeleteContactView.as_view(),
    name='article-delete',),
    url(r'^edit/(?P<pk>\d+)/$', article.views.UpdateContactView.as_view(),
    name='article-edit',),
)