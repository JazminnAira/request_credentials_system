# THIS SETUP IS APPLICABLE VIA ONLINE ONLY, USE WSGI DIRECTLY IF NEEDED

import os
import sys

from gradclear_project.wsgi import application




# sys.path.insert(0, os.path.dirname(__file__))


# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]
