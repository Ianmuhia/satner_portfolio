from django.urls import path
from blog.views import blog_single, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='blog_index'),
    path('blog_single/<int:pk>/', blog_single, name='blog_single')
]
