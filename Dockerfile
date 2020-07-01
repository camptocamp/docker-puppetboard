FROM grahamdumpleton/mod-wsgi-docker:python-3.5-onbuild

CMD [ "--mount-point", "/puppetboard", "wsgi.py" ]
