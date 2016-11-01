import os
import sys
import site

try:
    site.addsitedir('/home/user/developer/b2/lib/python2.7/site-packages')

    sys.path.append('/home/user/developer/28Oct16/myp')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myp.settings")

    # Activate your virtual env
    activate_env=os.path.expanduser("/home/user/developer/b2/bin/activate_this.py")
    #execfile(activate_env, dict(__file__=activate_env))
    exec(compile(open(activate_env).read(),activate_env,'exec'), dict(__file__=activate_env))
except Exception as e:
    print ("Exception occured ")
    print (e)
    sys.exit(-1)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
