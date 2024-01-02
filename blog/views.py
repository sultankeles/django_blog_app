from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Category, Blog, Comment, Likes, PostViews

from .serializers import CategorySerializer, BlogSerializer, UserBlogSerializer, CommentSerializer, LikesSerializer, PostViewsSerializer

from .permissions import IsStaffOrReadOnly


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]


class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Blog.objects.all()
        else:
            queryset = Blog.objects.filter(status = 'p')
            return queryset
        
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BlogSerializer
        return UserBlogSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        created_post_view = PostViews.objects.filter(user=self.request.user, blog=instance, post_views=True)
        if not created_post_view.exists():
            PostViews.objects.create(user=self.request.user, blog=instance, post_views=True)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]


class LikesMVS(ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer


class PostViewsMVS(ModelViewSet):
    queryset = PostViews.objects.all()
    serializer_class = PostViewsSerializer