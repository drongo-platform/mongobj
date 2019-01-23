#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='mongobj',
    version='1.0.1',
    description='Mongodb object mapping.',
    author='Sattvik Chakravarthy',
    author_email='sattvik@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
