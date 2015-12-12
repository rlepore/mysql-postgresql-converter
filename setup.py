from setuptools import setup


setup(
    name="mysql-postgresql-converter",
    url="https://github.com/lanyrd/mysql-postgresql-converter/blob/master/README.md",
    description="Lanyrd's MySQL to PostgreSQL conversion script.",
    author="Lanyrd",
    entry_points={
        'console_scripts': [
            'db_converter = db_converter:main'
        ]
    }
)
