from setuptools import setup, find_packages

setup(
    name='vault',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'vault=vault:cli'
        ],
    },
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ],
    setup_requires=[],
    tests_require=[
        'pytest'
    ]
)
