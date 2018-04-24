from setuptools import setup, find_packages


setup(
    name='Flask-WTF-Decorators',
    version='0.1',
    license='MIT',
    url='https://github.com/simpleapples/flask-wtf-decorators/',
    author='Zhiya Zang',
    author_email='zangzhiya@gmail.com',
    description='Decorators for flask-wtf',
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
