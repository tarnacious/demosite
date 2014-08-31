from setuptools import setup, find_packages
setup(
    name='demosite',
    version='1.0',
    long_description="a simple demo site",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'gunicorn'],
    entry_points={
        'console_scripts': ['development-server=demosite:development_server']
    }
)
