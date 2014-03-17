#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(name='tweet-content-stats',
      version='0.1',
      license='MIT',
      description='A python project that counts links, images, videos, retweets/likes/favorites/, check-INs in tweet texts to produce statistic of content.',
      long_description=open('README.md').read(),
      author='Fatih Sucu',
      author_email='<fatih.sucu@botego.com>',
      maintainer='Mustafa Atik',
      maintainer_email='<mustafa.atik@botego.com>',
      packages=['tcs'],
      platforms='any')