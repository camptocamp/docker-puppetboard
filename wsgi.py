from __future__ import absolute_import
import os

# Needed if a settings.py file exists
os.environ['PUPPETBOARD_SETTINGS'] = '/app/settings.py'
from puppetboard.app import app as application
