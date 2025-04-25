from rest_framework import permissions

class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = self.__build_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)
    
    def __get_permission(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTION': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
    
    def __build_permission_codename(self, method, view):
        try:
            app_name = view.queryset.model._meta.app_label
            permission_name = self.__get_permission(method)
            model_name = view.queryset.model._meta.model_name
            return f'{app_name}.{permission_name}_{model_name}'
        except AttributeError:
            return None