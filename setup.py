# webcheck - A Python based Robots.txt audit tool
# Copyright (c) 2021-2022 Moulik<Moulik at www.techyrick.com>
#
# Released under the GPLv3+ license. See LICENSE file for details.
#
from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
        name = 'webcheck',
        version="0.81",
        description = 'A Python based Robots.txt audit tool',
        long_description = read('README.md'),
        author = 'Moulik',
        author_email = 'techyrick.com@gmail.com',
        maintainer = 'moulik-source',
        maintainer_email = 'c.moulik31@gmail.com',
        url = 'https://github.com/moulik-source/webcheck',
        license = 'GPLv3+',
        platforms = 'Linux',
        py_modules = ['webcheck'],
        entry_points = {
            'console_scripts': ['webcheck = webcheck:main'],
        },
        include_package_data = True,
        install_requires = [
            'beautifulsoup4',
            'urllib3',
            'pip'
        ],
        keywords = 'Robots.txt Audit Webserver',
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: POSIX',
            'Programming Language :: Python :: 3.3',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
        ],
    )
