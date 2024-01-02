from django.urls import path, include

from .views import CategoryMVS, BlogMVS, CommentMVS, LikesMVS, PostViewsMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryMVS)
router.register('blog', BlogMVS)
router.register('comment', CommentMVS)
router.register('likes', LikesMVS)
router.register('postviews', PostViewsMVS)

urlpatterns = [
    path('', include(router.urls)),
]