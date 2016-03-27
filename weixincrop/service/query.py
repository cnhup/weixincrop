#coding:utf8
def get_server_host(request):
    return '%s://%s' % ('https' if request.is_secure() else 'http',request.get_host())

def get_full_path(request):
    return '%s://%s%s' % ('https' if request.is_secure() else 'http',request.get_host(),request.get_full_path())