from fabric.api import *
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def build():
    with lcd('docs'):
        local('sphinx-build -b html -d _build/doctrees . _build/html')

def test():
    local('nosetests')

def size():
    local('sloccount rstparser tests | grep -C2 SLOC-by-Language')

def coverage():
    local('coverage erase')
    local('coverage run `which nosetests`')
    local('coverage combine')
    local('coverage html')
    url = "file://%s/docs/_coverage/html/index.html" % BASE_DIR
    local('python -m webbrowser -t %s' % url)

