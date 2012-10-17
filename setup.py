# -*- coding:utf-8 -*-
import sys
sys.path.append('./src')
from distutils.core import setup
from pyempty import __version__

setup(name='pyempty',
      version=__version__,
      description='empty python project template',
      long_description=open("README.md").read(),
      author='onlytiancai',
      author_email='onlytiancai@gmail.com',
      packages=['pyempty'],
      package_dir={'pyempty': 'src/pyempty'},
      package_data={'pyempty': ['stuff']},
      license="Public domain",
      platforms=["any"],
      url='https://github.com/onlytiancai/pyempty')
