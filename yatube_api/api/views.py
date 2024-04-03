from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import mixins, permissions, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Follow, Post
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
from .permissions import OwnerOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_post(self):
        """Метод для получения поста."""
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    # Получаем комментарии только поста с заданным ID
    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


# class FollowViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = Follow.objects.all()
#         serializer = FollowSerializer(queryset, many=True)
#         return Response(serializer.data)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ('following', 'username')

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
