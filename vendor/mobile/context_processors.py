# based on: http://sullerton.com/2011/03/django-mobile-browser-detection-middleware/

def mobile_browser(request):
    dict = {'mobile_browser': False}
    if hasattr(request, 'is_mobile'):
        dict['mobile_browser'] = request.is_mobile
    return dict
