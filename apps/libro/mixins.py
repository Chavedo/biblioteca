from django.shortcuts import redirect

class LoginMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')