from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask-WTF-Decorators',
    version='0.1.2',
    license='MIT',
    url='https://github.com/simpleapples/flask-wtf-decorators/',
    author='Zhiya Zang',
    author_email='zangzhiya@gmail.com',
    description='Decorators for flask-wtf',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License'
    ],
    include_package_data=True,
    platforms='any',
    install_requires=['Flask>=0.7', 'Flask-WTF>=0.9'],
)
