MEDIA directory

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')  --> in settings

now come to urls.py and import that --> 
from django.conf.urls.static import static 
from django.conf import settings     --> for connect the media folder

and write the code whatever you want..
