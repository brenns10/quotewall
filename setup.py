from setuptools import setup

setup(
    name='quotewall',
    packages=['quotewall'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-login',
    ],
)
