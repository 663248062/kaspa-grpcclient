from setuptools import setup, find_packages

__version__ = '1.0'
requirements = open('requirements.txt').readlines()

setup(
    name = 'kaspa-grpcclient',
    version = __version__,
    author = 'Judy',
    author_email = '663248062@qq.com',
    url = '',
    description = 'kaspa coin grpc client',
    packages = find_packages(exclude=["tests"]),
    python_requires = '>=3.7.0',
    install_requires = requirements
)