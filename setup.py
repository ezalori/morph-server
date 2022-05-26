from setuptools import setup, find_packages

setup(
    name='vault',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ],
    setup_requires=[],
    tests_require=[
        'pytest'
    ]
)
