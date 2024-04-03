from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешаем внесение изменений только владельцу объекта
    для всех остальных доступны безопасные методы.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
