def checklogin(request):
    ctx = {'user': request.user}
    return ctx