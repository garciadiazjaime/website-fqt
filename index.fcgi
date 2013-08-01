#!/usr/local/bin/python2.7
import sys, os, user

# Add a custom Python path. (optional)
sys.path.insert(0, "/var/www/vhosts/fqt.org.mx/httpdocs")

# Switch to the directory of your project.
os.chdir("/var/www/vhosts/fqt.org.mx/httpdocs")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "fqt.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
