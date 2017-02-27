from setuptools import setup, find_packages

setup(
    name='quotewall',
    packages=find_packages(include=['quotewall*']),
    package_data={
        'quotewall': ['static/*', 'templates/*', 'templates/parts/*'],
    },
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask-login',
        'flask-migrate',
        'werkzeug',
    ],
)
