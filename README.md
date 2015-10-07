Puppetboard Docker image
==========================

[![Docker Pulls](https://img.shields.io/docker/pulls/camptocamp/puppetboard.svg)](https://hub.docker.com/r/camptocamp/puppetboard/)
[![Build Status](https://img.shields.io/travis/camptocamp/docker-puppetboard/master.svg)](https://travis-ci.org/camptocamp/docker-puppetboard)
[![By Camptocamp](https://img.shields.io/badge/by-camptocamp-fb7047.svg)](http://www.camptocamp.com)


## How to use

By default, Puppetboard looks for a PuppetDB on `localhost:8080`, so you need to deploy a configuration file for it.

Let's set up a `wsgi.py` file, which points to `default_settings.py`, e.g.:

```python
# wsgi.py
from __future__ import absolute_import
import os

# Needed if a settings.py file exists
os.environ['PUPPETBOARD_SETTINGS'] = '/app/default_settings.py'
from puppetboard.app import app as application
```

and

```python
# Minimal default_settings.py
import os

PUPPETDB_HOST = 'puppetdb'
PUPPETDB_PORT = 8081
PUPPETDB_SSL_VERIFY = False
PUPPETDB_KEY = '/app/puppetboard.key'
PUPPETDB_CERT = '/app/puppetboard.crt'
```

You'll need to create a keypair signed by your Puppet CA for `puppetboard.key` and `puppetboard.crt`.

Now launch docker:

```shell
docker run -p 80:80 --add-host puppetdb:<your_puppetdb_ip> \
  -v $PWD/wsgi.py:/app/wsgi.py \
  -v $PWD/default_settings.py:/app/default_settings.py \
  -v $PWD/puppetboard.crt:/app/puppetboard.crt \
  -v $PWD/puppetboard.key:/app/puppetboard.key \
  -ti camptocamp/puppetboard:latest
```

and Puppetboard will be available on your `http://localhost`
