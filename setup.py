from setuptools import setup
from setuptools import find_packages

packages = find_packages()
packages.append("pytimer")

setup(name="pytimer",
      version="0.0.1",
      description="simple code execution timer",
      url="https://github.com/sabhiram/py-timer",
      author="sabhiram",
      install_requires=[],
      packages=packages)
