# -*- coding: utf-8 -*-
import logging.config
from pyempty import mainweb

logging.config.fileConfig('../src/pyempty/logging.ini')
app = mainweb.app.wsgifunc()

if __name__ == '__main__':
    import os
    # 项目正式运行时static目录由nginx管理, 调试时可以直接使用web.py的调试模式的静态目录功能
    # 因为静态文件在src/pyempty目录下，所以要chdir一下，否则会在main目录下找
    os.chdir('../src/pyempty') 
    app = mainweb.app
    app.run()
