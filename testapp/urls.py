from django.urls import path
from django.urls.resolvers import URLPattern
from testapp import views

app_name='testapp'

urlpatterns=[
    path('',views.Index.as_view(),name="home"),
    path('set<int:pk>',views.Details.as_view(),name="test_details"),
    path('quiz<int:pk>',views.quiz,name="inquiz"),
    path('answer<int:pk>',views.solution,name="solution"),
    path('submession',views.submession,name='submession'),
    path('logout',views.userlogout,name='logout')
]