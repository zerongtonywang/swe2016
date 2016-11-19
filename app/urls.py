from django.conf.urls import url
from .views import IndexView, LandingView, TopicView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^home/?$', IndexView.as_view(), name='index'),
    url(r'^topic/(?P<topic_id>[0-9]+)/?$', TopicView.as_view(), name='topic')
]
