#!/usr/bin/env python

from distutils.core import setup

setup(name='gherkin-trigger',
      version='0.5',
      description='Jenkins Gerrit Trigger',
      author='Eric Windisch',
      author_email='ewindisch@docker.com',
      url='https://github.com/ewindisch/jenkins-gerrit-trigger',
      scripts=['bin/gherkin-trigger'],
     )
