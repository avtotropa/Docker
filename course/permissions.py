from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModerator(BasePermission):
    message = 'Вы не являетесь модератором'

    def has_permission(self, request, view):
        if request.user.moderator:
            return True
        return False


class IsCustomPermission(BasePermission):
    message = 'Создание и Удаление модератору запрещено!!!'

    def has_permission(self, request, view):
        if request.user.moderator and request.method in ('POST', 'DELETE'):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        elif request.user.moderator and request.method in ('POST', 'DELETE'):
            IsCustomPermission.message = 'Создание и Удаление модератору запрещено!!!'
            return False
        elif request.user.moderator:
            return True
        elif request.user != obj.owner:
            IsCustomPermission.message = 'Вы не являетесь владельцем'
            return False
        return True


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
