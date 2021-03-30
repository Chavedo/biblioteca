from django.shortcuts import redirect

class LoginYSuperUsuarioMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')

     