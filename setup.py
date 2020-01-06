from setuptools import setup

setup(
    name='cli',
    version='1.0',
    py_modules=['flask'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cli=cli:func
    ''',
)
