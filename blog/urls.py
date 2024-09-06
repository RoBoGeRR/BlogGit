from django.urls import path
from .views import post_share,post_list, post_detail, PostListView, post_comment
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
app_name = 'blog'
sitemaps = {
    'posts': PostSitemap,
}
urlpatterns = [
    # path('', PostListView.as_view(), name='post_list'),
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>', post_list, name='post_list_by_tag'),
    path('blog/<int:year>-<int:month>-<int:day>/<slug:slug>/', post_detail, name='post_detail'),
    path('id/<int:id>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]