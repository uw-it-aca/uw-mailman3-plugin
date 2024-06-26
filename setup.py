import os
from setuptools import setup, find_packages

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/uw-mailman3-plugin>`_.
"""
version_path = 'uw_mailman3_plugin/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/uw-mailman3-plugin"
setup(
    name='UW-Mailman3-Plugin',
    version=VERSION,
    packages=find_packages('.'),
    author="UW-IT T&LS",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[
        'mailman',
        'atpublic',
    ],
    license='Apache License, Version 2.0',
    description=('An plugin to modify mailman3 at the '
                 'University of Washington'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)

