from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.simple_tag
def posts_names():
    posts = Post.published.all()
    names_with_urls = []
    for post in posts:
        
        names_with_urls.append(f'<a href="{post.get_absolute_url()}">{post.title}')

    return ',<br>'.join(names_with_urls)