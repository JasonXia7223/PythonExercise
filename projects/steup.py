try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jason Xia',
    'url': '',
    'download_url': '',
    'author_email': 'jasonxia_7223@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project'
}

setup(**config)
