#-------------------------------------------------------------------------------
# Name:     Nansatmap
# Purpose:  Basemap extension for easy mapping with Nansat
#
# Author:
#
# Created:  04.09.2017
# Copyright:(c) NERSC
# License:  GPLv3
#-------------------------------------------------------------------------------
from setuptools import setup
from os import path

NAME = 'nansatmap'
REQS = ['nansat', 'scipy', 'matplotlib', 'basemap']

setup(
    name=NAME,
    version='0.1.1',
    description='Basemap extension for easy mapping with Nansat',
    long_description=long_description,
    zip_safe=True,
    author=('Anton Korosov', 'Morten Wergeland Hansen', 'Asuka Yamakava', 'Aleksander Vines',),
    author_email='anton.korosov@nersc.no',
    url='https://github.com/nansencenter/nansatmap',
    download_url='https://github.com/nansencenter/nansatmap/archive/v0.1.1.tar.gz',
    packages=['nansatmap'],
    install_requires=REQS,
    test_suite='nansatmap.tests',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
    ],
    keywords='maps ',
)
