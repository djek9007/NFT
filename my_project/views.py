from django.shortcuts import redirect

def redirect_to_login(request):
    if request.user.is_authenticated:
        return redirect('profile', user_id=request.user.id)
    return redirect('login')