from .models import Settings
from django.core.cache import cache

# def get_settings(request):
#     data = Settings.objects.last()
#     return {'settings_data':data}

def get_settings(request):
    try:
        settings_data = cache.get('settings_data')
        print('new cache')
    except:
        print('new data')
        settings_data = Settings.objects.last()
        cache.set('settings_data',settings_data,60*60*24)
        
    return {'settings_data':settings_data}