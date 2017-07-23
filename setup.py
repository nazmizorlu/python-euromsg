#!/usr/bin/env python
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-euromsg',

    version='0.0.1',

    description='Python utility for sending email over euro.message '
                '(https://www.euromsg.com) service ',
    long_description=long_description,

    url='https://github.com/nazmizorlu/python-euromsg',

    author='Nazmi ZORLU',
    author_email='nazmizorlu@gmail.com',

    maintainer='Nazmi ZORLU',
    maintainer_email='nazmizorlu@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Communications :: Email',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='euromsg euro.message',
    packages=['euromsg', ],
    install_require=['zeep>=1.3.0', ],
    zip_safe=True,
)