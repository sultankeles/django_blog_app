from rest_framework import serializers

from .models import Category, Blog, Comment, Likes, PostViews


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class BlogSerializer(serializers.ModelSerializer):

    comment_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'image',
            'category',
            'publish_date',
            'user',
            'status',
            'comment_count',
            'likes_count',
        )

    def get_comment_count(self, blog):
        return Comment.objects.filter(blog=blog).count()
    
    def get_likes_count(self, blog):
        return Likes.objects.filter(blog=blog).count()
    

class UserBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'title',
            'content',
            'image',
            'category',
            'publish_date',
            'user',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'user',
            'time_stamp',
            'content',
            'blog',
        )


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = (
            'user',
            'blog',
            'likes',
        )


class PostViewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostViews
        fields = (
            'user',
            'post_views',
            'blog',
            'time_stamp',
        )