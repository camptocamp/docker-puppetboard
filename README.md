Puppetboard Docker image
==========================

[![Docker Pulls](https://img.shields.io/docker/pulls/camptocamp/puppetboard.svg)](https://hub.docker.com/r/camptocamp/puppetboard/)
[![Build Status](https://img.shields.io/travis/camptocamp/docker-puppetboard/master.svg)](https://travis-ci.org/camptocamp/docker-puppetboard)
[![By Camptocamp](https://img.shields.io/badge/by-camptocamp-fb7047.svg)](http://www.camptocamp.com)


## How to use

By default, Puppetboard looks for a PuppetDB on `localhost:8080`, so you need to deploy a configuration file for it.

You'll need to create a keypair signed by your Puppet CA for `puppetboard.key` and `puppetboard.crt`.

Now launch docker, specifying the PuppetDB location and keys:

```shell
docker run -p 80:80 \
  --add-host puppetdb:<your_puppetdb_ip> \
  -v $PWD/puppetboard.crt:/app/puppetboard.crt \
  -v $PWD/puppetboard.key:/app/puppetboard.key \
  -ti camptocamp/puppetboard:latest
```

and Puppetboard will be available on your `http://localhost`!


You can also use environment variables to specify the PuppetDB and port:

```shell
docker run -p 80:80 \
  -e PUPPETDB_HOST=<your_puppetdb_ip> \
  -e PUPPETDB_PORT=8081 \
  -v $PWD/puppetboard.crt:/app/puppetboard.crt \
  -v $PWD/puppetboard.key:/app/puppetboard.key \
  -ti camptocamp/puppetboard:latest
```
