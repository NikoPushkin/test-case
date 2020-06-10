from django.shortcuts import redirect

def redirectPage(request):
    return redirect('user/')
