from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from recipes.pagination import CustomPagination
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users import serializers
from users.models import Follow, User


class FollowViewSet(UserViewSet):
    """Работает с пользователями."""
    pagination_class = CustomPagination

    @action(methods=('post',), detail=True,
            permission_classes=(IsAuthenticated,))
    def subscribe(self, request, id=None):
        """Создаёт или удалет связь между пользователями."""
        user = request.user
        author = get_object_or_404(User, id=id)

        if user == author:
            return Response(
                {'errors': 'Вы не можите подписаться на самого себя.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if Follow.objects.filter(user=user, author=author).exists():
            return Response(
                {'errors': 'Вы уже подписаны на этого автора.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        follow = Follow.objects.create(user=user, author=author)
        serializer = serializers.FollowSerializer(
            follow, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def delete_subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)

        if user == author:
            return Response(
                {'errors': 'Вы не можете отписаться от самого себя.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        follow = Follow.objects.filter(user=user, author=author)
        if follow.exists():
            follow.delete()
            return Response(
                {'message': 'Вы отписались от этого автора.'},
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {'errors': 'Вы уже отписались.'},
            status=status.HTTP_400_BAD_REQUEST)

    @action(methods=('get',), detail=False,
            permission_classes=(IsAuthenticated,))
    def subscriptions(self, request):
        """Список подписок пользоваетеля."""
        user = request.user
        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = serializers.FollowSerializer(
            pages, many=True, context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
