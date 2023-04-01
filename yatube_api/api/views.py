from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment, Group, Follow, User
from .serializers import GroupSerializer, FollowSerializer
from .serializers import PostSerializer, CommentSerializer
from .permissions import AuthorOrReadOnly, ReadOnly


class ApiPostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApiCommentsViewSet(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(
            author=self.request.user, post=post
        )

    def get_queryset(self):
        get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return Comment.objects.filter(post_id=self.kwargs.get("post_id"))

    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)


class ApiGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly,)


class ApiFollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("=user__username",)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
