from django.urls import re_path, path
from .views import *  # URLconf에서 뷰를 호출하므로 ,뷰 모듈에의 모든 클래스를 임포트함

app_name = 'blog'

urlpatterns = [
    # Example :/
    re_path(r'^$', PostLV.as_view(), name='index'),  # URL 패턴이름은 이름공간을 포함해 blog:index
    # Example : /post/(same as /)
    re_path(r'^post/$', PostLV.as_view(), name='post_list'),  # blog:detail PostLV는 2가지요청처리
    # Example :/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),  # /blog/post/영단어/ 요청을 처리
    # Ex:/archive/
    re_path(r'^archive/$', PostAV.as_view(), name='post_archive'),  # blog:archive
    # Ex:/2017/
    re_path(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    # Ex:/2017/nov
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    # Ex:2017/nov/10
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    # Ex:/today/
    re_path(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    # Ex:/tag/
    re_path(r'^tag/$', TagTV.as_view(), name='tag_cloud'),
    # Ex: /tag/
    re_path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
]
