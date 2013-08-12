# -*- coding: utf-8 -*-
import os
import web
from datetime import datetime
import logging

from . import config

curdir = os.path.dirname(__file__)
render = web.template.render(os.path.join(curdir, config.TEMPLATES_PATH))


class index(object):
    def GET(self):
        logging.debug('receive a /index request')
        web.header('Content-Type', 'text/html; charset=utf-8', unique=True)
        return render.index()


class currenttime(object):
    def GET(self):
        logging.debug('receive a /current_time request')
        return datetime.now().strftime('%Y-%m-%d %H:%M')

urls = ["/", index,
        "/current_time", currenttime,
        ]

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
