from setuptools import setup, find_packages

def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name='snake_game',
    version='1.0.0',
    description='snake game',
    author='Elomir Júnior',
    author_email='elomir.fj@live.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements-dev.txt')
)
