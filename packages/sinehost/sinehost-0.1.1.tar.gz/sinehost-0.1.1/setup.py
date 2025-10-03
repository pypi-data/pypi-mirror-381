from setuptools import setup, find_packages

setup(
    name='sinehost',
    version='0.1.1',
    author='sinesurge',
    author_email='sinesurgeproducts@gmail.com',
    description='C++-based audio host CLI launcher',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'essential': ['essential'],  # Include the binary
    },
    entry_points={
        'console_scripts': [
            'essential = essential.__main__:main',
        ],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
