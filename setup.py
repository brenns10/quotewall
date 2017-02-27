from setuptools import setup, find_packages

setup(
    name='quotewall',
    packages=find_packages(include=['quotewall*']),
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask-login',
        'flask-migrate',
        'werkzeug',
    ],
)
