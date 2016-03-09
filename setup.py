from setuptools import setup, find_packages
import os

execfile(os.path.join(os.path.dirname(__file__), 'randomnames/version.py'))


setup(
    name='python-randomnames',
    version=".".join(map(str, VERSION)),
    packages = find_packages(),

    author = 'Concentric Sky',
    author_email = 'django@concentricsky.com',
    description = 'Generate random adjective/noun pairs',
    license = 'Apache2'
)
